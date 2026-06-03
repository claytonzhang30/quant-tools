"""VPIN - Volume-synchronized Probability of Informed Trading."""
import numpy as np
import pandas as pd

class VPIN:
    def __init__(self, trades_df: pd.DataFrame, bucket_size: int = 1000, n_buckets: int = 50):
        self.bucket_size = bucket_size
        self.n_buckets = n_buckets
        self.value = self._calculate(trades_df)
    
    def _calculate(self, df: pd.DataFrame) -> float:
        """Calculate VPIN from trade data."""
        if df.empty:
            return 0.0
        
        # Classify trades as buy or sell
        df = df.copy()
        df['direction'] = np.where(df['price'] >= df['price'].shift(1), 1, -1)
        
        # Create volume buckets
        df['cum_vol'] = df['volume'].cumsum()
        df['bucket'] = (df['cum_vol'] // self.bucket_size).astype(int)
        
        # Calculate buy/sell volume per bucket
        buckets = df.groupby('bucket').apply(
            lambda g: pd.Series({
                'buy_vol': g.loc[g['direction'] == 1, 'volume'].sum(),
                'sell_vol': g.loc[g['direction'] == -1, 'volume'].sum()
            })
        )
        
        # VPIN = mean(|buy_vol - sell_vol|) / bucket_size
        if len(buckets) < 2:
            return 0.0
        
        order_imbalance = (buckets['buy_vol'] - buckets['sell_vol']).abs()
        return order_imbalance.mean() / self.bucket_size
