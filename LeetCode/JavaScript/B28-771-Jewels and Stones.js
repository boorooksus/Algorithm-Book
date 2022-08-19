/**
 * @param {string} jewels
 * @param {string} stones
 * @return {number}
 */
var numJewelsInStones = function (jewels, stones) {
  return Array.from(stones).filter((stone) => jewels.includes(stone)).length;
};
