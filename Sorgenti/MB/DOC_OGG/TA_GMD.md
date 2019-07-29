# GMD - Tipo collo
## OBIETTIVO
Impostare le caratteristiche comuni ai colli di uno stesso tipo.
## CONTENUTO DEI CAMPI
 :  : FLD T$TIFL __Fisico/Logico__

 :  : FLD T$TED1 __Tipo ente documento 1__
È un elemento della tabella BRE, che tipizza l'ente 1
 :  : FLD T$TEO1 __Obbligatorio__
Se impostato, l'ente 1 è obbligatorio.
 :  : FLD T$TDD1 __Tipo documento 1__
È un elemento della tabella V5D, che tipizza il documento 1
 :  : FLD T$TDO1 __Obbligatorio__
Se impostato, il documento 1 è obbligatorio.
 :  : FLD T$TED2 __Tipo ente documento 2__
È un elemento della tabella BRE, che tipizza l'ente 2
 :  : FLD T$TEO2 __Obbligatorio__
Se impostato, l'ente 2 è obbligatorio.
 :  : FLD T$TDD2 __Tipo documento 2__
È un elemento della tabella V5D, che tipizza il documento 2
 :  : FLD T$TDO2 __Obbligatorio__
Se impostato, il documento 2 è obbligatorio.
 :  : FLD T$GMDA __Giacenza in GMQUAN__
Se impostato, la quantità del collo è nell'archivio giacenze di magazzino. In esso sono contenute le informazioni ulteriori del collo (lotto/ubicazione, ecc...).
Se non impostato, la quantità del collo e le sue ulteriori informazioni (lotto/ubicazione,  ecc...) son contenute in un archivio parallelo, di struttura simile all'archivio giacenze, ma non in linea nell'applicazione di magazzino :  a magazzino si ha la quantità globale e nell'archivio parallelo la quantità per collo. Questa suddivisione ha lo scopo di 'alleggerire' la gestione di magazzino, nel caso in cui si sia in presenza di colli che non vengono trattati come elementi di base per la movimentazione interna, ma solo nelle attività di spedizione.
Questo campo è significativo _5_SOLO  nel caso in cui non venga utilizzato il gruppo flag (T$GMDL). In tal caso, infatti, verrà utilizzato il valore del flag 1 definito nella tabella B£Y.
 :  : FLD T$GMDB __Unità movim. assunta__
È un elemento della tabella GMB, e definisce l'unità di movimentazione per colli di questo tipo. In  essa sono contenute le caratteristiche dimensionali, di peso e di relazione.
 :  : FLD T$GMDC __Stato nascita__
È un elemento della tabella B£WCN e rappresenta, se impostato, lo stato assegnato al collo in fase di creazione
 :  : FLD T$GMDD __Area__

 :  : FLD T$GMDE __Tipo giacenza assunta__

 :  : FLD T$GMDF __Categoria parametri__
È un elemento della tabella C£E che definisce i parametri esterni collegabili al collo.
 :  : FLD T$GMDG __Livello di nascita__
Se, in inserimento del collo, non viene specificato uno stato, viene assunto questo livello, con il suo stato principale.
Nel caso di inserimento da packing list, viene assunto in modo automatico.
 :  : FLD T$GMDH __Contenitore Note__
È un elemento della tabella NSC. Se impostato, è il contenitore delle note relative ai colli di questo tipo .
 :  : FLD T$GMDI __Parametri interni__
È un elemento della tabella C£I che definisce i parametri interni collegabili al collo.
 :  : FLD T$GMDL __Gruppo flag__
È un elemento della tabella B£Y. Se valorizzato vengono assegnati i flag di questo elemento in fase di creazione del collo.
Se questo campo è valorizzato i valori definiti nella tabella B£Y per i flag 01 e 02 hanno priorità sugli eventuali valori specificati in questa tabella nei campi T$GMDA (Giacenza in GMQUAN) e T$GMDO (Tipo date implicite).
 :  : FLD T$GMDK __Suff.controllo campi__
È il suffisso del pgm GMCZ01C_x :  permette di modificare la tipologia degli oggetti dei campi presenti nel tracciato (vedi GMCZ01C_A).
 :  : FLD T$GMDJ __Forma presentazione__
È un elemento della tabella B£QCZ in cui si indica il programma di visualizzazione/gestione, utilizzato per i colli di questo tipo. Qualora questo campo non fosse compilato, verrà utilizzato per default il visualizzatore in formato completo (GMCZ01D_$C).
 :  : FLD T$GMDO __Tipo date implicite__
Indica il prefisso degli elementi della tabella C£JCZ che guidano la gestione delle 5 date implicite.
Questo campo è significativo _5_SOLO nel caso in cui non venga utilizzato il gruppo flag (T$GMDL). In tal caso, infatti, verrà utilizzato il valore del flag 2 definito nella tabella B£Y.
 :  : FLD T$GMDM __Numeratore colli__
È un elemento della tabella CRNGM.
È il numeratore che verrà utilizzato per la creazione dei colli di questo tipo.
Qualora non fosse specificato, verrà utilizzato il numeratore colli generale, presente nella tabella GM1.
Nel caso in cui il numeratore non venga specificato neanche nella tabella GM1, verrà utilizzato per default il numeratore NCOL (che dovrà essere obbligatoriamente definito nella tabella CRNGM).
 :  : FLD T$GMDN __Domande per costruzione codice__
È un elemento della tabella B£F e rappresenta il flusso di domande che sovrintende alla costruzione del codice (ed eventualmente alle altre caratteristiche) di un collo di questo tipo.
