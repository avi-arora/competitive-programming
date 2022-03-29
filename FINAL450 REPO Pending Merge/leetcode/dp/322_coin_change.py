class Solution:
    def coinChange(self, coins: [int], amount: int) -> int:
        table = [[amount+1]*(amount+1)] * len(coins)
        #initilize dp table
        
        print(table)
        for n in range(len(coins)):
            pass
            



if __name__ == "__main__":
    obj = Solution()
    obj.coinChange([1,2,4],6)