class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int prev=nums[0];
        auto i=nums.begin()+1;
        while(i!=nums.end()){
            if(*i==prev)
                nums.erase(i);
            else{
                prev=*i;
                i++;
            }
        }
        return nums.size();
    }
};