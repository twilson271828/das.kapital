from xmlrpc import client
import databento as db
import pandas as pd
import os

from databento.common.error import BentoClientError

class DataBentoClient:
    def __init__(self, api_key):
        self.api_key=api_key
        self.client = db.Historical(self.api_key)   
    
    def resolve_symbols(self,client,ds, t0, tf, symbol_ids,type_in,type_out):
        resolved_symbols_dict={}
        try:
            result = self.client.symbology.resolve(
                dataset=ds,
                start_date=t0,
                end_date=tf,
                symbols=symbol_ids,
                stype_in=type_in,
                stype_out=type_out
            )
            
            results_dict=result["result"]
            for k in results_dict.keys():
                resolved_symbols_dict[k]=results_dict[k][0]["s"]
            
            return resolved_symbols_dict
            
        except BentoClientError as e:
            return []
        
    def get_historical_data(self, ds, t0, tf, sch, output_filename,result_limit=5):
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
            print(instrument_ids)
            stype_in="instrument_id"
            stype_out="raw_symbol"
            resolved_symbols=[]
            resolved_symbols_dict=self.resolve_symbols(client,ds,t0,tf, instrument_ids,stype_in,stype_out)
            print(resolved_symbols_dict)
            #d[instrument_id]=symbol
            for instrument_id in instrument_ids:                
                sym=resolved_symbols_dict[str(instrument_id)]
                resolved_symbols.append(sym)
           
            df[df.columns[-1]] = resolved_symbols

            df.to_csv(output_filename,index=False)
            
            return df
        except BentoClientError as e:
            return pd.DataFrame()
            
        


     
        



