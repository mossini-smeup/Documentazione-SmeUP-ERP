# Obiettivo
Eseguire le azioni di movimentazione colli

# Funzioni
 * >INZ, Inizializzazione.
 * >CTR, Controllo.
 * >WRI, Scrittura.

_2_Inizializzazione
L'inizializzazione carica la DS delle impostazioni dall'elemento della tabella "GNK" relativo all'azione che si vuole eseguire.

_2_Controllo
I controlli sono specifici per ogni tipo azione. Verificano la validità dei dati di input.
Se hanno avuto tutti esito positivo vengono passati ai dati di output e si può procedere alla scrittura.

_2_Scrittura
La scrittura è specifica per ogni tipo azione. Ogni tipo azione esegue delle proprie funzioni con i dati di output ricevuti dal controllo. Prima di eseguirla è necesario eseguire le due funzioni precedenti di inzializzazione e controllo. La scrittura viene eseguita solo se sono stati ricevuti tutti i suoi campi minimi necessari per il tipo di azione.

# Azioni

_2_Sono stati definiti i seguenti tipi di azione : 

 * >01 = Creazione nuovo collo :  crea un nuovo collo del tipo passato
 * >02 = Creazione alias :  dato un contesto passato, crea un alias per un collo esistente
 * >03 = Creazione nuovo collo e relativo alias (se ricevuto) :  combina le azioni 01 e 02
 * >09 = Annullamento collo :  annulla un collo esistente

 * >11 = Ritorno alias collo :  dato un collo esistente, ritorna il suo alias
 * >12 = Ritorno collo da alias :  dato un alias esistente, ritorna il suo collo
 * >13 = Ritorno giacenza collo :  dato un collo esistente ritorna la giacenza relativa

 * >21 = Riempimento nuovo collo :  crea un nuovo collo e lo carica una giacenza
 * >22 = Riempimento collo esistente :  carica una giacenza per un collo esistente
 * >23 = Trasferimento collo :  trasferisce la giacenza di un collo
 * >24 = Svuotamento collo :  scarica la giacenza di un collo

 * >31 = Trasferimento collo a nuovo collo (Divisione) :  crea un nuovo collo e trasferisce la qtà dal collo origine
 * >32 = Trasferimento collo a collo esistente (Accorpamento) :   trasferisce la qtà dal collo origine ad un altro collo esistente

 * >41 = Stampa collo :  stampa etichetta collo

 * >51 = Inventario collo con liste di conta - conta :  inserisce qtà effettiva su riga GMDAIN a stato 10
 * >52 = Inventario collo con liste di conta - riconta :  modifica qtà effettiva su riga GMDAIN a stato 30
 * >53 = Inventario collo con liste di conta - nuova conta :  inserisce un nuova riga GMDAIN con qtà effettiva e mette qtà = 0 su riga GMDAIN precedente a stato 10
 * >54 = Inventario collo con liste di conta - annulla conta :  azzera qtà effettiva e ripristina stato = 10
 * >55 = Inventario collo con liste di conta - ritorno dati lista - Da contare :  ritorna i dati del GMDAIN in stato 10
 * >56 = Inventario collo con liste di conta - ritorno dati lista - Contato :  ritorna i dati del GMDAIN in stato 30

 * >61 = Inventario collo con cartellini - conta :  inserisce nuova riga GMRIIN in stato 30
 * >64 = Inventario collo con cartellini - annulla conta :  cancella riga GMRIIN in stato 30
 * >66 = Inventario collo con cartellini - ritorno dati cartellino - Contato :  ritorna i dati del GMRIIN in stato 30

## 01. Creazione collo
La funzione di "Creazione collo" genera un nuovo collo. Se l'azione è definta a scarto il collo sarà un collo di scarti (flag 6 = 1). Se in input viene attribuito il collo destinazione sarà il codice del nuovo collo, altrimenti il codice sarà determinato dal numeratore colli.
### Tabella "GNK"
 * Tipo azione :  "01"
 * Azione su scarti (Facoltativa)
### Input
 * Collo destinazione (Facoltativo)
 * Magazzino destinazione (Obbligatorio se multiplant)
 * Articolo destinazione (Obbligatorio)
 * Tipo collo (Obbligatorio)
 * Unità di movimentazione (Facoltativa)
 * Quantità (Facoltativa)
 * Tipo stampa (Facoltativo)
### Controlli
 * Il collo destinazione NON deve già esistere.
### Scrittura
 * Generazione nuovo collo
 * Se presente tipo stampa :  Esegue stampa collo.

