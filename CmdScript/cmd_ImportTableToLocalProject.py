import os
import site
import sys

OapiPath=os.path.split(__file__)[0]

OapiPkgPath=os.path.split(os.path.split(OapiPath)[0])[0]

site.addsitedir(OapiPkgPath)

import OmicPythonApi as Oapi

if __name__=="__main__":
    if sys.argv[1] =='-h':
        print(r"""
Create a local omicsoft project and load a table to the project. 
How to use: python TableImporter.py ProjectId ProjectFolder TablePath TableNameInProject
Example:
 python TableImporter.py test1 C:\Users\chenwi\tem C:\Users\chenwi\tem\test1.txt ImportedTable1  
Format of test1.txt input file:
 Probeset	y1	y2	y3
 x1	1	2	3
 x2	3	4	5
              """)
        sys.exit()
    
#    for i in range(len(sys.argv)):
#        print(i)
#        print(sys.argv[i])
    
    project1=Oapi.ImportTableToLocalProject()
    project1.ProjectId=sys.argv[1]
    project1.ProjectFolderPath=sys.argv[2]
    project1.InputTableFilePath=sys.argv[3]
    
    if len(sys.argv) > 4:
        project1.NameOfTableInProject=sys.argv[4]
    project1.Run()
    print(project1.Log)