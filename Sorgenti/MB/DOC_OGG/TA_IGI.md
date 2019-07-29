# IGI - Indici di gestione
## CONTENUTO DEI CAMPI
 :  : FLD T$ELEM Elemento
È il codice dell'elemento che rappresenta il singolo valore numerico del D5COSO.
_9_Esempio :  l'elemento 11 caratterizza il valore 11 del D5COSO.
Nella codifica è inoltre importante tener conto del fatto che il 1° carattere serve ad determinare se l'elemento rappresenta una riclassifica A (1° carattere="A") o una riclassifica B (1° carattere="B") o una riclassifica C (1° carattere="C") o una riclassifica D (1° carattere="D")
 :  : FLD T$DESC Descrizione
È il significato del valore.
 :  : FLD T$IGIA __Tipo valore/parametro/formula__
Il tipo valore, se specificato, identifica la modalità di ripresa/calcolo del valore.
_7_'NO' Numeri di un oggetto
I numeri di un oggetto sono definiti dal parametro, che identifica  il tipo di oggetto (es. DRBOF righe documento) e dalla formula che in questo caso è un puntatore al numero selezionato. Così per indicare la quntità Spedita, la tabella dovra essere  : 

 :  : PAR F(01) L(TAB)
- Tipo valore|'NO'|
- Parametro|'DRBOF' Tabella *CNTT
- Formula/parametro|'002'


_7_'FO' Formula di numeri oggetto
In sviluppo
_7_'CO' Costo per tipo
Se almeno uno dei 4 oggetti della chiave del record è un articolo, il valore può essere il costo dell'articolo ad un certo livello.
_9_Esempio

 :  : PAR F(01) L(TAB)
- Tipo valore|'CO'
- Parametro|'STD' Tabella TCO
- Formula/parametro|'2'   Tabella D0B (livello)


_7_'CD' Costo per data/natura
È equivalente al precedente 'CO' :  viene mantenuto per compatibilità con il passato.

_7_'RB' Saldo Bilancio
Utilizzato solo dal pgm specifico per il calcolo degli indici di bilancio, tramite esso viene ripreso il saldo di una linea di riclassifica ad una certa data.
Se ne può vedere un'applicazione negli elementi della IGI£G.

 :  : PAR F(01) L(TAB)
- Tipo valore|'RB'
- Parametro|Codice Riclassifica (TAC5M)
- Formula/parametro|Codice Linea Riclassifica (TAC5Nxx)


_7_'RA' Saldo Bilancio Annualizzato
Vale quanto precisato per il tipo RB con la sola differenza che come saldo viene ripreso, il saldo moltiplicato per numerogiorniesercizio/numerogiornidainizioesercizioadatasaldo).
E' uno dei metodi che permette di rendere più significativi gli indici calcolati durate un perido infra-esercizio su linee di riclassifica "economiche".

 :  : PAR F(01) L(TAB)
- Tipo valore|'RA'
- Parametro|Codice Riclassifica (TAC5M)
- Formula/parametro|Codice Linea Riclassifica (TAC5Nxx)


