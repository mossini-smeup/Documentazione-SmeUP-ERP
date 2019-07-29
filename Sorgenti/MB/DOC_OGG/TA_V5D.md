# V5D - Tipi documento
 :  : DEC T(ST) K(V5D)
## OBIETTIVO
Definire le caratteristiche del tipo documento utilizzato nella gestione cicli esterni.
## CONTENUTO DEI CAMPI
 :  : FLD T$ELEM
Identifica il codice del tipo documento.
 :  : FLD T$DESC
 :  : FLD T$V5DM __Ambiente__
È un elemento della tabella *CN/AA, che definisce l'ambiente di appartenenza dei documenti di questo tipo. Se lasciato in bianco viene assunto 'SM'.
 :  : FLD T$V5DS __S/S Mod.Documento__
È un sottosettore della tabella V5A, che raggruppa i modelli documenti appartenenti a questo tipo.
 :  : FLD T$V5DD __Modello Doc.Assunto__
È un elemento della tabella V5A, del sottosettore definito nel campo precedente, che definisce il modello del documento assunto all'inserimento di un documento di questo tipo.
 :  : FLD T$V5DC __Tipo sviluppo qtà__
È un elemento della tabella B£G. Nel caso in cui l'articolo sia soggetto a sviluppi quantità, fornisce la griglia dei due codici chiave della riga di sviluppo.
 :  : FLD T$V5DP __Programma stampa__
Nome del programma di stampa specifico per stampare il tipo documento definito. Se non specificato si assume V5DO07C$.
 :  : FLD T$V5DN __SS pgm stp__
È un sottosettore della tabella B£Q. Se viene impostato il programma di stampa documenti (V5OA01A) gestisce la stampa di più formati. (Si utilizza nel caso un documento abbia + forme di presentazione).
 :  : FLD T$V5D2 __Tipo ente intestat.__
È un elemento della tabella BRE. Indica il tipo ente a cui è intestato il documento e quello a cui si invia la conferma.
 :  : FLD T$V5D1 __Tipo ente spedizione__
È un elemento della tabella BRE. Indica il tipo ente a cui è effuettuata la spedizione degli oggetti contenuti nel documento.
 :  : FLD T$V5D3 __Tipo Ente Fatturaz.__
È un elemento della tabella BRE. Indica il tipo ente a cui è intestata la fattura collegata al documento.
 :  : FLD T$V5D4 __Categoria listini__
È un elemento della tabella C£*/CL che, se valorizzato, serve da filtro sui listini ammessi (deve coincidere con la categoria listini inserita nella tabella listino C£L).
 :  : FLD T$V5DA __Sez. provvig. testata__
È un elemento della tabella C£V, che definisce la sezione usata nel reperimento dei valori delle provvigioni di testata.
 :  : FLD T$V5DR __S/S stati gestiti__
È un sottosettore della tabella B£W che raggruppa gli stati possibili per questo tipo documento.
 :  : FLD T$V5DL __Livello di nascita__
Se, in inserimento del documento, non viene specificato uno stato, viene assunto questo livello con il suo stato principale.
 :  : FLD T$V5DB __Sez. listini testata__
È un elemento della tabella C£V, che definisce la sezione usata nel reperimento dei valori del listino di testata.
 :  : FLD T$V5DX __Gruppo flag testata__
È un elemento della tabella B£Y. Se valorizzato, e se non valorizzato li gruppo flag a livello di modello, alle testate documenti vengono assegnati i flag di questo elemento.
 :  : FLD T$V5DY __Gruppo flag riga__
È un elemento della tabella B£Y. Se valorizzato, e se non valorizzato il gruppo flag a livello di modello o a livello di riga, alle righe documenti vengono assegnati i flag di questo elemento.
 :  : FLD T$V5D0 __Tipo data reg.Mag.__
Indica la data da utilizzare come data di registrazione nei movimenti di magazzino.
I valori possibili sono : 
- . Data documento interno (è la data di testata del documento). Questa è la data di default;
- 1. Data documento esterno (è la data bolla);
- 2. Oggi (è la data di esecuzione del collegamento a magazzino);
- 3. Data di partenza.
 :  : FLD T$V5DZ __Contr.righe in coll.__
Se impostato, il programma di collegamento documenti controlla, prima di eseguire il collegamento stesso, che ci siano delle righe :  in caso contrario non lo esegue e la testata rimane da collegare.
 :  : FLD T$V5DF __Listino provvigioni__
