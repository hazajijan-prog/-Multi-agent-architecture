def get_user_input():
    user_goal = "I want to travel to Berlin with a low budget"

    preferences = {
        "destination": "Berlin",
        "budget": 8000
    }

    print("[User Input]")
    print("Goal:", user_goal)
    print("Preferences:", preferences)

    return user_goal, preferences