## 02. Creazione alias
La funzione di "Creazione alias" genera un alias per il collo.
### Tabella "GNK"
 * Tipo azione :  "02"
 * Contesto Alias (Obbligatorio)
### Input
 * Collo destinazione (Obbligatorio)
 * Alias (Obbligatorio)
 * Tipo stampa (Facoltativo)
### Controlli
 * L'azione definita in tabelle "GNK" deve contenere il contesto dell'alias.
 * L'alias sul collo destinazione NON deve già esistere.
### Scrittura
 * Generazione alias del collo
 * Se presente tipo stampa :  Esegue stampa collo.

## 03. Creazione collo e relativo alias
La funzione di "Creazione collo e relativo alias" esegue la funzione di "Creazione collo" e, se ricevuto l'alias, la funzione di "Creazione alias".
### Tabella "GNK"
 * Tipo azione :  "03"
 * Azione su scarti (Facoltativa)
 * Contesto Alias (Obbligatorio)
### Input
 * Collo destinazione (Facoltativo)
 * Magazzino destinazione (Obbligatorio se multiplant)
 * Articolo destinazione (Obbligatorio)
 * Tipo collo (Obbligatorio)
 * Unità di movimentazione (Facoltativa)
 * Quantità (Facoltativa)
 * Alias (Facoltativo)
 * Tipo stampa (Facoltativo)
### Controlli
 * Il collo destinazione NON deve già esistere.
 * Se richiesto alias :  l'azione definita in tabelle "GNK" deve contenere il contesto dell'alias.
### Scrittura
 * Generazione nuovo collo
 * Se richiesto alias :  Generazione alias.
 * Se presente tipo stampa :  Esegue stampa collo.

## 09. Annullamento collo
La funzione di "Annullamento collo" esegue l'annullamento logico del collo.
### Tabella "GNK"
 * Tipo azione :  "09"
### Input
 * Collo destinazione (Obbligatorio)
### Controlli
 * Il collo non deve essere stato movimentato.
### Scrittura
 * Esegue l'aggiornamento del collo portando il livello a "9" e lo stato a "90".

## 11. Ritorno alias da collo
La funzione di "Ritorno alias da collo" dato un collo restituisce il suo alias.
### Tabella "GNK"
 * Tipo azione :  "11"
 * Contesto Alias (Obbligatorio)
### Input
 * Collo origine (Obbligatorio)
### Controlli
 * L'azione definita in tabelle "GNK" deve contenere il contesto dell'alias.
### Scrittura
 * Ritorna nel campo alias output l'alias del collo

## 12. Ritorno collo da alias
La funzione di "Ritorno collo da alias" dato un alias restituisce il suo collo.
### Tabella "GNK"
 * Tipo azione :  "12"
 * Contesto Alias (Obbligatorio)
### Input
 * Alias (Obbligatorio)
### Controlli
 * L'azione definita in tabelle "GNK" deve contenere il contesto dell'alias.
### Scrittura
 * Ritorna nel campo collo output origine il collo dell'alias.

## 13. Ritorno giacenza collo
La funzione di "Ritorno giacenza collo" dato un collo restituisce la sua giacenza.
### Tabella "GNK"
 * Tipo azione :  "13"
### Input
 * Collo origine (Obbligatorio)
### Controlli
 * Non sono ammesse giacenza multiple su un collo.
### Scrittura
 * Ritorna : 
 ** nei campi area a tipo giacenza impostazioni origine, l'area e il tipo giacenza in giacenza.
 ** nei campi output origine, i campi di dettaglio della giacenza
 ** nel campo output quantità, la quantità in giacenza

## 21. Riempimento nuovo collo
La funzione di "Riempimento nuovo collo" esegue la funzione di "Creazione nuovo collo e relativo alias" e la funzione di "Riempimento collo esistente".
### Tabella "GNK"
 * Tipo azione :  "21"
 * Causale origine (Facoltativa)
 * Causale destinazione (Obbligatoria)
 * Azione su scarti (Facoltativa)
 * Contesto Alias (Facoltativo)

## 22. Riempimento collo esistente
La funzione di "Riempimento collo esistente" esegue il movimento trasferimento quantità sul collo destinazione. A richiesta da una giacenza origine.
### Tabella "GNK"
 * Tipo azione :  "22"
 * Causale origine (Facoltativa)
 * Causale destinazione (Obbligatoria)
 * Azione su scarti (Facoltativa)
 * Contesto Alias (Facoltativo)
