insert into alarm_definitions
 (alarm_definition_id,operator_id,created_at,status,priority,description,
   short_message,full_message)
values
 (1101,23,now(),'active','critical','BEU 123 OT1 High Level',
  'BEU 123 OT1 high level reached',
  'At site BEU 123 Oil Tank #1 has exceeded the high level mark'
  )
