function twoSum(nums: number[], target: number): number[] {
  const map: Map<number, number> = new Map<number, number>();
  for (let idx = 0; idx < nums.length; idx++) {
    const cur = target - nums[idx];
    const match = map.get(cur);
    if (match !== undefined) {
      return [idx, match];
    }
    map.set(nums[idx], idx);
  }
  return [];
}

console.log(twoSum([2, 7, 11, 15], 9));
