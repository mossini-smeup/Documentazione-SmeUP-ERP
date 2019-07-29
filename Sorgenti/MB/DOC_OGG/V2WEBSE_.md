 :  : HEA PRIV(001)

# NOTA
Questo documento deve essere spezzato in vari sotto documenti, uno per ogni webservice che si cataloga.

Ad esempio Sme.Up WebService Provider, se viene battezzato con codice 03, andrà documentato nel membro V2WEBSE_03




# Sme.Up WebService Provider

# Archibox WebService Provider

# Archibox WebService Consumer

Questi due webservice sono esposti da ARCHIBOX e consentono l'interrogazione da parte di SmeUp.

1) http://172.16.2.60/soap/getContainers?wsdl (ARCHIBOX)
input
param_archivio :  archivio
param_archibox :  sempre true
param_login :  utente archibox
param_pwd :  password relativa

output
ID :  stringa (ID del contenitore)
Description :  string (descrizione contenitore)

2) http://172.16.2.60/soap/getDocuments?wsdl (ARCHIBOX)
2)
param_archivio :  archivio
param_raccoglitore :  nome raccoglitore
param_archibox :  sempre true
param_login :  utente archibox
param_pwd :  password relativa
TIP :  TIPO+PARAMETRO Smeup

output
array di valori dipendenti da param_raccoglitore


Sono wrappati dal server 09.
Il server 09 espone i servizi JA_09_01,  JA_09_02, JA_09_03.


-------------------------------------------------------------------------------
Questo webservice viene richiamato dal plugin che si installa in EXCEL.

3) http://demo.smeup.com/LUServices/OpenSmeupService?WSDL (EXCEL)

Si trova al MIX.
Si connette all'AS400A, con utente SMEWW2D, ambiente GES_DE01


Il plugin excel è in grado di gestire solamente xml di tipo matrice.

-------------------------------------------------------------------------------


4) webservice su gilberto

NOTA :  per richiamare le pagine di test anteporre
http://gilberto.smea.it:8080
ai path di test

http://gilberto.smea.it:8080/PDFOpenSmeupWS/OpenSmeupService?WSDL

4.1) PDFOpenSmeupWS ----------------------------

Application Name :   PDFOpenSmeupWS
Tester :   /PDFOpenSmeupWS/OpenSmeupService?Tester
WSDL : /PDFOpenSmeupWS/OpenSmeupService?WSDL
Endpoint Name : OpenSmeup
Service Name: http://ws.smeup.it/
Port Name : OpenSmeupPort
Deployment Type : 109
Implementation Type : SERVLET
Implementation Class Name : it.smeup.ws.OpenSmeup
Endpoint Address URI : /PDFOpenSmeupWS/OpenSmeupService
Namespace : it.smeup.ws.OpenSmeup
Description :  Viene letto un pdf fisso. C'è anche la possibilità di richiamare una fun

    serverName :     srvamm.smeup.com
    userName :     fg
    environment :     0015 - GES_01


4.2) OpenSmeupWS --------------------------------------------

Application Name :  OpenSmeupWS
Tester : /OpenSmeupWS/OpenSmeupService?Tester
WSDL : /OpenSmeupWS/OpenSmeupService?WSDL
Endpoint Name : OpenSmeup
Service Name:http://ws.smeup.it/
Port Name : OpenSmeupPort
Deployment Type : 109
Implementation Type : SERVLET
Implementation Class Name : it.smeup.ws.OpenSmeup
Endpoint Address URI : /OpenSmeupWS/OpenSmeupService
Namespace : it.smeup.ws.OpenSmeup
Description : 

    serverName :     srvamm.smeup.com
    userName :     fg
    environment :     0015 - GES_01


4.3) ArchiboxSmeupWS ---------------------------------------------
é su Gilberto e risponde alle richieste di archibox.
Archibox utilizza questo webservice richiedendo l'esecuzione di una fun.
La fun notifica ad un servizio AS400 le azioni svolte da archibox.

utente archibox

Application Name : ArchiboxSmeupWS
Tester : /ArchiboxSmeupWS/OpenSmeupService?Tester
WSDL : /ArchiboxSmeupWS/OpenSmeupService?WSDL
Endpoint Name : OpenSmeup
Service Name:http://ws.smeup.it/
Port Name : OpenSmeupPort
Deployment Type : 109
Implementation Type : SERVLET
Implementation Class Name : it.smeup.ws.OpenSmeup
Endpoint Address URI : /ArchiboxSmeupWS/OpenSmeupService
Namespace : it.smeup.ws.OpenSmeup
Description : 

    serverName :     as400a.smea.it
    userName :     archibox
    environment :     0010 - SVI


4.4) ExcelOpenSmeupWS --------------------------------------
Application Name : ExcelOpenSmeupWS
Tester : /ExcelOpenSmeupWS/OpenSmeupService?Tester
WSDL : /ExcelOpenSmeupWS/OpenSmeupService?WSDL
Endpoint Name : OpenSmeup
Service Name:http://ws.smeup.it/
Port Name : OpenSmeupPort
Deployment Type : 109
Implementation Type : SERVLET
Implementation Classit.smeup.ws.OpenSmeup
Endpoint Address URI : /ExcelOpenSmeupWS/OpenSmeupService
Namespace : it.smeup.ws.OpenSmeup
Description : 


    serverName :     srvamm.smeup.com
    userName :     fg
    environment :     0015 - GES_01

-------------------------------------------------------------------------------
6) altri webservice?
- pittini???

7) servizio LOSER_37
richiama il webservice
http://ws.services.smea.it/

-------------------------------------------------------------------------------
NOTA :  per eseguire i test di connessione utilizzare la F seguente : 
F(EXB;B£SER_01;CON.PRO)



