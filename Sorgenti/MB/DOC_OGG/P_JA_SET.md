# OBIETTIVO
Questo servizio fornisce le funzionalità per la gestione dei setup dei componenti grafici.

 :  : PAR T(La gestione include le funzioni per : ) L(NUM)
- elencare i setup
- impostare un setup come default
- modificarlo
- crearne uno nuovo
- salvarlo
- rinominarlo
- eliminarlo
- leggerlo


## Cosa è un setup
Un setup è un XML che contiene le impostazioni di un modulo o di una parte di esso (ad esempio una sottoscheda).
Può essere ricavato dalle risposte che un utente ha fornito ad un questionario oppure può essere generato da un modulo grafico e avere pertanto un formato specifico e/o proprietario.

## Formato dell'XML del setup
Questo XML può avere un formato totalmente libero o può avere un formato di tipo sezione, cioè le risposte sono inserite in un XML che le divide per sezione (per maggiori dettagli vedi la documentazione del configuratore).
 :  : PAR T(Formato Libero)
Se il formato dell'XML è libero vorrà dire che la modifica o la creazione di uno nuovo non sarà possibile dal gestore dei setup ma solo dal modulo che usa il setup. In questo caso il gestore dei setup fornisce solo le funzioni di lista, salvataggio, ridenominazione, cancellazione e lettura.


## I questionari che definiscono i setup.
I setup di configurazione sono oggetti RE L- e sono degli script che definiscono le domande.
Sono membri del file SCP_CFG.
Un componenete di LoocUp avrà come questionario associato il membro "GRA_" + codice del modulo es :  il questionario del componente albero sarà GRA_TRE, mentre quello del G30 sarà GRA_G30.

## Come un modulo grafico può usare questo servizio
### Uso di un questionario standard
Chi sviluppa un componente e desidera rendere parametrizzabili delle proprietà deve definire un membro nel file SCP_CFG con il nome che rispetta lo standard definito sopra.
Le domande che dovrà inserire saranno le caratteristiche che desidera rendere personalizzabili dall'utente. Nell'XML che verrà salvato su AS400 troverà le risposte :  riporto qui un frammento della struttura dell'XML del setup : 

- tag sec code="sezione1"
- tag dom code="domanda1"
- tag ris code="risposta1" fine tag ris
- fine tag dom
-
- ripetizione di n tag dom
-
- fine tag sec
-
- ripetizione di tag sezione

Se il modulo ha una configurazione di default lo sviluppatore del modulo dovrà salvare una setup che ha come chiavi **-**-**, in questo modo esisterà un setup di default. L'utente potrà poi decidere di personalizzare le impostazioni di base creando i propri setup.
Lo sviluppatore, al momento del caricamento del modulo dovrà prevedere la chimata al servizio JA_SET con funzione.metodo "ACT.GET", che restituirà l'XML del setup e a questo punto potrà utilizzare le informazioni presenti.

### Uso senza questionario
Viene saltata la prima parte descritta sopra, ovvero la definizione del questionario, e cambia anche il modo di usare l'XML in quanto è il modulo stesso che si occupa di interpretare l'XML ricevuto.

## Identificazione di un setup
Un setup è normalmente associato a un questionario.
Setup di questionari differenti sono incompatibili (un questionario definisce le domande). I setup pertanto saranno raggruppati per questionario.

Dato un questionario i suoi setup sono identificati da 3 chiavi : 

- il contesto
- l'utente
- il nome

Se il setup è di tipo libero (non ho associato un questionario) avrò che l'oggetto questionario servirà a raggruppare setup omogenei.

Dato che il questionario raggruppa setup omogenei avrò che l'utente vede 3 chiavi (contesto, utente e nome ) ma può agire solo sull'ultima. Solo chi è autorizzato può modificare i setup di default e/o quelli di altri utenti. Il questionario è definito dal modulo di cui si sta definendo il setup.

## Setup di default
Il setup di default ha come nome (chiave 3) il valore "**".
Impostare come default un setup significa pertanto salvarlo con nome "**".
Il setup di default è quello letto (se esiste) quando viene caricato un modulo.
Quando un modulo richiede il setup di default fornisce come chiavi : 

- il codice del questionario
- il contesto
- l'utente

