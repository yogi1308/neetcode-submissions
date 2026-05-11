class Solution {
    public int search(int[] nums, int target) {
        Boolean found = false;
        int[] new_nums = Arrays.copyOf(nums, nums.length);
        int idx = -1;
        int base_idx = 0;
        while (!found && new_nums.length != 0) {
            int mid = new_nums.length / 2;
            if (new_nums[mid] == target) {
                idx = base_idx + mid;
                found = true;;}
            else if (new_nums[mid] < target) {
                new_nums = Arrays.copyOfRange(new_nums, mid + 1, new_nums.length);
                base_idx += mid + 1;}
            else {
                new_nums = Arrays.copyOfRange(new_nums, 0, mid);
                base_idx += 0;}
        }
        return idx;

    }
}
