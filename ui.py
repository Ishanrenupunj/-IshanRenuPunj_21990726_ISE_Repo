from calculator import calculate_service_total, find_tier_cost

def display_service_structure(name, service):
    """
    Display pricing tiers for a service.
    
    Args:
        name (str): Service name
        service (dict): Service details
    """
    print(f"{name} ({service['unit']}):")
    thresholds = service['thresholds']
    costs = service['costs']
    for i in range(len(costs)):
        start = thresholds[i]
        end = thresholds[i+1] if i+1 < len(thresholds) else "∞"
        print(f"{start}-{end}: ${costs[i]} per {service['unit']}")

def list_subscriptions(subs, services):
    """
    Display all current subscriptions and usage.
    
    Args:
        subs (dict): Current subscription amounts
        services (dict): Service details
    """
    if not subs:
        print("No subscriptions yet.")
        return
    for name, amount in subs.items():
        unit = services[name]['unit']
        print(f"{name}: {amount} {unit}(s)")

def show_breakdown(subs, services):
    """
    Show detailed cost breakdown per service and total.
    
    Args:
        subs (dict): Current subscription amounts
        services (dict): Service details
    """
    total = 0
    print("Current cost breakdown:")
    for name, amount in subs.items():
        service = services[name]
        per_unit = find_tier_cost(amount, service['thresholds'], service['costs'])
        cost = calculate_service_total(amount, service)
        total += cost
        print(f"{name}: {amount} @ ${per_unit} = ${cost:.2f}")
    print(f"TOTAL: ${total:.2f}")
