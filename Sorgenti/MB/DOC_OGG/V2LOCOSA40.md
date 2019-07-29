# COSTRUTTORE DATI DA FONTI ESTERNE

Gestisce il trasferimento di un file excel su As400 con aggiornamento di files di Data-Base Smeup tramite EDI.

Il processo è suddiviso in tre parti : 
* Trasferimento di un file CSV su un file DB di AS400.
* Trasformazione del file DB di AS400 in un nuovo file DB con colonne scelte e aggiunta di nuove colonne mediante l'utilizzo delle funzioni Smeup.
* Passaggio dati Data-Base Smeup tramite Mail_up.

## TRASFERIMENTO FILE CSV SU AS400

Traferisce un file CSV  su un file DB di aS400.
Il file origine deve essere in formato CSV con un numero massimo di colonne pari a 50.

Funzioni disponibili : 
* Cartella file origine :  Apre la cartella dove risiede il file origine. La cartella deve essere impostato nella variabile "VarFld"
* File origine :  Apre la scheda del file origine. Il file origine deve essere impostato nella variabile "VarFil"
* Trasferimento , Il file origine viene trasferito su AS400. Il file AS400 deve essere indicato nella variabile "VarDB1"
* Contenuto file trasferito. Presenta il risultato del trasferimento del file DB1 AS400

## TRASFORMAZIONE

Costruisce un nuovo file AS400 a partire da quello trasferito utilizzando funzioni Sme_up per l'aggiunta di nuove colonne.
Ogni colonna del nuovo file deve essere impostata nella riga di script " :  : FLU.FLD" , dove devono essere indicate le seguenti informazioni
* "Nam" = Nome della colonna (Max 10 caratteri), Obbligatorio
* "Txt"  = Descrizione della colonna. Obbligatorio
* "Typ"  = Tipo oggetto Smeup della colonna, Facoltativo
* "Ori"  = Campo del file DB1 con cui costruire la colonna, Obbligatorio
* "Met"  = Metodo con cui calcolare la nuova colonna a partire dalla colonna "Ori". La variabile "Ori" deve contentere necessariamente un colonna del nuovo DB2. Questo per avere la tipizzazione del campo.
* "Par"  = Parametri del metodo. Variano in fiunzione del metodo.
I metodi implementati sono
- "OAV" carica il valore risutante dell'OAV, Nel parametro va indicato l'attibuto video.
- "DES" deriva il codice dalla decrizione. Nessun parametro,
- "DEC" carica la decrizione, Nessun parametro
- "CAT" Concatena ka colonna "Ori" con qualunque altra colonna sia del DB1 che del DB2. Nel parametro va indicato il nome della colonna da concatenare.


Funzioni disponibili
* Variabili di trasformazione :  Presenta le variabili dello script  :  : FLU.FLD che rappresentano le colonne del nuovo file
* Trasformazione :  Esegue la costruzione del file DB2.  Il file AS400 deve essere indicato nella variabile "VarDB2"
* Contenuto file trasformato :  Presenta il risutltato della costruzionde del file DB2 AS400.

## TRAFERIMENO NUOVO FILE NEL DATA-BASE SMEUP TRAMITE MAIL_UP

Trasferisce il nuovo file nel Data-Base Smeup tramite Mail_up.

Ogni import deve essere impostato nella riga di script " :  : FLU.MUP" dove devono essere indicate le seguenti informazioni
* "Nam" = Nome dell'elaborazione, Obbligatorio
* "Txt" = Testo dell'elaborazione, Obbligatorio
* "Fil" = Nome del file Smeup da aggiornare, Obbligatorio
* "Met"  = Metodo con cui applicare mail_up
* "Par"  = Parametri del metodo. Variano in fiunzione del metodo.
* "Est"  = Fistri di estrazione, è possibile indicare le condizioni where in formato SQL aggiuntive per filtrare la tabella origine
I metodi implementati sono
- "OAV" Mail_up con import del campo corrispondente all'OAV scelto, Nel parametro vanno indicati i seguenti campi : .
* T1(XXXX) = Tipo oggetto Smeup del campo chiave 1, Obbligatorio in funzionde del file destinazione
* K1(XXXX) = Campo chiave 1, Obbligatorio
* T2(XXXX) = Tipi oggetto Smeup dal campo chiave 1, Obbligatorio in funzionde del file destinazione
* K2(XXXX) = Campo chiave 2, Obbligatorio in funzionde del file destinazione
* T3(xXXX) = Tipo oggetto Smeup del campo chiave 3, Obbligatorio in funzionde del file destinazione
* K3(XXXX) = Campo chiave 3, Obbligatorio in funzionde del file destinazione
* TP(XXXX) = Tipo oggetto Smeup del campo da aggiornare, Obbligatorio in funzionde del file destinazione
* OR(XXXX) = Colonna del Data-Base contentente il campo da aggiornare, Obbligatorio
* DE(XXXX) = Campo destinazione del file DataBase Smeup, Obbligatorio
* AZ(XXXXX)  Azione sul file ("WRI" Scittura, "UPD" Aggiornamento, "DEL" cancellazione, "WRIUPD" Scrittura se mancante, aggiornamento se presente), Obbligatorio
- "REC" da definire

Funzioni disponibili
* Variabili passaggio a Mail_up :  Presenta le variabili dello script  :  : FLU.MUP che indicano gli import nel Data-Base Smeup
* Passaggio Mail_up :  Esegue il trasferimento nel file EDRECI del DB2 secondo le condizioni indicate nella riga "FLU.EDI"
* Contenuto scenario Mail_up :  Presenta i dati caricati nel file EDRECI
* Controllo formale dati :  Presenta tutte le righe del file ESRECI in stato "10". Controlla la validità dei dati caricati nel file EDRECI in funzioni del file Smeup da aggiornare. Per ciascuna riga segnala la presenza di errori. L'esecuzione del controllo , tramite un bottone specifico, porta le righe senza errori in stato "40"
* Applicazione al DATABASE :  Presenta tutte le righe del file ESRECI in stato "40". L'esecuzione del'elaborazione, tramite un bottone specifico, esegue l'import del dato sul file Smeup e porta le righe elaborate in stato "80"

Funzioni EDI
* Messaggio "£CS" con programma "EDES_07". Il programma "EDES_07" è un deviatore ai programmi specifici relativi al file in aggiornamento..
* Messaggi implementati : 
** "MT-CS" per matricole, con programma specifico "EDES_08"
** "PAR-CS" per parametri, con programma specifico "EDES_09"
Per ora sono stati implementati programmi per l'aggiornamento dell'oggetto matricola e dei parametri

## OPEN
* Costruzione implicita nomi file come A40.Gruppo.Sezione.Sottosezione. Esempio A40X10102
* Caricamento implicito di tutti i campi della tabella DB1 in DB2 anche de non definiti. Si mettono i campi solo in aggiunta.
* Gestionne diretta metodi anche su campi origine. Attualmente i metodi sono applicabili su un campo riportato in DB2
* Derivazione implicita del tipo oggetto dove possibile. Per esempio OAV.
* Visualizzazione varibili in set'n play
* Fare un unica visualizzazione delle variabili, come somma variabili trasformazione  e variabli mail_up
* Gestione parametri metodo "DES" :  Risalita simili, eliminazione caratteri speciali, compatta caratteri "space"
* Gestione metodo EDI :  REC (record)
* La parte relativa al controllo e applicazione Mail_up dovrebbe eseguire delle funzioni standard del modulo Mail_up
