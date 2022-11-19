def half_time_scores(
    game_length,
    team_1_score_times,
    team_2_score_times
    ):
    game_length =  60 * game_length
    half_time = game_length/2
    total = 0
    for time in team_1_score_times:
        if time < half_time:
            total += 1
    for time in team_2_score_times:
        if time < half_time:
            total += 1
    return total