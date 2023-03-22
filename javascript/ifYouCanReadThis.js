const NATO = {
  a: 'Alfa',
  n: 'November',
  b: 'Bravo',
  o: 'Oscar',
  c: 'Charlie',
  p: 'Papa',
  d: 'Delta',
  q: 'Quebec',
  e: 'Echo',
  r: 'Romeo',
  f: 'Foxtrot',
  s: 'Sierra',
  g: 'Golf',
  t: 'Tango',
  h: 'Hotel',
  u: 'Uniform',
  i: 'India',
  v: 'Victor',
  j: 'Juliett',
  w: 'Whiskey',
  k: 'Kilo',
  x: 'Xray',
  l: 'Lima',
  y: 'Yankee',
  m: 'Mike',
  z: 'Zulu'
}

function to_nato(words) {
	const punctuation = [',', '.', '!', '?']
  let result = ''
  words.split('').forEach((letter, i, words) => {
    if (NATO[letter.toLowerCase()]) { result += `${NATO[letter.toLowerCase()]}` }
    if (punctuation.includes(letter)) { result += `${letter}` }
    if (i !== words.length - 1 && letter !== ' ') { result += ' ' }
  })
  return result
}