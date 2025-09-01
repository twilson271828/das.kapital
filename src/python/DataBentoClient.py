from xmlrpc import client
import databento as db
import pandas as pd

from databento.common.error import BentoClientError

class DataBentoClient:
    def __init__(self, api_key):
        self.api_key=api_key
        self.client = db.Historical(self.api_key)   
    
    def resolve_symbols(self,client,ds, t0, tf, symbol_ids,type_in,type_out):
        resolved_symbols=[]
        try:
            result = self.client.symbology.resolve(
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
        
    def get_historical_data(self, ds, t0, tf, sch, result_limit=5):
        try:
            data = self.client.timeseries.get_range(
                dataset=ds,
                schema=sch,
                start=t0,
                end=tf,
                limit=result_limit
            )
            df = data.to_df()
            instrument_ids=df["instrument_id"].to_list()
            stype_in="instrument_id"
            stype_out="raw_symbol"

            resolved_symbols=self.resolve_symbols(client,ds,t0,tf, instrument_ids,stype_in,stype_out)
            if( len(df)==len(resolved_symbols) ):
                df[df.columns[-1]] = resolved_symbols

            df.to_csv("data7.csv",index=False)
            
            return df
        except BentoClientError as e:
            return pd.DataFrame()
            return None
        
if __name__=="__main__":

    API_KEY="blah"
    dataset="GLBX.MDP3"
    schema="trades"
    start="2023-07-07T14:30:00"
    end="2023-07-07T14:40:00"
    limit=5

    client1=DataBentoClient(API_KEY)
    client1.get_historical_data(dataset,start,end,schema,limit)

     
        



