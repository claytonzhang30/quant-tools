# Quant Tools 📐

Quantitative trading tools — order book analysis, market microstructure, and execution algorithms.

## Modules

### Order Book Analysis
- Real-time order book depth visualization
- Bid-ask spread analysis
- Order flow imbalance detection
- Liquidity heatmap generation

### Market Microstructure
- Trade & quote (TAQ) data processing
- VPIN (Volume-synchronized Probability of Informed Trading)
- Kyle's Lambda estimation
- Realized volatility estimators

### Execution Algorithms
- TWAP (Time-Weighted Average Price)
- VWAP (Volume-Weighted Average Price)
- Implementation shortfall analysis
- Smart order routing

## Quick Start

```python
from quant_tools import OrderBook, TWAP, VPIN

# Analyze order book
book = OrderBook(exchange="binance", symbol="ETHUSDT")
depth = book.get_depth(levels=20)
imbalance = book.order_flow_imbalance()
print(f"OFI: {imbalance:.3f} ({'buy' if imbalance > 0 else 'sell'} pressure)")

# Execute with TWAP
twap = TWAP(
    symbol="ETHUSDT",
    side="buy",
    quantity=10.0,
    duration_seconds=3600
)
twap.execute()

# Calculate VPIN
vpin = VPIN(trades_df, bucket_size=1000)
print(f"VPIN: {vpin.value:.4f}")
```

## Structure

```
quant_tools/
├── orderbook/       # Order book analysis
├── microstructure/  # Market microstructure metrics
├── execution/       # Execution algorithms
├── risk/           # Risk management
└── data/           # Data handling utilities
```

## License

MIT
<!-- update 1 -->
<!-- update 2 -->
<!-- update 3 -->
<!-- update 4 -->
<!-- update 5 -->
<!-- update 6 -->
<!-- update 7 -->
<!-- update 8 -->
<!-- update 9 -->
<!-- update 10 -->
<!-- update 11 -->
<!-- update 12 -->
<!-- update 13 -->
<!-- update 14 -->
<!-- update 15 -->
<!-- update 16 -->
<!-- update 17 -->