Il setup viene cercato dal servizio CFSER_02 usando un meccanismo di risalita mantenendo fissato il questionario.
 T(Sequenza ricerca Setup)
- contesto-utente-**
- contesto-**-**
- **-**-**


La lista di setup per un determinato modulo è composta dai setup specifici per l'utente e da quelli generici (identificati da **) : 

- contesto ** utente ** nome **  - setup valido per tutti i contesti e per tutti gli utenti
- contesto xxxxx utente ** nome ** - setup valido per il contesto xxxxx e per tutti gli utenti
- contesto xxxxx utente yy nome ** - setup di default per il contesto xxxxx e per l'utente yy
- contesto xxxxx utente yy nome setup_A - setup alternativo per il contesto xxxxx e per l'utente yy
- contesto xxxxx utente yy nome setup_B - setup alternativo per il contesto xxxxx e per l'utente yy
- contesto xxxxx utente yy nome setup_C - setup alternativo per il contesto xxxxx e per l'utente yy

 T(Si capisce che dato un questionario si possono definire almeno 3 setup di default : )
- Il setup di default con il contesto xxx per l'utente yyy
- Il setup di default con il contesto xxx per tutti gli utenti
- Il setup di default per tutti i contesti e per tutti gli utenti.

Ad esempio posso salvare un default per tutti gli alberi (componente TRE, pertanto questionario associato RE L- GRA_TRE) e che vale per tutti i contesti e per tutti gli utenti.
L'utente yyy che lavorerà sugli alberi (questionario REL-GRA_TRE) dei menu (contesto *MNU) potrà personalizzare il setup di default generico e crearne uno apposito per sè.

 T(Il setup di default che andrà a salvare avrà come chiavi : )
- contesto :  *MNU
- utente :    yyy
- nome :  **



## Il setup nel gestionale
Un setup è un oggetto SmeUp di tipo CF e parametro L-xxxxxx, dove xxxxx è il codice del questionario.
Il codice del setup è un progressivo alfanumerico automatico che viene assegnato al momento del salvataggio.
Un oggetto setup consente di memorizzare un XML di dimensione massima di 30.000 caratteri.

## Informazioni tecniche
Quando viene salvato un setup su AS400 viene creato un record nel file B£MEDE0F.
I campi più significativi per la gestione dei setup del file B£MEDE0F sono : 

- MEIDOJ :  è il codice dell'oggetto setup. E' un progressivo automatico di 10 caratteri alfanumerici che viene creato dal programma AS400 che si occupa del salvataggio
- METIPA :  campo di 12 caratteri che contiene il Tipo e Parametro del questionario.
- MECODI :  campo di 15 caratteri che contiene il Codice del questionario.
- METIPO :  non usato
- MECOD1 :  campo di 15 caratteri che costituisce la Chiave 1 del setup (Contesto).
- MECOD2 :  campo di 15 caratteri che costituisce la Chiave 2 del setup (Utente).
- MECOD3 :  campo di 15 caratteri che costituisce la Chiave 1 del setup (Nome).


