function tapCodeTranslation(text) {
  const letters = ['abcde', 'fghij', 'lmnop', 'qrstu', 'vwxyz']
  const ref = {}
  letters.forEach((group,i) => group.split('').forEach((letter, j) => ref[letter] = [i+1, j+1]))
  ref["k"] = [1,3]
}