class Solution {
    public int[] getConcatenation(int[] nums) {
        int[] ans=new int[nums.length*2];
        int k=0;
        for(int i=0;i<2;i++){
            for(int j=0;j<nums.length;j++){
                ans[k++]=nums[j];
            }
        }
        return ans;
    }
}