"""Bank balance checking tool."""

BANK_BALANCE_SCHEMA = {
    "type": "function",
    "function": {
        "name": "check_bank_balance",
        "description": "Check the bank balance for a given account number",
        "parameters": {
            "type": "object",
            "properties": {
                "account_number": {
                    "type": "string",
                    "description": "The account number to check balance for"
                }
            }
        }
    }
}


def check_bank_balance(account_number: str = None) -> dict:
    """Check the bank balance for an account."""
    return {
        "account_number": account_number or "****1234",
        "balance": 12547.83,
        "currency": "USD",
        "account_type": "Checking",
        "last_updated": "2024-01-15T10:30:00Z"
    }
