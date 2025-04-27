/**
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix = function(strs) {
    let lc = strs[0]

    for (let i=1; i < strs.length; i++){
        let cw = strs[i]
        let j = 0
        let k = 0
        while ( j < cw.length && k < lc.length && cw[j] == lc[k]){
            j += 1
            k += 1
        }
        lc = lc.substring(0,k)
    }
    return lc
};