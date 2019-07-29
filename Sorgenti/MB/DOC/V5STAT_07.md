# Azioni sui dati - Generale

##  Estrazione dati
L'estrazione della statistica viene effettuata a partire da 2 file principali : 
 * C5TREG, è il file delle registrazioni contabili che viene scandito per tutte le estrazioni che riguardano il fatturato contabilizzato, ad eccezione del contabilizzato no registrazione.
 * V5TDOC, è il file dei documenti del ciclo esterno che viene scandito per tutte le altre estrazioni.

La ripresa da piano, utilizzata per esempio per includere nelle statistiche il Budget, si basa sul file MPPIAN.

##  Ripresa della statistica
La ripresa dei dati della statistica può essere gestita : 
 * Con lancio estemporaneo
 * Con lavoro schedulato
 * Con ripresa interattiva su singolo evento (attraverso la configurazione dei flussi su documenti e registrazioni contabili)

L'aggiornamento di un singolo documento o di una singola registrazione è altresì possibile attraverso la configurazione di un'azione di POP-UP.


## Esecuzione
Il lanciatore universale gestisce un parametro chiamato "Esecuzione". Attraverso la sua impostazione è possibile decidere se l'azione avrà effetto sui dati (scrittura/cancellazione/modifica) o se verrà prodotta solo una stampa.

Esecuzione "1" - Solo  Stampa
Esecuzione "3 "- Aggiornamento Dato (Verrà prodotto lo spool di stampa solo se impostata correttamente la tab. PGM)


## Tipi di ripresa (chiamate)

### Ciclo Attivo
 * _2_Ripresa Contabilizzato
 ** Scrittura                      TAB£AMO\V5STAT\ATT\GEK\WRI
 ** Cancellazione                  TAB£AMO\V5STAT\ATT\GEK\DEL
 * _2_Ripresa Contab.No Registrazioni 
 ** Scrittura                      TAB£AMO\V5STAT\ATT\GEC\WRI
 ** Cancellazione                  TAB£AMO\V5STAT\ATT\GEC\DEL
 * _2_Ripresa Atteso
 ** Scrittura                      TAB£AMO\V5STAT\ATT\GEA\WRI
 ** Cancellazione                  TAB£AMO\V5STAT\ATT\GEA\DEL
 * _2_Ripresa da Piano
 ** Scrittura                      TAB£AMO\V5STAT\ATT\GEP\WRI
 ** Cancellazione                  TAB£AMO\V5STAT\ATT\GEP\PUL
 * _2_Ripresa Ordinato (residuo)
 ** Scrittura                      TAB£AMO\V5STAT\ATT\GEO\WRI
 ** Cancellazione                  TAB£AMO\V5STAT\ATT\GEO\DEL
 * _2_Ripresa Ordinato (totale)
 ** Scrittura                      TAB£AMO\V5STAT\ATT\GOT\WRI
 ** Cancellazione                  TAB£AMO\V5STAT\ATT\GOT\DEL

### Ciclo Passivo
 * _2_Ripresa Contabilizzato
 ** Scrittura                      TAB£AMO\V5STAT\PAS\GEK\WRI
 ** Cancellazione                  TAB£AMO\V5STAT\PAS\GEK\DEL
 * _2_Ripresa Contab.No Registrazioni
 ** Scrittura                      TAB£AMO\V5STAT\PAS\GEC\WRI
 ** Cancellazione                  TAB£AMO\V5STAT\PAS\GEC\DEL
 * _2_Ripresa Atteso
 ** Scrittura                      TAB£AMO\V5STAT\PAS\GEA\WRI
 ** Cancellazione                  TAB£AMO\V5STAT\PAS\GEA\DEL
 * _2_Ripresa Ordinato
 ** Scrittura                      TAB£AMO\V5STAT\PAS\GEO\WRI
 ** Cancellazione                  TAB£AMO\V5STAT\PAS\GEO\DEL


