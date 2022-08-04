/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function (nums) {
  const res = new Array(nums.length);
  let multi = 1;
  for (let i = 0; i < nums.length; i++) {
    res[i] = multi;
    multi *= nums[i];
  }
  multi = 1;
  for (let i = nums.length - 1; i >= 0; i--) {
    res[i] *= multi;
    multi *= nums[i];
  }

  return res;
};

console.log(productExceptSelf([1, 2, 3, 4]));
