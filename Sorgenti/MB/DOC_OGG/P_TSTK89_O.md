# OBIETTIVO

## Obiettivo
Gestire tutte le azioni su un oggetto. Dal controllo all'aggiornamento dei suoi dati.
Il flusso di gestione è il seguente : 
. setup
. caricamento struttura
. caricamento dati
. controllo dati
. applicazione o abbandono
Ci sono poi delle funzioni aggiuntive che vengono lanciate in automatico dalle funzioni di gestione
. autorizzazioni
. overlay
. funzione successiva
. deriva oggetto

## Setup
La funzione di setup viene eseguita in automatico prima della gestione.
Ricostruisce tutti i parametri di input in funzione di quelli ricevuti e del nome setup (parametro input "NamSet")
Il "NamSet" corrisponde ad un tag NAM di SCP_A36. In questa tabella è impostare alcuni parametri di input. In particolare : 
* l'eventuale programma di exit
* la struttura SCP_LAY da utilizzare nella gestione
La priorità è sempre per i parametri ricevuti in input.

Lo script SCP_A36 corrisponde al tipo oggetto, in questo vengono ricercati i tag AZI e NAM : 
* AZI corrisponde all'azione di gestione (01, 02, 03, 04, 05) con risalita ad ** se manca l'AZI specifica e con eccezione per l'azione 00 che viene attivata come azione di pre-immissione.
* NAM definisce un contesto particolare in cui si vuole operare. ** è il default, cioè il contesto che viene utilizzato quando si vuole semplicemente eseguire l'azione di gestione sull'oggetto.

All'interno di un'istruzione AZI e NAM, ci può essere una o più istruzioni VAR, queste permettono sulla base dell'attributo Cnz di valutare quale configurazione di parametri applicare all'azione.
In Cnz possono essere indicate variabili d'ambiente o attributi dell'oggetto sulla base delle quali posso decidere che configurazione applicare.

L'azione di pre-immissione 00, viene eseguita in automatico se è stata definita come AZI, serve per definire una serie di domande da porre prima di arrivare la funzione di immissione vera e propria.

## Struttura
La struttura definisce i campi dell'oggetto che si vogliono gestire.
E' il formato video.
Lo standard gestisce solo campi che sono OAV dell'oggetto stesso. In caso si vogliano gestire campi
che non sono OAV vanno definiti nei programmi specifici in tutte le loro funzioni.
La struttura si divide in due parti : 
. lista di campi da gestire
. proprietà di ciascun campo.

La lista dei campi viene definita nei parametro "TipFlt" e "CodFlt".
Ci sono diversi modi per definire la lista dei campi.
Sono gestiti i seguenti tipi di lista "TipFlt" : 
.PRF            Preferiti
 E' una lista di OAV proveniente dai preferiti
.SCH            Schema (SVI)
 E' una lista OAV proveniente da uno schema
.PRE            Prefisso OAV
 E' la lista di OAV che iniziano con un determianto prefisso
.LIS            Lista OAV
 E' una lista di OAV proveniente dalla gestione dell liste.
.OAV            OAV Singolo
 Un singolo OAV
.CAT            Categoria OAV
 E' la lista degli OAV appartenenti ad una categoria
.GES            Solo OAV di gestione(Esclusi G, J, U, V)
 E' la lista degli OAV di gestione. Tutti gli OAV esclusi quelli che iniziano per G, J, U, V
.LAY            Da SCP_LAY
 Sono OAV definiti in uno script del file SCP_LAY
.S-             Questionario
 Sono OAV definiti in uno script del file SCP_CFG
.ALL            Tutti
Il parametro TipFlt e CodFlt che definisce la struttura può essere passato nel richiamo della
funzione. In caso non venga passato ogni oggetto può assumere un proprio default. Che può
essere modificato in una exit utente. In questo modo si possono gestire formati video diversi
all'interno dello stesso oggetto con molta versatilità

La struttura oltre a definire la lista dei campi definisce anche le proprietà di questi campi.
Le proprietà possono essere dell'oggetto o grafiche.

