
# Scrittura dati della fattura
La procedura di generazione e invio degli xml delle fatture elettroniche prevede la scrittura di un file di transito che contiene in diversi tracciati tutte le informazioni contenute nella fattura.
**$EDSEND0F è il file di transito da scrivere.**
**I tracciati dei file EDFEIT* sono utilizzati come DS esterna contenente i dati che vanno nel campo varying R$DATI del $EDSEND0F. 
La creazione dei file xml avviene su IFS e i file xml vengono poi inviati ad Abletech tramite webservice attraverso lo Smart Kit FE.
Il savf P_FENS è salvato per V5R4 e contiene file, programmi e i sorgenti.
Le istruzioni di installazione si trovano nel membro README del file sorgente DOC.

## Tracciati  da valorizzare : 

|  Nam="Tracciati" |
| 
| .COL Txt="Nome tracciato" |
| ---|----|
| 
| .COL Txt="Descrizione" |
| 
| .COL Txt="Obbligatorio" |
| 
| .COL Txt="Riga singola o multipla" |
| EDFEIT01|Testata|Obbligatorio|Singola |
| EDFEIT02|Dettaglio riga|Obbligatorio|Multipla |
| EDFEIT03|Totali|Obbligatorio|Singola |
| EDFEIT04|Commenti di testata|Opzionale|Multipla |
| EDFEIT05|Scadenze di pagamento|Opzionale|Multipla |
| EDFEIT07|Commenti di riga|Opzionale|Multipla |
| EDFEIT08|Log|Opzionale|Singola |
| EDFEIT09|Sconti testata|Opzionale|Multipla |
| EDFEIT10|Riepilogo IVA|Obbligatorio|Multipla |
| EDFEIT11|Sconti riga|Opzionale|Multipla |
| EDFEIT12|Testata (Altri dati)|Opzionale|Singola |
| EDFEIT13|Ordine acq/Contratto/Convenzione|Necessari se gestito CIG o CUP|Multipla |
| EDFEIT14|DDT|Opzionale|Multipla |
| EDFEIT15|SAL|Opzionale|Multipla |
| EDFEIT16|Codifiche articolo (con riferim. a riga del tracciato EDFEIT02)|Opzionale|Multipla |
| EDFEIT17|Cassa previdenziale|Opzionale|Singola |
| EDFEIT18|Dati trasporto|Opzionale|Singola |
| EDFEIT19|Allegati|Opzionale, serve ad esempio ad allegare il pdf della fattura|Multipla |
| 


## Campi file $EDSEND

