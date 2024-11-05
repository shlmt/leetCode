class Solution {
public:
    bool isPalindrome(int x) {
        string num = to_string(x);
        string revNum = num;
        reverse(revNum.begin(),revNum.end());
        return x>-1 && revNum==num;
    }
};