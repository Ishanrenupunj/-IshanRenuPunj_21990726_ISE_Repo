import csv

def load_services_from_file(path):
    """
    Load service details (thresholds, costs, units) from a CSV file.
    
    Args:
        path (str): Path to services.csv
    
    Returns:
        dict: Service data in the format:
            {service_name: {'unit': str, 'thresholds': list, 'costs': list}}
    """
    services = {}
    with open(path, newline='') as f:
        reader = csv.reader(f)
        rows = list(reader)
    
    i = 0
    while i < len(rows):
        name, unit = rows[i]                 # Service name and unit
        thresholds = list(map(float, rows[i+1]))  # Tier limits
        costs = list(map(float, rows[i+2]))       # Cost per tier
        services[name] = {
            'unit': unit,
            'thresholds': thresholds,
            'costs': costs
        }
        i += 3  # Move to the next service
    return services
