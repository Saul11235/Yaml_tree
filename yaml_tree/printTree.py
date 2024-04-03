# yaml_tree by: Edwin Saul https://edwinsaul.com

from os import get_terminal_size


def cutline(text,size):
    size=abs(int(size));text=str(text)
    if len(text)<size: return text+" "*(size-len(text)-1)
    else: return (text[0:size-1])


def printLine(text):
    console_width = get_terminal_size().columns
    print(cutline(text,console_width))


def printLineTree(tree,path):
    childs=tree.childs(path)
    for x in childs:
        new_path=path[:]+[x]
        line1="XX"
        line2=("    "*len(path))+" > "+str(x)
        line3=""

        #-----  cicle on printLineTree --------
        printLine(line1+"|"+line2+line3)
        printLineTree(tree,new_path)
        #---------------------------------------

def printTree(tree):
    print("path   : "+str(tree.get_path()))
    print("file   : "+str(tree.get_file()))
    print("know?  : "+str(tree.get_knowPath()))
    print("")
    varpath=[]
    printLineTree(tree,varpath)

# --------------------------------------------------------
if __name__=="__main__":
    pass
