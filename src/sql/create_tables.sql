 CREATE SCHEMA public;

CREATE TABLE public.MES(id BIGSERIAL PRIMARY KEY,ts_recv BIGINT,ts_event BIGINT,rtype INTEGER,publisher_id INTEGER,instrument_id INTEGER,action VARCHAR(1),side VARCHAR(1),depth INTEGER,price NUMERIC,size INTEGER,flags INTEGER,ts_in_delta INTEGER,sequence BIGINT,symbol VARCHAR(100));
CREATE INDEX idx_mes_ts_recv ON public.MES(ts_recv);
CREATE INDEX idx_mes_ts_event ON MES(ts_event);

CREATE TABLE  public.VX(id BIGSERIAL PRIMARY KEY,ts_event BIGINT,rtype INTEGER,publisher_id INTEGER,instrument_id INTEGER,action VARCHAR(1),side VARCHAR(1),depth INTEGER,price NUMERIC,size INTEGER,flags INTEGER,ts_in_delta INTEGER,sequence BIGINT,symbol VARCHAR(100));
CREATE INDEX idx_vx_ts_event ON public.VX(ts_event);
CREATE INDEX idx_vx_rtype ON public.VX(rtype);

CREATE TABLE public.DX(id BIGSERIAL PRIMARY KEY,ts_event BIGINT,rtype INTEGER,publisher_id INTEGER,instrument_id INTEGER,action VARCHAR(1),side VARCHAR(1),depth INTEGER,price NUMERIC,size INTEGER,flags INTEGER,ts_in_delta INTEGER,sequence BIGINT,symbol VARCHAR(100));
CREATE INDEX idx_dx_ts_event ON public.DX(ts_event);
CREATE INDEX idx_dx_rtype ON public.DX(rtype);
CREATE INDEX idx_dx_instrument_id ON public.DX(instrument_id); 

CREATE TABLE public.XCBF(id BIGSERIAL PRIMARY KEY,ts_event BIGINT,rtype INTEGER,publisher_id INTEGER,instrument_id INTEGER,action VARCHAR(1),side VARCHAR(1),depth INTEGER,price NUMERIC,size INTEGER,flags INTEGER,ts_in_delta INTEGER,sequence BIGINT,symbol VARCHAR(100));
CREATE INDEX idx_xcbf_ts_event ON public.XCBF(ts_event);
CREATE INDEX idx_xcbf_rtype ON public.XCBF(rtype);

-- psql -U hexen -h localhost -d daskapital -f create_tables.sql
--Nuke it - psql -U hexen -h localhost -d daskapital DROP SCHEMA public CASCADE;