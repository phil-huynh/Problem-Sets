def cash_on_hand(expenses):
    wallet = 30
    for expense in expenses:
        wallet += 30
        wallet -= expense
    return wallet