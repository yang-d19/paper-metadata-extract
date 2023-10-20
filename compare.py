class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_word

    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

    def get_all_words(self, prefix=''):
        results = []
        node = self.root
        for char in prefix:
            if char not in node.children:
                return results
            node = node.children[char]
        self._dfs(node, prefix, results)
        return results

    def _dfs(self, node, prefix, results):
        if node.is_word:
            results.append(prefix)
        for char, child_node in node.children.items():
            self._dfs(child_node, prefix + char, results)

# Create a Trie
trie = Trie()

# Insert words into the Trie
trie.insert("apple")
trie.insert("banana")
trie.insert("orange")
trie.insert("grape")

# Search for words
print(trie.search("apple"))  # True
print(trie.search("pear"))   # False

# Check if prefix exists
print(trie.starts_with("app"))  # True
print(trie.starts_with("pea"))  # False

# Get all words with a given prefix
print(trie.get_all_words("or"))  # ['orange']
print(trie.get_all_words("a"))   # ['apple']