def calculate_playlist(button_pushes):
    episodes = ["A", "B", "C", "D", "E"]

    for press in button_pushes:
        if press == 1:
            episodes[0], episodes[1] = episodes[1], episodes[0]
        if press == 2:
            moved = episodes.pop(0)
            episodes.append(moved)
        if press == 3:
            moved = episodes.pop(4)
            episodes.insert(0, moved)

    return episodes