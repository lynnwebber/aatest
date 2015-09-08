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

insert into notification_contacts
(contact_id,operator_id,name,status)
values
(1103,23,'walter farmer','active');

insert into notification_contacts
(contact_id,operator_id,name,status)
values
(1104,23,'buggs bunny','active');

insert into notification_contacts
(contact_id,operator_id,name,status)
values
(1105,23,'daffy duck','active');

;; ------------

insert into notification_methods
 (notification_method_id,contact_id,type,data)
values
 (11001,1100,'sms','3039093591');

insert into notification_methods
 (notification_method_id,contact_id,type,data)
values
 (11002,1100,'email','lynn.webber@wellkeeper.com');


insert into notification_methods
 (notification_method_id,contact_id,type,data)
values
 (11011,1101,'sms','5052581806');

insert into notification_methods
 (notification_method_id,contact_id,type,data)
values
 (11012,1101,'email','randy.krall@wellkeeper.com');


insert into notification_methods
 (notification_method_id,contact_id,type,data)
values
 (11021,1102,'email','todd.flaska@wellkeeper.com');

insert into notification_methods
 (notification_method_id,contact_id,type,data)
values
 (11022,1102,'sms','3036181769');

insert into notification_methods
 (notification_method_id,contact_id,type,data)
values
 (11031,1103,'email','walter.farmer@wellkeeper.com');

;; ----------------

insert into notification_lists
 (notification_list_id,operator_id,description)
values
 (101,23,'Branch Managers');

insert into notification_lists
 (notification_list_id,operator_id,description)
values
 (102,23,'Team Managers');

insert into notification_lists
 (notification_list_id,operator_id,description)
values
 (103,23,'FSO');


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

insert into notification_lists_notification_methods
 (notification_list_id,notification_method_id,position)
values
 (103,11031,0);
