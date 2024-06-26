class Solution:
    def isNStraightHand(self, hand, groupSize: int) -> bool:
        hand.sort()
        if groupSize < 2:
            return True

        size = len(hand)
        if size % groupSize != 0:
            return False

        arrays_by_missing_number = {}

        for i in range(size):
            if hand[i] not in arrays_by_missing_number:
                if hand[i] + 1 not in arrays_by_missing_number:
                    arrays_by_missing_number[hand[i] + 1] = [[hand[i]]]
                    continue
                arrays_by_missing_number[hand[i] + 1].append([hand[i]])
                continue
            array_with_missing_value = arrays_by_missing_number[hand[i]].pop()
            array_with_missing_value.append(hand[i])
            if len(arrays_by_missing_number[hand[i]]) == 0:
                del arrays_by_missing_number[hand[i]]
            if len(array_with_missing_value) == groupSize:
                continue
            if hand[i] + 1 not in arrays_by_missing_number:
                arrays_by_missing_number[hand[i] + 1] = [array_with_missing_value]
                continue
            arrays_by_missing_number[hand[i] + 1].append(array_with_missing_value)

        if len(arrays_by_missing_number) != 0:
            return False
        return True


Solution().isNStraightHand([1,1,2,2,3,3], 3)