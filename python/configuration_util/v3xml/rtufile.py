#!/usr/bin/env python
#
import sys
import argparse
import config as cfg
from xml.etree.ElementTree import Element, SubElement, tostring
from xml.etree import ElementTree
from xml.dom import minidom

# -------------------------------------------------------------
def prettify(elem):
    """Return a pretty-printed XML string for the Element.
    """
    rough_string = ElementTree.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")

# -------------------------------------------------------------
def get_wk_data_type(scada_type):
    rv = cfg.SCADA_valid_types[scada_type.lower()]
    return rv

# -------------------------------------------------------------
def infer_type_from_equip_name(equip_name):
    if 'tank' in equip_name.lower():
        return 'tank'
    elif 'ot' in equip_name.lower():
        return 'tank'
    elif 'wt' in equip_name.lower():
        return 'tank'
    elif 'flowmeter' in equip_name.lower():
        return 'flow_meter'
    elif 'flow meter' in equip_name.lower():
        return 'flow_meter'
    elif 'mc iii' in equip_name.lower():
        return 'flow_meter'
    elif 'mciii' in equip_name.lower():
        return 'flow_meter'
    else:
        return 'generic'

# -------------------------------------------------------------
def build_structure(site):
    rtu_update = Element('RTU_update')
    rtu_channel = SubElement(rtu_update, "RTU_channel")
    identification = SubElement(rtu_channel, "identification", {'rtuid':site['RTU_ID'], 'version':'01.00'})
    SubElement(identification, "pub_sub")
    params = SubElement(rtu_channel, "params")
    SubElement(params, "polling", {'server':'kepserver1.wellkeeper.info', 'interval':'5'})
    rtu = SubElement(rtu_channel, "rtu", {'panel':'none', 'vendor':''})
    SubElement(rtu, "telco", {'IpV4addr':site['IP_Address'], 'IpV6addr':' ', 'number':' ', 'vendor':' '})
    devices = SubElement(rtu_channel, "devices")

    # RTU equipment
    rtu_equipment = SubElement(rtu_update, "rtu_equipment_specification", {'rtuid':site['RTU_ID'], 'version':'01.00'})
    equipment = SubElement(rtu_equipment, "equipment")

    # RTU grouping
    rtu_grouping = SubElement(rtu_update, "rtu_grouping_specification", {'rtuid':site['RTU_ID'], 'version':'01.00'})
    grouping = SubElement(rtu_grouping, "grouping", {'desc':site['Site_Name'], 'id':'????', 'op':str(site['Operator_id']), 'type':'rtu'})

    return rtu_update

# -------------------------------------------------------------
def insert_meter_and_measurements(rtu,site,tagrecs):
    rtu_channel = rtu.find("RTU_channel")
    devices = rtu_channel.find("devices")
    meter = SubElement(devices, "meter", {'comm':site['IP_Address'], 'id':site['Device_Name'],'vendor':'unknown'})
    for rec in tagrecs:
        datatype = get_wk_data_type(rec['SCADA_Data_Type'])
        if rec['Measurement_Type'].upper() == 'BINARY':
            msmt = SubElement(meter, "msmt", {'id':rec['Tag_Name'],
                                              'false_text':rec['False_Text'],
                                              'true_text':rec['True_Text'],
                                              'name':rec['Tag_Description'],
                                              'intercept':"0.0",
                                              'inverted_logic':"unknown",
                                              'slope':"1.0",
                                              'type':'binary'})
            SubElement(msmt, "descriptor", {'baseReg':rec['SCADA_Address'],
                                            'datatype':datatype,
                                            'type':rec['Measurement_Type']})
        else:
            msmt = SubElement(meter, "msmt", {'id':rec['Tag_Name'],
                                              'name':rec['Tag_Description'],
                                              'intercept':"0.0",
                                              'slope':"1.0",
                                              'type':rec['Measurement_Type'],
                                              'units':rec['Units']})
            SubElement(msmt, "descriptor", {'baseReg':rec['SCADA_Address'],
                                                    'datatype':datatype})

# -------------------------------------------------------------
def get_equipment_and_tags(tagrecs):
    equip_tag_dict = {}
    # scan the tag records and find the uniique equipment and place
    #     them in the dictionary with a blank list
    for rec in tagrecs:
        equip_name = rec['Wellkeeper_Equipment']
        if equip_name not in equip_tag_dict:
            equip_tag_dict[equip_name] = []

    # scan the tags and place them in a list of records associated
    #    with the specific equipment
    for rec in tagrecs:
        equip_name = rec['Wellkeeper_Equipment']
        equip_tag_dict[equip_name].append(rec['Tag_Name'])

    return equip_tag_dict

# -------------------------------------------------------------
def insert_equipment(rtu,site,edict):
    eqcount = 0
    equipment = rtu.find("rtu_equipment_specification/equipment")
    grouping = rtu.find("rtu_grouping_specification/grouping")
    for k,v in edict.items():
        eqcount = eqcount + 1
        # infer equipment type (tank,flowmeter,generic) from equip name
        equip_type = infer_type_from_equip_name(k)
        # insert the equipment element under the equipment_specification
        equip_node = SubElement(equipment, equip_type, {'desc':k,
                                                    'id':'??eq_id_'+str(eqcount)+'??',
                                                    'latitude':str(site['Latitude']),
                                                    'longitude':str(site['Longitude']),
                                                    'op':str(site['Operator_id']) })
        # insert the equipment element under the grouping_specification
        group_node = SubElement(grouping,'equipment').text = '??eq_id_'+str(eqcount)+'??'
        # add the tags under the appropriate equipment
        for tag_name in v:
            tagId = site['RTU_ID']+'.'+site['Device_Name']+'.'+tag_name
            mtag = SubElement(equip_node, "m_tag").text = tagId

# -------------------------------------------------------------
# def insert_equipment(rtu,site,tagrecs):
#     equipment = rtu.find("rtu_equipment_specification/equipment")
#     generic = SubElement(equipment, "generic", {'desc':'TBD-SOON',
#                                                 'id':'??equipment_id??',
#                                                 'latitude':str(site['Latitude']),
#                                                 'longitude':str(site['Longitude']),
#                                                 'op':str(site['Operator_id']) })
#     for rec in tagrecs:
#         tagId = site['RTU_ID']+'.'+site['Device_Name']+'.'+rec['Tag_Name']
#         mtag = SubElement(generic, "m_tag").text = tagId

# -------------------------------------------------------------
def build_xml(args,siterecs,tagrecs):
    sitedict = siterecs[0]
    rtu = build_structure(sitedict)
    insert_meter_and_measurements(rtu,sitedict,tagrecs)
    etdict = get_equipment_and_tags(tagrecs)
    insert_equipment(rtu,sitedict,etdict)
    pretty_xml = prettify(rtu)
    with open(args.xmlfile,'w') as f:
        f.write(pretty_xml)

# -------------------------------------------------------------
if __name__ == "__main__":
    print("This is not a stand alone module it is meant to be imported")

