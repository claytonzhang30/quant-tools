"""Order book analysis."""
import numpy as np
from dataclasses import dataclass
from typing import List

@dataclass
class OrderBookLevel:
    price: float
    quantity: float
    side: str  # 'bid' or 'ask'

class OrderBook:
    def __init__(self, exchange: str, symbol: str):
        self.exchange = exchange
        self.symbol = symbol
    
    def get_depth(self, levels: int = 10) -> dict:
        """Get order book depth."""
        return {"bids": [], "asks": []}
    
    def order_flow_imbalance(self, levels: int = 10) -> float:
        """Calculate order flow imbalance. Positive = buy pressure."""
        depth = self.get_depth(levels)
        bid_vol = sum(q for _, q in depth.get("bids", []))
        ask_vol = sum(q for _, q in depth.get("asks", []))
        total = bid_vol + ask_vol
        if total == 0:
            return 0.0
        return (bid_vol - ask_vol) / total
    
    def bid_ask_spread(self) -> float:
        """Get current bid-ask spread."""
        depth = self.get_depth(1)
        if depth["bids"] and depth["asks"]:
            return depth["asks"][0][0] - depth["bids"][0][0]
        return 0.0
    
    def liquidity_heatmap(self, price_range: tuple, resolution: int = 100) -> np.ndarray:
        """Generate liquidity heatmap across price range."""
        return np.zeros(resolution)
