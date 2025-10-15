from DataBentoClient import DataBentoClient

if __name__=="__main__":

    API_KEY="poop3"
    dataset="GLBX.MDP3"
    schema="ohlcv-1m"
    stype_in="instrument_id"
    stype_out="raw_symbol"
    start="2025-10-14T00:00:00"
    end="2025-10-14T23:59:59"
    limit=None

    client =DataBentoClient(API_KEY)
    fn="ohlcv-1m_20251014.csv"

    client.get_historical_data(dataset, start, end, schema, fn,limit)
    
