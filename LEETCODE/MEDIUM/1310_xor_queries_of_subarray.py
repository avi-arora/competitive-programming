class Solution:
    
    def xorQueries(self, arr, queries):
        #build prefix array 
        prefix = [0] * len(arr)
        prefix[0] = prefix[0] ^ arr[0]
        for i in range(1, len(arr)):
            prefix[i] = prefix[i-1] ^ arr[i]
        
        result = []
        for query in queries:
            start, end = query
            if start == 0:
                result.append(prefix[end])
            else:
                result.append(prefix[start-1] ^ prefix[end])
        return result


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
    print(s.xorQueries(arr, queries))
        