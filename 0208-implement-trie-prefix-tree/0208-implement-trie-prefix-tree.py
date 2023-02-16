class Node:
    def __init__(self, letter=None):
        self.letter = letter
        self.children = {}
        self.isWord = False

class Trie:

    def __init__(self):
        self.root = Node()

        

    def insert(self, word: str) -> None:
        current = self.root
        for letter in word:
            if letter in current.children:
                current = current.children[letter]
            else:
                newNode = Node(letter)
                current.children[letter] = newNode
                current = newNode
        
        current.isWord = True
        

    def search(self, word: str) -> bool:
        current = self.root
        for letter in word:
            if letter not in current.children:
                return False
            else:
                current = current.children[letter]

        return current.isWord
        

    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for letter in prefix:
            if letter not in current.children:
                return False
            else:
                current = current.children[letter]
                
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)