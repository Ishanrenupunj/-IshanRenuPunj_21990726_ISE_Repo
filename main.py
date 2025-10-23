from services_loader import load_services_from_file
from calculator import calculate_service_total, find_tier_cost
from ui import display_service_structure, list_subscriptions, show_breakdown

def main():
    # Load services data from CSV
    services = load_services_from_file("services.csv")
    subscriptions = {}  # Stores user subscription amounts
    
    while True:
        # Display menu
        print("\nWelcome to ICSC – ISE Cloud Services Calculator")
        print("Add subscription for:")
        for i, name in enumerate(services, start=1):
            print(f"{i}) {name}")
        print("s) List subscriptions")
        print("$) Show cost breakdown")
        print("q) Quit")
        
        choice = input("> ").strip()
        
        # Quit program
        if choice.lower() == 'q':
            break
        # List subscriptions
        elif choice.lower() == 's':
            list_subscriptions(subscriptions, services)
        # Show cost breakdown
        elif choice == '$':
            show_breakdown(subscriptions, services)
        # Add/modify subscription
        elif choice.isdigit() and 1 <= int(choice) <= len(services):
            service_name = list(services.keys())[int(choice)-1]
            service = services[service_name]
            display_service_structure(service_name, service)
            amount = input(f"Enter new {service['unit']} amount: ").strip()
            try:
                subscriptions[service_name] = float(amount)
            except ValueError:
                print("Invalid input, please enter a number.")
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
