#
import argparse
import csv
import config as cfg

# -------------------------------------------------------------
def generate_kepware_load(args,recs):
    """
    generate a kepware load CSV file using the data that was provided in
    the spreadsheet
    """

    with open(args.outfile,'w') as csvout:
        writer = csv.DictWriter(csvout,fieldnames=cfg.kepware_load_header)
        writer.writeheader()
        for rec in recs:
            csvdict = {'Tag Name' : rec['Tag_Name'],
                    'Address' : rec['SCADA_Address'],
                    'Data Type' : rec['SCADA_Data_Type'],
                    'Respect Data Type' : '1',
                    'Client Access' : rec['Client_Access'],
                    'Scan Rate' : '100',
                    'Scaling' : '',
                    'Raw Low' : '',
                    'Raw High' : '',
                    'Scaled Low' : '',
                    'Scaled High' : '',
                    'Scaled Data Type' : '',
                    'Clamp Low' : '',
                    'Clamp High' : '',
                    'Eng Units' : '',
                    'Description' : rec['Tag_Description'],
                    'Negate Value' : ''}
            writer.writerow(csvdict)

# -------------------------------------------------------------
if __name__ == "__main__":
    print("This is not a stand alone module it is meant to be imported")
