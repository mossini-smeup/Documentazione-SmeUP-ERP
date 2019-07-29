# TIPI DI SPECIFICHE DI SME.UP
## Tipi di specifiche per la documentazione
Codificando opportunamente le specifiche di commento nel sorgente di un programma, il testo associato viene interpretato correttamente dai tool di documentazione dei programmi e dalle schede relative : 

| V* | Documentazione modifiche / versioni |
| ---|----|
| D* | Documentazione generale di un programma. All'interno delle DDS, individua una sezione di dati |
| HD* | Documentazione tecnica |
| HF* | Documentazione tecnica files |
| RD* | Documentazione routines |
| 


## Tipi di specifiche per la compilazione
Codificando opportunamente le specifiche di commento nel sorgente di un programma, il comando **CO** esegue determinate azioni in fase di compilazione : 

| PRP* | Comandi da eseguire prima di compilare. Es. la creazione di file di lavoro referenziati ---|
| all'interno del sorgente (altrimenti la compilazione andrebbe in errore perché il file non verrebbe trovato). |
| COP* | Opzioni di compilazione (sovrascrivono le opzioni predefinite del compilatore di sistema) |
| POP* | Comandi da eseguire dopo la compilazione. |
| 


In queste azioni possono essere applicate alcune variabili corrispondenti ai valori inseriti
nei parametri del comando CO stesso : 
 * &CO_MBR  :  Membro Origine
 * &CO_FILO :  File origine
 * &CO_LIBO :  Libreria Origine
 * &CO_OBJ  :  Oggetto
 * &CO_LIBD :  Libreria di destinazione
 * &CO_TIPO :  Tipo Origine

# Convenzioni nella denominazione dei campi video

| __Codifica__|__Descrizione__|__Contesto__ |
| ---|----|----|
| W$|campi input/output | in finestra |
| W£|campi di output (decodifiche) | in finestra |
| W§|campi di output (significati) | in finestra |
| S$|campi input/output | in subfile |
| S£|campi di output (decodifiche) | in subfile |
| S§|campi di output (significati) | in subfile |
| SFR1|Subfile | |
| SFC1|Controller (la specifica relativa va messa in testa per Looc.Up)| |
| SFP1|Piede | |
| WIN1|Finestra| |
| FMT|Formato a tutto schermo| |
| W$MESV|campo per l'emissione a video di messaggi di errore| |
| 


# Altre convenzioni nella denominazione di variabili

| __Prefisso__|__Descrizione__ |
| ---|----|
| T$ | Campi utilizzati nella definifizione di tabelle |
| £ | Variabile di una /COPY |
| AAA | Variabille di lavoro alfanumerica (es. AAA015) |
| NNN | Variabille di lavoro numerica (es. NNN153) |
| O | Variabile di salvataggio |
| 


# Convenzioni nella denominazione di file di stampa

| __Nome__|__Descrizione__ |
| ---|----|
| PRT80 | File di stampa a 80 caratteri |
| PRT132 | File di stampa a 132 caratteri |
| PRT198 | File di stampa a 198 caratteri |
| 


