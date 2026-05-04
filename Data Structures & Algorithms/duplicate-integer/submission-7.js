class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    /* 
    Set removes the duplicate
    Therefore if Set size and array are equal no dupllicate => False
    else  hasDup and is True
    */
    hasDuplicate(nums) {
        const numsAsSet = new Set(nums).size !== nums.length;
        return numsAsSet;
    }
}
