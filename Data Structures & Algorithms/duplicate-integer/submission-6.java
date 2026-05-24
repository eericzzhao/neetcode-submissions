class Solution {
    public boolean hasDuplicate(int[] nums) {
        Set<Integer> seen = new HashSet<>();
        for (num: nums) {
            if (seen.contains(num)){
                return true;
            }
            seen.add(num);
        }
        return false;
    }
}