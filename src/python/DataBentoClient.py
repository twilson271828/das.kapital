from xmlrpc import client
import databento as db

from databento.common.error import BentoClientError

class DataBentoClient:
    def __init__(self, api_key):
        self.api_key=api_key
        self.client = db.Historical(self.api_key)   

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

            res=result["result"]
            for k in res.keys():
                resolved_symbols.append(res[k][0]["s"])
            return resolved_symbols
            
        except BentoClientError as e:
            return []
        
    def get_historical_data(self, ds, t0, tf, schema, result_limit=5):
        try:
            data = self.client.timeseries.get_range(
                dataset=ds,
                schema=schema
                start=t0,
                end=tf,
                limit=result_limit
            )
            df = data.to_df()
            instrument_ids=df["instrument_id"].to_list()

            resolved_symbols=resolve_symbols(client,"GLBX.MDP3","2023-07-07T14:30:00","2023-07-07T14:40:00", instrument_ids,"instrument_id","raw_symbol")
            df[df.columns[-1]] = resolved_symbols
            print("len(df)=",len(df))
            df.to_csv("data6.csv",index=False)
            print(df.columns[-1])
            print(resolved_symbols)

            return df
        except Exception as e:
            print(f"An error occurred: {e}")
            return None
        



