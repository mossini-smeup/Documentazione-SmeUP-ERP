# C£V - Valori per tipo oggetto
 :  : DEC T(ST) K(C£V)
## OBIETTIVO
Permette di descrivere le sezioni presenti in un listino.
All'interno di un listino, ad esempio, si potrà avere la sezione articoli, la sezione attrezzature, la sezione trasporti ecc.
## SOTTOSETTORI
Permettono di separare gruppi di sezioni. Un sottosettore potrà essere associato ad un listino per limitare l'ambito di scelta.
## CONTENUTO DEI CAMPI
 :  : FLD T$C£VG **Griglia di controllo**
Elemento della tabella B£G :  definisce i tre oggetti intestatari dei listini di questa sezione.
 :  : FLD T$C£VV **Valuta**
Indica il tipo di controllo per il campo.
-    Bianco    = il campo non viene presentato
-     F         = presentato ma accetta anche il valore bianco
-    O         = obbligatorio
 :  : FLD T$C£VD **Data di validità**
Indica il tipo di controllo per il campo.
Controlli come in **T$C£VV**
 :  : FLD T$C£VL **Lotto**
Indica il tipo di controllo per il campo.
Controlli come in **T$C£VV**
 :  : FLD T$C£VS **Sottosettore valori**
Indica il sottosettore della tabella C£H nel quale sono descritti i valori associabili ad una sezione
 :  : FLD T$C£V1 **Significato valore 1/5**
Codice significato del valore :  elemento della C£H definito nel sottosettore impostato nel campo precedente.
 :  : FLD T$C£V6 **Significato valore 6**
Codice significato del valore :  elemento della C£H definito nel sottosettore impostato nel campo precedente.
 :  : FLD T$C£VP **Programma specifico di calcolo**
Indica un programma utente da utilizzare quando si vogliono reperire i valori di un listino.
Se non si indica un programma specifico, viene eseguito il programma base C£C£L0R. Il programma C£C£L0R_C legge i costi di un tipo costo specificato.
 :  : FLD T$C£VC **Condizione Programma**
Mediante questo campo è possibile gestire particolari funzionalità di calcolo.
Per il programma base, se questo campo non è bianco, il calcolo del valore avviene mediante risalita.
 :  : FLD T$C£VA **Unità di misura alternativa**
È un elemento della tabella UMS :  si indica quando la sezione descrive i prezzi unitari di un prodotto in una unità di misura fissata. Ad esempio, prezzi per chilo quando l'unità di misura interna è il numero. I programmi che reperiscono il valore verificheranno la congruenza di tale unità di misura con quella in gestione (interna o esterna). Se il valore è bianco, si assume che l'unità di misura del prezzo è quella di magazzino.
 :  : FLD T$C£VB **Significato valori da documento**
È un valore fisso V2/F_TVA :  se impostato, il significato dei cinque valori è dato dai significati di questo tipo valori.
 :  : FLD T$C£VR **Livello di nascita**
Se, in inserimento della riga di listino, non viene specificato uno stato, viene assunto questo livello con il suo stato principale.
 :  : FLD T$C£VE **Contenitore note**
È l'elemento della tabella NSC che contiene le note delle righe di listino di questa sezione.
È possibile definire le note in due modi : 
-    per identificativo di record
-    per chiave 1/2/3
Il modo verrà scelto automaticamente, in funzione di come è stata definita la griglia in tabella NSC (se il primo campo chiave è 'LS' è il primo modo).
 :  : FLD T$C£VN **Categoria parametri**
È un elemento della tabella C£E che definisce i parametri esterni collegabili alla riga di listino.
 :  : FLD T$C£VF **Prezzi in Unità di Misura alternativa**
Se imopostato, i prezzi nei documenti non vengono convertiti e sono considerati già in U.M. alternativa.
 :  : FLD T$C£VH **Suffisso programma di controllo**
Se inserito il carattere "X" , nel formato di dettaglio dei listini verrà richiamato il programma specifico "C£LIS0D_X", per eseguire controlli e indurre comportamenti personali.
 :  : FLD T$C£VI **Validità data D/A**
Inserendo 'D' o 'A' si può specificare un tipo di validità data, diversa da quella specificata in tabella C£L (listini), si possono avere sezioni con significati diversi, alcune con validità "Da" altre "fino Al".
È possibile inserire anche 'I' o 'F', corrispondenti rispettivamente a 'D' e 'A' ma che attivano la gestione della data di validità secondaria (facoltativa).
 :  : FLD T$C£VM **Validità lotto D/A**