_7_'RR' Saldo Bilancio Rolling
Vale quanto precisato per il tipo RA con la sola differenza che il saldo viene reso significativo sommando tutti i movimenti degli ultimi 12 mesi rolling (quindi anche quelli dell'esercizio precedente per la quota che compete.

 :  : PAR F(01) L(TAB)
- Tipo valore|'RR'
- Parametro|Codice Riclassifica (TAC5M)
- Formula/parametro|Codice Linea Riclassifica (TAC5Nxx)


_7_'RM' Saldo Bilancio Medio
Vale quanto precisato per il tipo RB con la sola differenza che come saldo viene ripreso, il saldo medio, calcolato come media fra il saldo alla data e di inizio esercizio.
Solitamente applicato alle linee patrimoniali quando utilizzate in rapporto a linea economiche.

 :  : PAR F(01) L(TAB)
- Tipo valore|'RM'
- Parametro|Codice Riclassifica (TAC5M)
- Formula/parametro|Codice Linea Riclassifica (TAC5Nxx)


_7_'RD' Saldo Bilancio - Differenza Finale/Iniziale
Vale quanto precisato per il tipo RB con la sola differenza che come saldo viene ripresa, la differenza fra saldo alla data e di inizio esercizio.

 :  : PAR F(01) L(TAB)
- Tipo valore|'RD'
- Parametro|Codice Riclassifica (TAC5M)
- Formula/parametro|Codice Linea Riclassifica (TAC5Nxx)


_7_'UT' Valore da programma utente
Il valore è calcolato tramite un Pgm esterno (Exit), scritto per la specifica esigenza. Un esempio di tale programma è costituito dal Pgm D5CALC_1 (IGIGUT_A per il modulo IGIREPT).

 :  : PAR F(01) L(TAB)
- Tipo valore|'UT'
- Parametro|'IGIGUT_A'


_7_'FL' Formula di valori precedenti
Calcolate le diverse tipologie di valori, è possibile scrivere una formula che li metta in relazione.
_9_Esempio :  se nell'elemento 01 è stata ripresa la quantità spedita e nell'elemento 02 il costo unitario, per il calcolo del
costo totale la formula sarà V01*V02.

 :  : PAR F(01) L(TAB)
- Tipo valore|'FL'
- Parametro|
- Formula|V01*V02

Nelle formule è possibile utilizzare anche le parentesi.

_7_'FT' Formula di valori di un altro tema
Valgono le medesime considerazioni del tipo FL, con la sola differenza che i valori vengono presi da un'altro tema. Questo tema deve obbligatoriamente avere le medesime chiavi del tema in elaborazione.

 :  : PAR F(01) L(TAB)
- Tipo valore|'FT'
- Parametro|SSD5O+Elemento D5O
- Formula|V01*V02


_7_'OA' OAV di un oggetto della chiave
Il campo viene riempito con un OAV (ovviamente numerico) di un oggetto della chiave del record. La sintassi è la seguente : 

 :  : PAR F(01) L(TAB)
- Tipo valore|'OA'
- Parametro|Oggetto intestatario dell'OAV (ex. AR)
- Formula|OAV dell'oggetto (ex. I/20)


_7_'PA' Parametro numerico di un oggetto
Il campo viene riempito con un parametro (ovviamente numerico) di un oggetto della chiave del record. Se il parametro è alla data, viene tenuto conto del periodo. La sintassi è la seguente : 

 :  : PAR F(01) L(TAB)
- Tipo valore|'PA'
- Parametro|Oggetto intestatario del parametro (ex. AR)
- Formula|Elemento C£E + Elemento B£Nxx


 :  : FLD T$IGIB.T$IGIA __parametro__
 :  : FLD T$IGIC.T$IGIA __parametro__
 :  : FLD T$IGID __U.misura__
Per il singolo valore è possibile specificare un'unità di misura che lo caratterizza.
 :  : FLD T$IGIE __Riclassifica A__
In questo campo è possibile specificare un elemento di riclassifica A (codici Axx) in cui questo valore andrà a confluire. Se, per esempio, l'elemento 05 di valore 1000 avesse in questo campo A01 e anche l'elemento 10 di valore 200, nel visualizzare la riclassifica nel pgm di dettaglio del D5COSO (pulsante F07) l'elemento A01 varrebbe 1200.
 :  : FLD T$IGIF __Riclassifica B__
In questo campo è possibile specificare un elemento di riclassifica B (codici Bxx), in cui questo valore andrà a confluire. Per un esempio vedere la riclassifica A. Il tasto funzione associato alla riclassifica B è F08.
 :  : FLD T$IGIG __Controllo__
I valori possibili sono : 
- vuoto -> il valore non è mai modificabile dal pgm di dettaglio del record.
- F -> il valore è modificabile dal pgm di dettaglio.
- O -> il valore deve essere inserito nel pgm di dettaglio.
 :  : FLD T$IGIL __Totalizzazione__
Per totalizzare dei valori, oltre le formule, è possibile utilizzare questo campo di totalizzazione che permette di gestire facilmente fino a 5 subtotali. I valori possibili sono : 
- +  :  il valore viene sommato.
- -  :  il valore viene sottratto.
 :  : FLD T$IGIH __Caratt. descrizione__
Attributo di visualizzazione
 :  : FLD T$IGII __Caratt. valore__
Vedi T$IGII
 :  : FLD T$IGIJ __Gestione incidenza__
È possibile specificare un valore come base di incidenza (che quindi sarà il 100%), per vedere come gli altri si rapportano rispetto ad esso. Per visualizzare le incidenze percentuali bisogna andare nel visualizzatore del D5COSO e scegliere in una delle 2 colonne libere l'opzione 1 (Incidenza %).
I valori possibili sono : 
- B :  il valore è la base di incidenza.
- E :  escludi il valore dalla visualizzazione dell'incidenza blank :  visualizza l'incidenza del valore rispetto alla base.
 :  : FLD T$IGIK __Gestione totale__
Vedi T$IGIJ
 :  : FLD T$IGIN __Natura costo__
Utilizzata per il costo oggetti. Permette di caratterizzare il valore per natura tramite un elemento della tabella D0A.
In questo modo è possibile visualizzare, tramite il visualizzatore costi, il costo di un oggetto non solo per le sue singole componenti, ma anche per natura di costo. Essendo la natura costo una tabella, è possibile creare delle nuove nature costo e caratterizzare i valori del costo con questa nuova natura.
 :  : FLD T$IGIP __Elem. Costo "L"__
È utilizzato quando, dall'applicazione dei costi base (CS), si vogliono reperire, tramite la routine £G17 (che viene utilizzata soltanto in questo modulo), dei costi avanzati (S2), memorizzati in D5COSO.
Il presente campo può assumere un valore tra  0 e 17, che individua uno dei componenti elementari di costo, secondo la struttura fissa a "L", tipica dei costi base (CS).
 :  : FLD T$IGIQ __Punti sep./decimali__
È possibile specificare il numero di punti separatori (max. 4) e di decimali (max. 6) da utilizzare nella visualizzazione del record del D5COSO.
Se non indicati vengono assunti quelli specificati nel tema.
L'arrotondamento effettuato (sempre e solo in visualizzazione) è di tipo H.
 :  : FLD T$IGIS __Riclassifica C__
In questo campo è possibile specificare un elemento di riclassifica C (codici Cxx), in cui questo valore andrà a confluire. Per un esempio vedere la riclassifica A.
 :  : FLD T$IGIT __Riclassifica D__
In questo campo è possibile specificare un elemento di riclassifica D (codici Dxx), in cui questo valore andrà a confluire. Per un esempio vedere la riclassifica A.
 :  : FLD T$IGIV __Gruppo__
In questo campo è possibile specificare un elemento di gruppo G (codici Gxx), in cui questo valore andrà a confluire. Il concetto di gruppo è attualmente utilizzato solo nelle schede di interrogazione degli indici di bilancio.