| 
| .COL Txt="Tipo" Lun="10" |
| ---|----|
| 
| .COL Txt="Codice" Lun="10" |
| 
| .COL Txt="Lunghezza" Lun="10" |
| 
| .COL Txt="Intestazione" Lun="50" |
| 
| .COL Txt="Descrizione" Lun="100" |
| Nome     |£89I_NM|15|Nome campo(Cod OAV)|Generalmente è il codice dell'OAV| |
| Proprietà|                  |REACCA_01|REACCA_01|REACCA_01U|REGESA_01|REGESA_01U| |
| .    D    £89I_NM|                     15    Nome campo (cod OAV) |
| .    D    £89I_TX|                     50    Testo |
| .    D    £89I_CF|                     10    Campo del file DB |
| .    D    £89I_OD|                     30    Tp oggetto dinamico |
| .    D    £89I_OG|                     12    Tp oggetto |
| .    D    £89I_LU|                      4  0 Lunghezza |
| .    D    £89I_ND|                      1  0 Numero Decimali |
| .    D    £89I_LG|                      4  0 Lunghezza Grafica |
| .    D    £89I_FG|                      3    Forma Grafica |
| .    D    £89I_PG|                    256    Proprietà Grafiche |
| .    D    £89I_PL|                    100    PArametro libelo |
| .    D    £89I_PA|                    100    Parametri specifici |
| .    D    £89I_KY|                      1    . Campo chiave |
| .    D    £89I_OB|                      1    . Obbligatorio |
| .    D    £89I_NT|                      1    . Non controllo tipo |
| .    D    £89I_NC|                      1    . Non controllo / ** |
| .    D    £89I_IO|                      1    . Input/Output |
| .    D    £89I_CS|                      2    . case sensitiv |
| .    D    £89I_TF|                      1    . testo fisso |
| .    D    £89I_LM                       1    . Log di modifica |
| .    D    £89I_AR                       1    . Autoenter |
| .    D    £89I_AU                       1    . Autorizzazioni |
| 

Nome campo
.    D  £89I_NM                      15    Nome campo (cod OAV)
        Generalmente è il codice dell'OAV.
Prorpietà : 
.    D  £89I_TX                      50    Testo
        E' l'intestazione del campo presentata in gestione
.    D  £89I_CF                      10    Campo del file DB
        E' il corrispondente campo da aggiornare del DB.
.    D  £89I_OD                      30    Tp oggetto dinamico
        E' il tipo oggetto espresso nella forma dinamica
        Viene utilizzato per determinare l'effettivo oggetto da controllare e
        per il dinamismo della matrice grafica.
.    D  £89I_OG                      12    Tp oggetto
        E' il tipo oggetto con risolto l'eventuale dinamismo per i controlli
.    D  £89I_LU                       4  0 Lunghezza
        E' la lunghezza del campo
.    D  £89I_ND                       1  0 Numero Decimali
        E' il numero di decimali per i campi numerici
.    D  £89I_LG                       4  0 Lunghezza Grafica
        E' la lunghezza di presentazione grafica del campo
.    D  £89I_FG                       3    Forma Grafica
        E' la forma di presentazione grafica del campo
.    D  £89I_PG                     256    Proprietà Grafiche
        E' il parametro di presentazione grafica del campo
.    D  £89I_PL                     100    PArametro libelo
        E' un parametro libero.
        Esempio di utilizzo : 
        nei parametri contine se il parametro è singolo, multimplo o datato,
        e la sua eventuale configurazione.
.    D  £89I_PA                     100    Parametri specifici
        E' un campo di work che sottostringa una serie di parametri definiti sotto
.    D  £89I_KY                       1    . Campo chiave
        Indica se all'interno del DB è un campo chiave
        Valori possibili : 
        " " Si
        "1" No
.    D  £89I_OB                       1    . Obbligatorio
        Indica se se il campo è obbligatorio
        Valori possibili : 
        " " non obbligatorio
        "O" obbligatorio
.    D  £89I_NT                       1    . Non controllo tipo
        Indica se l'oggetto non deve essere controllato
        Valori possibili : 
        " " Si
        "1" No
.    D  £89I_NC                       1    . Non controllo / **
        Indica se la consistenza non deve essere controllata
        Valori possibili : 
        " " Si
        "1" No
.    D  £89I_IO                       1    . Input/Output
        Indica il tipo di presentazione grafica
        Valori possibili : 
        "B" Input/Output
        "O" Solo Output
        "H" Hiden
