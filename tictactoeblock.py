def block_spot(mark1, mark2):
    # Define the winning combinations
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]

    # Check each winning combination
    for combo in winning_combinations:
        # If one of the marks is already in the combination
        if mark1 in combo or mark2 in combo:
            # Find the empty spot in the combination
            for spot in combo:
                if spot != mark1 and spot != mark2:
                    return spot
    # If no blocking spot is found
    return None

# Example usage:
mark1 = 0  # Assume X is marked at position 0
mark2 = 4  # Assume O is marked at position 4
print(block_spot(mark1, mark2)) 