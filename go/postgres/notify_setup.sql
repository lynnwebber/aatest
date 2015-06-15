-- setup notification test
--
drop trigger if exists rtu_sync_notify on my_test;
drop table if exists my_test;


--
create or replace function notify_rtu_channel() returns trigger as $$
declare
begin
    perform pg_notify(CAST('rtu_sync' AS text),
                      CAST(NEW.rtu_channel_id AS text));
    return NEW;
end;
$$ language plpgsql;

create table my_test (
    rtu_channel_id  int primary key,
    name    varchar,
    info    varchar
);

create trigger rtu_sync_notify
    after insert or update
    on my_test
    for each row
    execute procedure notify_rtu_channel();
