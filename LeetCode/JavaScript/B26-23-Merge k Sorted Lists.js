/**
 * 채점 결과 틀림
 */

// Definition for singly-linked list.
function ListNode(val, next) {
  this.val = val === undefined ? 0 : val;
  this.next = next === undefined ? null : next;
}

/**
 * @param {ListNode[]} lists
 * @return {ListNode}
 */
var mergeKLists = function (lists) {
  nodes = new Array();
  lists.forEach((element, i) => {
    if (!!element) {
      nodes.push([element.val, i, element]);
    }
  });

  const root = new ListNode();
  let cur = root;
  while (!!nodes) {
    nodes.sort((a, b) => a - b);
    [_, idx, node] = nodes.shift();
    cur.next = node;
    cur = cur.next;
    if (!!node && !!node.next) {
      nodes.push([node.next.val, idx, node.enxt]);
    }
  }
  return root.next;
};
