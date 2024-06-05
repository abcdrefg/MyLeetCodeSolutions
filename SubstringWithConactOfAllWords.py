class Solution:
    def findSubstring(self, s: str, words):
        wordSize = len(words[0])
        size = len(s)
        numberOfWords = len(words)
        indexes_of_words = {}
        indexes_of_concats = []
        found = False
        for i in range(0,size,wordSize):
            currWord = s[i:i+wordSize]
            found = False
            for word in words:
                if currWord == word:
                    if currWord in indexes_of_words:
                        indexes_of_words = {}
                        break
                    indexes_of_words[currWord] = i
                    found = True
                    if len(indexes_of_words.keys()) == numberOfWords:
                        indexes_of_concats.append(i - (numberOfWords-1)*wordSize)
                        indexes_of_words = {}
            if not found:
                indexes_of_words = {}
        return indexes_of_concats

Solution().findSubstring("barfoothefoobarman", ["foo","bar"])