/**
 * @param {number[]} temperatures
 * @return {number[]}
 */
var dailyTemperatures = function (temperatures) {
  const answer = new Array(temperatures.length);
  answer.fill(0);
  const stack = new Array();
  for (i in temperatures) {
    while (!!stack.length && temperatures[stack[stack.length - 1]] < temperatures[i]) {
      const prev = stack.pop();
      answer[prev] = i - prev;
    }
    stack.push(i);
  }

  return answer;
};

console.log(dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]));
