 :  : HEA PRIV(001)

# PDFOpenSmeupWS

Webservice installato su gilberto, una macchina della rete Smea.

Ha due metodi :  uno restituisce un PDF fisso, il secondo metodo riceve in ingresso un F generica e restituisce l'XML.

E' interrogabile all'indirizzo : 

http://gilberto.smea.it:8080/PDFOpenSmeupWS/OpenSmeupService?WSDL

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

