function solution(list){
  let index = 1, result = '', storage = [list[0]]
  while(index < list.length) {
    if(list[index] === storage[storage.length - 1] + 1) { storage.push(list[index]) }
    else {
      if (storage.length >= 3) { result += `${storage[0]}-${storage[storage.length - 1]},` }
      else if (storage.length === 2) { result += `${storage[0]},${storage[1]},` }
      else { result += `${storage[0]},` }
      storage = [list[index]]
    }
    index++
   }
   if (storage.length >= 3) { result += `${storage[0]}-${storage[storage.length - 1]}` }
   else if (storage.length === 2) { result += `${storage[0]},${storage[1]}` }
   else { result += `${storage[0]}` }
   return result
 }
