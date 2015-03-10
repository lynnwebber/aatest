#!/usr/bin/env python
class TestGen:

    def get_config_descriptors(self, config_id):
        """Retrieves the reading descriptor records associated with a config_id."""
        columns = [# reading_descriptors
                   ('msg_index', 'msg_index'),
                   ('msg_width', 'msg_width'),
                   ('reporting.reading_descriptors.data_type', 'data_type'),
                   ('endianness', 'endianness'),
                   ('ds_channel', 'ds_channel'),
                   ('efm_slave != -1 AS is_efm', 'is_efm'),
                   ('is_sfr', 'is_sfr'),
                   # analog_reading
                   ('analog_channel', 'analog_channel'),
                   # counter_reading
                   ('counter_channel', 'counter_channel'),
                   # modbus_reading
                   ('slave_id', 'slave_id'),
                   ('function_code', 'function_code'),
                   ('base_address', 'base_address'),
                   ('requested_registers', 'requested_registers'),
                   ('expected_bytes', 'expected_bytes'),
                   # binary_reading
                   ('binary_channel', 'binary_channel'),
                   # param_reading
                   ('name', 'param_name'),
                   ('value', 'param_value'),
                   # modblob_reading
                   ('blob_format', 'blob_format'),
                   ('sam_id', 'blob_sam_id'),
                   ('intervl', 'blob_interval'),
                   ('reporting.modblob_readings.slave_addr', 'blob_slave_addr'),
                   ('blob_display', 'blob_display'),
                   ('reporting.modblob_formats.func_code AS blob_func_code', 'blob_func_code'),
                   ('reporting.modblob_formats.bytes_per_reg AS blob_bytes_per_reg', 'blob_bytes_per_reg'),
                   ('reporting.modblob_formats.base_reg AS blob_base_reg', 'blob_base_reg'),
                   ('reporting.modblob_formats.total_regs AS blob_total_regs', 'blob_total_regs'),
                   ('reporting.modblob_formats.max_regs_per_req', 'blob_max_regs_per_req'),
                   # mu_channel
                   ('key_id', 'equip_id'),
                   ('type', 'equip_type'),
                   ]
        db_cols, labels = zip(*columns) # Unzip, a little trick from http://docs.python.org/library/functions.html
        query = """
           SELECT """ + ', '.join(db_cols) + """   
             FROM reporting.reading_descriptors
NATURAL LEFT JOIN reporting.analog_readings
NATURAL LEFT JOIN reporting.counter_readings
NATURAL LEFT JOIN reporting.modbus_readings
NATURAL LEFT JOIN reporting.binary_readings
NATURAL LEFT JOIN reporting.param_readings
        LEFT JOIN reporting.configs USING(config_id)
NATURAL LEFT JOIN reporting.modblob_readings
NATURAL LEFT JOIN reporting.modblob_formats
        LEFT JOIN mu_channel ON 
            (reporting.configs.muid = mu_channel.muid AND 
             reporting.reading_descriptors.ds_channel = mu_channel.channel AND
             mu_channel.modbus_slave_id = reporting.reading_descriptors.efm_slave
            ) WHERE config_id = %(config_id)d
         ORDER BY msg_index
        """
        args = {'config_id': config_id}

        
        print query % args


# ---- main -----
def main():
    print '-'*45+' start'
    tg = TestGen()
    tg.get_config_descriptors(2970)
    print '-'*45+' end'
    print '>'*20+' stop '+'<'*20

# ---------- run main -------------
if __name__ == "__main__":
    main()
