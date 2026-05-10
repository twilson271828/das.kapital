from DataBentoClient import DataBentoClient

if __name__=="__main__":

    API_KEY="poop3"
    dataset="GLBX.MDP3"
    schema="ohlcv-1m"
    stype_in="instrument_id"
    stype_out="raw_symbol"
    start="2024-10-14T00:00:00"
    end="2024-10-14T13:59:59"
    limit=500

    client =DataBentoClient(API_KEY)
    fn="ohlcv-1m_20241014.csv"

    client.get_historical_data(dataset, start, end, schema, fn,limit)
    
