class Solution:
    def groupAnagrams(self, strs):
        groupedAnagrams = {}

        for word in strs:
            sortedWord = ''.join(sorted(word))
            if sortedWord not in groupedAnagrams:
                groupedAnagrams[sortedWord] = [word]
                continue
            groupedAnagrams[sortedWord].append(word)

        return groupedAnagrams.values()