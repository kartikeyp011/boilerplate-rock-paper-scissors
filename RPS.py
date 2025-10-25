# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

def player(prev_play, opponent_history=[]):
    # Save opponent's move
    if prev_play != "":
        opponent_history.append(prev_play)

    # Use this many last moves to find patterns
    pattern_length = 4  

    # If not enough history, just play "R"
    if len(opponent_history) < pattern_length:
        return "R"

    # Get the last pattern of moves
    recent_pattern = opponent_history[-pattern_length:]

    # Dictionary to count what usually follows each pattern
    pattern_dict = {}

    # Build the pattern dictionary from the full history
    for i in range(len(opponent_history) - pattern_length):
        pattern = tuple(opponent_history[i:i + pattern_length])
        next_move = opponent_history[i + pattern_length]
        if pattern not in pattern_dict:
            pattern_dict[pattern] = {"R": 0, "P": 0, "S": 0}
        pattern_dict[pattern][next_move] += 1

    # Predict opponent's next move based on the most likely continuation
    predicted_move = "R"
    recent_tuple = tuple(recent_pattern)
    if recent_tuple in pattern_dict:
        predicted_move = max(pattern_dict[recent_tuple], key=pattern_dict[recent_tuple].get)

    # Counter the predicted move
    counter = {"R": "P", "P": "S", "S": "R"}
    return counter[predicted_move]
