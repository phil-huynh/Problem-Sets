/*
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */

function ListNode(val, next) {
  this.val = (val===undefined ? 0 : val)
  this.next = (next===undefined ? null : next)
}
 
var addTwoNumbers = function(l1, l2) {
  var l3 = new ListNode();
  var carry = true;

};