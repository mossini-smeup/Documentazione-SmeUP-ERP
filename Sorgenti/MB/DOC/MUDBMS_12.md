
# Creazione DB multipiattaforma con IBM DB2 LUW

Queste istruzioni si riferiscono alla creazione del DB necessario al funzionamento del multipiattaforma. Per
la procedura di l'installazione del prodotto IBM DB2 LUW si demanda alle istruzioni facilemente reperibili in rete.

Al seguente link

[https://github.com/smeup/asup/tree/master/org.smeup.sys.db.script.db2/binaries](https://github.com/smeup/asup/tree/master/org.smeup.sys.db.script.db2/binaries)

sono presenti i compilati del programma di creazione DB per le varie piattaforme.

Sono anche stati creati degli script per il lancio del programma di creazione e per la gestione dei DB
- Versione Windows : 

[https://github.com/smeup/asup/tree/master/org.smeup.sys.db.script.db2/win](https://github.com/smeup/asup/tree/master/org.smeup.sys.db.script.db2/win)

- Versione Linux (tutte le piattaforme HW) : 

[https://github.com/smeup/asup/tree/master/org.smeup.sys.db.script.db2/linux](https://github.com/smeup/asup/tree/master/org.smeup.sys.db.script.db2/linux)

Sia gli script che il file binario devono essere copiati nella cartella bin del software DB2, che per Windows si trova in

>C : \Program Files\IBM\SQLLIB\BIN\

mentre per Linux dovrebbe essere in

>/opt/ibm/db2/V10.5/bin

(10.5 è il numero di versione di DB2 LUW)

Collegandosi con un profilo abilitato al DB2, si dovrebbe poter creare un DB con il comando

>asupdb2create nome_database_da_creare

Al ternime dell'operazione potrebbe essere necessario riavviare il servizio DB2 per consentire la lettura dei nuovi parametri di configurazione.

>db2 stop database manager

>db2 start database manager

## Note su IBM DB2 LUW

### Esempio comando per attribuzione permessi amministativi ad un utente

> GRANT DBADM, CREATETAB, BINDADD, CONNECT, CREATE_NOT_FENCED, IMPLICIT_SCHEMA, LOAD ON DATABASE TO USER ASUP

### Dimensione tablespace

Si noti che la dimensione minima delle pagine deve essere 8 K per garantire la creazione di tabelle con grande lunghezza record.
Si veda ad esempio: http://www.ibm.com/developerworks/data/library/techarticle/0212wieser/

Per superare l'eventuale errore "SQL0286N A table space could not be found with a page size of at least ...." utilizzare i seguenti comandi

>
CREATE BUFFERPOOL MYDB_32K1 IMMEDIATE SIZE 250 AUTOMATIC PAGESIZE 32K;

CREATE LARGE TABLESPACE MYDB_32K1 PAGESIZE 32K MANAGED BY AUTOMATIC STORAGE EXTENTSIZE 32 PREFETCHSIZE 32 BUFFERPOOL MYDB_32K1;

CREATE SYSTEM TEMPORARY TABLESPACE MYDBTEMP_32K1 PAGESIZE 32K MANAGED BY AUTOMATIC STORAGE BUFFERPOOL MYDB_32K1;

### Comandi per aumentare dimensione file log transazioni

Nel caso si debbano inserire/cancellare molte informazioni in una sola transazione, occorre modificare i parametri relativi a numero e dimensione dei file di log,altrimenti è possibile generare l'errore : 
"SQL0964C Il file di log transazioni per il database è pieno"

>UPDATE DATABASE CONFIGURATION FOR db_name USING LOGFILSIZ 1024

UPDATE DATABASE CONFIGURATION FOR db_name USING LOGPRIMARY 20

UPDATE DATABASE CONFIGURATION FOR db_name USING LOGSECOND 236
