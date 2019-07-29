
## Introduzione

Il modulo oggetti remoti (WSREOB) si occupa della gestione di oggetti e OAV remoti.

Un oggetto è remoto quando le sue istanze vengono recuperate tramite webservice. Un esempio può essere l'oggetto V5_GDR (File di Google Drive) le cui istanze sono la lista dei file di una determinata cartella di Google Drive.

Un OAV (per approfondimenti su cosa è un OAV vedere :  http://wikidoc.smeup.com/Wiki.jsp?page=MBDOC_OPE-BX_OAV) è remoto quando il suo valore viene recuperato da un webservice.

I webservices utilizzabili sono quelli integrati in Sme.UP tramite il modulo A38. Per la lista di tali ws e per documentazione in materia sull'A38 chiamare : 

o v2 locos a38

Per recuperare gli script che definiscono gli oggetti e gli OAV remoti chiamare : 

F(TRE;*TBL;) 1(MB;SCP_WSI;)

Gli script che iniziano per V5 definiscono oggetti remoti, quelli che iniziano con OA_ definiscono OAV remoti.


- [Oggetti remoti](Sorgenti/MB/DOC/WSREOB_01)
- [OAV remoti](Sorgenti/MB/DOC/WSREOB_02)
