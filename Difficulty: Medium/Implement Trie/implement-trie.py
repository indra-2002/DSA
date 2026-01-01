#User function Template for python3
class TrieNode():
    def __init__(self):
        self.child={}
        self.end=None
class Trie:
    def __init__(self):
        # implement Trie
        self.root=TrieNode()
        
    def insert(self, word: str):
       # insert word into Trie
        node=self.root
        for c in word:
            if c not in node.child:
               node.child[c]=TrieNode()
            node=node.child[c]
        node.end=True
    def search(self, word: str) -> bool:
         # search word in the Trie
        node=self.root
        for c in word:
            if c not in node.child:
                return False
            node= node.child[c]
        return node.end

    def isPrefix(self, word: str) -> bool:
         # search prefix word in the Trie
        node=self.root
        for c in word:
            if c not in node.child:
                return False
            node=node.child[c]
        return True