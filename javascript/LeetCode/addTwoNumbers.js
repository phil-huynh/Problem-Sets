
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */

function ListNode(val, next) {
  this.val = (val===undefined ? 0 : val)
  this.next = (next===undefined ? null : next)
}

const sumCol = (val1, val2, carried) => {
    let total = val1 + val2 + carried
    let [result, carry] = total < 10 ? [total, 0] : [Number(total.toString().split('')[1]), 1]
    return [result, carry]
}

const addTwoNumbers = function(l1, l2) {
  const final = new ListNode(0, null)
  let [node, carried] = [final, 0]
  while (l1 || l2) {
      let num1 = l1 ? l1.val : 0
      let num2 = l2 ? l2.val : 0
      let colResult = sumCol(num1, num2, carried)
      node.val = colResult[0]
      carried = colResult[1]
      l1 = l1 ? l1.next : null
      l2 = l2 ? l2.next : null
      if (l1 || l2) {
        node.next = new ListNode(0, null)
        node = node.next
      }
      else {
          carried ? node.next = new ListNode(carried, null) : null
      }
  }
  return final
};