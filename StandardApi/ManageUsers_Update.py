from OmicPythonApi.Core.OmicPythonApi import *
class ManageUsers_Update(OmicPythonApi):
    """ A python api for ManageUsers_Update webcommand proc
        See Oscript and Log fields in the class object for details of the oshell jobs.
        Please refer to Omicsoft Wiki pages for details of the commands in Oscript.
        Wilson Chen, Omicsoft, 20190522
    """
    def __init__(self):
        """
        Input:
			1. ServerAddress
			2. ServerUserId: userid that logs into ArrayServer as admin
			3. ServerUserPsw
			4. UserID: userid that will be created and added to Array Server
			5. UserGroups: group id separated by comma (example: group1,group2,group3)
			6. Password: password of the new user
			7. FullName: full name of the new user
			8. Oaganization:
			9. Department:
			10. Labotatory
			11. Position
          12. Notes=
          13. Email=
          14. Phone
          15. Address
          16. WebLink=
          17. OtherEmail
          18. OtherPhone
          19. OtherWebLink
          20. SearchQuota
          21. SearchPerformed
          22. ProjectQuota
          23. ProjectDownloaded
          24. ProfileQuota
          25. ProfileDownloaded
          26. Disabled
          27. ExpirationDate
        Output: A new user is added into ArrayServer.
        """

        self.UserID=''
        self.UserGroups=''
        self.Password=''
        self.FullName=''
        self.Oaganization=''
        self.Department=''
        self.Laboratory=''
        self.Position=''
        self.Notes=''
        self.Email=''
        self.Phone=''
        self.Address=''
        
        self.WebLink=''
        self.OtherEmail=''
        self.OtherPhone=''
        self.OtherWebLink=''
        self.SearchQuota='1000000'
        self.SearchPerformed=''
        self.ProjectQuota='1000000'
        self.ProjectDownloaded=''
        self.ProfileQuota='1000000'
        self.ProfileDownloaded=''
        self.Disabled='N'
        self.ExpirationDate=''

        self.ServerAddress=''
        self.ServerUserId=''
        self.ServerUserPsw=''

        self.DownloadFullMetaData='False'
        self.DownloadGeneLevelData='True'


        self.Config=self.LoadConfigFile()
        self.OscriptTemplate=self.SetOscriptTemplate()
        self.Oscript=''
        self.Log=''
        return

    def SetOscriptTemplate(self):
        print('Load Oscript template')
        self.OscriptTemplate="""
Begin ExecuteCommand /Namespace=Server;
Server "@ServerAddress@" /UserID=@ServerUserId@ /Password=@ServerUserPsw@;
Command ManageUsers_Update;
Options
"
UserID=@UserID@
UserGroups={@UserGroups@}
Password=@Password@
FullName =@FullName@
Organization=@Organization@
Department=@Department@
Laboratory=@Laboratory@
Position=@Position@
Notes=@Notes@
Email=@Email@
Phone=@Phone@
Address=@Address@

WebLink=@WebLink@
OtherEmail=@OtherEmail@
OtherPhone=@OtherPhone@
OtherWebLink=@OtherWebLink@
SearchQuota=@SearchQuota@
SearchPerformed=@SearchPerformed@
ProjectQuota=@ProjectQuota@
ProjectDownloaded=@ProjectDownloaded@
ProfileQuota=@ProfileQuota@
ProfileDownloaded=@ProfileDownloaded@
Disabled=@Disabled@
ExpirationDate=@ExpirationDate@

#UserGroups	Alias=@UserGroupsAlias@
#UserFolderReaders=@UserFolderReaders@
#UserFolderEditors=@UserFolderEditors@
#LicenseGroup=@LicenseGroup@
";
End;
        """
        return(self.OscriptTemplate)

    def MakeOscript(self):
        """Modify Oscript
        Wilson Chen, 20171218"""
        print('Make oscript')
        Oscript=self.OscriptTemplate
        
        Oscript=Oscript.replace('@ServerAddress@',self.ServerAddress)
        Oscript=Oscript.replace('@ServerUserId@',self.ServerUserId)
        Oscript=Oscript.replace('@ServerUserPsw@',self.ServerUserPsw)
        
        Oscript=Oscript.replace('@UserID@',self.UserID)
        
        if r';' in self.UserGroups:
            self.UserGroups=self.UserGroups.replace(r';',r',')
        Oscript=Oscript.replace('@UserGroups@',self.UserGroups)
        
        Oscript=Oscript.replace('@Password@',self.Password)
        Oscript=Oscript.replace('@FullName@',self.FullName)
        Oscript=Oscript.replace('@Organization@',self.Organization)
        Oscript=Oscript.replace('@Department@',self.Department)
        Oscript=Oscript.replace('@Laboratory@',self.Laboratory)
        Oscript=Oscript.replace('@Position@',self.Position)
        Oscript=Oscript.replace('@Notes@',self.Notes)
        Oscript=Oscript.replace('@Email@',self.Email)
        Oscript=Oscript.replace('@Phone@',self.Phone)
        Oscript=Oscript.replace('@Address@',self.Address)

        Oscript=Oscript.replace('@WebLink@',self.WebLink)
        Oscript=Oscript.replace('@OtherEmail@',self.OtherEmail)
        Oscript=Oscript.replace('@OtherPhone@',self.OtherPhone)
        Oscript=Oscript.replace('@OtherWebLink@',self.OtherWebLink)
        Oscript=Oscript.replace('@SearchQuota@',self.SearchQuota)
        Oscript=Oscript.replace('@SearchPerformed@',self.SearchPerformed)
        Oscript=Oscript.replace('@ProjectQuota@',self.ProjectQuota)
        Oscript=Oscript.replace('@ProjectDownloaded@',self.ProjectDownloaded)
        Oscript=Oscript.replace('@ProfileQuota@',self.ProfileQuota)
        Oscript=Oscript.replace('@ProfileDownloaded@',self.ProfileDownloaded)
        Oscript=Oscript.replace('@Disabled@',self.Disabled)
        Oscript=Oscript.replace('@ExpirationDate@',self.ExpirationDate)

        self.Oscript=Oscript

        return(self.Oscript)
