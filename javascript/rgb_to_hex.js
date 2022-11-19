const conversions = {
  "0": "0",
  "1": "1",
  "2": "2",
  "3": "3",
  "4": "4",
  "5": "5",
  "6": "6",
  "7": "7",
  "8": "8",
  "9": "9",
  "10": "A",
  "11": "B",
  "12": "C",
  "13": "D",
  "14": "E",
  "15": "F",
}


const rgb = (r, g, b) => {
  const color = [r, g, b]
  const colors = color.map((num) => {
    let first = Math.floor(num/16)
    let second = Math.floor(((num/16) - first) * 16)
    return `${conversions[first.toString()]}${conversions[second.toString()]}`
  })
  return colors.join('')
}






// const singleHex = (num) =>{
//   first = Math.floor(num/16)
//   second =Math.floor(((num/16) - first) * 16)
//   return `${conversions[str(first)]}${conversions[str(second)]}`
// }
