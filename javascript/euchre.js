function cardGame(card1, card2, trump) {
  const p1win = "The first card won."
  const p2win = "The second card won."

  if (card1 === card2) {
    return "Someone cheats."
  }
  if (card1 === "joker" || card2 === "joker") {
    return card1 === "joker" ? p1win : p2win
  }

  const isTrumpCard = (card) => card.split('').includes(trump)
  const values = { "A": 14, "K": 13, "Q": 12, "J": 11 }

  const getCardValue = (card) => {
    let value = card.slice(0, card.length - 1)
    return Object.keys(values).includes(value) ? values[value] : Number(value)
  }

  const value1 = getCardValue(card1)
  const value2 = getCardValue(card2)

  if (isTrumpCard(card1) && isTrumpCard(card2)) {
    return value1 > value2 ? p1win : p2win
  }
  if (isTrumpCard(card1) || isTrumpCard(card2)) {
    return isTrumpCard(card1) ? p1win : p2win
  }
  if (card1[card1.length - 1] === card2[card2.length - 1]) {
    return value1 > value2 ? p1win : p2win
  }
  return "Let us play again."
}