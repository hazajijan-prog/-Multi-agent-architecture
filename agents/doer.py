def doer(plan_data, preferences):
    print("-- DOER --")

    destination = preferences["destination"]

    options = [
        {"destination": destination, "price": 5000, "flight": "Flight A", "hotel": "Hotel X"},
        {"destination": destination, "price": 9000, "flight": "Flight B", "hotel": "Hotel Y"}
    ]

    print("Available options:")
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")

    return {
        "options": options
    }