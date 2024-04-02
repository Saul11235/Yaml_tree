# yaml_tree by Edwin Saul

from os.path import isdir,isfile, join

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
        self.__file=""
        self.__knowPath=False
        # cell var counter
        self.__cellCounter=-1
        # cell oneFile or multiple files
        self.__OneFile=False
        # data in tree cell
        self.__cellName  =[]       # cell name 
        self.__cellValue =[]       # cell Value
        self.__cellStatus=[]       # true if exists false if not
        self.__cellHasContent=[]   # true if has content false is has childs
        self.__cellFather=[]       # code of father
        self.__cellChilds=[]       # list of code of childs
        self.__cellComments=[]     # list of code of childs
        self.__cellTag=[]          # tag of cell
        # first childs : childs of -1
        self.__firstChilds=[]
        # extensions for add elements
        self.__extensions=[".csv"] # extensions for add elements
        # data alias
        self.__alias={}       # "alias", []


    def print(self): printTree(self)
    def read(self):  readTree(self)
    def write(self): writeTree(self)


    def get_path(self):      return self.__path
    def get_file(self):      return self.__file
    def get_knowPath(self):  return self.__knowPath
    def get_data(self):      return [self.__cellName,self.__cellValue,self.__cellStatus,self.__cellHasContent,self.__cellFather,self.__cellChilds,self.__cellComments,self.__cellTag,self.__firstChilds]
    def get_extensions(self):return self.__extensions
    def get_alias(self):     return self.__alias


    def get(self,direction):
       pass


    def set(self,direction,value):
        pass


    def make(self,direction,new):
        codeFather=self.__get_code(direction)
        self.__raw_create(codeFather,new)


    def childs(self,direction):
        codeFather=self.__get_code(direction)
        if codeFather==-1:
            return self.__get_names_by_code(self.__firstChilds)
        else:
            return []


    def __raw_create(self,codeFather,name):
        self.__cellCounter+=1
        self.__cellName.append(str(name)[:])
        self.__cellValue.append(0)
        self.__cellStatus.append(True)
        self.__cellHasContent.append(True)
        self.__cellFather.append(codeFather)
        self.__cellChilds.append([])
        self.__cellComments.append(None)
        self.__cellTag.append(None)
        if codeFather==-1: # in root 
            self.__firstChilds.append(self.__cellCounter)
        else:
            self.__cellChilds[codeFather]=self.__cellChilds[codeFather].append(self.__cellCounter)
            self.__cellHasContent[codeFather]=False

    def __get_names_by_code(self,list_of_codes):
        names=[]
        for code in list_of_codes: names.append(self.__cellName[code])
        return names


    def __get_code(self,direction):
        if len(direction)==0: return -1 # root main
        elif type(direction)==str:
            direction=direction.replace("\\","/").split("/")
            pass
        elif type(direction)==list:
            if len(direction)==1:
                # code on root
                if direction[0] in self.__get_names_by_code(self.__firstChilds):
                    pass
                else: return -1
            else:
                pass
        else: return -1 # root main



#---------------------------------------------------

if __name__=="__main__": # tests
    a=tree()
    a.make("","data1")
    a.make("","data2")

#    a.make("data1","data3")
    a.print()
#    input()