.    D  £89I_CS                       2    . case sensitiv
        Indica il tipo case sensitiv
        Valori possibili : 
        "LC" Accetta minuscole
        "UC" Solo maiuscole
.    D  £89I_TF                       1    . testo fisso
        Indica se l'instestazione non deve essere cambiata nel caso di campi dinamici
        Valori possibili : 
        " " Cambia
        "1" Fissa
.    D  £89I_LM                       1    . Log di modifica
        Indica il tipo di log che si vuole attivare in modifica
        Valori possibili : 
      * " "  Se attivo log o notifica da oggetto
      * "1"  Si, sempre
      * "2"  Si, sempre con notifica
      * "3"  No, mai anche se attivo su oggetto)
      * "4"  No notifica, mai anche se attiv.su oggetto)
.    D  £89I_AR                       1    . Autoenter
        Indica se i campo innesca l'autoenter della matrice modificabile
        Valori possibili : 
        " " No
        "1" Si
.    D  £89I_AU                       1    . Autorizzazioni
        Contiene l'autorizzazione sul campo
        Questo campo imposta la proprietà _IO presente nell'OAV.
        In ultima istanza verifica che la prorietà di IO impostata nella exit o nell'SCP_LAY sia
        inferiore a quella di questo campo. In caso contrario
        Valori possibili : 
        "B" Input/Output
        "O" Solo Output
        "H" Hiden

Queste proprietò possono avere la seguente origine : 
"A" Da Definizione
    Come prima istanza le proprietà di un campo sono quelle insite nella sua definizione.
    Vengono impostate dal programma di gestione struttura B£K89S che le deriva direttamente dalla
    copy £OAV o £IR1 del file in gestione.
"B" Dal programma di gestione struttura
    Solo le proprietà costruite o forzate direttamente dal programma di gestione struttura B£K89S.
"C" Dal programma base
    Solo le caratteristiche costruite o forzate direttamente dal programma base B£K89G
"D" Dal programma specifico
    Solo le proprietà costruite o forzate dal programma specifico dell'oggetto B£K89_XX
"E" Dal programma di exit
    Solo le proprietà costruite o forzate dal programma di exit
"F" Dal SCP_LAY
    Solo le proprietà costruite o forzate nell'SCP_LAY
"G" Da Autorizzazioni
    Solo le proprietà forzate dei limiti imposti dalle autorizzazini

E' sempre possibile aggiugere elementi alla struttura o modificare le proprietà di un campo nel
programma di exit.

NOTA IMPORTANTE : 
Poichè la struttura si basa come default sugli OAV di un oggetto è importante che vengano
ricostruiti nel caso si aggiungano nuovi parametri, o nuove contenitori e/o capitoli note.
Il programma standard degli OAV costruisce questi attributi nel segente formato : 
. parametri  P/XXX/YYY dove
  .. XXX è la categoria, tabella "C£E" e campo DB C£TPRC
  .. YYY è il parametro, tabella "B£NXX" e campo DB C£NUMP.
  il programma standard di gestione B£K89_PA li riconosce e gestisce nel file di DB.
. note       N/XXX/YYY dove
  .. XXX è il contenitore, tabella "NSC" e campo DB C$TIPC
  .. YYY è il tipo informazione, tabella "NSI" e campo DB C$TIPI
  il programma standard di gestione B£K89_NT li riconosce e gestisce nel file di DB.

