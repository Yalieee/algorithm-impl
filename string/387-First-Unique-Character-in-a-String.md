# Concept
兩種方式，一種是建立 HashMap，Value 是次數，然後 loop 兩次原始字串。另一種是像下面這樣，建立兩個 hashSet 來查

```py
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        answerList = []
        hashSet = set()
        blackSet = set()

        for ind, char in enumerate(s):
            if char in hashSet:
                blackSet.add(char)
            else:
                hashSet.add(char)
                answerList.append((ind, char))

        for ind, char in answerList:
            if char not in blackSet:
                return ind

        return -1
```