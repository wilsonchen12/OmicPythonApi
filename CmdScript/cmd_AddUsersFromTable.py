import os
import site
import sys

OapiPath=os.path.split(__file__)[0]

OapiPkgPath=os.path.split(os.path.split(OapiPath)[0])[0]

site.addsitedir(OapiPkgPath)

import OmicPythonApi as Oapi

class AddUsersFromTable():
    def __init__(self,ServerAddress='',ServerUserId='',ServerUserPsw='',NewUserTableFilePath=''):
        import pandas as pd
        self.ServerAddress=ServerAddress
        self.ServerUserId=ServerUserId
        self.ServerUserPsw=ServerUserPsw
        self.NewUserTableFilePath=NewUserTableFilePath
        if not NewUserTableFilePath =='':
            self.NewUserTable=pd.read_csv(self.NewUserTableFilePath,sep='\t',index_col=0)
        else:
            self.NewUserTable=''
        return

    def Run(self):
        import pandas as pd
        import sys

#        if self.NewUserTable=='':
#            print('Please provide a table file with user infor')
#            sys.exit()

        for UserID in self.NewUserTable.index:
            print('Adding User: ' + UserID)
            a1=Oapi.ManageUsers_Add()
            a1.ServerAddress=self.ServerAddress
            a1.ServerUserId=self.ServerUserId
            a1.ServerUserPsw=self.ServerUserPsw

            a1.UserID=UserID
            a1.UserGroups=self.NewUserTable.loc[UserID,'UserGroups']

            a1.Password=self.NewUserTable.loc[UserID,'Password']
            a1.FullName = self.NewUserTable.loc[UserID,'FullName']
            a1.Organization= self.NewUserTable.loc[UserID,'Organization']
            a1.Department= self.NewUserTable.loc[UserID,'Department']
            a1.Laboratory= self.NewUserTable.loc[UserID,'Laboratory']
            a1.Position= self.NewUserTable.loc[UserID,'Position']
            a1.Notes= self.NewUserTable.loc[UserID,'Notes']
            a1.Email= self.NewUserTable.loc[UserID,'Email']
            a1.Phone= self.NewUserTable.loc[UserID,'Phone']
            a1.Address= self.NewUserTable.loc[UserID,'Address']
            a1.Run()
            #print(a1.Log)
        return

if __name__=="__main__":
    if sys.argv[1] =='-h':
        print(r"""
Read a user table and create new uers from table.

How to use: python AddUsersFromTable.py ServerAddress ServerAdminId ServerAdminPsw UserTableFilePath

Example:
 python AddUsersFromTable.py tcp://192.168.3.226:9065 admin omicsoft Z:\Users\wilson\document\Script_Library\Python\OmicPythonApi_Development\OmicPythonApi\examples\testData\NewUserTables.txt

UserTableFile is tab delimited txt file where first row needs to be the same as example below:
    UserID	UserGroups	Password	FullName	Organization	Department	Laboratory	Position	Notes	Email	Phone	Address
    wilson5	standard users,editors,curators	omicsoft	wilson chen	Qiagen	Omicsoft	Support	Scientist	test	wilson.chen@qiagen.com	xxxx	xxxx
    wilson6	standard users,editors,curators	omicsoft	wilson chen	Qiagen	Omicsoft	Support	Scientist	test	wilson.chen@qiagen.com	xxxx	xxxx
              """)
        sys.exit()

    if not len(sys.argv)==5:
        print('4 input parameters are required, please check input and try again')
        sys.exit()

    a1=AddUsersFromTable(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4])
    a1.Run()