## Caricamento valori
Il caricamento valori si distingue in tre diverse modalità in funzione dell'azioni che si sta
eseguento
. Azione "00" :  pre-immissione
. Azione "01" :  immissione nuovo oggetto
. Altre azioni :  gestione oggetto esistente
La pre-immissione generalmente chiede delle informazioni preliminari ncessarie prima di poter
esegure l'immissione. Non necessita della lettura di dati se non di quelli ricevuti in input.
Anche se poi è il programma specifico del'oggetto che definisce la sue specificità
L'immissione di uno oggetto generalente esegue il suo inizializzatore specifico.
Qualore si volesse far arrivare determinati campi all'inizializzatore o assuemrli come
default si deve utizzare il parametro "InzDat". La sua struttura è NomeCampo(Valore),
dove in NomeCampo può essere : 
. £89I_NM il nome dell'OAV           Esempio classe materiale articolo :   I/10(PIPPO)
. £89I_CF il nome del campo del DB                                       A§CLMA(PIPPO)
. £K89_OG l'oggetto                                                      TACLS(PIPPO)
Nel caso di oggetto vengono caricati tutti i campo con quell'oggetto
Il campo deve necessariamente essere presente nella struttura. Se non lo si vuole vedere basta
definirlo come Hidden.
La gestione di un oggetto esegue la lettura di tutti gli OAV che compongono la struttura.
Per ottimizzare le lettura nel caso di OAV interni è stato inibilito il caricamento tramite OAV
e implementata la lettura diretta del reòord del file.
Questa funzione viene eseguita dal programma specifico dell'oggetto.
In ultima istanza sia per per l'immissione che per la gestione si passa dal programma specifico
sia dell'oggetto che della exit utente dove è possibile intervenire sul caricamento di dati
Anche in questo caso è possibile intrventire sui campi nel programma di exit

## Controllo
I controlli sono a tre livelli : 
. controlli generici di oggetto
. controlli specifici dell'oggetto
. controlli utente
I controllo generici sono fatti dalla K89 e controllano semplicemente la validità dell'oggetto
(tranne il caso in cui non venga esplicamente detto nelle sue proprieà di non eseguire controlli)
I controllo specifici dell'oggetto sono definiti nel programma specifico dell'oggetto. Ogni
oggetto può decidere determinati controlli di validtà o di congruenza dei dati.
I controllo utente sono definiti nel programma di exit.

## Applicazione
L'applicazione è l'esecuzionw dell'azione che si è scelta nel richiamo. Parametro "AziExe".
Sono gestite le seguenti azioni : 
"00" Pre-Immissione
"    E una funzione che presenta un formato video. Si caricano dei campi ma poi non esegue
     alcuna azione sul DB, ma una funzione successiva di immissione.
     Può essere usata come configurazione di un campo.
     Oppure come una richiesta iniziale di valori per poi lanciare l'azione "01" con quei
     valori preimpostati
"01" Immissione
     E' l'azione di immissione di un oggetto
"02" Modifica
     E' l'azione di modifica di un oggetto
"03" Copia
     E' l'azione di copia un oggetto in un altro oggetto
"04" Cancella
     E' l'azione di cancellazione di un oggetto
"05" Visualizza
     E' l'azione di visualizzazione i un oggetto


## Deriva
* Oggetto.
Permette di derivare il codice oggetto qualora in input non si conosca me ci siano altre informazioni con cui è possibile identificarlo univocamente.
Per esempio nei clienti quando si conosce la partita iva ma non il codice cliente.
Viene eusato principalmente per l'import di dati LOA40.

## AUT
* Autorizzazioni
Controlla l'autorizzazione sull'azione scelta

## OVR
* Overlay
E' la funzione che esegue l'ovrlay delle proprieta dei campi della struttura dall SCP_LAY scelto

## Funzioni e metodi
SET       Setup
CAR       Carica OAV
 ALL       Struttura e valori
 STR       Struttura
 VAL       Valori
 ERR       Solo in errore
AUT       Autorizzazioni
OVR       Overlay
CTR       Controllo
           Standard
 OGG       Oggetto (carica valori)
APP       Applicazione
DER       Derivazione
 OGG       Oggetto

## Parametri K89
.AziExe Azione da eseguire
.TipFlt Tipo filtro
.CodFlt Codice filtro
.InzDat Dati per inizializzazioe
.ScpLay ScpLay di override delle proprità dei campi
.PgmK89 E' il suffisso XX del programma specifico B£K89_XX che si vuole forzare in sostituzione del suffisso standard che corrisponde all'oggetto in essere (£K89I_TP)
.ParK89 Sono dei parametri specifici da fa arrivare al programma di exit
.FltErr Indica che si vuole forzare la presentazione dei soli campi in errore.
.PgmExi E' programma di exit

