class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    getConcatenation(nums) {
        //NAIVE
        // let arr = []
        // for(let i = 0; i < 2; i++){
        //     console.log(i)
        //     for(let num of nums){
        //         arr.push(num);
        //     }
        // }
        // return arr;

        let b = nums.concat(nums)
        return b
    }
}