|  Nam="$EDSEND" |
| 
| .COL Txt="Obbligatorio" Ogg="V2SI/NO" |
| ---|----|
| 
| .COL Txt="Nome campo" |
| 
| .COL Txt="Descrizione" |
| 
| .COL Txt="Tipo Dato" |
| 
| .COL Txt="Varying" |
| 
| .COL Txt="Lun." |
| 
| .COL Txt="Dec." |
| 
| .COL Txt="Spiegazione" |
| 1|R$MESS|Codice messaggio trasmesso|A||15||'£FE' |
| 1|R$ENOR|Indirizzo origine|A||15||'£FE02' |
| 1|R$ENDE|Indirizzo destinazione|A||15||'£FE01' |
| 1|R$CD01|Codice ricerca 1|A||15||Registro IVA (Sezionale IVA + Anno :  es. VE .18). Prima il sezionale e poi l'anno divisi da punto |
| 1|R$CD02|Codice ricerca 2|A||15||Numero Fattura |
| 1|R$CD03|Codice ricerca 3|A||15||'CLI'+ Codice cliente (es. CLI31A789). Se nome tracciato EDFEIT02 o EDFEIT07 o EDFEIT11 o EDFEIT16 o EDFEIT13 o EDFEIT14 mettere il numero riga fattura a cui si riferisce (es. 0005) |
| 1|R$USAG|Utente aggiornamento|A||10||Utente |
| 1|R$DTNA|Data di nascita|S||8|0|YYYYMD |
| 1|R$ORNA|Ora di nascita|S||6|0|HHMMSS |
| 1|R$DTES|Data di esecuzione|S||8|0|YYYYMD |
| 1|R$ORES|Ora di esecuzione|S||6|0|HHMMSS |
| 1|R$BATC|Numero lotto|A||10||Numero identificativo univoco del lotto di trasmissione (es. 1600000006) |
| 1|R$NRTR|N.ro Transazione|P||9|0|Contatore univoco delle righe del lotto. Va incrementato in modo sequenziale a ogni scrittura |
| 1|R$TTRA|Tipo Tracciato|A||10||'F-' |
| 1|R$NTRA|Nome Tracciato|A||10||nome del tracciato utilizzato (es. EDFEIT01, EDFEIT02 ecc) |
| 1|R$LIVE|Livello|A||1||'2' |
| 1|R$STAT|Stato messaggio|A||2||'10' |
| |R$AL01|Codice 1|A||15||non usato |
| |R$AL02|Codice 2|A||15||non usato |
| |R$AL03|Codice 3|A||15||non usato |
| |R$AL04|Codice 4|A||15||non usato |
| |R$AL05|Codice 5|A||15||non usato |
| |R$NR01|Numero 1|P||15|5|non usato |
| |R$NR02|Numero 2|P||15|5|non usato |
| |R$NR03|Numero 3|P||15|5|non usato |
| |R$NR04|Numero 4|P||15|5|non usato |
| |R$NR05|Numero 5|P||15|5|non usato |
| |R$DT01|Data 1|P||8|0|non usato |
| |R$DT02|Data 2|P||8|0|non usato |
| |R$DT03|Data 3|P||8|0|non usato |
| |R$DT04|Data 4|P||8|0|non usato |
| |R$DT05|Data 5|P||8|0|non usato |
| |R$FL01|Riservato Smeup|A||1||non usato |
| |R$FL02|Stato invio fat.PA|A||1||ad uso interno della procedura |
| |R$FL03|Esito invio fat.PA|A||1||ad uso interno della procedura |
| |R$FL04|Livello PTF|A||1||ad uso interno della procedura |
| |R$FL05|Riservato Smeup|A||1||non usato |
| |R$FL06|Riservato Smeup|A||1||non usato |
| |R$FL07|Riservato Smeup|A||1||non usato |
| |R$FL08|Riservato Smeup|A||1||non usato |
| |R$FL09|Riservato Smeup|A||1||non usato |
| |R$FL10|Riservato Smeup|A||1||non usato |
| |R$FL11|Riservato utente|A||1||non usato |
| |R$FL12|Riservato utente|A||1||non usato |
| |R$FL13|Riservato utente|A||1||non usato |
| |R$FL14|Riservato utente|A||1||non usato |
| |R$FL15|Riservato utente|A||1||non usato |
| |R$FL16|Riservato utente|A||1||non usato |
| |R$FL17|Riservato utente|A||1||non usato |
| |R$FL18|Riservato utente|A||1||non usato |
| |R$FL19|Riservato utente|A||1||non usato |
| |R$FL20|Riservato utente|A||1||non usato |
| 1|R$DATI|DATI A LUNGHEZZA VARIABILE|A|SI|20.000||dati della DS esterna corrispondente al nome tracciato indicato nel campo R$NTRA |
| 


Nel file **Tracciato_FatturaPA_versione_1.2.1 - campi gestiti.xls** sono indicati i riferimenti a campo e tracciato $EDSEND per ciascun tag dell'xml ministeriale.

# COMPILAZIONE : 
Gli oggetti distribuiti nel savf **P_FENS** sono compilati a V5R4.

In caso abbiate necessità di compilare il pgm $B£G02B è necessario farlo compilando il sorgente in interattivo dopo aver fatto il bind tramite i comandi sotto riportati.
 * CRTBNDDIR BNDDIR(QTEMP/APRB64) TEXT('APR_BASE64 Binding Directory')
 * ADDBNDDIRE BNDDIR(APRB64) OBJ( (QSYSDIR/QAXIS10HT *SRVPGM))

Qualora non riusciste a compilare il pgm per assenza della PTF IBM che contiene il service program QAXIS10HT, il pacchetto funzionerà comunque correttamente utilizzando funzioni alternative, anche se con delle performance inferiori.

# CONFIGURAZIONE GENERAZIONE XML FATTURE : 
Il percorso su IFS nel quale verranno creati gli xml delle fatture è determinato dal pgm $V5FE01.
Il programma richiamato con funzione GET e metodo ROT restituisce la root della fatturazione elettronica.
La versione distribuita prevede come percorso **/Smedoc/FatturaElettronica/NS**
Richiamato con funzione GET e metodo PAT restituisce invece il percorso dove verrà scritto l'xml della singola fattura
La versione distribuita prevede come percorso la root a cui viene aggiunta una cartella per il registro iva, una per la data fattura e una ulteriore cartella con il numero di fattura.
Per modificare i percorsi intervenire opportunamente personalizzando il pgm **$V5FE01**.

