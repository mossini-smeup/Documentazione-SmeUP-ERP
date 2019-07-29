# WFA - Processi workflow
 :  : DEC T(ST) K(WFA)
## OBIETTIVI
Caratterizzare i processi di workflow definiti.
## SOTTOSETTORI
Non gestiti
## INTRODUZIONE
In questa tabella vengono specificate le impostazioni generali di processo, che caratterizzeranno
globalmente i singoli ordini di workflow. Le impostazioni locali vengono invece fornite nello
script, transizione per transizione.
## CONTENUTO DEI CAMPI
 :  : FLD T$WFAA Iniz. ordini
 :  : FLD T$WFAB Tipo oggetto master
Definisce il tipo dell'oggetto a cui è associato l'ordine di workflow.
Per gli oggetti con parametro obbligatorio è sensibile al parametro, altrimenti no.
 :  : FLD T$WFAC Tipo oggetto owner
Definisce il tipo dell'oggetto responsabile dell'ordine di workflow.
Per ora è sempre TAB£U.
 :  : FLD T$WFAD Tipo impegno dft
Definisce il tipo di impegno default con cui nascono gli impegni del workflow a meno di
ridefinizioni sulle transizioni.
 :  : FLD T$WFAE
Se valorizzato a '1' definisce un processo come revisione di un processo già esistente (processo iniziale).
Il processo iniziale è, per convenzione, lo stesso processo a meno dei due caratteri finali di revisione.
Ad esempio :  PROCESSO01 è la revisione di PROCESSO.
 :  : FLD T$WFAF Iniz. attività
Definisce l'elemento della WFW letto per inizializzare le attività su questo workflow.
 :  : FLD T$WFAG Gruppo processo
Forza uno script per questo processo. In questo modo è possibile avere diversi processi che condividono lo stesso script.
**N.B. :  E' utilizzato solo se non esiste uno script il cui nome corrisponde a quello** **dell'elemento di WFA.**
 :  : FLD T$WFAH Tipo risorsa calen.
 :  : FLD T$WFAI Cod. risorsa calen.
 :  : FLD T$WFAJ Associazione oggetto
Definisce se aggiungere agli oggetti di tipo 'master' un'azione di popup per aprire workflow di
questo tipo. Valori ammessi : 
' ' :  è un workflow di oggetto per tutti gli oggetti di questo tipo/parametro.
'1' :  è un workflow di oggetto per tutti gli oggetti di questo tipo e parametro qualsiasi.
'2' :  è un workflow di oggetto per tutti gli oggetti.
Si noti che per oggetti con parametro non obbligatorio (es. articoli) questo flag non è discriminante :  il parametro non viene valutato.
 :  : FLD T$WFAK Lead time totale
Si può impostare il lead time totale che verrà applicato, negli ordini di questo processo, per
calcolare la data di fine richiesta a partire dall'istante di inserimento.
Se non impostato, si assume la data fine richiesta uguale alla data di inserimento.
Questo valore è espresso in ore e decimillesimi di ora (oggetto istante (I2) di tipo 2).
 :  : FLD T$WFAL Livello lock
Si imposta il livello di lock a cui verranno sottoposti gli ordini di questo processo.
Default :  a livello di ordine, ovvero mentre sto dichiarando un'impegno di un ordine non posso
contemporaneamente dichiararne un altro oppure cambiare lo stato dell'ordine.
 :  : FLD T$WFAM Sottosettore stati
Imposta il sottosettore di WFS in cui definire stati logici particolari da utilizzare nello
svolgimento degli ordini. E' utile nel caso in cui il workflow non sia relativo ad un oggetto
master specifico; in caso contrario spesso si utilizza lo stato dell'oggetto.
 :  : FLD T$WFAN Disabilita gestione
Se impostato indica che nel pop.up dell'oggetto master vengono disabilitate le azioni di gestione
"normali", perchè la gestione viene effettuata da questo (ed eventualmente altri) workflow.
Ad esempio sugli articoli verrebbero disabilitate le chiamate dirette al BRAR01D perchè le
azioni di gestione sarebbero eseguite da impegni di workflow.
Nota bene :  attivando questo flag si disabilita la gestibilità degli stati da parte dell'utente,
in quanto gli stati vengono gestiti automaticamente dal workflow.
 :  : FLD T$WFAO Punto di creazione
Indica da dove viene lanciata la creazione di ordini di questo processo. Valori ammessi : 
' ' :  dalle schede standard di inserimento ordini, per workflow che non nascono a partire da
un'istanza di oggetto.
'1' :  dal pop.up di quello che diventa l'oggetto master del workflow.
'2' :  gestito da utente, ad esempio da schede specifiche in cui vengono richiesti più parametri
prima della creazione, oppure creato come sottoworkflow di altri ordini, oppure ancora dai flussi
di un oggetto.
 :  : FLD T$WFAP Modo creazione
Indica cosa lanciare come azione di creazione di un ordine di workflow. Valori ammessi : 
' ' :  la scheda dell'ordine da creare, in cui tramite bottone viene eseguita la creazione e da cui
si possono iniziare ad eseguire gli impegni.
'1' :  creazione cieca con DMSG di avviso effettuata creazione.
'2' :  creazione con esecuzione diretta degli impegni attivi.
'3' :  come '2', ma solo se il tutto avviene in Looc.up (old).
'4' :  creazione cieca.
'5' :  come '2', non torna messaggio se nessun impegno eseguito.
 :  : FLD T$WFAQ Max.ord.att.x ogg.
Se valorizzato indica quanti ordini di questo tipo possono essere contemporaneamente attivi sullo
stesso oggetto master.
Per ora viene controllato solo nei pop.up.
 :  : FLD T$WFAR Azione di gestione
Da valorizzare se la creazione di un ordine di questo tipo è un'azione di gestione sull'oggetto
master.
