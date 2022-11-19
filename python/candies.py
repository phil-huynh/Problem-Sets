def nia_eat(favorite_color, candy):
    pile = []
    favorites = candy.copy()
    indexes = []
    time = 0
    for i, piece in enumerate(candy):
        if piece != favorite_color:
            pile.append(piece)
            indexes.insert(0, i)

    for index in indexes:
        favorites.pop(index)

    if pile:
        time += 17

    for favorite in favorites:
        time += 23

    return time

candies = [
  "red", "yellow", "red", "green", "yellow", "brown",
  "green",  "brown", "brown", "brown", "brown", "brown",
  "blue", "green"
]

print(nia_eat("brown", candies))