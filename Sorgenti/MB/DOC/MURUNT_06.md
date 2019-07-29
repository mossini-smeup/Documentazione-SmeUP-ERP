# Avvio come Eclipse product
Effettuato il download di un'applicazione esistente o effettutato il build di un prodotto
personalizzato, per avviare il product collegato all'applicazione 'application-nio'
in ambiente Linux occorre eseguire il comando : 
**/mu/application-nio/application-nio** per un'esecuzione interattiva, oppure
**nohup /mu/application-nio/application-nio & > /mu/application-nio/application-nio.log**
per un'esecuzione batch.

nella cartella dove è contenuto l'eseguibile è presente il file 'application-nio.ini'
dove è possibile configurare i parametri di lancio del product : 


| 
| .COL Txt="Nome" LunAut="1" A="L" |
| ---|----|
| 
| .COL Txt="Descrizione" LunAut="1" A="L" |
| 
| .COL Txt="Valori" LunAut="1" A="L" |
| -asup.config|File Application.xmi|Percorso file system |
| -asup.application.name|Nome applicazione| |
| -asup.application.port|Porta applicazione| |
| -Dosgi.clean|Pulizia cache| |
| -Dosgi.console|Attivazione della console OSGI|<host> : <port> |
| -Dosgi.console.ssh|Attivazione della console OSGI in SSH|<host> : <port> |
| -Dosgi.instance.area.default|Cartella di root|Percorso file system |
| -Dosgi.requiredJavaVersion|Versione Java|1.8, 1.9 |
| 

