var lengthOfLongestSubstring = function(s) {
    let i = 0, j = 0;
    let maxLength = 0;
    const mySet = new Set();

    while (j < s.length) {
        if (!mySet.has(s[j])) {
            mySet.add(s[j]);
            maxLength = Math.max(maxLength, j - i + 1);
            j++;
        } else {
            mySet.delete(s[i]);
            i++;
        }
    }
    return maxLength;
};
