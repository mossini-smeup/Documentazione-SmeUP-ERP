# Archibox Webservice Get Documents

Questo Webservice è in esecuzione sulla macchina che ha installato il software Archibox.

Consente di recuperare i Documenti.

Per facilitarne l'utilizzo all'interno di Loocup è stato creato un server (09) che rende il webservice interrogabile tramite F.



il webservice risponde a questo indirizzo : 

[http://172.16.2.60/soap/getDocuments?wsdl](http://172.16.2.60/soap/getDocuments?wsdl)

## Parametr : i

### Input
 - param_archivio :  archivio
 - param_raccoglitore :  nome raccoglitore
 - param_archibox :  sempre true
 - param_login :  utente archibox
 - param_pwd :  password relativa
 - TIP :  TIPO+PARAMETRO Smeup

### output
array di valori dipendenti da param_raccoglitore

