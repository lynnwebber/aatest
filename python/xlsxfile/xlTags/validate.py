#
import sys
import argparse
import pyexcel as px
import config as cfg


# -------------------------------------------------------------
#      functions for tag processing
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
def check_rec_for_rqrd_fields(rec):
    """
    checks a single record of spreadsheet input for the required fields
    """
    error_flag = False
    if rec['Tag_Description'] == '':
        error_flag = True
        print("Error - No description for tag %s" % (rec['Tag_Name']))
    if rec['SCADA_Address'] == '':
        error_flag = True
        print("Error - No address provided for tag %s" % (rec['Tag_Name']))
    if rec['SCADA_Data_Type'] == '':
        error_flag = True
        print("Error - No data type provided for tag %s" % (rec['Tag_Name']))
    if rec['Units'] == '' and rec['SCADA_Data_Type'].lower() != 'boolean':
        error_flag = True
        print("Error - No units provided for tag %s" % (rec['Tag_Name']))
    if rec['Measurement_Type'] == '' and rec['SCADA_Data_Type'].lower() != 'boolean':
        error_flag = True
        print("Error - No Measurement Type provided for tag %s" % (rec['Tag_Name']))
    if rec['Wellkeeper_Equipment'] == '':
        error_flag = True
        print("Error - No Wellkeeper Equipment provided for tag %s" % (rec['Tag_Name']))

    return error_flag

# -------------------------------------------------------------
def check_rec_scada_data_type(rec):
    """
    checks the SCADA_Data_Type to ensure it is one of data types that kepware
    exects
    """
    err = False
    dtyp = rec['SCADA_Data_Type'].capitalize()
    if dtyp not in cfg.SCADA_valid_types:
        err = True
        print("Error - SCADA Data Type provided is invalid for tag %s" % (rec['Tag_name']))
    return (err,dtyp)

# -------------------------------------------------------------
def check_rec_client_access(rec):
    """
    checks the client access field and corrects as necessary and returns proper
    value for the field
    """
    ca = rec['Client_Access']
    if ca == '':
        return 'RO'
    if ca.upper() in cfg.valid_client_access:
        return ca.upper()
    else:
        return 'RO'

# -------------------------------------------------------------
def check_rec_measurement_type(rec):
    """
    checks the value of the measurement type to validate that it is
    one of the known types
    """
    warning = False
    wktyp = rec['Measurement_Type'].upper()
    if wktyp not in cfg.valid_types:
        warning = True
        print("Warning - measurement type provided not in the list of valid types for tag %s" % (rec['Tag_name']))
    return (warning,wktyp)

# -------------------------------------------------------------
def check_rec_true_text(rec):
    """
    checks to see if this is a boolean tag if not sets value to NA
    otherwise
    checks the value of the true text, if blank sets to True
    else makes no changes
    """
    dtype = rec['SCADA_Data_Type'].lower()
    if dtype != 'boolean':
        return "NA"

    txt = rec['True_Text']
    if txt == '':
        return 'True'
    else:
        return txt

# -------------------------------------------------------------
def check_rec_false_text(rec):
    """
    checks to see if this is a boolean tag if not sets value to NA
    otherwise
    checks the value of the false text, if blank sets to False
    else makes no changes
    """
    dtype = rec['SCADA_Data_Type'].lower()
    if dtype != 'boolean':
        return "NA"

    txt = rec['False_Text']
    if txt == '':
        return 'False'
    else:
        return txt

# -------------------------------------------------------------
def reformat_scada_address(rec):
    """
    convert the scada address to a string
    if the number is less than 10,000 then also add a leading zero
      to the conversion (for kepware load)
    """
    val = rec['SCADA_Address']
    if val >= 10000:
        return str(val)
    else:
        return '0'+str(val)

# -------------------------------------------------------------
def load_and_correct_tags(args):
    """ 
    Loads a wellkeeper formatted tags sheed from a workbook and fills in the infered
    data that is not entered, validates the fields that are entered against the 
    proper values and then places them in a list of dictionaries to return
    """
    sheetrecs = []
    err = False
    warning = False
    recs = px.iget_records(file_name=args.spreadsheet,sheet_name='Tags',name_columns_by_row=0)
    for rec in recs:
        if rec['Tag_Name'] != '':
            sheetrecs.append(extract_fields_to_dict(rec))
    px.free_resources()

    for rec in sheetrecs:
        # check to see if all of the fields needed are there
        err = check_rec_for_rqrd_fields(rec)
        if err:
            print("Missing required fields in provided spreadsheet - (see error message above) - exiting")
            break

        # check the scada_data_type for one of the valid values
        err,val = check_rec_scada_data_type(rec)
        if err:
            print("Invalid value in SCADA Data Type - (see error message above) - exiting")
        rec['SCADA_Data_Type'] = val

        # make the adjustments for boolean types
        if rec['SCADA_Data_Type'] == 'Boolean':
            rec['Measurement_Type'] = 'Binary'

        # check client access for the two valid types or make it RO
        rec['Client_Access'] = check_rec_client_access(rec)

        # Check the measurement type against the list and upper case it
        warning,val = check_rec_measurement_type(rec)
        rec['Measurement_Type'] = val

        # check the true and false texts and update the defualt values if blank
        rec['True_Text'] = check_rec_true_text(rec)
        rec['False_Text'] = check_rec_false_text(rec)

        # Perform Format correction on SCADA Addresses
        rec['SCADA_Address'] = reformat_scada_address(rec)

    return (err,sheetrecs)


# -------------------------------------------------------------
if __name__ == "__main__":
    print("This is not a stand alone module it is meant to be imported")



