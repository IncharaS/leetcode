function maxArea(height: number[]): number {
    let i: number = 0;
    let j: number = height.length - 1;
    let max_: number = 0;

    while (i < j) {
        max_ = Math.max(max_, Math.min(height[i], height[j]) * (j - i));
        if (height[i] > height[j]) {
            j--;
        } else {
            i++;
        }
    }

    return max_;
}
