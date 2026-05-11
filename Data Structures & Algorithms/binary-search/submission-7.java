class Solution {
    public int search(int[] nums, int target) {
        int base_idx = 0;
        while (nums.length != 0) {
            int mid = nums.length / 2;
            if (nums[mid] == target) {
                return base_idx + mid;
            }
            else if (nums[mid] < target) {
                nums = Arrays.copyOfRange(nums, mid + 1, nums.length);
                base_idx += mid + 1;
            }
            else {
                nums = Arrays.copyOfRange(nums, 0, mid);
                base_idx += 0;
            }
        }
        return -1;
    }
}
