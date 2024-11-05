class Solution {
public:
    bool isValid(string s) {
        stack<char> st;
        unordered_map<char, char> brackets = {
            {'(', ')'},
            {'[', ']'},
            {'{', '}'}
        };
        for (char c:s){
            if(brackets.count(c))
                st.push(c);
            else{
                if(st.empty()) return false;
                char c2 = st.top();
                st.pop();
                if (brackets[c2] != c) 
                    return false;
            }
        }
        return st.empty();
    }
};