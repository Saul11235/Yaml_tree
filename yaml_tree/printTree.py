# yaml_tree by: Edwin Saul https://edwinsaul.com


def printTree(tree):
    print("path   : "+str(tree.get_path()))
    print("know?  : "+str(tree.get_knowPath()))
    print(tree.get_data())
    print(tree)
