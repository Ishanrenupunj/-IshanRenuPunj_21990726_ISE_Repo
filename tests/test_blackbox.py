from services_loader import load_services_from_file
from calculator import find_tier_cost, calculate_service_total

services = load_services_from_file("services.csv")

# Normal case
assert find_tier_cost(100, [0,50,1000,8000], [0.62,0.58,0.55,0.52]) == 0.58

# Boundary case
assert find_tier_cost(50, [0,50,1000,8000], [0.62,0.58,0.55,0.52]) == 0.58

# Error case
try:
    find_tier_cost(-10, [0,50,1000,8000], [0.62,0.58,0.55,0.52])
except ValueError:
    print("Error case passed")

# Service total calculation
assert calculate_service_total(100, services["Compute"]) == 100*0.58

print("Black-box tests passed")