Inserendo 'D' o 'A', si può specificare un tipo di validità lotto diverso da quello specificato in tabella C£L (listini), si possono avere sezioni con significati diversi, alcune con validità "Da", altre "fino Al"; inoltre è possibile specificare nella stessa sezione una validità per la data e una per il lotto.
 :  : FLD T$C£VO **Parametri impliciti**
È un elemento della tabella C£I che definisce i parametri collegabili alla riga di listino, contenuti all'interno dell'archivio.
 :  : FLD T$C£VQ **Gruppo flag**
È un elemento della tabella B£Y. Se valorizzato, all'atto dell'inserimento della riga di listino verranno assegnati i flag di questo elemento.
 :  : FLD T$C£VT **Contr.valori in rip.**
È un campo di 5 caratteri e serve per gestire il controllo dei valori durante la ripresa del prezzo (es. nei documenti).
Viene gestito ogni singolo carattere, il primo gestisce il valore 1, il secondo il valore 2 e così fino al quinto.
Il singolo carattere può assumere i seguenti significati : 
- ' '  Il campo 'Valore n' è controllato (quindi non verrà ripreso il listino se diverso da 0)
- '1'  Il campo 'Valore n' NON è controllato e sostituito.
Indipendentemente dal fatto che sia uguale o diverso da 0 viene effettuata la ripresa del listino ed il campo verrà sostituito qualsiasi sia il suo valore.
- '2'  Il campo 'Valore n' NON è controllato e NON è sostituito.
Indipendentemente dal fatto che sia uguale o diverso da 0 viene effettuata la ripresa del listino MA il campo NON verrà sostituito rimanendo il valore precedentemente immesso.
_9_N.B. :  Se diversamente specificato Assume il valore ' ', e, anche in caso di campo impostato a '2' ma definito di ripresa dalla testata (vedi tabella V5D), viene gestito come il significato '1'.
_9_N.B. :  E' importante notare che sono descritti due concetti :  una è se il listino viene ripreso o no, l'altro è se il campo debba essere controllato/sostituito. Con il valore a blank è sufficiente che ci sia anche solo un campo <> da 0 per cui il listino non venga letto e per cui anche i campi con valore 1 non vengano aggiornati.
 :  : FLD T$C£VY **Contr.valori in rip2**
Il significato di questo campo è il medesimo del precedente "Contr.valori in rip." con la
differenza che il presente campo condiziona la ripresa per i valori dal 6 al 10, laddove siano
attivati. Se non sono gestiti i valori aggiuntivi la compilazione del campo risulta superflua.
Qui sotto riprendiamo la struttura del campo : 
È un campo di 5 caratteri e serve per gestire il controllo dei valori durante la ripresa del prezzo (es. nei documenti).
Viene gestito ogni singolo carattere, il primo gestisce il valore 1, il secondo il valore 2 e così fino al quinto.
Il singolo carattere può assumere i seguenti significati : 
- ' '  Il campo 'Valore n' è controllato (quindi non verrà ripreso il listino se diverso da 0)
- '1'  Il campo 'Valore n' NON è controllato e sostituito.
Indipendentemente dal fatto che sia uguale o diverso da 0 viene effettuata la ripresa del listino ed il campo verrà sostituito qualsiasi sia il suo valore.
- '2'  Il campo 'Valore n' NON è controllato e NON è sostituito.
Indipendentemente dal fatto che sia uguale o diverso da 0 viene effettuata la ripresa del listino MA il campo NON verrà sostituito rimanendo il valore precedentemente immesso.
_9_N.B. :  Se diversamente specificato Assume il valore ' ', e, anche in caso di campo impostato a '2' ma definito di ripresa dalla testata (vedi tabella V5D), viene gestito come il significato '1'.
 :  : FLD T$C£VU **Listino provvigioni**
Se si inserisce '1', significa che la sezione contiene valori di provvigioni agenti. Nel programma di gestione del listino comparirà il campo "Tipo Provv." che consentirà di specificare la tipologia del valore (Percentuale o Importo).
 :  : FLD T$C£VW **Stato minimo listino**
Se impostato, condiziona la selezione o meno di un record di listino, durante la lettura tramite £C£L : 
Scarta tutti i record di listino con uno stato inferiore a quello impostato
 :  : FLD T$C£VX **Stato Massimo listino**
Se impostato, condiziona la selezione o meno di un record di listino durante la lettura tramite £C£L : 
Scarta tutti i record di listino con uno stato superiore a quello impostato.
_Attenzione_ :  non viene assunto nessun default. Se questo stato è minore dello stato minimo, tutti i record vengono scartati.
