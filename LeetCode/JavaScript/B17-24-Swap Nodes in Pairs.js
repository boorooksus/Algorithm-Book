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
var swapPairs = function (head) {
  if (!!head && !!head.next) {
    const b = head.next;
    [head.next, b.next] = [swapPairs(b.next), head];
    return b;
  }
  return head;
};
