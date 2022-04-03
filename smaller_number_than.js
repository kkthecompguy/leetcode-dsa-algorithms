
var smallerNumbersThanCurrent = function(nums) {
  
  let solution = []
  for(let i = 0; i < nums.length; i++){
      solution.push(nums.filter(x => x < nums[i]).length)
  }
  return solution
};