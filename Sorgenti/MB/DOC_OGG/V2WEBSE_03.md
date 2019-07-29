# Archibox Webservice Get Containers

Questo Webservice è in esecuzione sulla macchina che ha installato il software Archibox.

Consente di recuperare i Containers.

Per facilitarne l'utilizzo all'interno di Loocup è stato creato un server (09) che rende il webservice interrogabile tramite F.

## Parametri

il webservice risponde a questo indirizzo, ma non è prevista una pagina di test.
[http://172.16.2.60/soap/getContainers?wdsl](http://172.16.2.60/soap/getContainers?wdsl)


### input
 - **param_archivio** :  archivio
 - **param_archibox** :  sempre true
 - **param_login** :  utente archibox
 - **param_pwd** :  password relativa

### output
 - **ID** :  stringa (ID del contenitore)
 - **Description** :  string (descrizione contenitore)
