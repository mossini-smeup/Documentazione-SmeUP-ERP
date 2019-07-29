# C£E - Categoria parametri
 :  : DEC T(ST) K(C£E)
## OBIETTIVO
Gestire un gruppo di parametri variabili per entità. Questa struttura si utilizza ad esempio per associare ad un articolo (o ad un tipo di articoli) un gruppo di variabili non presenti a livello anagrafico, perchè tipiche del contesto applicativo in cui ci si trova.
## CONTENUTO DEI CAMPI
 :  : FLD T$C£EE **File appartenenza**
Se indicato, permette di gestire fisicamente i records di questa categoria di parametri in un archivio C£CONx0F, dove x è il contenuto del presente campo.
Attraverso l'assegnazione di una singola categoria di parametri, ad archivi fisici diversificati, si possono realizzare categorie di parametri alternativamente verticalizzate o trasversali, attraverso i sistemi informativi, permettendo, ad esempio, la gestione di alcuni parametri centralizzati (indipendenti dal sistema informativo) ed altri invece specifici.
La gestione è del tutto speculare a quella esistente per le tabelle TABELx0F.
 :  : FLD T$C£EG **Griglia di controllo**
Elemento della tabella B£G. Si rimanda a questa per approfondimenti.
 :  : FLD T$C£ES **Sottosettore valori**
Indica un sottosettore di B£N utilizzato per individuare i codici di variabili validi. I due campi successivi permettono di limitare la scelta all'interno del sottosettore per codice o per contenuto di un campo.
 :  : FLD T$C£EI **Prefisso cod. valori 1/2/3**
Permette di condizionare, all'interno del sottosettore specificato, i parametri ammessi. Si possono specificare fino a tre diversi prefissi. Non serve specificare l'asterisco.
_9_Esempi
T    = Tutti i parametri che iniziano con T
XY   = Tutti quelli che iniziano con XY
 :  : FLD T$C£ED **Limite di selezione**
Permette di selezionare gli elementi della tabella B£N in funzione della sua condizione di selezione.
 :  : FLD T$C£ER **Regole di controllo**
Permette di definire la categoria di regole (Tabella C£T) per la verifica complessiva dei parametri.
 :  : FLD T$C£EN **Contenitore note**
È possibile associare un contenitore. La presenza di questo campo permette di associare note a livello di oggetto. Le note sui parametri sono attive se è specificato il contenitore e il singolo parametro è definito come commentabile nella B£N.
 :  : FLD T$C£EM **Condizioni/Azioni**
Permette di associare alla categoria di parametri una categoria di condizionamenti che verranno verificati al momento dell'inserimento dei parametri stessi.
Si veda la documentazione delle "CONDIZIONI/AZIONI" e delle tabella C£N che le guida.
 :  : FLD T$C£EO **Parametri per risalita**
Se presente una categoria di parametri, questa viene utilizzata nelle funzioni di lettura dei parametri quando non è stato trovato alcun valore fra quelli richiesti. Se, ad esempio, ho una categoria di parametri che fornisce il tipo ordine di un prodotto, posso associare a questa una categoria con gli stessi parametri legati ad esempio alla classe articolo.
**Caratteristiche**
1.   Le categorie associate per la risalita devono avere uguali il sottosettore dei valori.
2.   La risalita è attiva solo per gli oggetti (AR=Articolo e CN=Contatti/Enti RI=Risorse). Il tipo di informazione con cui risalire viene derivato dalla griglia della categoria stessa.
3.   Nel caso in cui la griglia accetti **, il riferimento superiore di una categoria può essere la categoria stessa.
In questo caso cambia solo il codice (risalita standard)
_9_Esempio
XX1  =    Categoria per Cliente/Articolo
Se risale a XX2
XX2  =    Può essere alternativamente
Cliente/Classe prodotto(TACLS)
Agente(TAAGE)/Articolo
Agente(TAAGE)/Classe prodotto(TACLS)
Se risale a XX3
XX3  =    Può essere, successivamente
Agente/**
**/Classe prodotto
**/**
Il programma usa il primo che contiene dei dati
 :  : FLD T$C£EP **Programma specifico di visualizzazione**
Permette di indicare un programma che verrà utilizzato tutte le volte che si richiede interrogazione. Ciò, al fine di ottimizzare il modo con cui i parametri si presentano all'utente finale.
L'applicazione fornisce un prototipo di programma (C£CR01_00), da utilizzare quando si vuole costruire un programma specifico.
 :  : FLD T$C£EB **Ricerca automatica**
Se impostato, questo campo consente di attivare automaticamente la ricerca in caso di parametro obbligatorio di tipo TA (tabella) e lasciato vuoto.
 :  : FLD T$C£EL **Visualizzazione Estesa**
Se indicato, attiva la visualizzazione a 132 colonne del programma di gestione parametri. Sarà inoltre possibile indicare, per singolo parametro, un attributo di visualizzazione (Tabella B£N).

 :  : FLD T$C£EK **Richiesta conferma    **
E' un valore ' ' '1'. Se impostato a '1' il programma di gestione parametri chiederà una conferma di modifica dati
tramite il tasto funzionale F6

 :  : FLD T$C£EJ   Tipo Gest.Autorizz.     
Permette di definire se i parametri sono autorizzati attraverso : 
* classe STATI - funzione PA
* classe PLC-C£CONR funzione = cat. parametri (elemento C£E). E' prerequisito l'attivazione della protezione campo sulla tabella B£2.
