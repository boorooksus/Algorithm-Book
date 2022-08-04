/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
const reverse = (node, prev = null) => {
  if (!node) {
    return prev;
  }
  const next = node.next;
  node.next = prev;
  return reverse(next, node);
};

var reverseList = function (head) {
  return reverse(head);
};
