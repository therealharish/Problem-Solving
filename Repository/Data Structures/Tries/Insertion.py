class TrieNode:
  def __init__(self, map = {}, bool=True):
    self.map = map
    self.bool = bool

def insert(root, word):
  for char in word:
    if(char in root.map):
      root = root.map[char]
    else:
      root.map[char] = TrieNode()
      root.bool = True
      root = root.map[char]

root = TrieNod()
print(insert(root, "abc"))
    
    
  