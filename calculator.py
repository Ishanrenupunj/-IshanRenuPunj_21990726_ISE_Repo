def find_tier_cost(amount, thresholds, costs):
    """
    Determine the per-unit cost based on the usage tier.
    
    Args:
        amount (float): Usage amount
        thresholds (list): Tier thresholds
        costs (list): Costs per tier
    
    Returns:
        float: Per-unit cost
    """
    for i in range(len(thresholds)-1):
        if thresholds[i] <= amount < thresholds[i+1]:
            return costs[i]
    return costs[-1]  # Last tier (open-ended)

def calculate_service_total(amount, service):
    """
    Calculate the total cost for a service.
    
    Args:
        amount (float): Amount of service used
        service (dict): Service details
    
    Returns:
        float: Total cost
    """
    per_unit_cost = find_tier_cost(amount, service['thresholds'], service['costs'])
    return amount * per_unit_cost
