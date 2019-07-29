 :  : HEA RESP(FF) STAT(80) USAG(FF) DTAG(20160615) ORAG(105800)


# Importare i dati
Importare i dati su AS400 è un'operazione che può essere compiuta in vari modi.
In questo documento Illustreremo la modalità basata su JDBC-ODBC, sviluppata in Loocup.


# Note generali sull'importazione
Se la tabella sorgente contiene caratteri particolari questi verranno sostituiti dal segno "_".
Sono ammessi solo i numeri, le lettere, il segno "_" e il segno "£" .
Se il nome della tabella sorgente è più lungo di 8 caratteri questo verrà troncato. Nella descrizione del file creato su AS400 verrà riportata il nome della tabella sorgente per esteso, privato dei caratteri con codice ascii minore di 32 o maggiore di 122.



# Modalità di accesso al servizio di importazione

Per facilitare l'accesso ai dati esterni è stato predisposta una voce di menù in Loocup. Nelle installazioni di default è presente in **Strumenti** , **Migrazione DB**.
E' stata inoltre predisposta una scheda accessibile tramite il componente di Loocup DBM.

Inoltre nelle schede degli oggetti J7 XLS/XLSX e J7 CSV sono state predisposte delle modalità di interrogazione/importazione dei file.

# Servizo di importazione

Il servizio che importa i dati da un database esterno verso AS400 è il JA_00_19 oppure il JA_00_39.
Il componente di riferimento è il DBM

Il JA_00_39 estende le funzionalità del JA_00_39 e ne semplifica l'utilizzo.
Estende in quanto supera le problematiche della lettura dei file XLS con colonne contenenti dati misti (numerici e alfanumerici), consente inoltre di accedere ai file XLSX.


## Accesso o importazione di dati da database ORACLE
Per importare i dati da un DBOracle, per conoscere i parametri da passare al servizio, si può consultare l'oggetto J5 EDT_SCH/G.DBM.IOR


## Accesso o importazione di dati da database ACCESS
L'accesso a database di tipo ACCESS, è possibile solo configurando una fonte dati ODBC.
Questo impone che venga configurata la fonte dati sul pc dove Loocup è in esecuzione.

## Accesso o importazione da database che supportano il JDBC

Per l'importazione da database che supportano JDBC è necessario : 
 - Avere tra le librerie di Looc.up il JAR del driver JDBC (directory libs)
 - Conoscere il nome della classe Driver Jdbc (solitamente fornito con la documentazione del Driver)
 - Conoscere la Url di connessione al database (solitamente fornito con la documentazione del Driver)

Esempi : 

### MySQL
 :  : PAR L(TAB) T(MySQL)
**Jar** | mysql-connector-java-<versione>-bin.jar ( scaricare da http://dev.mysql.com/downloads/connector/j/ )
**Classe Driver**| com.mysql.jdbc.Driver
**Url di connessione** | jdbc : mysql : //<server>[ : port]/<database>


### Microsoft SQL Server
 :  : PAR L(TAB) T(Microsoft SQL Server)
**Jar** |  jtds-<versione>.jar ( scaricare da http://jtds.sourceforge.net/)
**Classe  Driver** | net.sourceforge.jtds.jdbc.Driver
**Url di connessione** | jdbc : jtds : sqlserver : //<server>[ : port]/<database>



## Importazione da database DB2 con i driver JDBC

### Nomi di libreria riservati

- QSYS2
- SYSCAT
- SYSFUN
- SYSIBM
- SYSPROC
- SYSSTAT
- SYSTEM

In aggiunta è fortemente sconsigliato l'utilizzo di nomi che cominciano per Q oppure per SYS in quanto per convenzione sono riservati al sistema operativo.

E' inostre sconsigliato l'utilizzo di SESSION come nome di schema.

### Metadati
L'acceso ai metadati richiede apposite sintassi di interrogazione, differenti dagli altri DB.

Ad esempio l'elenco delle tabelle è ottenibile mediante la seguente query : 

SELECT *
    FROM QSYS2.TABLES

oppure tramite la seguente query : 

SELECT *
    FROM SYSIBM.TABLES

La prima da la garanzia di essere valida per ogni versione del SO, mentre la seconda potrebbe cambiare al cambiare della release del SO.
La seconda ha il vantaggio di essere molto più performante rispetto alla prima.



### Problematiche note relativamente all'importazione da EXCEL utilizzando il servizio JA_00_19 e metodo IMP.XLS
Esistono varie problematiche legate a BUG dei driver ODBC-JDBC : 
 - le colonne che contengono valori di tipo diverso, ad esempio numerici e alfanumerici, non restituiscono correttamente uno o più tipi. Se ad esempio nella colonna sono presenti in maggioranza valori alfanumerici non vengono restituiti i valori numerici. La soluzione è di esportare il foglio in formato CSV e poi di importarlo. NOTA :  forzare le colonne di tipo solo testo non ha alcun effetto.
 - la prima riga è sempre considerata di intestazione
 - le celle contenenti formule non vengono valutate correttamente :  salvare il foglio in formato CSV e importarlo.
 - le celle contenenti valori numerici senza virgola possono venire restituiti come numeri terminanti con ".0". Salvare il foglio in CSV e poi importarlo.
 - Dimensione del foglio :  65,536 righe di 256 colonne
 - Contenuto di una cella :  32,767 caratteri
 - non è possibile accedere a documenti protetti da password se non sono aperti in Excel.
 - durante il processo di esportazione non è possibile apportare modifiche al foglio excel
 - Fogli di un documento :  limitati alla memoria disponibile
 - Nomi di un documento :  limitati alla memoria disponibile
 - Non è possibile accedere a fogli con nomi contenenti i seguenti caratteri : 
 -- " - apice doppio
 -- ! - punto eclamativo
 -- [ - parentesi quadra aperta
 -- ] - parentesi quadra chiusa
 -- { - parentesi graffa aperta
 -- } - parentesi graffa chiusa
NOTA1 :  l'apice singolo, il ?, il | (pipe), la / e la \ non sono ammessi come nomi dei fogli.

NOTA2 :  è consigliato limitare il set dei caratteri a lettere, numeri e "_".


Maggiori dettagli nel documento (in inglese) : 
[ http://support.microsoft.com/default.aspx?scid=kb;en-us;257819]( http://support.microsoft.com/default.aspx?scid=kb;en-us;257819)

paragrafo "A Caution about Mixed Data Types"
