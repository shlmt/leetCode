class Solution {
public:
    int finalValueAfterOperations(vector<string>& operations) {
        int num=0;
        for(string s:operations){
            if(s.find("++")!=-1) num++;
            else if(s.find("--")!=-1)num--;
        }
        return num;
    }
};