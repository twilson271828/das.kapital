
from xmlrpc import client
import databento as db

from databento.common.error import BentoClientError

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




def test_resolve_symbols(client,ds, t0, tf, symbol_ids,type_in,type_out):
        resolved_symbols=[]
        try:
            result = client.symbology.resolve(
                dataset=ds,
                start_date=t0,
                end_date=tf,
                symbols=symbol_ids,
                stype_in=type_in,
                stype_out=type_out
            )

        except BentoClientError as e:
            return []
        



def resolve_symbols(client,ds, t0, tf, symbol_ids,type_in,type_out):
        resolved_symbols=[]
        try:
            result = client.symbology.resolve(
                dataset=ds,
                start_date=t0,
                end_date=tf,
                symbols=symbol_ids,
                stype_in=type_in,
                stype_out=type_out
            )
            res = result["result"]
            
            for k in res.keys():
                if res[k]:
                    resolved_symbols.append(res[k][0]["s"])
            return resolved_symbols
            
        except BentoClientError as e:
            return []
        


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
    df = data.to_df()
    instrument_ids=df["instrument_id"].to_list()

    resolved_symbols=resolve_symbols(client,"GLBX.MDP3","2023-07-07T14:30:00","2023-07-07T14:40:00", instrument_ids,"instrument_id","raw_symbol")
    df[df.columns[-1]] = resolved_symbols
    print("len(df)=",len(df))
    df.to_csv("data8.csv",index=False)
    print(df.columns[-1])
    print(resolved_symbols)

    

if __name__ == "__main__":
    API_KEY="poop2"
    get_data(API_KEY)
    
    
