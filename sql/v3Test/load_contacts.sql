delete from notification_lists_notification_methods;
delete from notification_lists;
delete from notification_methods;
delete from notification_contacts;

insert into notification_contacts
 (contact_id,operator_id,name,status)
values
 (1100,23,'lynn webber','active');

insert into notification_contacts
 (contact_id,operator_id,name,status)
values
 (1101,23,'randy krall','active');

insert into notification_contacts
 (contact_id,operator_id,name,status)
values
 (1102,23,'todd flaska','active');

;; ------------

insert into notification_methods
 (notification_method_id,contact_id,type,data)
values
 (11001,1100,'sms','3039093591');

insert into notification_methods
 (notification_method_id,contact_id,type,data)
values
 (11011,1101,'sms','5052581806');

insert into notification_methods
 (notification_method_id,contact_id,type,data)
values
 (11021,1102,'email','todd.flaska@wellkeeper.com');

;; ----------------

insert into notification_lists
 (notification_list_id,operator_id,description)
values
 (101,23,'Branch Managers');

insert into notification_lists
 (notification_list_id,operator_id,description)
values
 (102,23,'Team Managers');

;; ------------------

insert into notification_lists_notification_methods
 (notification_list_id,notification_method_id,position)
values
 (101,11011,0);

insert into notification_lists_notification_methods
 (notification_list_id,notification_method_id,position)
values
 (102,11001,0);

insert into notification_lists_notification_methods
 (notification_list_id,notification_method_id,position)
values
 (102,11021,1);
