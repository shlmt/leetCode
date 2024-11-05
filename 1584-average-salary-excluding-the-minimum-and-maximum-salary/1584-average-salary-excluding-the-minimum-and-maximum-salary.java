class Solution {
    public double average(int[] salary) {
        int sum=0 ,min=1000000, max=0;
        for(int i=0;i<salary.length;i++){
            if(min>salary[i])
                min=salary[i];
            if(max<salary[i])
                max=salary[i];
            sum+=salary[i];
       }
       return (double)(sum-min-max)/(salary.length-2);
    }
}