### Criteri di selezione delle riprese, sia per attivo che per passivo : 
 * **GEK - Ripresa contabilizzato**; considera solo i documenti V5 contabilizzati e le eventuali registrazioni E4 senza documenti V5 collegati. Vengono esclusi documenti contabilizzati per i quali non esiste la registrazione contabile relativa.
 ** Scandisce il file C5TREG.
 * **GEC - Ripresa contabilizzato - No registrazione**; considera solo i documenti V5 contabilizzati per i quali non esiste la registrazione contabile relativa. In particolari situazioni, possono NON essere presenti le registrazioni E4 relative ai documento V5. Per esempio, in ambienti dove non viene utilizzata la contabilità SME-UP o in ambienti convertiti senza dati contabili relativi.
 ** Scandisce il file V5TDOC.
 * **GEA - Ripresa atteso**; considera solo i documenti in attesa di fatturazione o fatturati, ma non ancora contabilizzati.
 ** Scandisce il file V5TDOC.
 * **GEP - Ripresa d piano**; può essere utilizzata per riprendere i dati di Budget, i quali tipicamente vengono gestiti attraverso un piano MP.
 ** Scandisce il file MPPIAN.
 * **GEO - Ripresa ordinato residuo**; considera solo gli ordini clienti /fornitori attivi del modello scelto e solo per la quantità residua in essere.
 ** Scandisce il file V5TDOC.
 * **GOT - Ripresa ordinato totale**; considera tutti gli ordini clienti/fornitori del modello scelto nell'intervallo considerato, compreso quelli già saldati.
 ** Scandisce il file V5TDOC.

## Metodi di ripresa
Nel lancio della ripresa è necessario scegliere il metodo di ripresa che si vuole adottare : 
 * Metodo "A"  :  _2_RIPRESA GLOBALE; la ripresa effettua come primo passo la cancellazione di tutti i documenti presenti in statistica nell'intervallo di date scelto e la relativa ricreazione senza considerare alcun filtro specificato con F13.
 * Metodo "B"  :  _2_RIPRESA NORMALE; non viene fatta una cancellazione preliminare. Nell'intervallo scelto vengono aggiornati i record esistenti, scritti i nuovi record. Vengono considerati i filtri eventualmente impostati con F13.
 * Metodo  "C" :  _2_SOLO MANCANTI; vengono creati solo i documenti eventualmente non presenti in statistica, senza aggiornare gli esistenti.


## Log di ripresa
Per ottenere un log sulle azioni di ripresa, è possibile gestire la tabella PGM, attivando per i seguenti programmi la funzione di LOG (Campo LOG = "1") : 
* V5STA01 Il log fornisce un elenco dei documenti per i quali è stata lanciata la statistica.
* V5STA05 Il log fornisce l'esito dell'azione di creazione della statistica del singolo documento.

E' possibile scegliere anche il livello di dettaglio del log.

Sul campo "Condizioni Log" della tabella PGM sono gestiti i seguenti valori : 
 * **"1" o Non Specificato** :   traccio tutti gli eventi
 * **"2"** :  traccio solo i messaggi informativi e gli errori
 * **"9"** :  traccio solo gli errori.

Oltre allo spool di stampa, viene gestito il tracciamento anche attraverso il Trace&Play (£TAP). Il Trace&Play è richiamabile da LoocUp dalla Scheda Debug  nella sezione omonima (Ctrl+F9).

# Azioni sui dati - Dettaglio

## Ripresa Estemporanea
La ripresa estemporane può essere lanciata dall'utente : 
 * con il lanciatore B£AP00G da interfaccia 5250, sfruttando le azioni definite per il modulo V5STAT.
 * attraverso la scheda V5STAT di LOOC-UP.

Per ogni tipo di ripresa sarà necessario specificare i parametri definiti nello script.
Per esempio, nella ripresa del Fatturato Contabilizzato Attivo è necessario specificare : 

 - Data Protocollo Iniziale
 - Data Protocollo Finale
 - Metodo di Ripresa


Questa "Data Protocollo" viene usata anche nell'estrazione degli altri tipi di statistica, assumento ovviamente un significato diverso, quindi : 
- nel caso di ripresa contabilizzato ovviamente verrà usata per la  data protocollo
- nel caso delle fatture non contabilizzate questa data coinciderà con la data fattura
- nel caso delle bolle la data sarà usata per la data bolla
- infine per gli ordini questa coinciderà con la data ordine
(verranno messe quindi messo nel campo D6DPRO date con significati diversi a seconda della tipologia di statistica).


## Ripresa schedulata
La schedulazione delle riprese della statistica è possibile impostarla attraverso il richiamo del programma B£FUNC, passandogli gli opportuni parametri.

