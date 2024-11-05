class Solution {
public:
    string makeFancyString(string s) {
        int count=1;
        char prev=' ';
        string str="";
        for(char c:s){
            if(c==prev){
                count++;
                if(count>=3){
                    continue;
                }
            }
            else count=1;
            prev=c;
            str+=c;
        }
        return str;
    }
};