È un elemento della tabella C£L. Se impostato, lo assume per le provvigioni in luogo di quello dell'ente.
 :  : FLD T$V5D5 __Ma./Sc. 1__
È un elemento della tabella V5S. Inserendo un valore in questo campo si abilita il tipo documento ad impostare dei valori di Spesa, Maggiorazioni e/o sconti, nella testata del documento in esame (esempio sconto ente)
 :  : FLD T$V5D6 __Ma./Sc. 2__
È un elemento della tabella V5S. Inserendo un valore in questo campo si abilita il tipo documento ad impostare dei valori di Spesa, Maggiorazioni e/o sconti, nella testata del documento in esame (esempio sconto ente).
 :  : FLD T$V5D7 __Ma./Sc. 3__
È un elemento della tabella V5S. Inserendo un valore in questo campo si abilita il tipo documento ad impostare dei valori di Spesa, Maggiorazioni e/o sconti, nella testata del documento in esame (esempio sconto ente).
 :  : FLD T$V5D8 __Ma./Sc. 4__
È un elemento della tabella V5S. Inserendo un valore in questo campo si abilita il tipo documento ad impostare dei valori di Spesa, Maggiorazioni e/o sconti, nella testata del documento in esame (esempio sconto ente).
 :  : FLD T$V5D9 __Ma./Sc. 5__
È un elemento della tabella V5S. Inserendo un valore in questo campo si abilita il tipo documento ad impostare dei valori di Spesa, Maggiorazioni e/o sconti, nella testata del documento in esame (esempio sconto ente).
 :  : FLD T$V5DT __Copia Ma/Sc. su righe__
Se impostato, si predispone alla copia da testata a righe per le magg/sconti che lo prevedono.
Se non impostato, non esegue la copia da testata a righe, anche per le magg/sconti che lo prevederebbero.
 :  : FLD T$V5DV __Calcolo Pesi/Volumi__
Se impostato, nella funzione di valorizzazione documento ritorna (accedendo all'anagrafica) il peso e il volume degli articoli.
 :  : FLD T$V5DE __Trat. cambio in der.__
Se lasciato bianco, durante la creazione della testata in "DERIVAZIONE" da altro documento, mantiene il cambio di quest'ultimo. Impostando il campo a '1' il cambio viene azzerato.
 :  : FLD T$V5DG __Livelli articolo__
Si possono impostare due livelli (elementi della tabella B£W/00). Questi definiscono gli estremi di validità per gli articoli accettati nelle righe dei documenti che appartengono a questo tipo, se intestate ad oggetti articoli.
Valgono le seguenti convenzioni : 
-    se non impostato il minimo si assume ' '.
-    se non impostato il massimo si assume '9'.
Questo controllo vale sempre e solo in inserimento e variazione della riga del documento.
 :  : FLD T$V5DH
Si possono impostare due livelli (elementi della tabella B£W/00). Questi definiscono gli estremi di validità per gli articoli accettati nelle righe dei documenti che appartengono a questo tipo, se intestate ad oggetti articoli.
Valgono le seguenti convenzioni : 
-    se non impostato il minimo si assume ' '.
-    se non impostato il massimo si assume '9'.
Questo controllo vale sempre e solo in inserimento e variazione della riga del documento.
 :  : FLD T$V5DI __ATP abilitato__
Se impostato, significa che per questo tipo documento è possibile il calcolo ATP (available to promise). Perchè esso sia effettivamente eseguibile, occorrerà che nel tipo riga sia stato impostato un modello ATP. In questo modo si ottiene che lo stesso tipo riga possa essere usato su più tipi documenti, ma sia attivato l'ATP solo in alcuni (ad esempio, sugli ordini clienti ma non sulle bolle di uscita inserite manualmente).
Inoltre, si può disattivare l'ATP solo su alcuni tipi riga (ovviamente quelle non di oggetto articolo, in più, ad esempio quelle per campioni, prove :  produzioni limitate che non danno un significativo contributo all'impegno di materiali e risorse). In teoria, dovrebbero essere esclusi dall'ATP i tipi riga che non entrano nel gruppo fonti della pianificazione.
 :  : FLD T$V5DJ __Pgm aggius.qt.master__
Normalmente la quantità master, per il calcolo del valore della riga e per la determinazione del saldo, è quella in unità di misura esterna. Se impostato questo valore, per le righe documenti di questo tipo, viene lanciato il programma di aggiustamento 'V5QMAST_x', con funzione calcolo valore o determinazione saldo, che ritorna l'unità di misura master per la riga in esame (esterna/interna).
 :  : FLD T$V5DK __Suf.Pgm Calcolo Val.__
