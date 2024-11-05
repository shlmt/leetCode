class Solution {
    public int search(int[] nums, int target) {
        int i=0;
        int j=nums.length;
        while(j>i){
        int m=(int)i+(j-i)/2;
        if(nums[m]==target)
            return m;
        if(nums[m]<target)
            i=m+1;
        else if(nums[m]>target)
            j=m;
        }
        return -1;
    }
}