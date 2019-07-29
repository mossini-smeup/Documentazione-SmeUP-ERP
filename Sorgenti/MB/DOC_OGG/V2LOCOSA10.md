
# Funzioni/Metodi

* **ELK** :  elenco degli elementi per codice, con schema fisso codice/descrizione
* **ELK.COM** :  elenco degli elementi per combo, con schema fisso codice/descrizione
* **ELE** :  elenco degli elementi di una lista
* **EQR** :  elenco degli elementi di una query

# Dati di chiave

* **ELK e ELE** :  istanza di una lista nel codice 1 (es. 1(LI;TAB£AMO;*)). Se per queste funzioni mi arriva un oggetto differente, verrà utilizzata una lista di virtuale dell'oggetto, avente come unico codice quello passato nella chiave 1.
* **ELK.COM** :  nel codice 1 ci sia aspetta un oggetto qualsiasi, senza indicazione del codice. Es. 1(TA;B£AMO;)

# Dati di Input (P ed INPUT)

* **Comuni (escluso metodo COM)**
** SchPar :  Stringa di parametri che possono poi essere recepiti dall'eventuale pgm di schema specifico
** Flt : 
*** Se valorizzato ad N disattiva il controllo del filtro di Job dell'oggetto e la corrispondente gestione del tasto F13
*** Se valorizzato ad S, il filtro di job viene sostituito dal filtro di "sezione" :  tutte le volte che la sezione verrà ricaricata il filtro verrà pulito e reinizializzato, questo a meno che venga valorizzato il parametro NoClRi ad 1.
** NoClRi :  quando viene settato il filtro di ricerca, impedisce che questo venga pulito alla prima chiamata.
** Context :  Stringa che va ad aggiungersi al codice Context costruito dal pgm
** Opz :  valorizzandolo con un elemento delle classe VOCOD_VER, permette di aggiungere all'inizio dello schema una colonna opzioni (tipizzata VOCOD_VER ed avente codice corrispondente alla variabile passata nel parametro). Assume valore 000101, mentre valorizzandola a No, viene disattivato il suo utilizzo.
** Parametri per condizionare query SQL
*** FROM :  Stringa FROM SQL libera che va a sostituire il file che nativamente risulta corrispondere all'oggetto che si vuole elaborare
*** WHR :  Stringa WHERE SQL libera che va ad aggiungersi alla WHERE dell'oggetto e/o dei filtri
*** ORDER :  Stringa ORDER SQL libera che forza l'applicazione di un particolare ordinamento alla query di estrazione dei dati
*** LI :  Definizione di una LISTA, la cui WHERE corrispondente va ad aggiungersi alla WHERE dell'oggetto, la struttura per questo campo è la seguente :  LI(TipoOggetto;NomeLista;NomeCampoFile)
*** FST :  stringa di filtro per codice/descrizione (si veda £G83 con comparatore SD). A differenza dei precedenti parametri viene applicata anche in caso di lista non sql.
*** FST_Rtg :  valorizzato a 1 in presenza del parametro FST fa si che il risultato della matrice (se non è paginato) venga ordinato per il rating di corrispondenza della riga rispetto alla stringa di filtro.
*** FSA :  stringa di filtro avanzata (si veda l'api £K41). Come la FST viene applicata anche in caso di lista non sql.
** Parametri per colonna icona di dettaglio (VOCOD_VER 000103)
*** Det attiva su tutte le righe la colonna con la lente
*** CndDet deve essere valorizzato con un codice attributo dell'oggetto di riferimento :  solo le righe per cui per questo attributo risulta un valore presenteranno la colonna della lente riempita
*** IntDet il contenuto passato in questo parametro verrà posto come intestazione della colonna del dettaglio
** Qry :  Valorizzato a Yes indica che il pgm viene richiamato in modalità ricerca. Viene per questo aggiunta allo schema la colonna per la scelta della query. NOTA BENE :  se viene usata questa modalità potrebbe essere opportuno includere nella scheda di richiato il membro di scheda B£EQRY_SEL, per gestire gli automatismi di selezione).
** NAg :  Valorizzato a 1 disattiva l'aggiunta automatica del tasto F07 per l'inserimento di nuove istanze del tasto F18 per il passaggio al modulo di riferimento dell'oggetto.
** OAg :  Sovrascrive l'oggetto 1 del tasto F07
** PopNot :  Sezione per NOTIFY da tasto F07
** Refresh :  valorizzato ad 1 forza la rilettura della definizione della query di riferimento
** NSql :  Valorizzato ad 1 disattiva l'utilizzo dell'sql per la risoluzione della query.
** ChL :  Valorizzato ad 1 attiva il filtro sul livello dell'oggetto secondo quanto previsto dalle /COPY £IVD e £K04 nel campo £K04O_LV.
** NK01 :  Disattiva l'informazione che permette di identificare l'oggetto di riga (Informazione di griglia Fill="K01") che disattiva ad esempio gli swipe in web.
** SetOvr :  permetti di passare degli attributi di override sul setup del componente grafico. I valori ed gli attributi vanno specificati tramite l'utilizzo delle parentesi. Es. SetOvr(ShowGroup(Yes) ShowTotal(Yes))
** MCol :  permette passando due numeri di passare un numero di colonna ed il numero totale di colonna (es. se passo MCol(2,3)) nel risultato avrò solo i risultati della "seconda colonna" es. Riga 2, Riga 5, Riga 8, Riga 11 ecc.
** NFro :  se il caricamento è sql, ma lo schema può omettere dei record, questo attributo permette di dire che alla fetch non vengano caricati solo il numero di record previsti per la pagina (disattiva l'utilizzo del "Fetch First nnn rows only")

* **Specifici Metodo EQR - Query di Elementi (rispecchiano quanto costruito dal costruttore A08 quando riceve in input una query)
** Q1cTip :  Tipo Oggetto Riferimento
** Q1cPar :  Parametro Oggetto Riferimento
** Q1cQry :  Codice Query
** Q1cFlt :  Filtro specifico della query (con struttura codicecampofiltro1(valorecampofiltro1), codicecampofiltro2(valorecampofiltro2), con unica eccezione campi con operatore Range, in questo caso abbiamo struttura  codicecampofiltron_I(valorecampofiltron_I) per il limite iniziale e codicecampofiltron_F(valorecampofiltron_F) per il limite finale.
** Q1cPag :  Filtro paginazione (il formato dipende dalla natura della specifica query)
** Q1cSch :  Schema
** Q1cOrd :  Ordinamento
** Q1cFst :  Stringa di filtro per codice/descrizione (si veda £G83 con comparatore SD)
** Q1cNre :  Numero righe
** Q1cAOD :  Se valorizzato ad A o D forza l'ordinamento ASCEND o DESCEND

* **Specifici Metodo ELE - Lista Elementi**
** Sch :  Schema passato in input
** SchF :  Se valorizzato, indica che lo schema passato nel precedente parametro sarà fisso e quindi non modificabile dall'interrogazione della lista
** Ele :  Contiene l'elenco degli OAV, separati da ";". Può contenere anche eventuali nomi di campi che possono essere definiti nel parametro successivo dati aggiuntivi (Eda).
** Eda :  in presenza del parametro Ele, Eda permette di aggiungere di attribuire dei parametri di configurazione agli oav utilizzati nel parametro Ele. La sintassi si veda quella dell'oggetto J5EDT_SCH/G.LIS.LID. La configurazione di più attributi andrà separata tramite pipe.
** Ord :  Ordinamento proposto come default
** OrdF :  Se valorizzato, indica che l'ordinamento passato nel precedente parametro sarà fisso e quindi non modificabile dall'interrogazione della lista
** RPa :  Righe per Pagina, forza il default relativo al n° di righe per pagina da presentare
** Upd :  Attiva l'aggiornamento della matrice. Può valore Yes per aggiungere come seconda sezione la matrice d'aggiornamento, Only per far si che l'unica sezione sia già in aggiornamento. Perchè l'aggiornamento sia possibile è comunque inoltre necessario che esista il programma "_A" corrispondente al file.
** DDWN :  Parametro di Drill Down con la struttura prevista dal B£SER_83 - FLDn(Nome Campo) VALn(Valore) OPEn(Operazione)
** Ctx :  Con Testo. Nella costruzione dell'albero ogni foglia ha visualizzato oltre al codice la descrizione.
** SS :  sottoscheda. Nella costruzione dell'albero è possibile definire una sottoscheda da richiamarre
** NCf :  Se valorizzato ad "1" disattiva la presentazione del tasto funzione F18 per la configurazione di schemi/ordinamenti.
** NTit :  Se valorizzato ad "1" disattiva la costruzione automatica del titolo da parte del servizio
** Parametri per funzioni di MDV
*** SchSet :  schema che si vuole memorizzare per la lista - solo per funzione MDV.SCH
*** OrdSet :  schema che si vuole memorizzare per la lista - solo per funzione MDV.ORD

* **Specifici Metodo ELK.COM - Combo**
** K :  viene attesa la stringa di ricerca. Queste le possibili combinazioni attese : 
** Se il parametro inizia per "!" verrà eseguita la query per codice (*KEY) usando come posizionamento i caratteri successivi
** Se il parametro inizia per "?" verrà eseguita la query per descrizione (*DEC) usando come posizionamento i caratteri successivi
** Se il parametro inizia per " : " verrà eseguita la query per codice (*KEY) usando come filtro stringa su codice/descrizione i caratteri successivi
** In tutti gli altri casi verrà eseguita la query per codice (*KEY) usando come filtro stringa su codice/descrizione tutti i caratteri passati

* **Specifici Metodo SNP - Set'n play**
** Met :  Metodo passato alla G40 solo per funzioni di test.

# Note Aggiuntive

## CONTEXT per la memorizzazione dei setup
* Di default viene composto da : 
** LOA10_SE
** £UIBME
** Oggetto di Riferimento
** Nome Schema
** Eventuale stringa passata con il parametro Context

## Determinazione Schema di Default
* Per il metodo ELE viene assunto cercando in risalita questi schemi : 
** Q/DFT
** T/DFT
** *FIL/*ALL se l'oggetto corrisponde ad un file
** *TAB/*ALL se l'oggetto corrisponde è una tabella
** T/CD* Codice/Descrizione


