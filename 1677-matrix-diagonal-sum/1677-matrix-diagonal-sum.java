class Solution {
    public int diagonalSum(int[][] mat) {
        int sum=0;
        for(int i=0;i<mat.length;i++){
            sum+=mat[i][i];
        }
        for(int j=mat.length-1,k=0;j>=0;j--,k++){
            sum+=mat[k][j];
        }
        if(mat.length%2==1)
            sum-=mat[(int)mat.length/2][(int)mat.length/2];
        return sum;
    }
}