from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import re,css

class Experience:
    def __init__(self,exp):
        exps=exp.split(":")
        self.company=exps[0]
        self.date=exps[1]
        self.details=exps[2]

    def getCompany(self):
        return self.company
    def getDate(self):
        return "("+self.date+")"
    def getDetails(self):
        return self.details
    
class Project:
    def __init__(self,project):
        exps=project.split(":")
        self.proj=exps[0]
        self.tech=exps[1]
        self.details=exps[2]

    def getCompany(self):
        return self.proj
    def getDate(self):
        return "( Technology used : "+self.tech+")"
    def getDetails(self):
        return self.details

def readCsv(path):
    lines=[]
    data={}
    with open(path,'r') as file:
        line=file.readline()
        while line:
            line=file.readline()
            parts=line.split("\t")
            tmp=""
            for part in parts:
                if part.startswith('"') or part.endswith('"'):
                    part=part.strip('"')
                tmp+=part+"\t"
            lines.append(tmp)
    for line in lines:
        tmp=line.split('\t');
        if len(tmp)>1:
            #print(tmp)
            data[tmp[1]]=tmp
    return data

if __name__=='__main__':
    pass