--
-- Name:  pod_transaction_seq
--

-- drop sequence if exists pod_transaction_seq cascade;

CREATE SEQUENCE pod_transaction_seq
    start with 1
    increment by 1
    no minvalue
    no maxvalue
    cache 1;

ALTER TABLE public.pod_transaction_seq OWNER TO wellkeeper;
GRANT ALL ON SEQUENCE pod_transaction_seq to wellkeper;
GRANT ALL ON SEQUENCE pod_transaction_seq to writers;
GRANT select ON SEQUENCE pod_transaction_seq to readers;


--
-- Name:  pod_transaction
--
drop table if exists pod_transactions cascade;

CREATE TABLE pod_transactions (
    trans_id integer DEFAULT nextval('pod_transaction_seq'::regclass) NOT NULL,
    config_id integer,
    podid integer,
    trans_time timestamp NOT NULL,
    trans_type char(4) NOT NULL,
    trans_json character varying NOT NULL
);

-- primary and foreign keys 
ALTER TABLE ONLY pod_transactions
    ADD CONSTRAINT pod_trans_pkey PRIMARY KEY (trans_id);

ALTER TABLE ONLY pod_transactions
    ADD CONSTRAINT pod_trans_pod_fk FOREIGN KEY (podid) REFERENCES pod(podid) ON UPDATE CASCADE ON DELETE CASCADE;
-- ALTER TABLE ONLY pod_transactions
--    ADD CONSTRAINT pod_trans_config_fk FOREIGN KEY (config_id) REFERENCES reporting.configs(config_id);

-- Indexs
create index podid_idx on pod_transactions (podid);
CREATE index trans_time_idx on pod_transactions (trans_time);
CREATE index trans_combined_idx on pod_transactions (config_id,podid,trans_time);

ALTER TABLE public.pod_transactions OWNER TO wellkeeper;
GRANT all ON TABLE pod_transactions to wellkeper;
GRANT select,insert,update,delete ON TABLE pod_transactions to writers;
GRANT select ON TABLE pod_transactions to readers;

--
-- Name:  pod_trans_queue_seq
--

drop sequence if exists pod_trans_queue_seq cascade;

CREATE SEQUENCE pod_trans_queue_seq
    start with 1
    increment by 1
    no minvalue
    no maxvalue
    cache 1;

ALTER TABLE public.pod_trans_queue_seq OWNER TO wellkeeper;
GRANT ALL ON SEQUENCE pod_trans_queue_seq to wellkeeper;
GRANT ALL ON SEQUENCE pod_trans_queue_seq to writers;
GRANT select ON SEQUENCE pod_trans_queue_seq to readers;


--
-- Name: pod_trans_queue
--
drop table if exists pod_trans_queue cascade;

CREATE TABLE pod_trans_queue (
    queue_id integer DEFAULT nextval('pod_trans_queue_seq'::regclass) NOT NULL,
    trans_data character varying NOT NULL,
    trans_complete char(4) NOT NULL
);

-- primary and foreign keys 
ALTER TABLE ONLY pod_trans_queue
    ADD CONSTRAINT pod_trans_q_pkey PRIMARY KEY (queue_id);

-- Indexs
create index tran_complete_idx on pod_trans_queue (trans_complete);

ALTER TABLE public.pod_trans_queue OWNER TO wellkeeper;
GRANT all ON TABLE pod_trans_queue to wellkeeper;
GRANT select,insert,update,delete ON TABLE pod_trans_queue to writers;
GRANT select ON TABLE pod_trans_queue to readers;
--
-- end
--
