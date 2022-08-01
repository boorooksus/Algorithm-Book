/**
 * @param {string} paragraph
 * @param {string[]} banned
 * @return {string}
 */
var mostCommonWord = function (paragraph, banned) {
  const words = paragraph
    .toLowerCase()
    .replace(/[^a-z]/g, " ")
    .split(" ");
  const counts = new Map();

  for (word of words) {
    if (word && !banned.includes(word)) {
      const count = counts.get(word);
      if (count) {
        counts.set(word, count + 1);
      } else {
        counts.set(word, 1);
      }
    }
  }
  return Array.from(counts.entries()).sort((a, b) => (a[1] < b[1] ? 1 : -1))[0][0];
};

console.log(mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]));
