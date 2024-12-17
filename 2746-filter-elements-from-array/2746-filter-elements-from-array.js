/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function(arr, fn) {
    return arr.filter((ele,i)=>fn(ele,i))
};