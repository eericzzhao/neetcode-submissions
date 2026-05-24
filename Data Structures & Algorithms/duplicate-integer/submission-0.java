class Solution{
    public boolean containsDuplicate(int[] nums){
        HashSet<Integer> unseen = new HashSet<>();
        for (int num : nums){
            if (unseen.contains(num))
                return true;
            unseen.add(num);
        }
        return false;
    }
}