class Solution {
public:
    int lengthOfLastWord(string s) {
        reverse(s.begin(), s.end());
        bool start = false;
        int len = 0;
        for(char c:s){
            if(c==' '){
                if(start) break;
                else continue;
            } 
            else{
                start=true;
                len++;
            }
        }
        return len;
    }
};