# LANCIO GENERAZIONE XML FATTURE : 
Il programma da richiamare per creare gli xml delle fatture è il **$EDFUC0X**.
Il programma legge i record di $EDSEND0F con livello uguale a '2' e per ciascuna fattura richiama il pgm **$V5FE00** che genera l'xml, portando poi i campi livello e stato del record rispettivamente a '8' e '80'.
In caso vengano rilevati errori (ad esempio campi obbligatori mancanti) lo stato viene valorizzato a '85', gli errori vengono scritti sia nel tracciato EDFEIT08 su $EDSEND che in uno spool e l'xml viene salvato con prefisso ERR_ nella sottocartella Errati del percorso restituito per la singola fattura.

# Come distinguere se si necessita di uno Smart Kit Smeup o NON Smeup

- Se il ciclo attivo è gestito con i **documenti V5** di Sme.UP ERP va configurato uno **Smart Kit Sme.UP**, comunicando quindi al consulente di infrastruttura oltre a utente e pqssword anche il codice ambiente.
- Se il cliente ha la **contabilità di Sme.UP ERP, ma il ciclo attivo non è gestito con i documenti V5** di Sme.UP ERP, va configurato uno **Smart Kit Sme.UP** (utente con programma iniziale B£QQ50, JOBD con librerie SMEUP, Smart Kit configurato con un Ambiente associato tramite UP UT5 all'utente di collegamento) aggiungendo nello **script SCP_CLO** dell'utente dello Smart Kit l'attivazione del plugin necessario per le funzioni non Smeup utilizzate per l'invio fatture tramite il pacchetto NON Smeup.
- Se il cliente **non utilizza Sme.UP ERP** va configurato uno **Smart Kit NON Sme.UP** (l'utente con programma iniziale *NONE, JOBD QDFTJOBD, Smart Kit configurato senza impostare l'ambiente).


## Invio fatture tramite pacchetto NON Smeup in ambienti con Contabilità Sme.UP
Impostarte nello script SCP_CLO dell'utente di collegamento dello Smart Kit l'attivazione del plugin aggiungendo sotto la sezione ** :  : C.SEZ Cod="Server"** le seguenti righe : 
_  :  : C.SER Cod="031" Txt="Abletech Connector Server" Add="localhost" Protocol="JAVA"                Param="class=Smeup.smeui.uicommon.uiexternalservices.java.ix_abletetch.IXWebserviceJavaExternalService" LoadOnStartup="1" 

Nel caso non sia già presente la sezione ** :  : C.SEZ Cod="Server"** aggiungerla prima delle righe sopra indicate.


# CONFIGURAZIONE INVIO AD ABLETECH : 
I parametri di collegamento per l'invio ad Abletech vanno impostati nella exit **$V5CFG_U** di cui si fornisce il sorgente di esempio.

E' necessario **creare la libreria SMEUPUIDQ** necessaria per la creazione delle code dati di comunicazione tra i programmi RPG e Smart Kit.

# REPERIMENTO AooID : 
Per reperire l'AooID necessario all'invio delle fatture ad Abletech è necessario configurare nella exit $V5CFG_U l'utente e la password forniti da Abletech, oltre all'URL di produzione.
Una volta compilato il pgm di exit, richiamare il pgm **$V5AB05** che visualizzerà a video gli AooID associati all'utenza e le relative partite iva.
Aggiungere l'AooID corretto nella exit **$V5CFG_U** e ricompilare il programma.
A questo punto si è pronti ad eseguire l'invio delle fatture ad Abletech.

# LANCIO INVIO AD ABLETECH : 
Il programma da richiamare è il **$V5FE90G** che consente di impostare quali fatture visualizzare e poi esegue il pgm **$V5FE90L** che presenta l'elenco delle fatture in un subfile. Se lo stato invio delle fatture (corrispondente al R$FL02 di $EDSEND) è '2' (da inviare) o '4' (Errore invio) è possibile selezionare le fatture e premendo F06 lanciarne la trasmissione in batch.
Una volta lanciata la trasmissione in batch lo stato invio passa a '3' (Invio in corso).
Per ciascuna fattura è possibile interrogare il log con opzione '05' (che lancia il pgm V5FE90D) leggendolo da $EDSEND.
In caso la trasmissione venga eseguita con successo viene restituito da Abletech un identificativo della fattura (alfanumerico lungo 36 caratteri) che viene scritto nel file $C£ALIA0F. Inoltre il campo R$FL02 dei record di $EDSEND relativi alla fattura (con campo R$MESS = '£FE') viene valorizzato a '5' (Inviato).


| 
| .COL Txt="CAMPO" LunAut="1" |
| ---|----|
| 
| .COL Txt="DESCRIZIONE" LunAut="1" |
| 
| .COL Txt="CONTENUTO" LunAut="1" |
| E$TIP1 | Tipo parametro cod.1   | 'OGFT'| |
| E$COD1 | Codice 1| registro iva| |
| E$TIP2 | Tipo parametro cod.2   | '**'| |
| E$COD2 | Codice 2| numero fatture| |
| E$SCD2 | Suffisso Codice 2| ''| |
| E$LIVE | Livello| '2'| |
| E$STAT | Stato| '10'| |
| E$CONT | Contesto| '£FE'| |
| E$ALIA | Alias| identificativo restituito da Abletech | |
| 


In caso errore nella trasmissione il campo R$FL02 dei record di $EDSEND relativi alla fattura (con campo R$MESS = '£FE') viene valorizzato a '4' (Errore invio).
Vengono inoltre scritti dei record di $EDSEND per il tracciato EDFEIT08 con il log degli  errori.
Il log è interrogabile dal subfile di selezione e invio delle fatture con opzione '05'.

# LOG COMUNICAZIONE CON WEBSERVICE ABLETECH : 
Per interrogare i log di cominicazione eseguire la call al pgm **$V5FE92G** impostando le date di riferimento per visualizzare il dettaglio ($V5FE092D).

# LIMITAZIONI : 
La versione corrente ha alcune limitazioni : 
* permette in incorporare nell'xml solo allegati che si trovano su IFS
* il numero fattura ha lunghezza massima 15 per il ciclo attivo.

# INTERROGAZIONE ESITI : 
Permette di verificare lo stato della singola fattura inviata ad Abletech.
Il programma da richiamare è il $V5FE82G con la funzione (campo U$FUNZ ) 'CHK' e
metodo (campo U$METO ) 'ESI', passando in input il registro iva nel campo U$RIVA e il numero
fattura nel campo U$NRFA .
Il programma restituisce in output l'esito (campo U$ESIT ). Gli esiti possibili sono : 

|  Nam="Esiti" |
| 
| .COL Txt="Valore" |
| ---|----|
| 
| .COL Txt="Descrizione" |
| 1         |Inviata (SDI o Intermediario) |
| 2         |Scartata (SDI o Intermediario) |
| 3         |Mancata consegna a ufficio PA |
| 4         |Consegnata a destinatario |
| 5         |Accettata da ufficio PA |
| 6         |Rifiutata da ufficio PA |
| 7         |Decorrenza termini |
| 8         |Impossibilità recapito |
| A         |Consegnata a SDI |
| 


In caso di errore viene restituito '1' nel campo  U$ERRO, infine un messaggio testuale (campo U$MESS) che indica lo stato rilevato oppure l'eventuale messaggio di errore.
Nello specifico applicativo, il programma esegue un web service di primo livello per il reperimento dell'esito della fattura, se il primo web service non ha rilevato l'esito viene eseguito un web service di secondo livello.

# DOWNLOAD FE PASSIVA : 
## INSTALLAZIONE
Nuovo database che contiene l'elenco delle fatture scaricate
* XFATPA0F
Nuovo database che contiene i dati delle fatture passive elaborate
* $EDRECI0F con i relativi logici
Nuovi programmi : 
* $C5_093LOG
* $C5FE93A
* $C5FE93B
* $C5FE93C
* $C5FE93D
* $C5FE93E
* $C5FE93K
* $C5FE93M
* $B£K19G
* $B£K19_001
* $TSTK19
Programmi da aggiornare : 
* $B£K11G
* $EDEDT0
* $EDFUC0T


|  Nam="FILE XFATPA0F" |
| 
| .COL Txt="CAMPO" LunAut="1" |
| ---|----|
| 
| .COL Txt="DESCRIZIONE" LunAut="1" |
| 
| .COL Txt="CONTENUTO" LunAut="1" |
|  XFPIVA | Partita IVA            | Partita iva fornitore                 | |
|  XFCOFI | Codice Fiscale         | Codice fiscale fornitore              | |
|  XFTDOR | Tipo documento         | TD01,TD02,TD03,TD04,TD05,TD06,TD20    | |
|  XFDDOR | Data documento         | Data fattura fornitore                | |
|  XFNDOR | Numero documento       | Numero fattura fornitore              | |
|  XFIFAT | Id.Fattura             | Identificativo univoco fattura        | |
|  XFFILE | File                   | Nome file che accompagna la fatt.for. | |
|  XFISDI | Identificativo SDI     | Identificativo SDI fattura fornitore  | |
|  XFDENO | Denominazione          | Ragione sociale fornitore             | |
|  XFDRIC | Data ricezione         | Data ricezione fattura                | |
|  XFPERC | Percorso XML           | Percorso dettaglio documento XML      | |
|  XFPROG | Registrazione contabile| Eventuale numero di registraz.contab  | |
| 


Oltre a questi campi ci sono 10 campi liberi alfa, 10 campi liberi numerici e 10 campi liberi date.
## PROCEDURE
Per questo argomento sono stati sviluppate 3 nuove funzioni : 
* $C5FE93A :  esegue download elenco fatture degli ultimi 3 mesi. L'elenco delle fatture viene scritto nel file XFATPA0F a parità di partita iva, codice fiscale, tipo documento, data documento, numero documento. Il programma non ha parametri di ingresso
* $C5FE93C :  programma che legge il file XFATPA0F ove il percorso (campo XFPERC) sia uguale a blank e richiama per ogni identificativo fattura il programma $C5FE93B. Il programma non ha parametri di ingresso
* $C5FE93B :  dato l'identificativo fattura esegue il download dei file di dettaglio. Questo programma ha come parametro di ingresso l'identifativo fattura lungo 36 Alfa
* $C5FE93D :  programma che legge il file XFATPA0F ove il codice registrazione (campo XFPROG) sia uguale a blank, verifica se la fattura è già stata elaborata richiamando il $C5FE93K e richiama per ogni fattura non ancora elaborata il programma $C5FE93E, passando il percorso del file XML (XFPERC) nel campo $K19XMLF e nel campo $K19PARA l'identificativo SdI, l'identificativo Abletech e la data ricezione. Il programma non ha parametri di ingresso
* $C5FE93E :  dato il percorso del file XML della fattura ne esegue l'elaborazione scrivendo il file $EDRECI0F con gli stessi tracciati EDFEIT* utilizzati per le fatture attive. Questo programma ha come parametro di ingresso il percorso dell'XML e un campo opzionale parametro in cui indicare l'identificativo SdI, l'identificativo Abletech e la data ricezione. Come campi di output restituisce un messaggio e un indicatore di errore.
* $C5FE93K :  dato il nome del file XML della fattura verifica se è già stato elaborato e scritto su $EDRECI0F.
* $C5FE93M :  Esempio di programma che legge i file contenuti in una cartella su IFS verifica se il file xml è già stato elaborato richiamando il $C5FE93K e richiama per ogni fattura non ancora elaborata il programma $C5FE93E, passando il percorso del file XML nel campo $K19XMLF . Il pgm $C5FE93M è pensato per gestire il caso di file fattura scaricati direttamente dal cassetto fiscale o in altro modo rispetto al download da Abletech tramite lo smart kit. Il pgm $C5FE93E è in grado di elaborare solo file XML. Se la fattura è in formato .p7m è necessario estrarre l'XML per poterlo elaborare (operazione effettuata dallo smart kit nel caso di download da Abletech).

# RIAVVIO SMART KIT : 
Il programma da richiamare è il $V5FE94G che visualizza il nome dello smart kit e se attivo/non
attivo; premendo F06 viene eseguito il pgm $V5FE90L che ne esegue il riavvio.
Ovviamente solo se lo smart kit è attivo è possibile riavviarlo, in caso contrario per
avviarlo è necessaria assistenza sistemistica.
Dopo aver premuto F06, premendo invio è possibile verificare se lo smart kit è stato riavviato.


# SUGGERIMENTI PER ADEGUAMENTO A VERSIONI SUCCESSIVE : 
* Spostare i file dati in una libreria separata.
* Creare una libreria in cui mettere le personalizzazioni (i pgm modificati e la exit $V5CFG_U)
* In questo modo a fronte di aggiornamenti è possibile confrontare con opzione 54 solo i sorgenti della libreria di personalizzazione (per identificare i pgm da adeguare) e per il resto semplicemente sostituire la P_FENS con la versione aggiornata.


## LISTA LIBRERIE CONSIGLIATA per l'utente che esegue estrazione e invio fatture
QTEMP
P_FENSDAT (libreria contenente i file dati)
P_FENSPER (libreria contenente le personalizzazioni e le exit)
P_FENS (libreria contentente i pgm distribuiti standard)
QGPL

## Impostazioni utente Smart Kit
>     Programma iniziale . . . . . . . . . . . .  :    *NONE
       Libreria . . . . . . . . . . . . . . . .  : 
     Menu iniziale  . . . . . . . . . . . . . .  :    MAIN
       Libreria . . . . . . . . . . . . . . . .  :      *LIBL
      Descrizione lavoro . . . . . . . . . . . .  :    QDFTJOBD
        Libreria . . . . . . . . . . . . . . . .  :      QGPL


