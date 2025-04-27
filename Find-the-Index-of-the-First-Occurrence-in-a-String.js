/**
 * @param {string} haystack
 * @param {string} needle
 * @return {number}
 */
var strStr = function(haystack, needle) {
    let needle_length = needle.length
    let haystack_length = haystack.length

    for(let i = 0; i < haystack_length - needle_length + 1; i ++){
        if (haystack.substring(i, i + needle_length) == needle){
            return i
        }
}
    return -1
};