### Input
 * Magazzino origine (Obbligatorio, se presente causale origine)
 * Articolo origine (Obbligatorio, se presente causale origine)
 * Codici dettaglio giacenza origine (Obbligatori, se presente causale origine)
 * Collo destinazione (Obbligatorio)
 * Magazzino destinazione (Obbligatorio)
 * Articolo destinazione (Obbligatorio)
 * Codici dettaglio giacenza destinazione (Obbligatori)
 * Quantità (Obbligatoria)
 * Data registrazione (Facoltativa)
 * Tipo stampa (Facoltativo)
### Controlli
 * Se richiesto movimento origine :  Il tipo giacenza origine NON deve essere per collo (altrimenti usare il trasferimento).
 * Il tipo giacenza destinazione deve essere per collo.
 * Se presente giacenza destinazione tutti i dati di input di destinazione devono corrispondere ai dati presenti in giacenza. Nel caso in cui si volesse reperirli direttamente da giacenza, qualora esistesse, esegue prima la funzione "13" di "Ripresa giacenza Collo".
### Scrittura
 * Se presente causale origine :  Movimento con causale origine
 * Movimento con causale destinazione

## 23. Trasferimento collo
La funzione di "Trasferimento collo" esegue i movimenti di trasferimento della giacenza del collo origine ai campi destinazione. Il trasferimento viene eseguito per l'intera giacenza del collo.
### Tabella "GNK"
 * Tipo azione :  "23"
 * Causale origine (Obbligatoria)
 * Causale destinazione (Obbligatoria)
 * Azione su scarti (Facoltativa)
### Input
 * Collo origine (Obbligatorio)
 * Magazzino destinazione (Obbligatorio)
 * Articolo destinazione (Obbligatorio)
 * Codici dettaglio giacenza destinazione (Obbligatori)
 * Data registrazione (Facoltativa)
 * Tipo stampa (Facoltativo)
### Controlli
 * Il tipo giacenza origine deve essere per collo.
 * Deve esistere la giacenza del collo origine. Dalla sua giacenza deriva il magazzino origine, l'articolo origine, il codici di dettaglio giacenza origine, la quantità da trasferire.
 * L'area e il tipo giacenza in giacenza devono corrispondere e quelli della causale origine .
 * Il tipo giacenza destinazione deve essere per collo.
### Scrittura
 * Movimento con causale origine
 * Movimento con causale destinazione

