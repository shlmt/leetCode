class Solution {
public:
    int maxMoves(vector<vector<int>>& grid) {
        int rows = grid.size();
        int cols = grid[0].size();
        vector<vector<int>> dp(rows, vector<int>(cols, 0));
        for(int j=cols-2; j>=0; j--){
            for (int i=0; i<rows; i++){
                if (grid[i][j] < grid[i][j + 1]) 
                    dp[i][j] = max(dp[i][j], dp[i][j + 1] + 1);
                if (i > 0 && grid[i][j] < grid[i - 1][j + 1]) 
                    dp[i][j] = max(dp[i][j], dp[i - 1][j + 1] + 1);
                if (i < rows - 1 && grid[i][j] < grid[i + 1][j + 1]) 
                    dp[i][j] = max(dp[i][j], dp[i + 1][j + 1] + 1);
            }
        }
        int max=dp[0][0];
        for (int i=1; i<rows; i++) if(dp[i][0]>max) max=dp[i][0];
        return max;
    }
};