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
Create a local omicsoft project and import an expression table file to the project, attach design and annotation table. 
How to use: python cmd_ImportMicroarrayTableToLocalProject.py MicroarrayTablePath AnnotationTableFilePath DesignTableFilePath ProjectId ProjectFolderPath NameOfImportedOmicdata

Note: MicroarrayTablePath, AnnotationTableFilePath, DesignTableFilePath and ProjectFolderPath are required to be FULL path (see example below)

Example:
 python cmd_ImportMicroarrayTableToLocalProject.py C:\Users\chenwi\tem C:\Users\chenwi\tem\Expression.txt C:\Users\chenwi\tem\AnnotationTable.txt C:\Users\chenwi\tem\DesignTable.txt C:\Users\chenwi\tem test1 ImportedTable1

Format of Expression.txt input file:
Probe Set ID	01A	02A	03A	04A	05A	06A	07A	08A	09A	10A	11A	12A	13A	14A	15A	16A	17A	18A	19A	20A	21A	22A	23A	24A
AFFX-BioB-5_at	7.3542	7.0832	6.3511	6.4752	6.1791	6.7724	6.7322	6.7278	6.7920	6.7013	6.5672	6.7381	6.3691	6.6208	6.0453	6.5046	5.5381	6.2089	6.0039	6.1170	5.9671	6.3191	6.1983	6.6942
AFFX-BioB-M_at	7.8395	7.5960	6.7611	7.0479	6.7599	7.2694	7.4222	7.2810	7.3618	7.3280	6.9716	7.3789	6.8506	7.2077	6.5399	6.7753	5.7431	6.5997	6.3031	6.4440	6.4867	6.8611	6.4872	6.8734

AnnotationTable.txt format:
Probe Set ID	Gene Symbol
1367452_at	Sumo2
1367453_at	Cdc37
 
DesignTable.txt format:
chip	time	treatment	group
01A	1	control	control.t1
02A	1	control	control.t1
03A	1	control	control.t1
04A	1	DBP	DBP.t1
05A	1	DBP	DBP.t1
06A	1	DBP	DBP.t1
              """)
        sys.exit()

    a1=Oapi.ImportMicroarrayTableToLocalProject()
    a1.MicroarrayTableFilePath=sys.argv[1]
    a1.AnnotationTableFilePath=sys.argv[2]
    a1.DesignTableFilePath=sys.argv[3]
    a1.ProjectId=sys.argv[4]
    a1.ProjectFolderPath=sys.argv[5]
    
    if len(sys.argv) > 6:
        a1.NameOfImportedOmicdata=sys.argv[6]
    else:
        a1.NameOfImportedOmicdata='ImportedOmicdata'
    a1.Run()
    print(a1.Log)