## LOA36
La K89 viene utilizzata principalmente dal LOA36_OA nella gestione di un oggetto.
Esegue tutte le funzioni di
. caricamento struttura
. caricamento dati
. controllo dati
. applicazione
Nella funzione di applicazio è possibile eseguire una funzione successiva. La funzine successiva
viene eseguita solo se l'azione è andata a buon fine.
La funzione finale deve essere passata nel parametro "FunFin". Non deve essere messo l'oggetto
master 1(XX;YYY;ZZZZ) perchè viene costruito dinamicamente dal servizio in modo che possa richiamare
il nuovo oggetto in immissione e l'oggetto in essere in gestione. Inoltre nel suo parametro P()
vengono passati tutti i campi della struttura nel formato NomeCampo(Valore), dove nome campo
è solo la variabile £89I_NM che contiene il nome dell'oav.
Inoltre nel formato video ci sono due bottoni di utility che presentano : 
. i campi previsti della struttura dell'oggetto
. i campi effettivamente gestiti nella struttura in essere. In questo caso snon presenti anche
  valori e errori.
Parametri gestiti nel LOA36.
 NamSet     Nome del Setup
 MatMod     Indica se la matrice è modificabile
 BtnF06     Indica se si vuole gestire il bottone di conferma
 BtnF03     Indica se si vuole gestire il bottone di exit
 MsgExe     Indica se si vuole un messaggio finale dopo l'execuzione a buon fine
 FunSuc     Indica la funzione successiva che viene lanciata se l'esecuzione è a buon fine.
 FunSucInp  Indica se non si vogliono passare i dati ddella matrice come dati di input alla FunSuc
 CloFin     Indica se si vuole chiudere la finestra alla fine dell'esecuzione
 PgmA36     Indica il programma specifico di gestione
 TipFlt     Gestito in K89
 CodFlt     Gesttio in K89
 FltErr     Gestito in K89
 AziExe     Gestito in K89
 InzDat     Gestito in K89
.SscInf     Gestito nella Scheda LOA36. Possibile impostazione in K89.
.SscInfPos  Gestito nella Scheda LOA36. Possibile impostazione in K89.
.SscInfDim  Gestito nella Scheda LOA36. Possibile impostazione in K89.
 ScpLay     Gesttio in K89
 PgmK89     Gestito in K89
 ParK89     Gestito in K89
 PgmExi     Gestito in K89
 FldPerCol  Numero colonne per riga
 FunSucSos  Si vuol forzare la Funz.sucessiva rispetto a quella eventualemnte costruita nella exit.
 DatG00     Carica i parametri di input dalla £G00

## Messaggio
Ogni errore viene caricato nelle schiere dei messaggi : 
. £89O_PN Puntatore schera DB
. £89O_TP Tipo messaggio
. £89O_CD Codice messaggio
. £89O_TX Testo messaggio
. £89O_GM Gravità messaggio
. £89O_PG Programma messaggio
Per ogni campo viene presensato il suo primo messaggio.
E' sempre possibile visualizare attraverso il bottone "Dettaglio messaggi" tutti i messaggi
caricati. Dove in particolare sarà visibile la gravità e il programma che ha determinato il
il messaggio. Se la gravità del messaggio è inferiore a "33" il messaggio sarà di solo warning e non determinerà l'errore sul suo campo.


## Gestione Parametri Smeup (Campi configurati)

I parametri si possono presentare in 9 tipologie di gestione.

Ciascuna viene gestita nella £K89 con una sua forma specifica

* parametro SINGOLO alfanumerico
Viene presentato come campo il parametro con l'oggetto della tabella "B£N"
Il parametro K89I_PL contiente l'informazione di parametro singolo alfanumerico nella forma Par(A)

* parametro SINGOLO numerico
Viene presentato come campo il parametro con l'oggetto fisso "NR"
Il parametro K89I_PL contiente l'informazione di parametro singolo numerico nella forma Par(N)

* parametro SINGOLO alfanumerico e numerico
Il parametro viene suddiviso in due campi : 
** Un campo alfanumerico con l'oggetto dalla tabella "B£N". Viene aggiunto il suffisso /A£K89 al
nome del campo (Esempio P/NOM/NOM/A£K89)
Il parametro K89I_PL contiente l'informazione di parametro singolo alfanumerico nella forma Par(SA)
** Un campo numerico con oggetto fisso "NR". Viene aggiunto il suffisso /N£K89 al nome del campo.
(Esempio P/NOM/NOM/N£K89).
Il parametro K89I_PL contiente l'informazione di parametro singolo numerico nella forma Par(SN)