Un esempio di chiamata può essere il seguente
>.          Call B£FUNC
.          PARM('
.          PG(B£AP00G)    - Lanciatore Universale
.          FU(ESE)     - Funzione di esecuzione
.          ME(BLI)     - Metodo Cieco, senza interazione video
.          D2($IND(TAB£AMO\V5STAT\ATT\GEK\WRI)  - Tipo di statistica da lanciare
.          $FRM(3)      - Parametro di Esecuzione
.          $O01(20100101)    - Parametro 1 di lancio
.          $O02(20101231)    - Parametro 2 di lancio
.          $O03(A))     - Parametro 3 di lancio
.          ')


Per facilitare la scrittura del comando da schedulare, è consigliabile richiamare il pgm B£AP00G e simulare il richiamo della ripresa che si vuole schedulare.
Senza procedere al lancio, attraverso il comando F20 = Dati Tecnici, selezionare i dati di Output. In questo modo è possibile vedere i parametri di lancio del programma e utilizzarli nella schedulazione.
I parametri da sostituire sono : 

- $IND
- $O1, $O2, $O3 cioè gli oggetti che definiscono i parametri di lancio.


Se si vogliono schedulare diverse tipologie di ripresa (fatturato contabilizzato, atteso, ...), è necessario schedulare più lavori.

Al posto delle date fisse, è possibile utilizzare le date dinamiche, utili, per esempio, per schedulare lavori che riprendano sempre gli ultimi 3 mesi di fatturato. La data impostata negli oggetti $O.. sarà del tipo "&OGI0", secondo gli standard SME-UP (vedi £DA8).

## Ripresa interattiva da singolo evento
E' possibile configurare il gestionale, in modo che l'aggiornamento della statistica avvenga in tempo reale.
Questo è possibile agganciando ai flussi di inserimento/modifica/cancellazione dei documenti V5 e delle registrazioni contabili, un programma specifico.
Il programma che gestisce il lancio da flusso è il V5STA01S.

__Funzione__ -  Viene passata l'azione da eseguire : 
 * Funzione RIP :    ricrea la statistica
 * Funzione UTI.PUL :   cancella la statistica

__Metodo__  -  E' possibile impostare il tipo di statistica "forzata" da creare/aggiornare (AF, PF, ecc..) : 
Se non ricevuto il METODO, il pgm calcola il tipo di statistica in base all'oggetto in entrata.
 * Se oggetto E4, lancio la creazione della statistica AF o PF, in base al tipo IVA della testata della registrazione.
 * Se oggetto DO, in base al valore assunto dal flag 19, imposto il tipo di statistica.

__Oggetto__
Il pgm riceve in entrata l'oggetto da elaborare, che può essere una registrazione E4 o un documento DO.
Se richiamato da un flusso di azioni sui documenti V5 (Es. Flusso di creazione di una bolla) e quindi non sono valorizzati i parametri dell'oggetto 1 in entrata (£FUNT1, £FUNP1, £FUNK1), l'oggetto viene derivato dall'area dati £V5PDS, gestita dal programma.

## Ripresa interattiva da singolo evento - Configurazione consigliata sui flussi

### REGISTRAZIONI E4
Per integrare nel flusso di contabilizzazione la generazione della statistica, è necessario configurare delle azioni in fase di inserimento, modifica e cancellazione dell'oggetto E4
 * _2_Flusso di inserimento (Tab. B£H = Gruppi di Azioni)
 ** I - E4
 *** B£J-E4 Elemento XXXX Lancio   V5STA01S
 *** Funzione RIP
 * _2_Flusso di Modifica (Tab. B£H = Gruppi di Azioni)
 ** M - E4
 *** B£J-E4 Elemento XXXX Lancio   V5STA01S
 *** Funzione RIP
 * _2_Flusso di Cancellazione (Tab. B£H = Gruppi di Azioni)
 ** D - E4
 *** B£J-E4 Elemento XXXX Lancio   V5STA01S
 *** Funzione UTI.PUL

La cancellazione lancia il flusso di cancellazione della statistica, ma non la ricrea.  La creazione non è possibile lanciarla in cancellazione, poichè non avrebbe effetto sulla statistica :  in quel momento testata C5 e documento V5 sono ancora integri.
L'aggiornamento della statistica sarà eseguito dalla ricontabilizzazione o da una modifica sul documento V5.

### DOCUMENTI DO
E' necessario agganciare la creazione della statistica ai seguenti flussi : 

* Flussi B£H  T-DO  flusso di transazione che intercetta le modifiche dei documenti
* Flussi B£H  P-DO  flusso di transazione che intercetta la cancellazione dei documenti
* Flussi V5G CA/CP flussi di azione su ciclo attivo o passivo (Es. :  creazione bolla, creazione fattura, ...).

### FLUSSI T-DO
Il flusso di transazione viene lanciato a qualsiasi modifica del documento. Se ci sono flussi specifici per "Modello", il flusso deve essere agganciato anche a questi.
 * _2_Flusso di Transazione  (Tab. B£H = Gruppi di Azioni)
 ** T - DO
 *** B£J-XX Elemento XXXX Lancio   V5STA01S
 *** Funzione RIP
 ** T - DOxx
 *** B£J-XX Elemento XXXX Lancio   V5STA01S
 *** Funzione RIP

La stampa fattura con questa configurazione non lancerebbe la creazione della statistica. La statistica verrebbe ricreata con la successiva contabilizzazione :  per risolvere questo problema bisognerebbe intervenire sul programma di stampa fatture.

### FLUSSI P-DO
Al flusso di pre-cancellazione agganciamo l'eliminazione dalla statistica del documento.
 * _2_Flusso di Pre-Cancellazione  (Tab. B£H = Gruppi di Azioni)
 ** P - DO
 *** B£J-XX Elemento XXXX Lancio   V5STA01S
 *** Funzione UTI.PUL
 ** P - DOxx
 *** B£J-XX Elemento XXXX Lancio   V5STA01S
 *** Funzione UTI.PUL

### FLUSSI V5G
Anche su ogni flusso del ciclo attivo o passivo, è necessario agganciare l'aggiornamento della statistica. In fase di creazione di una bolla o di una fattura, infatti, il flusso di transazione viene lanciato prima dell'assegnazione del numero bolla/fattura.
Per questo motivo, è necessario aggiungere l'aggiornamento della statistica dopo la stampa bolla o fattura.
 * _2_CA-xxxxxx  (Tab. B£H = Gruppi di Azioni)
 ** B£J-xx Ele. xxxx  Lancio   V5STA01S
 ** Funzione RIP
 * _2_CP-xxxxxx  (Tab. B£H = Gruppi di Azioni)
 ** B£J-xx Ele. xxxx  Lancio   V5STA01S
 ** Funzione RIP

### POP UP su DOCUMENTI/REGISTRAZIONI
E' possibile agganciare anche alle azioni di POP-UP della registrazione E4 o del documento V5, l'aggiornamento della statistica. In questo modo si può richiamare facilmente a richiesta dell'utente l'aggiornamento immediato della statistica.
E' inoltre possibile agganciare una scheda Looc Up di interrogazione della singola registrazione o del singolo documento,  che permette di confrontare i valori della registrazione/documento con il contenuto della statistica.


### POP-UP di CREAZIONE STATISTICA
 * _2_A - E4  (Tab. B£H = Gruppi di Azioni)
 ** B£J - Ele. xxxx
 ** Set. B£J  - Sub. E4 Flussi di testata registraz.
 ** Ele. xxxx
 ** Descrizione          Creazione Statistica V5STAT                   Attr.Vis
 ** Nome programma       V5STA01S
 ** Param.01 (funzione)  RIP
 ** Param .02 (metodo)
 * _2_A - DO (Tab. B£H = Gruppi di Azioni)
 ** B£J -  Ele. xxxx
 ** Set. B£J  - Sub.DO Documenti V5
 ** Ele. xxxx
 ** Descrizione          Creazione Statistica V5STAT                   Attr.Vis
 ** Nome programma       V5STA01S
 ** Param.01 (funzione)  RIP
 ** Param.02 (metodo)

### POPUP di INTERROGAZIONE STATISTICA
 * _2_A - E4 (Tab. B£H = Gruppi di Azioni)
 ** B£J -  Ele. xxxx
 ** Set. B£J GRUPPI DI AZIONI               Sub. E4 Flussi di testata registraz.
 ** Ele. xxxx                                                           Archivio 0
 ** Descrizione          Dettaglio Statistica V5STAT                   Attr.Vis
 ** Attivazione          J    Solo Looc Up
 ** Nome programma      JATRE_18C
 ** Param.01 (funzione)  EXD
 ** Param .02 (metodo)
 ** Parametri aggiuntivi 2(MB;SCP_SCH;V5STATC_E4)
 * _2_A - DO (Tab. B£H = Gruppi di Azioni)
 ** B£J -  Ele.xxxx
 ** Set. B£J GRUPPI DI AZIONI               Sub. E4 Flussi di testata registraz.
 ** Ele. xxxx                                                           Archivio 0
 ** Descrizione          Dettaglio Statistica V5STAT                   Attr.Vis
 ** Attivazione          J    Solo Looc Up
 ** Nome programma      JATRE_18C
 ** Param.01 (funzione)  EXD
 ** Param .02 (metodo)
 ** Parametri aggiuntivi 2(MB;SCP_SCH;V5STATC_DO)
