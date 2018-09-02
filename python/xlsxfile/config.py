# configuration file


valid_client_access = ['RO','RW']

valid_types = ['TANK_LEVEL','PIPE_PSIA','PIPE_PSIG','TEMP_F','FLOW_RATE','PERCENT','DURATION',
            'VOLUME','VOLTS','SETPOINT','ACTUATOR','AMPS','CONTROLLER_STATE','COUNTER',
            'DECIBEL','ENERGY','GAS_LEVEL','HERTZ','HORSEPOWER','LEVEL','LOAD','MASS',
            'MERCURY','PARTICULATE_LEVEL','PLATE_SIZE','SIGNAL_STRENGTH','SPECIFIC_GRAVITY',
            'SPEED','STATE','STROKES','TEMP_C','TIME','TORQUE','VESSEL_LEVEL',
            'WATER_VOLUME','WIND_DIR']

SCADA_valid_types = ['Boolean','Byte','Short','Word','Long','Dword','Float','Double','Llong',
            'Qword','Char','String']

kepware_load_header = ['Tag Name','Address','Data Type','Respect Data Type','Client Access','Scan Rate',
        'Scaling','Raw Low','Raw High','Scaled Low','Scaled High','Scaled Data Type',
        'Clamp Low','Clamp High','Eng Units','Description','Negate Value']

