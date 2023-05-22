def draw(deck):
#     print_deck(deck, True)   # Using unicode characters
#     print_deck(deck, False)  # Using regular characters

    drawn_cards = []

    while deck:
        if len(deck) > 1:
            first_card = deck.pop(0)
            next_card = deck.pop(0)
            drawn_cards.append(first_card)
            deck.append(next_card)
        else:
            card = deck.pop(0)
            drawn_cards.append(card)
    if len(drawn_cards) % 2 == 0:
        result = [drawn_cards[:int(len(drawn_cards)/2)] ,drawn_cards[int(len(drawn_cards)/2):]]
    else:
        result = [drawn_cards[:int(str(len(drawn_cards)/2).split('.')[0]) + 1], drawn_cards[int(str(len(drawn_cards)/2).split('.')[0]) + 1:]]
    return [f"even deck({len(drawn_cards)}):" if len(drawn_cards) % 2 ==0 else f"odd deck ({len(drawn_cards)}):", f"even front({len(result[0])}):" if len(result[0]) % 2 ==0 else f"odd front ({len(result[0])}):" , result[1]],



# print("\n",draw([1, 2]))
# print("\n",draw([1, 2, 3]))
print(draw([1, 2, 3, 4]))
print(draw([1, 2, 3, 4, 5]))
print(draw([1, 2, 3, 4, 5, 6]))
print(draw([1, 2, 3, 4, 5, 6, 7]))
print("\n")
print(draw([1, 2, 3, 4, 5, 6, 7, 8]))
print(draw([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(draw([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(draw([1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ,11]))
print("\n")
print(draw([1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ,11 ,12]))
print(draw([1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ,11 ,12 ,13]))
print(draw([1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ,11 ,12 ,13 ,14]))
print(draw([1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ,11 ,12 ,13 ,14, 15]))
print("\n")
print(draw([1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ,11 ,12 ,13 ,14, 15, 16]))
print(draw([1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ,11 ,12 ,13 ,14, 15, 16, 17]))
print(draw([1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ,11 ,12 ,13 ,14, 15, 16, 17, 18]))
print(draw([1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ,11 ,12 ,13 ,14, 15, 16, 17, 18, 19]))
print("\n")
print(draw([1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ,11 ,12 ,13 ,14, 15, 16, 17, 18, 19, 20]))
print(draw([1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ,11 ,12 ,13 ,14, 15, 16, 17, 18, 19, 20, 21]))
print(draw([1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ,11 ,12 ,13 ,14, 15, 16, 17, 18, 19, 20, 21, 22]))
print(draw([1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ,11 ,12 ,13 ,14, 15, 16, 17, 18, 19, 20, 21, 22, 23]))
print("\n")
print(draw([1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ,11 ,12 ,13 ,14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]))
print(draw([1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ,11 ,12 ,13 ,14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]))
print(draw([1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ,11 ,12 ,13 ,14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]))
print(draw([1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ,11 ,12 ,13 ,14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27]))
print("\n")
print(draw([1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ,11 ,12 ,13 ,14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28]))
print(draw([1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ,11 ,12 ,13 ,14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]))
print(draw([1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ,11 ,12 ,13 ,14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]))
print(draw([1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ,11 ,12 ,13 ,14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]))
print("\n")
print(draw([1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ,11 ,12 ,13 ,14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32]))
print(draw([1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ,11 ,12 ,13 ,14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]))
print(draw([1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ,11 ,12 ,13 ,14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34]))
print(draw([1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ,11 ,12 ,13 ,14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]))
print("\n")
print(draw([1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ,11 ,12 ,13 ,14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]))
print(draw([1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ,11 ,12 ,13 ,14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37]))
print(draw([1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ,11 ,12 ,13 ,14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38]))
print(draw([1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ,11 ,12 ,13 ,14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39]))
print("\n")
print(draw([1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ,11 ,12 ,13 ,14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]))
print(draw([1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ,11 ,12 ,13 ,14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41]))
print(draw([1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ,11 ,12 ,13 ,14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42]))
print(draw([1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ,11 ,12 ,13 ,14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43]))