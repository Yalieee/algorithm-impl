# Notice
注意要有一個標記。理由是當裡面有 `Apple` 時，搜尋 `App` 應該回傳 False

```py
class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}


    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        current = self.root
        for char in word:
            if char not in current:
                current[char] = {}
            current = current[char]
        current['existed'] = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        current = self.root
        for char in word:
            if char not in current:
                return False
            current = current[char]

        return 'existed' in current

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        current = self.root
        for char in prefix:
            if char not in current:
                return False
            current = current[char]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
```