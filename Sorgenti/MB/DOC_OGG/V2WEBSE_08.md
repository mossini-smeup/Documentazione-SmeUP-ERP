 :  : HEA PRIV(001)

# ArchiboxSmeupWS

E' un webservice, installato su Gilberto e risponde alle richieste di Archibox.
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
