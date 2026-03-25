from utils.input_handler import get_user_input
from utils.validation import validate_input
from agents.planner import planner
from agents.doer import doer
from agents.critic import critic
from agents.human import human_review


def main():
    # Steg 1: User input
    user_goal, preferences = get_user_input()

    # Steg 2: Validation
    missing = validate_input(preferences)

    if missing:
        print("[Validation]")
        print("Not enough information")
        print("Missing:", missing)
        print("Returning to user")
        return

    print("[Validation]")
    print("Input is valid. Continue to Planner")

    # Steg 3: Planner
    plan_data = planner(user_goal, preferences)

    # Steg 4: Doer
    doer_data = doer(plan_data, preferences)

    options = doer_data["options"]

    # Visa alternativ + låt user välja
    choice = input("Select an option (1 or 2): ").strip()

    if not choice.isdigit():
        print("Invalid choice")
        return

    choice_index = int(choice) - 1

    if choice_index < 0 or choice_index >= len(options):
        print("Invalid choice")
        return

    selected_option = options[choice_index]

    # Steg 5: Critic
    critic_result = critic(selected_option, preferences)

    if not critic_result["approved"]:
        print("Selected option is not valid")
        return

    # Steg 6: Human in the loop
    approved = human_review(critic_result["best_option"])

    if not approved:
        print("Stopped by human")
        return

    # Steg 7: Output
    print("-- OUTPUT --")
    print(critic_result["best_option"])


if __name__ == "__main__":
    main()
    
    