class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}
        self.trie["value"] = False
    
    def find(self, h, key):
        try:
            ans = h[key]
        except:
            return 0
        else:
            return ans
    
    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        pointer = self.trie
        i = 0
        for a in word:
            if i == len(word)-1:
                if self.find(pointer, a):
                    # pointer = pointer[a]
                    pointer[a]["value"] = True
                else:
                    pointer[a] = {"value":True}
                    # pointer = pointer[a]
            else:
                if self.find(pointer, a):
                    pointer = pointer[a]
                else:
                    pointer[a] = {"value":False}
                    pointer = pointer[a]
            i+=1

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        pointer = self.trie
        i = 0
        for a in word:
            if i==len(word)-1:
                if self.find(pointer, a):
                    pointer = pointer[a]
                    value = pointer["value"]
                else:
                    return False
            else:
                if self.find(pointer, a):
                    pointer = pointer[a]
                else:
                    return False
            i+=1
        return value
    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        pointer = self.trie
        for a in prefix:
            if self.find(pointer, a):
                pointer = pointer[a]
            else:
                return False
        return True
