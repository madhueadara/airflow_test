from sqlalchemy import create_engine

def load_to_database(df: pd.DataFrame, table_name: str):
    engine = create_engine('postgresql://user:pass@localhost:5432/sales_db')
    df.to_sql(
        table_name,
        engine,
        if_exists='append',
        index=False,
        method='multi'
    )
