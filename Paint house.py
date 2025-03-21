#LC: yes, 256
#problems : NA

#recursive
#TC: O(k*2^n) ,n is no of houses; levels in tree is 2*n, there are k such trees
###TLE Error
#ex: [[5,6,5],[15,8,8],[13,19,7],[16,1,9],[15,2,18],[13,18,8],[4,1,3],[3,3,3],[16,14,14],[7,6,1],[7,17,17],[8,20,10],[12,16,1],[8,11,8],[14,7,12],[8,18,13],[6,2,3],[16,1,11],[4,2,10],[17,16,17],[1,8,17],[1,12,17],[1,11,10]]
#SC: O(k*2^n) recursive call stacks
class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        
        def helper(costs, idx, color):
            if idx == len(costs):
                return 0
            if color == 0:
                return costs[idx][0] + min(helper(costs, idx+1, 1), helper(costs, idx+1, 2))
            if color == 1:
                return costs[idx][1] + min(helper(costs, idx+1, 0), helper(costs, idx+1, 2))
            if color == 2:
                return costs[idx][2] + min(helper(costs, idx+1, 0), helper(costs, idx+1, 1))
            return None
        
        costsR = helper(costs, 0, 0)
        costsB = helper(costs, 0, 1)
        costsG = helper(costs, 0, 2)
        
        return min(costsR, min(costsB, costsG))
    
#DP
#TC: O(n) ,n is no of houses; 
# #SC: O(1) , no auxiliary data strcture used 
class Solution:
    def minCost(self, costs: List[List[int]]) -> int:  
        n = len(costs)
        for i in range(n-2, -1, -1):
            costs[i][0] += min(costs[i + 1][1], costs[i + 1][2])
            costs[i][1] += min(costs[i + 1][0], costs[i + 1][2])
            costs[i][2] += min(costs[i + 1][0], costs[i + 1][1])
        if len(costs) == 0: return 0
        return min(costs[0]) 
    
# #Space optimzation! Bottom up.
# #TC: O(n) ,n is no of houses; 
# #SC: O(1) , no data strcture used only local vars
class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        costR = costs[n-1][0]
        costB = costs[n-1][1]
        costG = costs[n-1][2]
        
        for i in range(n-2, -1, -1):
            tempR = costR
            costR = costs[i][0] + min(costB, costG)
            tempB = costB
            costB = costs[i][1] + min(tempR, costG)
            costG = costs[i][2] + min(tempR, tempB)
            
        return min(costR, min(costB, costG))
            
        