class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        string a = strs[0];
        int N = strs.size(), count;
        while(true){
            count=0;
            for(string s:strs)
                if(s.starts_with(a)) count++;
            if(count==N) return a;
            a=a.substr(0,a.length()-1);
        }
    }
};