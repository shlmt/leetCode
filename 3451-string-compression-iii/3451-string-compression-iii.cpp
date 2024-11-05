class Solution {
public:
    string compressedString(string word) {
       char c=word[0];
       int count=1;
       string comp="";
       for(int i=1;i<word.length();i++){
            if(word[i]!=c || count==9){
                    comp+=to_string(count)+c;
                    count=1;
                    c=word[i];
            } 
            else count++;
       }
       comp+=to_string(count)+c;
       return comp;
    }
};