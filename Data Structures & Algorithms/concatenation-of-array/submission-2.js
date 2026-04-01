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

        let n = nums.length;
        let newArr = Array( 2 * n)

        for(let i = 0; i < n; i ++){
            newArr[i] = nums[i]
        }

        for(let i = 0; i < n; i ++){
            newArr[i + n] = nums[i]
        }

        return newArr;

    }
}
