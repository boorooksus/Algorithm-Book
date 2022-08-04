/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function (prices) {
  let low = Infinity,
    res = 0;
  for (price of prices) {
    res = Math.max(price - low, res);
    low = Math.min(price, low);
  }
  return res;
};

console.log(maxProfit([7, 1, 5, 3, 6, 4]));
