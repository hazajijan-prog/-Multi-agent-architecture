def human_review(best_option):
    print("-- HUMAN IN THE LOOP --")
    print("Option to review:")
    print(best_option)

    decision = input("Approve this option? (yes/no): ").strip().lower()

    if decision in ["yes", "y"]:
        print("Approved")
        return True

    if decision in ["no", "n"]:
        print("Rejected")
        return False

    print("Invalid input, treating as rejection")
    return False