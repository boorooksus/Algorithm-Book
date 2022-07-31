/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function (nums, target) {
  const indices = {};
  let res = [];
  for (let i = 0; i < nums.length; i++) {
    if (indices[target - nums[i]] > -1) {
      return [i, indices[target - nums[i]]];
    }
    indices[nums[i]] = i;
  }
};

console.log(twoSum([2, 7, 11, 15], 9));
