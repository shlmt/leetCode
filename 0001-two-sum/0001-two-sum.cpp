class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> map = {};
        for(int i=0;i<nums.size();i++) map[nums[i]]=i;
        for(int i=0;i<nums.size();i++){
            int x = target-nums[i];
            if(map.count(x) && map[x]!=i)
                return {map[x],i};
        }  
        return {-1,-1};
    }
};