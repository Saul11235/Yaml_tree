# yaml_tree by Edwin Saul

try:     from printTree  import printTree
except:  from .printTree import printTree 

try:     from readTree  import readTree
except:  from .readTree import readTree 

try:     from writeTree  import writeTree
except:  from .writeTree import writeTree

class tree:

    def __init__(self):
        # path  for scan info
        self.__path=""
        self.__knowPath=False
        # cell var counter
        self.__cellCounter=-1
        # cell oneFile or multiple files
        self.__OneFile=False
        # data in tree cell
        self.__cellName  =[]  # cell name 
        self.__cellValue =[]  # cell Value
        self.__cellStatus=[]  # true if exists false if not
        self.__cellFather=[]  # code of father
        self.__cellChilds=[]  # list of code of childs
        self.__cellIsPath=[]  # true if is path false if is var or file 
        self.__cellIsFile=[]  # true if is file, false if is path or var
        # first childs : childs of -1
        self.__firstChilds=[]
        # data alias
        self.__alias={}       # "alias", []

    def print(self): printTree(self)
    def read(self):  readTree(self)
    def write(self): writeTree(self)

    def get_path(self):    return self.__path
    def get_knowPath(self):return self.__knowPath
    def get_data(self):    return [self.__cellName,self.__cellValue,self.__cellStatus,self.__cellFather,self.__cellChilds,self.__cellIsPath,self.__cellIsFile,self.__firstChilds]
    def get_alias(self):   return self.__alias



#---------------------------------------------------

if __name__=="__main__": # tests
    a=tree()
    a.print()




