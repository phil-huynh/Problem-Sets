/*
https://www.codewars.com/kata/5a3141fe55519e04d90009d8/train/javascript

Lеt's create function to play cards. You receive 3 arguments: card1 and card2 are cards from a single deck; trump is the main suit, which beats all others.

You have a preloaded deck (in case you need it):

deck = ["joker","2♣","3♣","4♣","5♣","6♣","7♣","8♣","9♣","10♣","J♣","Q♣","K♣","A♣",
                "2♦","3♦","4♦","5♦","6♦","7♦","8♦","9♦","10♦","J♦","Q♦","K♦","A♦",
                "2♥","3♥","4♥","5♥","6♥","7♥","8♥","9♥","10♥","J♥","Q♥","K♥","A♥",
                "2♠","3♠","4♠","5♠","6♠","7♠","8♠","9♠","10♠","J♠","Q♠","K♠","A♠"]
Game rules
If both cards have the same suit, the higher one wins
If both cards have trump, the higher one wins
If the cards have different suits and no one has trump, return "Let us play again."
If one card has trump, but not the other, the one with the trump wins
If there is a winner, return "The first/second card won."
If the two cards are the same, return "Someone cheats."
The joker always wins
Examples
"3♣", "Q♣", "♦"  -->  "The second card won."
"5♥", "A♣", "♦"  -->  "Let us play again."
"8♠", "8♠", "♣"  -->  "Someone cheats."
"2♦", "A♠", "♦"  -->  "The first card won."
"joker", "joker", "♦"  -->  "Someone cheats."
*/

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