function add(a, b) {
  a = a.split("")
  b = b.split("")
  a.reverse()
  b.reverse()
  let carried = 0
  let result = []
  let top;
  let bottom;
  if (a.length >= b.length) {
    top = a
    bottom = b
  } else {
    top = b
    bottom = a
  }
  top.forEach((number, index) => {
    let total = 0
    if(carried == 1) {
      total = 1
    }
    if (bottom[index]) {
     total += (Number(number) + Number(bottom[index]))
    } else {
      total += Number(number)
    }
    if (total >= 10) {
      carried = 1
      total = total.toString()
      total = Number(total[1])
    } else {
      carried = 0
    }
    result.push(total)
    total = 0
    if (index === top.length - 1){
      if (carried === 1) {
        result.push(1)
      }
    }
  })
  result.reverse()
  return result.join("")
}