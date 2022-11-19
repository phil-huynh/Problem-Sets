def outcome(starting_player, matches):
    winner = starting_player
    for match in matches:
        if match[1] == winner:
            winner = match[0]
    return winner