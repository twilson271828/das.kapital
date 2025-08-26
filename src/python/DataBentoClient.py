from xmlrpc import client
import databento as db

class DataBentoClient:
    def __init__(self, api_key):
        self.api_key=api_key
        self.client = db.Historical(self.api_key)   

    def resolve_symbols(self, ds, t0, tf, symbol_ids,type_in,type_out):
        try:
            resolved_symbols = self.client.symbology.resolve(
                dataset=ds,
                start=t0,
                end=tf,
                symbols=symbol_ids,
                stype_in=type_in,
                stype_out=type_out
            )
            return resolved_symbols
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    def get_historical_data(self, ds, t0, tf, schema, result_limit=5):
        try:
            data = self.client.timeseries.get_range(
                dataset=ds,
                schema=schema
                start=t0,
                end=tf,
                limit=result_limit
            )
            return data
        except Exception as e:
            print(f"An error occurred: {e}")
            return None


