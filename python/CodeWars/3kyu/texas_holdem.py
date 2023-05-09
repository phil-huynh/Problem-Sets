# Texas Hold'em is a Poker variant in which each player is given two "hole cards". Players then proceed to make a series of bets while five "community cards" are dealt. If there are more than one player remaining when the betting stops, a showdown takes place in which players reveal their cards. Each player makes the best poker hand possible using five of the seven available cards (community cards + the player's hole cards).

# Possible hands are, in descending order of value:

# Straight-flush (five consecutive ranks of the same suit). Higher rank is better.
# Four-of-a-kind (four cards with the same rank). Tiebreaker is first the rank, then the rank of the remaining card.
# Full house (three cards with the same rank, two with another). Tiebreaker is first the rank of the three cards, then rank of the pair.
# Flush (five cards of the same suit). Higher ranks are better, compared from high to low rank.
# Straight (five consecutive ranks). Higher rank is better.
# Three-of-a-kind (three cards of the same rank). Tiebreaker is first the rank of the three cards, then the highest other rank, then the second highest other rank.
# Two pair (two cards of the same rank, two cards of another rank). Tiebreaker is first the rank of the high pair, then the rank of the low pair and then the rank of the remaining card.
# Pair (two cards of the same rank). Tiebreaker is first the rank of the two cards, then the three other ranks.
# Nothing. Tiebreaker is the rank of the cards from high to low.
# Given hole cards and community cards, complete the function hand to return the type of hand (as written above, you can ignore case) and a list of ranks in decreasing order of significance, to use for comparison against other hands of the same type, of the best possible hand.

# hand(["A♠", "A♦"], ["J♣", "5♥", "10♥", "2♥", "3♦"])
# # ...should return ("pair", ranks: ["A", "J", "10", "5"]})
# hand(["A♠", "K♦"], ["J♥", "5♥", "10♥", "Q♥", "3♥"])
# # ...should return ("flush", ["Q", "J", "10", "5", "3"])
# EDIT: for Straights with an Ace, only the ace-high straight is accepted. An ace-low straight is invalid (ie. A,2,3,4,5 is invalid). This is consistent with the author's reference solution.

def rank_value(x):
    if x == "J":
        return 11
    if x == "Q":
        return 12
    if x == "K":
        return 13
    if x == "A":
        return 14
    return int(x)

def sort_ranks(cards):
    cards.sort(key=rank_value)
    return cards

def hand_sort(x):
    return rank_value(x[0])

def sort_hand(cards):
    cards.sort(key=hand_sort)
    return cards

def get_card_info(cards):
    result = []
    for card in cards:
        if "10" not in card:
            result.append([card[:1], card[1:]])
        else:
            result.append([card[:2], card[2:]])
    result = sort_hand(result)
    return result

def check_for_flush(cards):
    checker = {}
    for card in cards:
        if card[1] not in checker:
            checker[card[1]] = [card[0]]
        else:
            checker[card[1]].insert(0, card[0])
    for key in checker:
        if len(checker[key]) >= 5:
            return True, checker[key]
    return False, None

def straight_check(cards):
    value = rank_value(cards[0])
    if len(cards) < 5:
        return None
    for i in range(len(cards)):
        if i == 0:
            pass
        else:
            if rank_value(cards[i]) == value - 1:
                value = rank_value(cards[i])
            else:
                return None
    return cards

def check_for_straights(cards, value_list):
    has_flush, flush_cards = check_for_flush(cards)
    straight_flush_hand = []
    straight_hand = []
    if has_flush:
        for i in range(3):
            try:
                straight_flush_hand = straight_check(flush_cards[i:i+5])
                if straight_flush_hand:
                    return straight_flush_hand, straight_hand
            except IndexError:
                break
    if not straight_flush_hand:
        for i in range(3):
            try:
                straight_hand = straight_check(value_list[i:i+5])
                if straight_hand:
                    return straight_flush_hand, straight_hand
            except IndexError:
                break
    return straight_flush_hand, straight_hand


def organize_card_info(card_info_list):
    card_values = {}
    value_list = []
    sets = {"four": [], "triples": [], "pairs": [], "remaining": []}
    for card in card_info_list:
        if card[0] not in card_values:
            card_values[card[0]] = 1
            value_list.insert(0, card[0])
        else:
            card_values[card[0]] += 1
    for card in card_values:
        if card_values[card] == 4:
            sets["four"].append(card)
        if card_values[card] == 3:
            sets["triples"].append(card)
        if card_values[card] == 2:
            sets["pairs"].append(card)

    sets["triples"].sort(reverse=True, key=rank_value)
    sets["pairs"].sort(reverse=True, key=rank_value)
    return sets, value_list

def hand(hole_cards, community_cards):
    all_cards = hole_cards + community_cards
    card_info_list = get_card_info(all_cards)
    sets, value_list = organize_card_info(card_info_list)
    straight_flush_hand, straight_hand = check_for_straights(card_info_list, value_list)
    if straight_flush_hand:
        return ("straight-flush", straight_flush_hand)

    if sets["four"]:
        four = value_list.pop(value_list.index(sets["four"][0]))
        value_list.insert(0, four)
        return ("four-of-a-kind", value_list[:2])

    if len(sets["triples"]) > 1:
        return ("full house", sets["triples"])

    if sets["triples"] and sets["pairs"]:
        sets["triples"].append(sets["pairs"][0])
        return ("full house", sets["triples"])

    has_flush, flush_hand = check_for_flush(card_info_list)
    if has_flush:
        flush_hand = flush_hand[:5]
        return ("flush", flush_hand)
    if straight_hand:
        return ("straight", straight_hand)
    if sets["triples"]:
        three = value_list.pop(value_list.index(sets["triples"][0]))
        value_list.insert(0, three)
        return ("three-of-a-kind", value_list[:3])
    if len(sets["pairs"]) > 1:
        result = sets["pairs"][:2]
        for value in value_list:
            if value not in sets["pairs"]:
                result.append(value)
                break
        return ("two pair", result)
    if sets["pairs"]:
        pair = value_list.pop(value_list.index(sets["pairs"][0]))
        value_list.insert(0, pair)
        return ("pair", value_list[:4])

    return ("nothing", value_list[:5])



print(hand(['A♠', '6♠'], ['7♠', '4♠', '7♥', '8♠', '5♠']))


