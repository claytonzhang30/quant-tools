"""Value at Risk calculations."""
import numpy as np

def historical_var(returns: np.ndarray, confidence: float = 0.95, holding_period: int = 1) -> float:
    """Calculate Historical VaR."""
    sorted_returns = np.sort(returns)
    index = int((1 - confidence) * len(sorted_returns))
    var = -sorted_returns[index] * np.sqrt(holding_period)
    return var

def parametric_var(mean: float, std: float, confidence: float = 0.95, holding_period: int = 1) -> float:
    """Calculate Parametric VaR (assuming normal distribution)."""
    from scipy.stats import norm
    z = norm.ppf(1 - confidence)
    return -(mean + z * std) * np.sqrt(holding_period)

def expected_shortfall(returns: np.ndarray, confidence: float = 0.95) -> float:
    """Calculate Expected Shortfall (CVaR)."""
    var = historical_var(returns, confidence)
    return -returns[returns <= -var].mean()
