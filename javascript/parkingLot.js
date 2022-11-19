// class Bike {
//   constructor(license) {
//     this.license = license
//   }
// }

// class Car {
//   constructor(license) {
//     this.license = license
//   }
// }
// class Van {
//   constructor(license) {
//     this.license = license
//   }
// }

// class ParkingLot {
//   constructor(size) {
//     this.size = size
//     this.spaces = new Array(size).fill("")
//   }

//   checkSpaces() {
//     let largest = 0
//     let count = 0
//     let index = 0
//     let results = []
//     this.spaces.forEach((space, i)=> {
//       if (space === "") {
//         if (count === 0) {
//           index = i
//         }
//         count += 1
//         if (i === this.spaces.length - 1) {
//           results.push([count, index])
//         }
//       }
//       else {
//         if (count !== 0) {
//           results.push([count, index])
//           count = 0
//         }
//       }
//     });
//     return results
//   }

//   park(vehicle) {
//     let vehicleType = vehicle.constructor.name
//     let spaceValue;
//     if (vehicleType=== 'Bike') {
//       spaceValue = 1
//     }
//     if (vehicleType === 'Car') {
//       spaceValue = 2
//     }
//     if (vehicleType === 'Van') {
//       spaceValue = 3
//     }
//     let availableSpaces = this.checkSpaces()
//     for (let space of availableSpaces) {
//       if (space[0] >= spaceValue) {
//         for(let i = space[1]; i <= space[1] + spaceValue - 1; i++) {
//           this.spaces[i] = vehicle.license
//         }
//         return true
//       }
//     }
//     return false
//   }

//   retrieve(license) {
//     if (!this.spaces.includes(license)) {
//       return false
//     }
//     this.spaces.forEach((plate, index) => {
//       if (plate === license) {
//         this.spaces[index] = "";
//       }
//     })
//     return true
//   }
// }



// lot = new ParkingLot(6)
// console.log(lot.spaces)

// const B1 = new Bike("B1")
// const B2 = new Bike("B2")
// const B3 = new Bike("B3")
// const B4 = new Bike("B4")
// const B5 = new Bike("B5")
// const B6 = new Bike("B6")

// const C1 = new Car("C1")
// const C2 = new Car("C2")
// const C3 = new Car("C3")
// const C4 = new Car("C4")
// const C5 = new Car("C5")
// const C6 = new Car("C6")

// lot.park(C1)
// console.log(lot.spaces)
// lot.park(B2)
// console.log(lot.spaces)
// lot.park(B3)
// lot.retrieve(B2.license)
// console.log(lot.spaces)
// lot.park(B4)
// console.log(lot.spaces)







// function add(a, b) {
//   console.log(a, b)
//   a = a.split("")
//   b = b.split("")
//   a.reverse()
//   b.reverse()
//   let carried = 0
//   let result = []
//   let top;
//   let bottom;
//   if (a.length >= b.length) {
//     top = a
//     bottom = b
//   } else {
//     top = b
//     bottom = a
//   }
//   top.forEach((number, index) => {
//     let total = 0
//     if(carried == 1) {
//       total = 1
//     }
//     if (bottom[index]) {
//      total += (Number(number) + Number(bottom[index]))
//     } else {
//       total += Number(number)
//     }
//     if (total >= 10) {
//       carried = 1
//       total = total.toString()
//       total = Number(total[1])
//     } else {
//       carried = 0
//     }
//     result.push(total)
//     total = 0
//   })
//   return result.reverse().join("")
// }






function nextBigger(n){
  n = n.toString()
  let index;
  let last;
  for (let i = n.length - 1; i >= 0; i--) {
    if (i === n.length - 1 && n[i] === 0) { continue }
    if (i === 0 && n[i] >= last) { return -1 }
    if (!last || Number(n[i] >= last)) { last = Number(n[i]) }
    else if (Number(n[i]) < last) {
      index = i
      break
    }

  }
  let front = n.slice(0, index)
  let end = n.slice(index)
  let lowest = end[1]
  let lowIndex = 1
  end = end.split('')
  for (let j = 1; j < end.length; j++) {
    if(Number(end[j]) < lowest && Number(end[0]) < Number(end[j])) {
      lowest = Number(end[j])
      lowIndex = j
    }
  }
  end[lowIndex] = end[0]
  end[0] = lowest.toString()
  let piece = end.slice(1)
  piece.sort()
  let final = [end[0]]
  piece.forEach((num) => {
    final.push(num)
  })
  final = final.join("")
  result = `${front}${final}`
  return Number(result)
}

console.log(nextBigger(91100))
  // let anagrams = {}
  // const getAnagrams = (combo, leftover) => {
  //   if (combo.length === piece.length) {
  //     anagrams[combo] = true
  //   }
  //   for (let i = 0; i < leftover.length; i++) {
  //     getAnagrams(combo + leftover[i], leftover.slice(0, i) + leftover.slice(i + 1))
  //   }
  // }
  // // getAnagrams("", piece)
  // let nums = []
  // for (key in anagrams) {
  //   if (Number(key) > Number(endString))
  //     nums.push(Number(key))
  // }
  // nums.sort()
  // let newEnd = `${nums[0]}`
  // let final = `${front}${newEnd}`

