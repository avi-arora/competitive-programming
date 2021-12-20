class Solution:
    def minimumAbsDifference(self, arr):
        """
        >>> test.minimumAbsDifference([4,2,1,3])
        [[1, 2], [2, 3], [3, 4]]

        >>> test.minimumAbsDifference([1,3,6,10,15])
        [[1, 3]]

        >>> test.minimumAbsDifference([3,8,-10,23,19,-4,-14,27])
        [[-14, -10], [19, 23], [23, 27]]

        Solution not accepted, TLE
        """
        result = []
        arr.sort()
        minabs = float("inf")
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                currabs = abs(arr[i] - arr[j])
                if currabs < minabs:
                    minabs = currabs
                    result = []
                    result.append([arr[i],arr[j]])
                elif currabs == minabs:
                    result.append([arr[i],arr[j]])
        return result

    def minimumAbsDifferenceBasicImporvement(self, arr):
        """
        >>> test.minimumAbsDifferenceBasicImporvement([4,2,1,3])
        [[1, 2], [2, 3], [3, 4]]

        >>> test.minimumAbsDifferenceBasicImporvement([1,3,6,10,15])
        [[1, 3]]

        >>> test.minimumAbsDifferenceBasicImporvement([3,8,-10,23,19,-4,-14,27])
        [[-14, -10], [19, 23], [23, 27]]

        Accepted.
        """
        result = []
        arr.sort()
        minabs = float("inf")
        for i in range(len(arr)-1):
            curr = abs(arr[i] - arr[i+1])
            if curr < minabs:
                minabs = curr
        for i in range(1, len(arr)):
            if abs(arr[i-1] - arr[i]) == minabs:
                result.append([arr[i-1], arr[i]])
        return result


if __name__ == "__main__":
    import doctest
    doctest.testmod(extraglobs={"test": Solution() })