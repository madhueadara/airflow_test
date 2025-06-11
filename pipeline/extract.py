import pandas as pd
from pathlib import Path

def ingest_raw_data(source_dir: str) -> pd.DataFrame:
    """Read and concatenate CSV files from source directory"""
    data_dir = Path(source_dir)
    dfs = []

    for file in data_dir.glob('*.csv'):
        df = pd.read_csv(file, parse_dates=['timestamp'])
        dfs.append(df)
        # Move processed file
        file.rename(data_dir.parent / 'processed' / file.name)

    return pd.concat(dfs, ignore_index=True)
