import os
file= open ("text.txt","a")
file.write("r\n")
file.write("5\n")
file.write("s\n")
file.write("6\n")
file.write("r\n")
file.write("7\n")
file.write("g\n")
file.write("7\n")
def dic(self,path="",dic=dict({})):
        
        #file= open("exname.txt","r")
        #name=file.readline()
        file1=open(str("%s.txt"%(path)),"r")
        while (not(file1.tell() == os.fstat(file1.fileno()).st_size)):
            state=""
            key=file1.readline()
            value=file1.readline()
            for key1 in dic.keys():
                if(key1==key):
                     state="r"
                     dic[key1]=str("%f"%(float(dic[key1])+float(value)))
            if(not(state=="r")):        
                 dic.update({key:value})
        print(dic)
        return dic
def sort(self,di=dict({})):
        for key1 in di.keys():
            for key2 in di.keys():
                if (key1==key2):
                    di[key1]=int(di[key1])+int(di[key2])
                    del di[key2]
        print(di)
        return di

s=dict({})
s=dic(s,"text")
print(s)