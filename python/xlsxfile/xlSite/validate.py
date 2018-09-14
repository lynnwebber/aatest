#
import sys
import argparse
import pyexcel as px
import config as cfg

# -------------------------------------------------------------
#          site information
# -------------------------------------------------------------

# -------------------------------------------------------------
def load_site_info(args):
    """ 
    Loads a wellkeeper formatted "tags" sheet from a workbook and fills in the infered
    data that is not entered, validates the fields that are entered against the 
    proper values and then places them in a list of dictionaries to return
    """
    siterec = []
    err = False
    warning = False
    recs = px.iget_records(file_name=args.spreadsheet,sheet_name='Site',name_columns_by_row=0)
    for rec in recs:
        if rec['Tag_Name'] != '':
            sheetrecs.append(extract_site_fields_to_dict(rec))
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



