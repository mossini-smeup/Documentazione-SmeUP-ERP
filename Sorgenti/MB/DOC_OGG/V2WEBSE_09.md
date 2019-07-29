 :  : HEA PRIV(001)

# ExcelOpenSmeupWS

Webservice installato su gilberto, una macchina della rete Smea.

Ha un metodo che riceve in ingresso un F generica e restituisce l'XML.

E' stato utilizzato per mettere a punto il webservice che c'è al MIX e che viene interrogato dal plugin di EXCEL.

E' testabile all'indirizzo : 
 :  : DEC T(J1) P(PATHFILE) K( http://gilberto.smea.it:8080/ExcelOpenSmeupWS/OpenSmeupService?Tester) I(pagina di test)

**Va posta attenzione alla porta :  il WS utilizza la 8080**


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
