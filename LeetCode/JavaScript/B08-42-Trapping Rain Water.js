/**
 * @param {number[]} height
 * @return {number}
 */
var trap = function (height) {
  let left = 0,
    right = height.length - 1;
  let leftMax = height[left],
    rightMax = height[right];
  let volume = 0;
  while (left < right) {
    if (leftMax < rightMax) {
      volume += leftMax - height[left];
      left += 1;
      leftMax = Math.max(height[left], leftMax);
    } else {
      volume += rightMax - height[right];
      right -= 1;
      rightMax = Math.max(height[right], rightMax);
    }
  }
  return volume;
};

console.log(trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]));