## 24. Svuotamento collo
La funzione di "Svuotamento collo" esegue il movimento di scarico del collo dalla giacenza origine.
E se richiesto il carico in una giacenza destinazione (non per collo).
Lo svuotamento può essere : 
* parziale :  se viene indicata una quantità;
* totale :  se NON viene indicata una quantità (assume l'intera quantità in giacenza).
### Tabella "GNK"
 * Tipo azione :  "24"
 * Causale origine (Obbligatoria)
 * Causale destinazione (Facoltativa)
 * Azione su scarti (Facoltativa)
### Input
 * Collo origine (Obbligatorio)
 * Collo destinazione (Obbligatorio, se presente causale origine)
 * Magazzino destinazione (Obbligatorio, se presente causale origine)
 * Articolo destinazione (Obbligatorio, se presente causale origine)
 * Codici dettaglio giacenza destin. (Obbligatori, se presente causale origine)
 * Quantità (Facoltativa)
 * Data registrazione (Facoltativa)
 * Tipo stampa (Facoltativo)
### Controlli
 * Il tipo giacenza origine deve essere per collo.
 * Deve esistere la giacenza del collo origine. Dalla sua giacenza deriva il magazzino origine, l'articolo origine, il codici di dettaglio giacenza origine, e se non indicata la quantità da trasferire.
 * L'area e il tipo giacenza in giacenza devono corrispondere e quelli delle causale origine.
 * La quantità in giacenza deve essere maggiore o uguale alla quantità richiesta.
 * Il tipo giacenza destinazione NON deve essere per collo
### Scrittura
 * Movimento con causale origine
 * Se presente causale destinazione :  Movimento scon causale destinazione.

## 31. Trasferimento collo a nuovo collo (Divisione)
La funzione di "Traferimento collo a nuovo collo" esegue la funzione di "Creazione nuovo collo e relativo alias" e  i movimenti di trasferimento della giacenza del collo origine sul collo destinazione.
### Tabella "GNK"
 * Tipo azione :  "31"
 * Causale origine (Obbligatoria)
 * Causale destinazione (Obbligatoria)
 * Azione su scarti (Facoltativa)
 * Tipo stampa (Facoltativa)
### Input
 * Collo origine (Obbligatorio)
 * Collo destinazione (Facoltativo)
 * Tipo collo (Obbligatorio)
 * Unità di movimentazione (Facoltativa)
 * Quantità (Obbligatoria)
 * Data registrazione (Facoltativa)
 * Tipo stampa (Facoltativo)
### Controlli
 * Il tipo giacenza origine deve essere per collo.
 * Deve esistere la giacenza del collo origine. Dalla sua giacenza deriva il magazzino origine, l'articolo origine, il codici di dettaglio giacenza origine.
 * L'area e il tipo giacenza in giacenza devono corrispondere e quelli delle causale origine.
 * La quantità in giacenza deve essere maggiore o uguale alla quantità richiesta.
 * Il tipo gicenza destinazione deve essere per collo.
 * Controlli di "Creazione collo con relativo alias".
### Scrittura
 * Generazione nuovo collo
 * Se richiesto alias :  Generazione alias.
 * Movimento con causale origine
 * Movimento con causale destinazione
 * Se presente tipo stampa :  Esegue stampa collo.

## 32. Trasferimento collo a collo esistente (Accorpamento)
La funzione di "Accorpamento collo" esegue i movimenti di trasferimento della giacenza del collo origine sul collo destinazione.
### Tabella "GNK"
 * Tipo azione :  "32"
 * Causale origine (Obbligatoria)
 * Causale destinazione (Obbligatoria)
 * Azione su scarti (Facoltativa)
 * Tipo stampa (Facoltativa)
### Input
 * Collo origine (Obbligatorio)
 * Collo destinazione (Facoltativo)
 * Magazzino destinazione (Obbligatorio)
 * Articolo destinazione (Obbligatorio)
 * Codici dettaglio giacenza destinazione (Obbligatori)
 * Quantità (Facoltativa)
 * Data registrazione (Facoltativa)
 * Tipo stampa (Facoltativo)
### Controlli
 * Il tipo giacenza origine deve essere per collo.
 * Deve esistere la giacenza del collo origine. Dalla sua giacenza deriva il magazzino origine, l'articolo origine, il codici di dettaglio giacenza origine, e, se non indicata, la quantità da trasferire.
 * L'area e il tipo giacenza in giacenza devono corrispondere e quelli delle causale origine.
 * La quantità in giacenza deve essere maggiore o uguale alla quantità richiesta.
 * Il tipo giacenza destinazione deve essere per collo.
 * Il collo origine e il collo destinazione devono essere diversi.
 * Se esiste la giacenza del collo destinazione, i codici richiesti devono corripondenre a quelli in giacenza. Nel caso in cui si volesse reperirli direttamente da giacenza, qualora esistesse, esegue prima la funzione "13" di "Ripresa giacenza Collo".
### Scrittura
 * Movimento con causale origine
 * Movimento con causale destinazione
 * Se presente tipo stampa :  Esegue stampa collo.

## 41. Stampa collo
La funzione di "Stampa collo" esegue la stampa del collo.
### Tabella "GNK"
 * Tipo azione :  "41"
### Input
 * Collo destinazione (Obbligatorio)
 * Tipo stampa (Obligatorio)
### Controlli
### Scrittura
Esegue la stampa

## 51. Inventario collo con liste di Conte - conta
La funzione di "Inventario collo con liste di conta - conta" ricerca il collo nelle liste di conta del condice inventario richiesto e, se trovata riga in stato 10, inserisce la quantità effettiva e porta lo stato a 30.
### Tabella "GNK"
 * Tipo azione :  "51"
### Input
 * Collo
 * Inventario
 * Quantità contata
### Controlli
 * La riga deve esistere in GMDAIN e lo stato deve essere 10
### Scrittura
 * Nella riga trovata inserisce la quantità effettiva e porta lo stato a 30

## 52. Inventario collo con liste di Conte - riconta
La funzione di "Inventario collo con liste di conta - riconta" ricerca il collo nelle liste di conta del condice inventario richiesto e, se trovata riga in stato 30, aggiorna la quantità effettiva.
### Tabella "GNK"
 * Tipo azione :  "52"
### Input
 * Collo
 * Inventario
 * Quantità contata
### Controlli
 * La riga deve esistere in GMDAIN e lo stato deve essere 10
### Scrittura
 * Nella riga trovata modifica la quantità effettiva e porta lo stato a 30

## 53. Inventario collo con liste di Conte - nuova conta
La funzione di "Inventario collo con liste di conta - nuova conta" ricerca il collo nelle liste di conta del condice inventario richiesto e, se trovata riga in stato 10, aggiorna lo stato a 30, inoltre scrive una nuova riga a stato 30 con le nuove chiavi giacenza e la quantità effettiva.
### Tabella "GNK"
### Tabella "GNK"
 * Tipo azione :  "53"
### Input
 * Collo
 * Inventario
 * Quantità contata
 * Area
 * Tipo giacenza
 * Chiavi giacenza
### Controlli
 * La riga deve esistere in GMDAIN e lo stato deve essere 10
### Scrittura
 * Nella riga origine trovata porta lo stato a 30
 * Inserisce una nuova riga con area, tipo giacenza, chiavi giacenza da input quantità effettiva e stato 30

## 54. Inventario collo con liste di Conte - annulla conta
La funzione di "Inventario collo con liste di conta - annulla conta" ricerca il collo nelle liste di conta del condice inventario richiesto e, se trovata una o due righe in stato 30, sulle righe trovate azzera la quantità effettiva e aggiorna lo stato a 10, se in una riga abbiamo sia la qtà prevista che quella effettiva a zero la riga viene cancellata.
### Tabella "GNK"
 * Tipo azione :  "54"
### Input
 * Collo
 * Inventario
### Controlli
 * La riga deve esistere in GMDAIN e lo stato deve essere 30

### Scrittura
 * Su tutte le righe trovate (massimo 2) azzera qtà effettiva e ripristina stato = 10
 * Se una delle 2 righe ha sia la qtà prevista e quella effettia = zero la cancella

## 55. Inventario collo con liste di Conte - Ritorna dati DaContare
La funzione di "Inventario collo con liste di conta - Ritorna dati da contare" ricerca il collo nelle liste di conta del condice inventario richiesto e, se trovata riga in stato 10, restituisce i dati trovati nei campi origine.
### Tabella "GNK"
 * Tipo azione :  "55"
### Input
 * Collo origine
 * Inventario
### Controlli
 * La riga deve esistere in GMDAIN e lo stato deve essere 10
### Scrittura
 * Ritorna le Key di giacenza e la quantità trovate nei codici origine

## 56. Inventario collo con liste di Conte - Ritorna dati Contato
La funzione di "Inventario collo con liste di conta - Ritorna dati contato" ricerca il collo nelle liste di conta del condice inventario richiesto e, se trovata riga in stato 30, restituisce i dati trovati nei campi origine.
### Tabella "GNK"
 * Tipo azione :  "56"
### Input
 * Collo origine
 * Inventario
### Controlli
 * La riga deve esistere in GMDAIN e lo stato deve essere 30
### Scrittura
 * Ritorna le Key di giacenza e la quantità trovate nei codici origine

## 61. Inventario collo con cartellini - conta
La funzione di "Inventario collo con cartellini - conta" carica il collo nei cartellini di conta, non sono ammessi più cartellini con lo stesso collo.
### Tabella "GNK"
 * Tipo azione :  "53"
### Input
 * Inventario
 * Lotto di conta
 * Numero di conta
 * Collo
 * Area
 ^ Tipo giacenza
 * Articolo
 * Chiavi giacenza
 * Quantità effettiva
### Controlli
 * Inventario , Lotto di conta, Collo, Area, Tipo giacenza, Articolo, Chiavi giacenza devono esistere
 * Numero di conta, deve essere compreso nell'intervallo della tabella GML
 * Inventario e collo non devono già esistere
### Scrittura    : 
 * inserisce nuova riga GMRIIN in stato 30

## 64. Inventario collo con cartellini - annulla conta
La funzione di "Inventario collo con cartellini - annulla conta" ricerca il collo nei cartellini e, se trovato, cancella il record.
### Tabella "GNK"
 * Tipo azione :  "53"
### Input
 * Inventario
 * Collo
### Controlli
 * Deve esistere
### Scrittura
 * Cancella riga GMRIIN

## 66. Inventario collo con cartellini - Ritorna dati Contato
La funzione di "Inventario collo con cartellini - Ritorna dati contato" ricerca il collo nei cartellini del condice inventario richiesto e, se trovata riga in stato 30, restituisce i dati trovati nei campi origine.
### Tabella "GNK"
 * Tipo azione :  "66"
### Input
 * Collo origine
 * Inventario
### Controlli
 * La riga deve esistere in GMRIIN e lo stato deve essere 30
### Scrittura
 * Ritorna le Key di giacenza e la quantità trovate nei codici origine

# APPENDICE
Come esempio generale vedere il programma : 
 :  : DEC T(MB) P(SRC    ) K(GMMFC00_XX)
Come esempi specifici vedere i programmi : 
 :  : DEC T(MB) P(SRC    ) K(GMMFC00_01)
