/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var addTwoNumbers = function (l1, l2) {
  const root = new ListNode();
  let node = root;
  let carry = 0;

  while (l1 || l2 || carry) {
    let sum = 0;
    if (!!l1) {
      sum += l1.val;
      l1 = l1.next;
    }
    if (!!l2) {
      sum += l2.val;
      l2 = l2.next;
    }
    sum += carry;
    [sum, carry] = [sum % 10, Number(sum >= 10)];

    node.next = new ListNode(sum);
    node = node.next;
  }

  return root.next;
};