Il codice dell'oggetto CF L-xxxxxxx è l'IDOJ (l'IDOJ è un identificativo univoco) del record presente nel B£MEDE0F.
La dimensione massima è di 30.000 caratteri.

## Accesso al setup.
Al setup si può accedere sia con l'IDOJ (campo MEIDOJ) sia specificando quattro valori :  l'oggetto questionario unito alle tre chiavi di setup (contesto, utente e nome)
 :  : PAR T(Struttura chiavi B£MEDE0F) L(PUN)
- MEIDOJ :  è l'IDOJ del setup :  è la chiave univoca del record.
- METIPA :  Tipo e Parametro del questionario.
- MECODI :  Codice del questionario.
- METIPO :  non usato
- MECOD1 :  Chiave 1 setup (Contesto).
- MECOD2 :  Chiave 2 setup (Utente).
- MECOD3 :  Chiave 3 setup (Nome).



# Set'n'play : 
Da LOOC.up :  menu principale, servizi, funzione libera.
Impostare
Tipo Funzione :  FUN
Componente :     INT
Servizio :       JA_SET


La Entry degli oggetti è comune per tutte le funzioni : 
T/P/K1 :  Questionario di loocup (es RE L- GRA_G30)
T/P/K2 :  Chiave 1  contesto  - può essere costituito dal campo Funzione.metodo
T/P/K3 :  Chiave 2  utente
T/P/K4 :  Chiave 3  il nome della configurazione

# FUNZIONI/METODI
## Azioni dirette o singole (ACT)

- ACT.SAV salva la configurazione con il nome corrente (SAVe)
- ACT.SAS salva con nome differente la configurazione (Save AS)
- ACT.DEL elimina la configurazione (DELete)
- ACT.DEF imposta la configurazione come default (DEFault)
- ACT.NEW creo una nuova configurazione
- ACT.EDT modifico la configurazione specificata dalle chiavi passate
- ACT.LIS mostro la lista delle configurazioni (LISt)
- ACT.GET Leggo il setup selezionato da AS400 e lo restituisco come XML senza eseguire il lock
- ACT.GTW Leggo il setup selezionato da AS400 e lo restituisco come XML senza eseguire il lock. L'XML del setup letto viene visualizzandolo con il programma predefinito.
- ACT.GES apro la finestra di gestione setup in modalità gestione (con tutti i pulsanti attivi)

Per i metodi in cui il campo Parametro è definito si può specificare se andare in gestione dopo l'azione se mostrare le informazioni di debug del modulo.

## GES mostro la finestra di gestione dei setup
Se questo parametro è blank significa che tutti i pulsanti sono attivi
E' anche possibile la gestione dei singoli pulsanti.
Viene utilizzato il parametro secondo una logica posizionale.
Ad ogni posizione corrisponde un pulsante o un'azione e si può abilitare o disabilitare.
Per i dettagli vedi la sezione dei parametri.
### Nota
I pulsanti Salva, Salva con nome e Elimina, sono abilitati dal setup letto da AS400 :  se ad esempio un setup è vincolato allora sarà possibile solo salvarlo con un nome diverso.
Se il setup letto è nullo o non è stato passato, allora varranno i vincoli di lock definiti nel parametro.

 :  : I.RUL   Descrizione                                  Para Comp Tipi Au
*ALL      Tutti
ACT       Azioni per eseguire il test                            TP10
.SAV       salva il setup                              PA20      TP10
.SAS       rinomina il setup                           PA20      TP10
.DEL       elimina il setup                            PA20      TP10
.DEF       imposta come default                        PA20      TP10
.NEW       creo nuovo setup                                      TP10
.EDT       modifica setup                                        TP10
.LIS       lista setup                                 PA20      TP10
.GET       leggi setup                                 PA30      TP10
.GTW       leggi XML setup                                       TP10
.LGT       lista setup e restituisci scelto            PA30      TP10
.DBG       gestione modalità debug                               TP10
GES        gestione
.                                                      PA10      TP10
.GES                                                   PA10      TP10
.TST                                                   PA50      TP10
 :  : RPA                              TpParametro         Lung.DOVAuD
PA10 Disabilita Salva              V2SI/NO             00001
PA10 Disabilita Salva come         V2SI/NO             00001
PA10 Disabilita Elimina            V2SI/NO             00001
PA10 Disabilita Nuova              V2SI/NO             00001
PA10 Disabilita Modifica           V2SI/NO             00001
PA10 Disabilita Applica            V2SI/NO             00001
PA10 Apri Contesto                 V2SI/NO             00001
PA10 Apri Utente                   V2SI/NO             00001
PA10 Disabilita Ricerca            V2SI/NO             00001
PA20 Vai in gestione dopo l'azione V2SI/NO             00001
PA20 Mostra finestra debug         V2SI/NO             00001
PA30 Vedi Xml con gestore predef.  V2SI/NO             00001
PA40 Mostra finestra debug         V2SI/NO             000010
PA50 Mostra finestra debug         .VAAAAA             000010
 :  : LIS
AAAAA
A AAAAAAAA
B BBBBBBBB
C CCCCCCCC
 :  : RCO          2         3         4         5         6         7
CO10 G30
 :  : ROG      TpPa1       TpPa2       TpPa3       TpPa4       TpPa5       Descrizione
TP10 1 OOO REL-        **                                              Questionario
TP10 2 OFF **                                                          Contesto
TP10 3 OOF UP                                                          Utente
TP10 4 OFF **                                                          Nome setup
 :  : I.RUL.END
