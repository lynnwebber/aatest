-- select nlnm.position,nlnm.notification_method_id, nlnm.delay, nm.contact_id, nm.type, nm.data, nc.name
-- from notification_lists_notification_methods nlnm
-- join notification_methods nm on (nlnm.notification_method_id=nm.notification_method_id)
-- join notification_contacts nc on (nm.contact_id=nc.contact_id)
-- where notification_list_id in (select notification_list_id
--     from alarm_definitions_notification_lists
--     where alarm_definition_id = 1101
--     order by position asc)
-- order by ;


select adnl.notification_list_id, nlnm.position,nlnm.notification_method_id, nlnm.delay, nm.contact_id, nm.type, nm.data, nc.name
from alarm_definitions_notification_lists adnl
join notification_lists_notification_methods nlnm on (adnl.notification_list_id=nlnm.notification_list_id)
join notification_methods nm on (nlnm.notification_method_id=nm.notification_method_id)
join notification_contacts nc on (nm.contact_id=nc.contact_id)
where alarm_definition_id = 1101
order by adnl.position asc, nlnm.position;
