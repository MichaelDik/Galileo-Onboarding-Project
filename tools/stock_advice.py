"""Stock advice tool."""

STOCK_ADVICE_SCHEMA = {
    "type": "function",
    "function": {
        "name": "get_stock_advice",
        "description": "Get stock investment advice for a given stock symbol",
        "parameters": {
            "type": "object",
            "properties": {
                "symbol": {
                    "type": "string",
                    "description": "The stock symbol (e.g., AAPL, GOOGL, MSFT)"
                }
            }
        }
    }
}


def get_stock_advice(symbol: str = None) -> dict:
    """Get stock advice for a given stock symbol."""
    symbol = symbol or "AAPL"
    return {
        "symbol": symbol,
        "recommendation": "BUY",
        "target_price": 185.50,
        "current_price": 175.20,
        "confidence": "High",
        "reasoning": "Strong fundamentals, positive earnings growth, and favorable market conditions suggest upward momentum."
    }
