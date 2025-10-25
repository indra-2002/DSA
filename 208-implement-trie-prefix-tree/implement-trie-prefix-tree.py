class TrieNode:
    def __init__(self):
        self.child={}
        self.end=False

class Trie(object):

    def __init__(self):
        self.root=TrieNode()
           

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        node = self.root
        for c in word:
            if c not in node.child:
                node.child[c]=TrieNode()
            node=node.child[c]
        node.end=True
    

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        node=self.root
        for c in word:
            if c not in node.child:
                return False
            node=node.child[c]
        return node.end
        

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        node=self.root
        for c in prefix:
            if c not in node.child:
                return False
            node=node.child[c]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)