public class Solution {
    public bool ContainsNearbyDuplicate(int[] nums, int k) {
        if(k==0) return false;
        HashSet<int> set = new HashSet<int>();
        for(int i=0; i<nums.Length; i++){
            if(set.Contains(nums[i])) return true;
            if(i-k >= 0) set.Remove(nums[i-k]); // or if set.Count()>k
            set.Add(nums[i]);
        }
        return false;
    }
}