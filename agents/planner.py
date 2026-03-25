def planner(user_goal, preferences):
    plan = [
        "Search flights",
        "Search hotels",
        "Compare options",
        "Select best option within budget"
    ]

    print("-- PLANNER --")
    print("Goal:")
    print(user_goal)

    print("Steps:")
    for i, step in enumerate(plan, 1):
        print(f"{i}. {step}")

    return {
        "goal": user_goal,
        "plan": plan
    }