class Solution:
    def relativeSortArray(self, arr1: [int], arr2: [int]) -> [int]:

        number_by_index = {}
        size1 = len(arr1)
        for i in range(size1):
            if arr1[i] not in number_by_index:
                number_by_index[arr1[i]] = 1
                continue
            number_by_index[arr1[i]] += 1

        arr_to_return = []

        for i in range(len(arr2)):
            for index_arr1 in range(number_by_index[arr2[i]]):
                arr_to_return.append(arr2[i])
            del number_by_index[arr2[i]]

        for num in sorted(number_by_index.keys()):
            for i in range(number_by_index[num]):
                arr_to_return.append(num)
        return arr_to_return

Solution().relativeSortArray([28,6,22,8,44,17], [22,28,8,6])