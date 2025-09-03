class Node:
    def __init__(self, name):
        self.name = name
        self.father = None

def create_family_tree_hardcoded():
    # Hardcoded family tree
    names = ["Pralhad", "Hiranyakashapa", "Kashayapa Brahma", "Chaturmukha Brahma", "I don't know"]

    # Create nodes from the names list
    nodes = [Node(name) for name in names if name.lower() != "i don't know"]

    # Link nodes to form the tree
    for i in range(len(nodes) - 1):
        nodes[i].father = nodes[i + 1]

    # Return the root of the tree (the last generation individual)
    return nodes[0]

def print_family_tree(node):
    if node is not None:
        print(f"{node.name}")
        print_family_tree(node.father)

# Example usage
if __name__ == "__main__":
    root = create_family_tree_hardcoded()
    print("Family Tree:")
    print_family_tree(root)
