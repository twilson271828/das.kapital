import zstandard as zstd
from pathlib import Path 
import shutil 
import os
import  tarfile
import databento as db
import pandas as pd




def extract_zst(file_path):
    dctx = zstd.ZstdDecompressor()
    with open(file_path, 'rb') as ifh:
        with open(file_path.stem, 'wb') as ofh:
            dctx.copy_stream(ifh, ofh)  
        store = db.DBNStore.from_file(file_path.stem)
        df = store.to_df()
        df.to_csv(f"csv/{file_path.stem}.csv", index=False)
        os.remove(file_path.stem)  # Clean up the intermediate .zst file




if __name__=="__main__":
    files = list(Path(os.getcwd()).glob('*.zst'))
    output_path = Path("csv")
    if output_path.exists():
        shutil.rmtree(output_path)
    output_path.mkdir()
    
    for file in files:
        print(f"Extracting {file}...")
        extract_zst(file)
        #print(f"Finished extracting {file}.")   
        
