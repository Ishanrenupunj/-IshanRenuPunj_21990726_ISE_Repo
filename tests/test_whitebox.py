from services_loader import load_services_from_file
from calculator import find_tier_cost, calculate_service_total

services = load_services_from_file("services.csv")

# White-box paths for find_tier_cost
assert find_tier_cost(0, [0,50,1000,8000], [0.62,0.58,0.55,0.52]) == 0.62
assert find_tier_cost(1500, [0,50,1000,8000], [0.62,0.58,0.55,0.52]) == 0.55
assert find_tier_cost(10000, [0,50,1000,8000], [0.62,0.58,0.55,0.52]) == 0.52

# White-box paths for calculate_service_total
assert calculate_service_total(0, services["Compute"]) == 0
assert calculate_service_total(10000, services["Compute"]) == 10000*0.52

print("White-box tests passed")
