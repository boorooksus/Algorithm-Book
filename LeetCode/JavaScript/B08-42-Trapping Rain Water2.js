/**
 * @param {number[]} height
 * @return {number}
 */
var trap = function (height) {
  stack = [];
  volume = 0;

  for (let i = 0; i < height.length; i++) {
    while (!!stack && height[stack[stack.length - 1]] < height[i]) {
      const top = stack.pop();
      if (stack.length === 0) {
        break;
      }
      const dist = i - stack[stack.length - 1] - 1;
      const water = Math.min(height[stack[stack.length - 1]], height[i]) - height[top];
      volume += dist * water;
    }
    stack.push(i);
  }

  return volume;
};

console.log(trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]));