Se si desidera utilizzare un programma particolare di calcolo valori, è possibile specificare il suffisso del programma da richiamare. Viene lanciato il programma di aggiustamento 'V5V5V0_x'. Per maggiori informazione sulla modalità di utilizzo del programma, leggere le note riportate nel sorgente del programma prototipo (V5V5V0_X).
Nota :  Il suffisso K non può essere utilizzato in quanto già utilizzato per la costruzione delle
chiavi
 :  : FLD T$V5DO __Scol/Coll. automatico__
Impostando tale flag verranno attivate le azioni di scollegamento/collegamento automatiche previste dallo standard (es.collegamento magazzino e qualità), senza che questi debbanno essere gestiti nelle tabelle dei flussi. In questo caso i suddetti flussi, se precedentemente attivi, dovranno essere ASSOLUTAMENTE dismessi per la parte che riguarda lo standard. Questo in modo da evitare che i collegamenti lanciati dai flussi e quelli del pgm standard si sovrappongano.
 :  : FLD T$V5DW __Log collegamento__
Permette di ridurre i log emessi in caso di presenza di errori nella fase di collegamento del
documento. E' possibile utilizzare i seguenti valori : 
' ' = Emissione log standard
'A' = Non viene generato il log in caso di testata già collegata
 :  : FLD T$V5DU __Suff.Parz.Lista__
Il campo rappresenta il suffisso dei programmi V5DO01L_x,V5DO05L_x e V5D007A_x  (dove x = al contenuto del campo della
tabella).
Valorizzando il campo si abilita il lancio dei programmi in oggetto che consentono di effettuare parzializzazioni
specifiche nella lista delle testate (V5DO01L_x) e delle righe (V5DO05L_x) e impostare £PRZQS specifica nello stampatore
(V5DO07A).
I programmi sono gestiti con lo stesso suffisso e possono essere attivati singolarmente.
 :  : FLD T$V5DQ __Abilita Storicizzazione Numeri__
Se abilitata la gestione della Storicizzazione dei Numeri, Tabella B£7, indica se questo documento deve essere
storicizzato.
 :  : FLD T$V5D$   Blocco Documenti
La gestione del blocco logico dei documenti in manutenzione viene gestita dalla tabella V51 con un campo specifico
(rimandiamo alla documentazione di quest'ultimo per un dettaglio maggiore.
In questa tabella è possibile effetuare delle eccezione per singolo tipo documento, e questo campo può assumere i
seguenti valori : 
' '   Lasciando il campo in bianco l'attivazione del blocco logico sul tipo documento in manutenzione è delegata alla
      scelta fatta nella tabella V51
'1'   Inserendo 1 al tipo documento viene ATTIVATA la gestione del blocco indipendentemente dalla scelta fatta in V51
'2'   Inserendo 2 al tipo documento viene DISATTIVATA la gestione del blocco indipendentemente dalla scelta fatta in V51
 :  : FLD T1V5DC   Natura Documento
Caratterizza i documenti di questo tipo.
E'un campo necessario per le interrogazioni di Loocup
 :  : FLD T1V5DB   Att.Scen.
Attiva o disattiva la gestione dello scenario nel documento
Il campo può assumere i valori di : 
1 = Attivazione scenario per questo tipo documento
2 = Disattivazione scenario per questo tipo documento
  = La gestione dello scenario è delegata al campo presente in tabella V51
Per una maggiore documentazione riferirsi alla PTF V521213A
 :  : FLD T1V5DD   Exit generale controlli Testata
Il campo definisce il suffisso del programma V5DO01D_x. Se attivato e presente viene richiamato
come exit generale per i controlli su tutti i visualizzatori di testata del tipo documento.
In questa exit è possibile inserire i controlli comuni a tutti i visualizzatori.
Riferirsi al prototipo della exit V5DO01D_X presente in V5SRC, per l'implementazione e la
relativa documentazione.
 :  : FLD T1V5DE   Exit generale controlli Riga
Il campo definisce il suffisso del programma V5DO05D_x. Se attivato e presente viene richiamato
come exit generale per i controlli su tutti i visualizzatori di riga del tipo documento.
In questa exit è possibile inserire i controlli comuni a tutti i visualizzatori.
Riferirsi al prototipo della exit V5DO05D_X presente in V5SRC, per l'implementazione e la
relativa documentazione.