* Parametro MULTIPLO alfanumerico
Il parametro viene presentato con un campo che diventa : 
* Un oggetto "LC" con tipo oggetto l'oggetto della tabella "B£N" (Esempio LCTABSA)
* Una lunghezza fisso di 2000
* Un campo di solo output
* Il campo contiene tutti i valori multipli nell'identificatico CD() e con separatore di record ";"
Esempio :  CD(AR1);CD(AR2);CD(AR3);
Il parametro K89I_PL contiente l'informazione di parametro multiplo alfanumerico nella forma Par(MA)
e l'informazione della configurazione nella forma LC(CD)

* Parametro MULTIPLO numerico
Il parametro viene presentato con un campo che diventa : 
* Un oggetto "LC" con tipo oggetto fisso "NR" (Esempio LCNR)
* Una lunghezza fisso di 2000
* Un campo di solo output
* Il campo contiene tutti i valori multipli nell'identificatico NR() e con separatore di record ";"
Esempio :  NR(1,50000);NR(2,50000);NR(7,00000);
Il parametro K89I_PL contiente l'informazione di parametro multiplo numerico nella forma Par(MN)
e l'informazione della configurazione nella forma LC(NR)

* Parametro MULTIPLO alfanumerico e numerico
Il parametro viene presentato con un campo che diventa : 
* Un oggetto "LC" con tipo oggetto l'oggetto della tabella "B£N" (Esempio LCTABSA)
* Una lunghezza fisso di 2000
* Un campo di solo output
* Il campo contiene tutti i valori multipli nell'identificatico CD() e NR() con separatore di
record ";"
Esempio :  CD(AR1)NR(1,50000);CD(AR2)NR(2,50000);CD(AR3)NR(7,00000);
Il parametro K89I_PL contiente l'informazione di parametro multiplo alfanumerico e numerico nella
forma Par(MAN) e l'informazione della configurazione nella forma LC(CD;NR)

* Parametro MULTIPLO E DATATO alfanumerico
Il parametro viene presentato con un campo che diventa : 
* Un oggetto "LC" con tipo oggetto l'oggetto della tabella "B£N" (Esempio LCTABSA)
* Una lunghezza fisso di 2000
* Un campo di solo output
* Il campo contiene tutti i valori multipli nell'identificatico CD(), DI() e DF() e con separatore
di record ";"
Esempio :  CD(AR1)DI(20150101)DF(20151231);CD(AR2)DI()DF();CD(AR3)DI(20150501)DF(20150531);
Il parametro K89I_PL contiente l'informazione di parametro multiplo alfanumerico e datato nella
forma Par(DA) e l'informazione della configurazione nella forma LC(CD;DI;DF)

* Parametro MULTIPLO E DATATO numerico
Il parametro viene presentato con un campo che diventa : 
* Un oggetto "LC" con tipo oggetto fisso "NR" (Esempio LCNR)
* Una lunghezza fisso di 2000
* Un campo di solo output
* Il campo contiene tutti i valori multipli nell'identificatico NR(), DI() e DF() e con separatore
di record ";"
Esempio :  NR(1,50000)DI(20150101)DF(20151231);NR(7,00000)DI(20150501)DF(20150531);
Il parametro K89I_PL contiente l'informazione di parametro multiplo numerico e datato nella
forma Par(DN) e l'informazione della configurazione nella forma LC(NR;DI;DF)

* Parametro MULTIPLO E DATATO alfanumerico e numerico
Il parametro viene presentato con un campo che diventa : 
* Un oggetto "LC" con tipo oggetto l'oggetto della tabella "B£N" (Esempio LCTABSA)
* Una lunghezza fisso di 2000
* Un campo di solo output
* Il campo contiene tutti i valori multipli nell'identificatico CD(), NR(), DI(), e DF(), e con
separaotre di record ";"
Esempio :  CD(AR1)NR(1,50000)DI(20150101)DF(20151231);CD(AR2)NR(7,00000)DI(20150501)DF(20150531);
Il parametro K89I_PL contiente l'informazione di parametro multiplo alfanumerico, numerico e datato
nella forma Par(DAN) e l'informazione della configurazione nella forma LC(CD;NR;DI;DF)

