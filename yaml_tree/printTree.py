# yaml_tree by: Edwin Saul https://edwinsaul.com

from os import get_terminal_size


def printLine(text):
    text=str(text)
    console_width = get_terminal_size().columns
    if len(text)<console_width: print(text)
    else: print(text[0:console_width-1])


def printLineTree(tree,path):
    childs=tree.childs(path)
    for x in childs:
        new_path=path+[x]
        line=(" "*len(path))+" "+str(x)
        #-----  cicle on printLineTree --------
        printLine(line)
        printLineTree(tree,new_path)
        #---------------------------------------

def printTree(tree):
    print("path   : "+str(tree.get_path()))
    print("file   : "+str(tree.get_file()))
    print("know?  : "+str(tree.get_knowPath()))
    print("")
    printLineTree(tree,[])

# --------------------------------------------------------
if __name__=="__main__":
    printLine(100*"------")
    input()

