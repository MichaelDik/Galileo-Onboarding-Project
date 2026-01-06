"""Customer information tool."""

CUSTOMER_INFO_SCHEMA = {
    "type": "function",
    "function": {
        "name": "get_customer_info",
        "description": "Get customer information for a given customer ID or name",
        "parameters": {
            "type": "object",
            "properties": {
                "customer_id": {
                    "type": "string",
                    "description": "The customer ID or name to look up"
                }
            }
        }
    }
}


def get_customer_info(customer_id: str = None) -> dict:
    """Get customer information for a given customer ID or name."""
    customer_id = customer_id or "CUST-001"
    
    # Hardcoded customer data - Characters from The Office
    customers = {
        "CUST-001": {
            "customer_id": "CUST-001",
            "name": "Michael Scott",
            "email": "michael.scott@dundermifflin.com",
            "phone": "+1-570-555-0123",
            "account_type": "Premium",
            "member_since": "2020-03-15",
            "total_investments": 125000.00,
            "risk_tolerance": "Moderate"
        },
        "CUST-002": {
            "customer_id": "CUST-002",
            "name": "Dwight Schrute",
            "email": "dwight.schrute@dundermifflin.com",
            "phone": "+1-570-555-0456",
            "account_type": "Standard",
            "member_since": "2021-07-22",
            "total_investments": 45000.00,
            "risk_tolerance": "Conservative"
        },
        "CUST-003": {
            "customer_id": "CUST-003",
            "name": "Jim Halpert",
            "email": "jim.halpert@dundermifflin.com",
            "phone": "+1-570-555-0789",
            "account_type": "Premium",
            "member_since": "2019-11-08",
            "total_investments": 250000.00,
            "risk_tolerance": "Aggressive"
        },
        "CUST-004": {
            "customer_id": "CUST-004",
            "name": "Pam Beesly",
            "email": "pam.beesly@dundermifflin.com",
            "phone": "+1-570-555-0321",
            "account_type": "Standard",
            "member_since": "2022-01-10",
            "total_investments": 35000.00,
            "risk_tolerance": "Moderate"
        },
        "CUST-005": {
            "customer_id": "CUST-005",
            "name": "Stanley Hudson",
            "email": "stanley.hudson@dundermifflin.com",
            "phone": "+1-570-555-0654",
            "account_type": "Premium",
            "member_since": "2018-05-20",
            "total_investments": 180000.00,
            "risk_tolerance": "Conservative"
        }
    }
    
    # Create a name lookup dictionary
    name_lookup = {customer["name"].lower(): customer_id for customer_id, customer in customers.items()}
    
    # Try to find by customer ID first, then by name
    lookup_key = customer_id
    if customer_id.upper().startswith("CUST-"):
        # It's a customer ID
        result = customers.get(customer_id.upper())
    else:
        # Try to find by name (case-insensitive)
        result = customers.get(name_lookup.get(customer_id.lower()))
    
    # Return customer info or default if not found
    if result:
        return result
    
    return {
        "customer_id": customer_id,
        "name": "Unknown Customer",
        "email": "N/A",
        "phone": "N/A",
        "account_type": "Standard",
        "member_since": "N/A",
        "total_investments": 0.00,
        "risk_tolerance": "N/A"
    }
