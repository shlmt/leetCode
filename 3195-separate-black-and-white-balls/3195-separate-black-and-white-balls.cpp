class Solution {
public:
    long long minimumSteps(string s) {
        long numOf1 = 0, swaps=0;
        for(char c:s){
            if(c=='1') numOf1++;
            else swaps+=numOf1;
        }
        return swaps;
    }
};