def model_based_agent(location, status):

    # Internal state
    if not hasattr(model_based_agent, "internal_state"):
        model_based_agent.internal_state = {
            "A": "Unknown",
            "B": "Unknown"
        }

    # Update state
    model_based_agent.internal_state[location] = status

    # If dirty, suck
    if status == "Dirty":
        return "Suck"

    # If both are clean, stop
    elif (model_based_agent.internal_state["A"] == "Clean"
          and model_based_agent.internal_state["B"] == "Clean"):
        return "Stop"

    # If at A, move right
    elif location == "A":
        return "Move Right"

    # If at B, move left
    elif location == "B":
        return "Move Left"


# MAIN PROGRAM
print("Output:")

print(model_based_agent("A", "Dirty"))
print(model_based_agent("A", "Clean"))
print(model_based_agent("B", "Dirty"))
print(model_based_agent("B", "Clean"))
