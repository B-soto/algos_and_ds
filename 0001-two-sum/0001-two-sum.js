/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    
    let seen_set = {}
    
    for (let i = 0; i < nums.length; i++){
        let num = nums[i]
        let comp = target - num
        console.log(comp)
        
        if (comp in seen_set){
            return [i, seen_set[comp]]
        }else{
            seen_set[num] = i
        }
        
    }
    
};