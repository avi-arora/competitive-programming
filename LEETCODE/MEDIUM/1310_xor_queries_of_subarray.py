class Solution:
    
    def xorQueries(self, arr, queries):
        pass


    def xorQueries_BruteForce(self, arr, queries):
        """
        Giving TLE on large dataset
        """
        result = []
        for query in queries:
            start, end = query
            xorResult = arr[start]
            for i in range(start+1, end+1):
                xorResult ^= arr[i]
            result.append(xorResult)
        return result


if __name__ == "__main__":
    s = Solution()
    arr, queries = [1,3,4,8], [[0,1],[1,2],[0,3],[3,3]]
    print(s.xorQueries_BruteForce(arr, queries))
        