# Utilizzo degli indicatori
Questi i significati che normalmente vengono attributi agli indicatori : 
 * **35** :  indicatore di errore di una funzione
 * **36** :  indicatore di ricerca (segnala che la ricerca è stata effettuata)
 * **50-55** :  indicatore di comodo utilizzato per test di carattere istantaneo (un'instruzione condiziona l'indicatore e l'istruzione successiva testa tale indicatore, viene utilizzato ad esempio su CHAIN, LOOKUP, READE ecc.).

Se sono inoltre presenti campi **video** : 
 * **10** :  indicatore che indica la necessità di riemettere il formato video (es. se ho fatto una ricerca accendo l'indicatore per forzare la riemissione del formato video per visualizzare la mia scelta)
 * **60** :  indicatore di errore generale (di solito va a condizionare il campo del messaggio a video)
 * **61-89** :  indicatori di errore specifico (vengono usati per condizionare gli errori dei singoli campi video)

Nell'utilizzo degli indicatori, è importante sottolineare che il loro significato si esaurisce alla successiva istruzione. Ciò significa che, una volta acceso o spento un indicatore per un particolare compito, lo stato dell'indicatore (ON o OFF) deve essere immediatamente testato.
La visibilità di un indicatore è infatti locale rispetto all'istruzione seguente, non globale sull'intero programma.
In questo modo non bisogna preoccuparsi di modificare lo stato di indicatori utilizzati in altre parti del programma (ad esempio, se lo stato di un indicatore acceso all'inizio del programma viene testato alla fine, potrebbe succedere che qualcuno ne modifichi lo stato in qualche punto intermedio, provocando comportamenti errati nell'esecuzione), visto che la "validità" dell'indicatore si esaurisce localmente.

>* Esempio di valutazione locale dello stato di un indicatore (indicatore 50)
C     $KEY          LOOKUP    ARRAY                                  50
C                   IF        *IN50=*ON
C                   EXSR      FUNCTION
C                   ENDIF


E' da sottolineare che **gli indicatori rappresentano una tecnica di programmazione obsoleta_ :  al loro posto è preferibile infatti utilizzare operazioni quali _%EOF, %FOUND_, ecc. per controllare un particolare stato o una particolare condizione.
**L'utilizzo degli indicatori risulta tuttavia comodo nei file video.**

# Tasti funzionali
La tabella sottostante illustra gli utilizzi dei tasti funzione comunemente utilizzati : 


| F03 | Uscita |
| ---|----|
| F05 | Refresh |
| F06 | Conferma |
| F12 | Annullamento |
| F13 | Parzializzazioni |
| F17 | Impostazioni |
| F24 | Altri tasti funzione |
| 


Correlata all'utilizzo dei tasti funzionali è la /copy **£KEY**, che definisce delle costanti corrispondenti ai valori esadecimali di tasti funzione.
In questo modo è possibile utilizzare le costanti al posto dei valori esadecimali, con ovvi vantaggi in termine di manutenibilità e comprensibilità del codice.

# Tabella PGM
La tabella PGM consente di gestire le impostazioni relative alla modalità di esecuzione di un programma e all'attivazione dei log relativamente al programma stesso.

**Documentazione specifica**
- [PGM - Programma](Sorgenti/MB/DOC_OGG/TA_PGM)

# Programmi "FUNIZZATI"
Il concetto di programma "funizzato" si basa sulla constatazione che se un programma è dotato di una entry standard, allora è possibile eseguirne la chiamata indicandone il nome in modo parametrico in una tabella, senza che sia necessario includere nel sorgente il nome del programma come stringa fissa.

Una particolare categogia di programmi funizzati sono le "_2_Azioni". Questi sono programmi studiati per eseguire un'azione minima su un oggetto, ad esempio all'interno di un flusso collegato all'inserimento, alla modifica o alla cancellazione di un articolo, oppure la selezione delle righe di un ordine durante l'esecuzione di una entrata merci.

Le azioni sono catalogate per applicazione / contesto, per inserire una nuova azione nel catalogo bisogna scriverla in una schiera contenuta nel programma _1_xxFUN0, dove xx è l'applicazione.
Le azioni catalogate si possono interrogare in abiente grafico dalla scheda applicazione.

Per essere utilizzate dalle applicazioni le azioni devono essere inserite in un elemento della tabella B£J e devono essere richiamate dalla tabella B£H (riferirsi all'Help di queste tabelle).

**Esempio di Entry : **
 :  : PAR L(MON)
*--------------------------------------------------------------*   .
I/COPY QILEGEN,£FUNDS1                                              .
I/COPY QILEGEN,£TABB£1DS                                            .
I/COPY QILEGEN,£PDS                                                 .
*--------------------------------------------------------------*   .
D* M A I N                                                          .
*--------------------------------------------------------------*   .
C                   EVAL      £FUND1=§FUNW1                       .
C                   EVAL      £FUND2=§FUNW2                       .
C                   ...
*
C                   SETON                                        LR .
*--------------------------------------------------------------*   .
C/COPY QILEGEN,£INZSR                                               .
C/COPY QILEGEN,£FUN                                                 .
*--------------------------------------------------------------* .
D* ROUTINE INIZIALE                                               .
*--------------------------------------------------------------* .
C     £INIZI        BEGSR                                         .
*                                                                .
C     *ENTRY        PLIST                                         .
C                   PARM                    §FUNNP                .
C                   PARM                    §FUNFU                .
C                   PARM                    §FUNME                .
C                   PARM                    §FUNMS                .
C                   PARM                    §FUNFI                .
C                   PARM                    §FUNCM                .
C                   PARM                    §FUNW1                .
C                   PARM                    §FUNW2                .
*                                                                .
C     *LIKE         DEFINE    £FUNNP        §FUNNP                .
C     *LIKE         DEFINE    £FUNFU        §FUNFU                .
C     *LIKE         DEFINE    £FUNME        §FUNME                .
C     *LIKE         DEFINE    £FUNMS        §FUNMS                .
C     *LIKE         DEFINE    £FUNFI        §FUNFI                .
C     *LIKE         DEFINE    £FUNCM        §FUNCM                .
C     *LIKE         DEFINE    £FUNW1        §FUNW1                .
C     *LIKE         DEFINE    £FUNW2        §FUNW2                .
*                                                                  .
C                   ENDSR                                           .
*--------------------------------------------------------------*


Parametri : 

| __Parametro__ | __Lunghezza__ | __Descrizione__ |
| ---|----|----|
| £FUNP | 10   | Programma da chiamare |
| £FUNFU | 10   | Parametro 1 di B£J / FUNZIONE |
| £FUNME | 10   | Parametro 2 di B£J / METODO |
| £FUNMS | 07   | Codice messaggio d' errore |
| £FUNFI | 10   | File messaggi errori |
| £FUNCM | 2   | Ultimo tasto funzionale eseguito |
| £FUND1 | 512  | DS Fissa - Vedi di seguito |
| £FUND2 | 512  | DS Tipica del contesto |
| 


Mappatura £FUND1 (campi principali) : 

| __Campo__ | __Lunghezza__ | __Descrizione__ |
| ---|----|----|
| £FUNCO | 10  | Contesto (V5MOVI / GMCONF / E) |
| £FUNNR | 9.0 | Numero relativo di record |
| £FUNGR | 3  | Griglia (Tabella B£G) |
| £FUNT1 | 2  | Tipo Codice 1 (Oggetto 1) |
| £FUNP1 | 10  | Par. Codice 1 (Oggetto 1) |
| £FUNK1 | 15  | Codice 1 (Oggetto 1) |
| £FUNI1 | 15  | Intestaz. Codice 1 |
| £FUNS1 | 35  | Descriz. Codice 1 |
| £FUNT2 | 2  | Tipo Codice 2 (Oggetto 2) |
| £FUNP2 | 10  | Par. Codice 2 (Oggetto 2) |
| £FUNK2 | 15  | Codice 2 (Oggetto 2) |
| £FUNI2 | 15  | Intestaz. Codice 2 |
| £FUNS2 | 35  | Descriz. Codice 2 |
| £FUNT3 | 2  | Tipo Codice 3 (Oggetto 3) |
| £FUNP3 | 10  | Par. Codice 3 (Oggetto 3) |
| £FUNK3 | 15  | Codice 3 (Oggetto 3) |
| £FUNI3 | 15  | Intestaz. Codice 3 |
| £FUNS3 | 35  | Descriz. Codice 3 |
| £FUNPS | 40 | Parametri Specifici |
| 


Le DS £FUND1, £FUND2, £FUNW1 e £FUNW1 sono dichiarate nella /copy £FUNDS1. Le restanti variabili dell'entry sono definite invece nella /copy £FUN.

## Deviatore
Un deviatore viene utilizzato per "normalizzare" un programma non "funizzato". Si tratta di un programma "funizzato" che esegue una chiamata ad un altro programma, che sarà quindi visto dagli altri programmi tramite l'entry standard del deviatore (in modo analogo all'utilizzo di un adattatore per una spina di corrente).
