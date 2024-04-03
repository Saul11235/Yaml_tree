# yaml_tree by Edwin Saul

#from os.path import isdir,isfile, join

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
        self.__cellCounter=-1  # nums 0-999999 celda  -1 root  -2 NE
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
        self.__alias={}            # "alias", []
        self.__aliasName=[]        # alias Name
        self.__aliasDefinition=[]  # alias Definition
        self.__aliasCells=[]        # alias cells
        


    def print(self): printTree(self)
    def read(self):  readTree(self)
    def write(self): writeTree(self)



    def get_path(self):      return self.__path
    def get_file(self):      return self.__file
    def get_knowPath(self):  return self.__knowPath
    def get_data(self):      return [self.__cellName,self.__cellValue,self.__cellStatus,self.__cellHasContent,self.__cellFather,self.__cellChilds,self.__cellComments,self.__cellTag,self.__firstChilds]
    def get_extensions(self):return self.__extensions
    def get_alias(self):     return self.__alias


    def exists(self,direction,name):    # OK
        code=self.__get_code(direction)
        if self.__is_a_valid_code(code):
            keys=list(self.__get_dict_childs(code).keys())
            if name in keys: return True
            else: return False
        else: return False



    def get(self,direction):
        code=self.__get_code(direction)
        if code==-1: return None
        elif not(self.__cellStatus(code)): return None
        elif self.__cellHasContent(code): return self.__cellValue[code]
        else: return None



    def set(self,direction,value): #OK
        code=self.__get_code(direction)
        if self.__is_a_valid_code(code) and type(value) in [bool,int,float,str,list]:
            self.__cellValue[code]=value



    def make(self,direction,value=0): # OK
        direction=self.__split_direction(direction)
        path=direction[0]; new=direction[1]
        if len(new)==0: return None
        code=self.__get_code(path)
        if self.__is_a_valid_code(code):
            if self.exists(path,new): return False
            else:
                self.__raw_create(code,new); return True 
                self.set(direction,value)
        else: return None


    def childs(self,direction): #OK
        code=self.__get_code(direction)
        if not(self.__is_a_valid_code(code)): return []
        else:
            child_dict =self.__get_dict_childs(code)
            list_childs=list(child_dict.keys())
            return list_childs



    def __raw_create(self,codeFather,name): #OK
        if not(self.__is_a_valid_code(codeFather)): return None # no create
        self.__cellCounter+=1
        self.__cellName.append(str(name)[:])
        self.__cellValue.append(0)
        self.__cellStatus.append(True)
        self.__cellHasContent.append(True)
        self.__cellFather.append(codeFather)
        self.__cellChilds.append(list())
        self.__cellComments.append(None)
        self.__cellTag.append(None)
        if codeFather==-1: # in root 
            self.__firstChilds.append(self.__cellCounter)
        else:
            old_childs=list(self.__cellChilds[codeFather])
            new_childs=old_childs[:]+[self.__cellCounter][:]
            self.__cellChilds[codeFather]=new_childs
            self.__cellHasContent[codeFather]=False


    def __get_dict_childs(self,code): #OK
        if not(self.__is_a_valid_code(code)): return {}
        dict_childs={}
        code_childs=[]
        if code==-1: code_childs=self.__firstChilds
        else       : code_childs=self.__cellChilds[code]
        code_childs=list(code_childs)
        for element in code_childs:
            if self.__cellStatus[element]:
                dict_childs[self.__cellName[element]]=element
        return dict_childs



    def __is_a_valid_code(self,code): #OK
        if type(code)!=int: return False #  no integer
        elif code==-1: return True       #  root
        elif code==-2: return False      #  wrong code
        elif code<0  : return False      #  negative code
        elif code>self.__cellCounter: return  False # overflow
        else : return self.__cellStatus[code] #exist cell


    def __cicle_get_code(self,array): # OK
        code=-1; runOk=True
        for x in array:
            if runOk:
                childs=self.__get_dict_childs(code)
                keys=list(childs.keys())
                if not(x in keys): runOk=False
                else: code=childs[x]
        if runOk: return code
        else: return -2
            

    def __get_code(self,direction): # OK
        if len(direction)==0: return -1 # root main
        elif type(direction)==str: # direction in str format
            direction=direction.replace("\\","/").split("/")
            return self.__cicle_get_code(direction)
        elif type(direction)==list: # direction in list format
            return self.__cicle_get_code(direction)
        else: return -2 # Error code


    def __split_direction(self,direction):       # return [ path  namefile]
        if len(direction)==0: return [[],""]   # root main
        elif type(direction)==str or type(direction)==list: 
            if type(direction)==str:direction=list(direction.replace("\\","/").split("/"))
            path=direction[0:len(direction)-1]
            cell=direction[len(direction)-1]
            return [path,cell]
        else: return [[],""]



#---------------------------------------------------

if __name__=="__main__": # tests
    a=tree()
    a.make("data1")
    a.make("data1")
    a.make("data2")
    a.make("data3")
    a.make("data4")
    a.make("data74")

    a.make("data1/data4")
    a.make("data1/data5")
    a.make("data1/data8")
    a.make("data1/data9")

    a.make("data1/data4/data6")
    a.make("data1/data4/data7")
    a.print()
#    a.print_custom()

#    print(a.childs(""))

#    print(a.childs("data1"))
#
#    print(a.childs(""))

#    a.make("data1","data3")
#    print("terminado")

#    print(a.childs(""))

