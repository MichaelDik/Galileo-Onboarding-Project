"""Tools module for financial assistant functions."""

from .bank_balance import check_bank_balance, BANK_BALANCE_SCHEMA
from .stock_advice import get_stock_advice, STOCK_ADVICE_SCHEMA
from .customer_info import get_customer_info, CUSTOMER_INFO_SCHEMA

# Tool registry mapping function names to their implementations
TOOL_FUNCTIONS = {
    "check_bank_balance": check_bank_balance,
    "get_stock_advice": get_stock_advice,
    "get_customer_info": get_customer_info,
}

# All tool schemas for OpenAI function calling
TOOLS = [
    BANK_BALANCE_SCHEMA,
    STOCK_ADVICE_SCHEMA,
    CUSTOMER_INFO_SCHEMA,
]

__all__ = [
    "check_bank_balance",
    "get_stock_advice",
    "get_customer_info",
    "TOOL_FUNCTIONS",
    "TOOLS",
]
