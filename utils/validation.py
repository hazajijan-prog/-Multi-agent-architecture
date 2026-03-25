def validate_input(preferences):
    required_fields = ["destination", "budget"]

    missing = []
    for field in required_fields:
        if field not in preferences:
            missing.append(field)

    return missing