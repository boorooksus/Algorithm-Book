/**
 * @param {number[]} nums
 * @return {number}
 */
var arrayPairSum = function (nums) {
  let res = 0;
  nums
    .sort((a, b) => a - b)
    .forEach((val, i) => {
      if (i % 2 == 0) {
        res += val;
      }
    });

  return res;
};
