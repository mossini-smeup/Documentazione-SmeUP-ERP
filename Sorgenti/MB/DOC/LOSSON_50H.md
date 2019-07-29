## Backup and recovery
In this appendix we provide information needed for backup and recovery of the single signon
components.
### Microsoft Active Directory
Our scenario uses Kerberos authentication in the Microsoft Active Directory of your Windows
2000 server. Backup and recovery of the Active Directory is therefore essential. For details
refer to the Microsoft Technet whitepaper Active Directory Disaster Recovery at : 
 :  : DEC T(J1) P(PATHFILE) [http://www.microsoft.com/technet/prodtechnol/windows2000serv/technologies/activedirectory/support+
](http://www.microsoft.com/technet/prodtechnol/windows2000serv/technologies/activedirectory/support+
)
/adrecov.mspx)
This document also covers the Domain Controller replication, which prevents the Kerberos
Network Authentication Service to be the single point of failure in the network. If you want to
make your network more reliable and available you should consider setting up Domain
Controller replication.
### Objects on your iSeries system
Details about the iSeries objects used to store the information for Network Authentication
Service and EIM are given here.
For details about how to backup and recover iSeries objects, refer to Backup and Recovery,
SC41-5304.
### The iSeries Network Authentication Service objects
All objects used by the Network Authentication Service on the iSeries server are located in
the Integrated File System (IFS) directory : 
/QIBM/UserData/OS400/NetworkAuthentication
We recommend that you backup all objects and sub-directories of this directory on the same
schedule that you back up your iSeries security data.
### The EIM domain on the iSeries LDAP directory server
The EIM domain is implemented in an LDAP directory. If you use the directory server
integrated in OS/400, it stores information in the following locations : 
 *  The database library (QUSRDIRDB by default), which contains the directory servers
contents. The name of the library can be found in iSeries navigator Network -> Servers ->
TCP/IP -> Directory Server -> Properties.
 * The QDIRSRV2 library, which is used to store publishing information (not used by EIM).
 * The QUSRSYS library, which stores various items in objects beginning with QGLD
(specify QUSRSYS/QGLD* to save them).
 *  If you configure the directory server to log directory changes, a database library called
QUSRDIRCL that the change log uses.
Important :  Correct object authorities of the Network Authentication Service objects and
EIM objects are essential for your system and network security. To maintain them after the
restore, it is not sufficient simply to restore the objects. You need to Restore User Profiles
(RSTUSRPRF) prior to restoring the objects and to Restore Authorities (RSTAUT) after
restoring the objects. For details refer to Backup and Recovery, SC41-5304.
Appendix A. Backup and recovery 227
We recommend that you backup the libraries and objects listed above on the same schedule
that you back up your iSeries security data. It may be necessary to save-while-active since
the option to end the LDAP server may not available to you.
The configuration data is stored in the following directory : 
/QIBM/UserData/OS400/Dirsrv/
You should also save the files in that directory whenever you change the LDAP configuration
or apply PTFs.
Another approach, from an availability perspective, is to use LDAP replication. Through V5R2,
the OS/400 directory server has the capability to replicate data between a master server and
one or more read-only replica servers. You can find more on replication in the IBM Redbooks
on LDAP : 
 * Implementation and Practical Use of LDAP on the iSeries Server, SG24-6193
 * Understanding LDAP, SG24-4986
 * LDAP Implementation Cookbook, SG24-5110
### The iSeries EIM configuration
Except for the data in the EIM domain in the LDAP directory, EIM uses configuration
information you enter when you run the EIM configuration wizard. This configuration data
contains the URL of the LDAP server and the name of the parent DN (if any).
The EIM configuration data is saved automatically with your security data using the Save
Security Data (SAVSECDTA) command.
You restore it simply by restoring the QSYS user profile object.
### Sample CL program to save your data
Example A-1 is a sample CL program that will save your data that relates to Network
Authentication Service, LDAP, and EIM.
> T(Example :  A-1)
/******************************************************************************/
/* SAVSSOOBJ - Save SSO objects (and more) */
/* Parm :  Device to which the objects are saved, */
/* i.e. DEV parameter for various SAV... commands */
/* */
/* Saves the following :  */
/* - OS/400 security data including EIM configuration in the QSYS *USRPRF */
/* - LDAP configuration and Network Authentication Service objects from IFS */
/* - LDAP objects from QUSRSYS (their name start with QGLD) */
/* - All default LDAP libraries. */
/* You may need too change the following in the SAVLIB command :  */
/* * Change the name of the LDAP database library, if you changed */
/* the default name in DIrectory Server Properties */
/* * Remove the name of the QUSRDIRCL library if you have not set up */
/* the logging of changes. */
/* * Remove the name of the QDIRSRV2 library if you are not using */
/* directory publishing */
/******************************************************************************/

PGM PARM(&DEV)
DCL VAR(&DEV) TYPE(*CHAR) LEN(10) /* PARM :  Device for save commands */
/* Establish error handling */


