// console.log('\n')

/*
################################################
####  CONDITIONALS  ############################
################################################
*/

// const toggle = true


// toggle && console.log('\nResult of 2+2 on line 6:', 2+2, '\n')

// const ternary = toggle ? " ~ toggle is true" : " ~ toggle is false"

// console.log("🚀 ternary stored in variable:", ternary)
// console.log('\n')


// const show_if_true = () => console.log(" ~ toggle is true")
// const show_if_false = () => console.log(" ~ toggle is false")

// console.log("🚀 unassigned ternary ==> toggle ? show_if_true() : show_if_false()")
// toggle ? show_if_true() : show_if_false()


/*
################################################
####  SPREAD OPERATOR ARRAYS  ##################
################################################
*/


// const array1 = [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ]
// console.log("\n🚀 ~ array1:", array1)

// const array2 = [ 10, 20, 30, 40, 50, 60, 70, 80, 90 ]
// console.log("\n🚀 ~ array2:", array2)

// const array3 = [...array1, ...array2]
// console.log("\n🚀 ~ array3:", array3)


/*
################################################
####  SPREAD OPERATOR OBJECTS  #################
################################################
*/

// const obj1 = {
//   one: true,
//   two: true,
//   three: true,
// }

// const obj2 = {
//   four: true,
//   five: true,
//   six: true,
// }

// const obj3 = {
//   seven: true,
//   eight: true,
//   nine: true,
// }

// const obj4  = {...obj1, ...obj2, ...obj3}

// console.log("\n🚀 ~ Here is obj1:")
// console.log(obj1)

// console.log("\n🚀 ~ Here is obj2:")
// console.log(obj2)

// console.log("\n🚀 ~ Here is obj3:")
// console.log(obj3)

// console.log("\n🚀 ~ Here is obj4:")
// console.log(obj4)


/*
################################################
####  SPREAD OPERATOR FUNCTIONS  ###############
################################################
*/

// const showArgs = (...args) => console.log("Here are my args: ", args)

// console.log("\n🚀 ~ showArgs ")

// showArgs('one', 'two', 'three', 'four')


// const spreadArgs = (name, role, language) => {
//   console.log(" name:", name)
//   console.log(" role:", role)
//   console.log(" language:", language)
// }

// const info = ['Phil', 'SEIR', 'Javascript']

// console.log("\n🚀 ~ spreadArgs ")

// spreadArgs(...info)


// const infoObj = {
//   name: 'Phil',
//   role: 'SEIR',
//   language: 'Javascript',
// }

// const objArgs = () => {
//   console.log(" name:", name)
//   console.log(" role:", role)
//   console.log(" language:", language)
// }

// console.log("\n🚀 ~ objArgs ")

// objArgs({name, role, language} = infoObj)


// const objArgs2 = ({name, role, language}) => {
//   console.log(" name:", name)
//   console.log(" role:", role)
//   console.log(" language:", language)
// }

// console.log("\n🚀 ~ objArgs2")

// objArgs2(infoObj)

/*
################################################
####  FOR LOOPS  ##################
################################################
*/
// console.log('\n')

// const arr = [ 'Python', 'Javascript', 'CSS', 'HTML', 'React', 'Django']


// for (let i = 0; i < arr.length; i++) {
//   console.log("item:", arr[i], "is at index:", i)
// }


// console.log('\n')

// for (let item of arr) {
//   console.log("item:", item)
// }


/*
################################################
####  HIGHER ORDER FUNCTIONS  ##################
################################################
*/

// const array = [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ]

// const cache = {}

// filtered.forEach(num => cache[num] = true)
// console.log("\n🚀  .forEach() ")
// console.log("~ cache:", cache)

// const squares = array.map(num => num**2)

// console.log("\n🚀  .map() ")
// console.log("~ squares:", squares)
// console.log("~ array:", array)

// const filtered = array.filter(num => num % 2 === 0)
// console.log("\n🚀  .filter() ")
// console.log(" filtered:", filtered)

// const squared_sum = squares.reduce((total, num) => total + num, 0)
// console.log("\n🚀  .reduce() ")
// console.log("squared_sum:", squared_sum)

// console.log("\n🚀  Chaining functions => .map().reduce() ")
// const squared_sum2 = array.map(num => num**2).reduce((total, num) => total + num, 0)
// console.log("~ squared_sum2:", squared_sum2)

// console.log("\n🚀  Chaining functions => .map().filter().reduce() ")
// const squared_evens = array.map(num => num**2)
// .filter(num => num % 2 === 0)
// .reduce((total, num) => total + num, 0)
// console.log("~ squared_evens:", squared_evens)
