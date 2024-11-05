class Solution {
public:
    int strStr(string haystack, string needle) {
        for(int i=0; haystack.length()-i >= needle.length();i++)
            if(haystack.substr(i,needle.length())==needle) return i;
        return -1;
    }
};