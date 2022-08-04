function ListNode(val, next) {
  this.val = val === undefined ? 0 : val;
  this.next = next === undefined ? null : next;
}

/**
 * @param {ListNode} head
 * @return {boolean}
 */
var isPalindrome = function (head) {
  let slow = head,
    fast = head,
    rev = null;
  while (!!fast && !!fast.next) {
    fast = fast.next.next;
    [rev, rev.next, slow] = [slow, rev, slow.next];
  }
  if (!!fast) {
    slow = slow.next;
  }
  while (!!rev && slow.val === rev.val) {
    [slow, rev] = [slow.next, rev.next];
  }
  return !!!rev;
};

console.log(isPalindrome([1, 2, 2, 1]));
