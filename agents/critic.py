def critic(option, preferences):
    print("-- CRITIC --")

    budget = preferences["budget"]

    if option["price"] > budget:
        print("Option exceeds budget")
        
        decision = input("This option is over your budget. Continue anyway? (yes/no): ").strip().lower()

        if decision in ["yes", "y"]:
            print("User accepted higher cost")
            return {
                "approved": True,
                "best_option": option
            }

        print("User rejected due to budget")
        return {
            "approved": False,
            "best_option": None
        }

    print("Option is valid:")
    print(option)

    return {
        "approved": True,
        "best_option": option
    }