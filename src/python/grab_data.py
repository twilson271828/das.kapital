
from xmlrpc import client
import databento as db


def rank_by_volume(API_KEY,top=10):
    # Request OHLCV-1d data
    client = db.Historical(API_KEY)
    data = client.timeseries.get_range(
        dataset="GLBX.MDP3",
        symbols="ALL_SYMBOLS",
        schema="trades",
        start="2024-08-15"
    )

    df = data.to_df()
    print(df)
    return df.sort_values(by="volume", ascending=False)["instrument_id"].to_list()[:top]


def get_symbol_properties_ranked_by_volume(API_KEY,top=10):
    # Request OHLCV-1d data
    client = db.Historical(API_KEY)
    data = client.timeseries.get_range(
        dataset="GLBX.MDP3",
        symbols="ALL_SYMBOLS",
        schema="ohlcv-1d",
        start="2023-08-15"
    )
    df = data.to_df()
    top_instruments = df.sort_values(by="volume", ascending=False)["instrument_id"].to_list()[:top]

    data = client.timeseries.get_range(
        dataset="GLBX.MDP3",
        stype_in="instrument_id",
        symbols=top_instruments,
        schema="definition",
        start="2023-08-15",
    )

    # Convert to DataFrame
    df = data.to_df()
    return df[["instrument_id", "raw_symbol", "min_price_increment", "match_algorithm", "expiration"]]




def  get_schemas(API_KEY):
    client = db.Historical(API_KEY)
    schemas=client.metadata.list_schemas(dataset="GLBX.MDP3")
    print(schemas)



def get_data1(API_KEY):
    client = db.Historical(API_KEY)
    data = client.timeseries.get_range(
        dataset="GLBX.MDP3",
        symbols=["ESM2", "NQZ2"],
        schema="ohlcv-1s",
    start="2022-06-06T14:30:00",
    end="2022-06-06T14:40:00",
    limit=20
    )
    data.replay(print)
    df = data.to_df()
    df.to_csv("data5.csv", index=False)




def get_data(API_KEY):
    client = db.Historical(API_KEY)
    
    # Fetching data for the Micro E-mini Nasdaq 100 futures contract
    # from the MDP3 dataset, trades schema, for the date July 1, 2024
    data = client.timeseries.get_range(
    dataset="GLBX.MDP3",
    schema="trades",
    stype_in="instrument_id",
    stype_out="raw_symbol",
    start="2023-07-07T14:30:00",
    end="2023-07-07T14:40:00",
    limit=5
    )
    #data.replay(print)
    df = data.to_df()
   
    instrument_ids=df["instrument_id"].to_list()
    result=client.symbology.resolve(
        dataset="GLBX.MDP3",
        symbols=instrument_ids,
        stype_in="instrument_id",
        stype_out="raw_symbol",
        start_date="2023-07-07T14:30:00",
        end_date="2023-07-07T14:40:00"
    )
    resolved_symbols=[]
    for k in result["result"].keys():        
        d=result["result"][k][0]
        resolved_symbols.append(d["s"])

    print(resolved_symbols)

if __name__ == "__main__":
    API_KEY="db-i8y3YgWwrYBuX4c8gYSbrbpFwvXnC"
    get_data(API_KEY)
    
    
