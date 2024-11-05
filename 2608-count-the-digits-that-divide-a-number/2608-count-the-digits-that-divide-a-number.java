class Solution {
    public int countDigits(int num) {
        int n=num;
        int count;
        for(count=0;n!=0;n/=10){
            if(num%(n%10)==0){
                count++;
            }
        }
        return count;
    }
}