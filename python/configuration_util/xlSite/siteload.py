#
import sys
import argparse
import pyexcel as px
#import config as cfg

# -------------------------------------------------------------
#          site information
# -------------------------------------------------------------

# -------------------------------------------------------------
def extract_fields_to_dict(rec):
    """
    extract the data from the ordered dict type that is part of pyexcel and 
    place it into a dict object that will be appended to the return of the 
    load_and_correct... function
    """
    tdict = {}
    for k,v in rec.items():
        tdict[k] = v
    return tdict

# -------------------------------------------------------------
def check_site_for_rqrd_fields(rec):
    """
    checks a single record of site sheet for the required fields
    """
    error_flag = False
    if rec['Operator'] == '':
        error_flag = True
        print("Error - No operator provided for site %s" % (rec['Site_name']))
    if rec['IP_Address'] == '':
        error_flag = True
        print("Error - No IP address provided for site %s" % (rec['Site_Name']))
    if rec['Port'] == '':
        error_flag = True
        print("Error - No port provided for site %s" % (rec['Site_Name']))
    if rec['Latitude'] == '':
        error_flag = True
        print("Error - No Latitude provided for site %s" % (rec['Site_Name']))
    if rec['Longitude'] == '':
        error_flag = True
        print("Error - No Longitude provided for site %s" % (rec['Site_Name']))

    return error_flag

# -------------------------------------------------------------
def load_site_info(args):
    #TODO add device column to spreadsheet and instructions
    #TODO extract device
    #TODO consider operator prefix for site
    """ 
    Loads a wellkeeper formatted "site" sheet from a workbook and validates that
    the appropriate values are present
    Note: since there is only one site the script will use the first line pulled
    from the sheet as the information for the site
    """
    sheetrecs = []
    err = False
    err_count = 0
    recs = px.iget_records(file_name=args.spreadsheet,sheet_name='Site',name_columns_by_row=0)
    for rec in recs:
        if rec['Site_Name'] != '':
            sheetrecs.append(extract_fields_to_dict(rec))
    px.free_resources()

    for rec in sheetrecs:
        # check to see if all of the fields needed are there
        err = check_site_for_rqrd_fields(rec)
        if err:
            err_count = err_count + 1
            break

    if err_count > 0:
        raise ValueError("Errors detected loading Site - please review messages ")
        return []
    else:
        return sheetrecs

# -------------------------------------------------------------
if __name__ == "__main__":
    print("This is not a stand alone module it is meant to be imported")



