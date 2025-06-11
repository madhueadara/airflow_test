def calculate_metrics(df: pd.DataFrame) -> pd.DataFrame:
    """Add derived columns and aggregations"""
    df['total_sales'] = df['amount'] * df['quantity']
    df['hour_of_day'] = df['timestamp'].dt.hour

    return df.groupby(['product_id', 'region']).agg({
        'total_sales': 'sum',
        'transaction_id': 'count'
    }).reset_index()
