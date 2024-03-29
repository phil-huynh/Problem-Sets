/*
https://www.codewars.com/kata/52a723508a4d96c6c90005ba/train/javascript

Complete the function that returns the lyrics for the song 99 Bottles of Beer as an array of strings: each line should be a separate element - see the example at the bottom.

Note: in order to avoid hardcoded solutions, the size of your code is limited to 1000 characters

Lyrics
99 bottles of beer on the wall, 99 bottles of beer.
Take one down and pass it around, 98 bottles of beer on the wall.

98 bottles of beer on the wall, 98 bottles of beer.
Take one down and pass it around, 97 bottles of beer on the wall.

...and so on...

3 bottles of beer on the wall, 3 bottles of beer.
Take one down and pass it around, 2 bottles of beer on the wall.

2 bottles of beer on the wall, 2 bottles of beer.
Take one down and pass it around, 1 bottle of beer on the wall.

1 bottle of beer on the wall, 1 bottle of beer.
Take one down and pass it around, no more bottles of beer on the wall.

No more bottles of beer on the wall, no more bottles of beer.
Go to the store and buy some more, 99 bottles of beer on the wall.

Example
[ "99 bottles of beer on the wall, 99 bottles of beer.",
  "Take one down and pass it around, 98 bottles of beer on the wall.",
  "98 bottles of beer on the wall, 98 bottles of beer.",

  ...and so on...

  "3 bottles of beer on the wall, 3 bottles of beer.",
  "Take one down and pass it around, 2 bottles of beer on the wall.",
  "2 bottles of beer on the wall, 2 bottles of beer.",
  "Take one down and pass it around, 1 bottle of beer on the wall.",
  "1 bottle of beer on the wall, 1 bottle of beer.",
  "Take one down and pass it around, no more bottles of beer on the wall.",
  "No more bottles of beer on the wall, no more bottles of beer.",
  "Go to the store and buy some more, 99 bottles of beer on the wall." ]

  */

const what = 'of beer'
const where = "on the wall"
const bottle = (num) => num === 1 ? 'bottle' : 'bottles';
const howMany = (num) => num === 0 ? num = 'no more' : num;
const lineOne = (num) => `${num} ${bottle(num)} ${what} ${where}, ${num} ${bottle(num)} ${what}.`
const lineTwo = (num) => `Take one down and pass it around, ${howMany(num)} ${bottle(num)} ${what} ${where}.`
const finalVerse = (arr) => {
  arr.push(`No more bottles ${what} ${where}, ${howMany(0)} ${bottle(0)} ${what}.`)
  arr.push(`Go to the store and buy some more, ${howMany(0)} ${bottle(0)} ${what} ${where}.`)
}

const sing = () => {
  const song = [];
  let beers = 99;
  while (beers) {
    song.push(lineOne(beers));
    beers--;
    song.push(lineTwo(beers));
  }
  finalVerse(song)
  return song
}