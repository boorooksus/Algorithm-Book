/**
 * @param {string} s
 * @return {string}
 */
var removeDuplicateLetters = function (s) {
  const set = new Set(s);
  for (char of Array.from(set).sort()) {
    const suffix = s.slice(s.indexOf(char));
    if (isEqual(set, new Set(suffix))) {
      return char + removeDuplicateLetters(suffix.replaceAll(char, ""));
    }
  }
  return "";
};

const isEqual = (a, b) => {
  if (a.size !== b.size) {
    return false;
  }

  return Array.from(a).every((element) => {
    return b.has(element);
  });
};

console.log(removeDuplicateLetters("bcabc"));
