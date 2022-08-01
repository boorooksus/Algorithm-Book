/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function (strs) {
  const anagrams = {};
  for (word of strs) {
    const key = word.split("").sort().join("");
    if (anagrams[key] === undefined) {
      anagrams[key] = [word];
    } else {
      anagrams[key] = [...anagrams[key], word];
    }
  }
  return Object.values(anagrams);
};

console.log(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]));
