/*
https://www.codewars.com/kata/52bb6539a4cf1b12d90005b7/train/javascript

Write a method that takes a field for well-known board game "Battleship" as an argument and returns true if it has a valid disposition of ships, false otherwise. Argument is guaranteed to be 10*10 two-dimension array. Elements in the array are numbers, 0 if the cell is free and 1 if occupied by ship.

Battleship (also Battleships or Sea Battle) is a guessing game for two players. Each player has a 10x10 grid containing several "ships" and objective is to destroy enemy's forces by targetting individual cells on his field. The ship occupies one or more cells in the grid. Size and number of ships may differ from version to version. In this kata we will use Soviet/Russian version of the game.


Before the game begins, players set up the board and place the ships accordingly to the following rules:
There must be single battleship (size of 4 cells), 2 cruisers (size 3), 3 destroyers (size 2) and 4 submarines (size 1). Any additional ships are not allowed, as well as missing ships.
Each ship must be a straight line, except for submarines, which are just single cell.

The ship cannot overlap or be in contact with any other ship, neither by edge nor by corner.

This is all you need to solve this kata. If you're interested in more information
*/

const checkShips = (battleship, cruisers, destroyers, submarines) => {
  if (
    battleship === 1 &&
    cruisers === 2 &&
    destroyers === 3 &&
    submarines === 4
  ) { return true }
  return false
}

const nearOtherShips = (board, i, j) => {
  if (
    (j-1 >= 0 && board[i][j-1] === 2) ||
    (j-1 >= 0 && i-1>=0 && board[i-1][j-1] === 2) ||
    (i-1 >= 0 && board[i-1][j] === 2 ) ||
    (i-1 >= 0 && j+1 < board.length && board[i-1][j+1] === 2) ||
    (j+1 < board.length && board[i][j+1] === 2) ||
    (i+1 < board.length && j+1 < board.length && board[i+1][j+1] === 2 ) ||
    (i+1 < board.length && board[i+1][j] === 2 ) ||
    (i+1 < board.length && j-1>=0 && board[i+1][j-1] === 2)
  ) { return true }
  return false
}

const boatCheckRow = (board, i, j) => {
  let [count, square] = [0, board[i][j]]
  while (square === 1 && j < 10) {
    board[i][j] = 2
    count++
    j++
    square = board[i][j]
  }
  return count
}

const boatCheckCol = (board, i, j) => {
  let [count, square] = [0, board[i][j]]
  while (square === 1 && i < 10) {
    board[i][j] = 2
    count++
    i++
    square = board[i][j]
  }
  return count
}

function validateBattlefield(field) {
  const ships = { bat: 0, cru: 0, des: 0, sub: 0 }
  const shipLengths = { 4: "bat", 3: "cru", 2: "des"}
  field.forEach((row, i) => {
    row.forEach((square, j) => {
      if (square === 1) {
        if (nearOtherShips(field, i, j)) { return false }
        let across = boatCheckRow(field, i, j)
        field[i][j] = 1
        let down = boatCheckCol(field, i, j)
        if (across === 1 && down === 1) {
          ships.sub++
        }
        if (across > down) {
          if (down > 1) { return false }
          ships[shipLengths[across]]++
        }
        if (down > across) {
          if (across > 1) { return false }
          ships[shipLengths[down]]++
        }
      }
    })
  })
  return checkShips(ships.bat, ships.cru, ships.des, ships.sub)
}




//TEST is TRUE
  let test = [
              [1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
              [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
              [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
              [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
              [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
              [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            ]

let testResult = validateBattlefield(test)
