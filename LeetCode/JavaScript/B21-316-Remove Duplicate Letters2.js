/**
 * @param {string} s
 * @return {string}
 */
var removeDuplicateLetters = function (s) {
  const counter = new Map(),
    seen = new Map(),
    stack = new Array();
  Array.from(s).forEach((char) => {
    counter.set(char, counter.get(char) ? counter.get(char) + 1 : 1);
  });

  for (char of s) {
    counter.set(char, counter.get(char) - 1);
    if (seen.get(char)) {
      continue;
    }
    while (!!stack.length && stack[stack.length - 1] > char && !!counter.get(stack[stack.length - 1])) {
      seen.set(stack.pop(), false);
    }

    stack.push(char);
    seen.set(char, true);
  }

  return stack.join("");
};

console.log(removeDuplicateLetters("cbacdcbccbb"));
