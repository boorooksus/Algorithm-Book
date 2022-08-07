/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function (s) {
  const table = {
    "(": ")",
    "{": "}",
    "[": "]",
  };

  stack = new Array();

  for (c of s) {
    if (!!table[c]) {
      stack.push(c);
    } else {
      if (stack.length === 0 || c !== table[stack.pop()]) {
        return false;
      }
    }
  }

  return !stack.length;
};
