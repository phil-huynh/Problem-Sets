def calories(entree_num, side_num, dessert_num, drink_num):
    entrees = {
      0: 0,
      1: 522,
      2: 399,
      3: 501
    }
    sides = {
      0: 0,
      1: 130,
      2: 125,
      3: 72
    }
    desserts = {
      0: 0,
      1: 222,
      2: 391,
      3: 100
    }
    drinks = {
      0: 0,
      1: 10,
      2: 8,
      3: 120
    }
    return entrees[entree_num] + sides[side_num] + desserts[dessert_num] + drinks[drink_num]




def total_song_knowers(num_villagers, attendees_lists):
    songlists= {}
    all_songs = 0
    knows_all_songs = 0
    for villager in range(num_villagers):
        songlists[villager + 1] = []
    for i, night in enumerate(attendees_lists):
        if 0 in night:
            all_songs += 1
            for person in songlists:
                if person in night:
                    songlists[person].append(i)
        else:
            jam_session = {}
            for person in night:
                for tune in songlists[person]:
                    jam_session[tune] = True
            jam_session = list(jam_session.keys())
            for person in night:
                songlists[person] = jam_session.copy()

    for villager in songlists:
        if len(songlists[villager]) == all_songs:
            knows_all_songs += 1
    return knows_all_songs

# print(total_song_knowers(3, [[0, 1], [1, 2, 3], [3, 1, 0]]))
# print(total_song_knowers(4, [[0, 2], [1, 0], [1, 0, 3, 4]]))
# print(total_song_knowers(7, [[0, 2, 4, 3], [4, 5], [5, 6, 7], [5, 1], [1, 5, 7, 0]]))





ref = {
  "0": '0',
  "1": '1',
  "2": 'ABC',
  "3": 'DEF',
  "4": 'GHI',
  "5": 'JKL',
  "6": 'MNO',
  "7": 'PQRS',
  "8": 'TUV',
  "9": 'WXYZ'
}

def find_combos(combo, digits, combos):
    if len(digits) == 0:
        combos.append(combo)
        return
    letters = []
    [letters.append(letter) for letter in ref[digits[0]]]
    for letter in letters:
        find_combos(combo + letter, digits[1:], combos)

def translate(words, digits):
    digits = str(digits)
    combos = []
    total = 0
    find_combos("", digits, combos)
    for combination in combos:
        if combination in words:
            total += 1
    return total

# print(translate(['TOMO', 'MONO', 'DAK'], 6666))
print(translate(['DOM', 'FON', 'TOM'], 366))
# print(translate(['JA', 'LA'], 52))