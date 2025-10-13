from DataBentoClient import DataBentoClient

if __name__=="__main__":

    API_KEY="poop3"
    dataset="GLBX.MDP3"
    schema="trades"
    stype_in="instrument_id"
    stype_out="raw_symbol"
    start="2023-07-07T14:30:00"
    end="2023-07-07T16:40:00"
    limit=20
    client =DataBentoClient(API_KEY)
    fn="data10.csv"

    client.get_historical_data(dataset, start, end, schema, fn,limit)
    
