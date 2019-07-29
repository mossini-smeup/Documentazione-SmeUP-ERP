
# Obiettivo

Stampare e trasmettere i dati relativi alle certificazioni uniche.

# Segnalazioni e controlli

La stampa produce una stampa di log attraverso cui è possibile controllare i dati di dettaglio ed anche i totali.

_2_NOTA BENE :  non vengono controllati eventuali errori/segnalazioni rilevate da Sme.Up. Tali segnalazioni (che cmq non includono tutte le segnalazioni previste dall'agenzia delle entrate) sono verificabili tramite il lancio della "Stampa di controllo" delle certificazioni. E' quindi consigliabile eseguire sempre una stampa di controllo prima dell'esecuzione in definitiva.

# Trasmissione Parziale

Se si ha intenzione di sfruttare l'opportunità di inviare i dati separatamente per i soggetti con obbligo di trasmissione entro marzo e quelli con obbligo di trasmissione entro la scadenza del 770, si consiglia di operare filtrando in estrazione per i soli soggetti interessati alla scadenza di marzo (uno per uno) e solo per la seconda scadenza lanciare l'estrazione globale.

# Parametri di esecuzione

* **Anno** :  anno di riferimento dei dati da trasmettere

* **Tipo Modello** :  sintetico o ordinario a seconda della tipologia che si vuole inviare

* **Stampa modelli** :  l'elaborazione produrra sempre una stampa di log che riproduce i dati elaborati, con questa opzione è però possibile decidere di produrre in formato pdf o spool, anche i modelli ministeriali. NOTA BENE :  in formato pdf, verranno prodotti tanti file quanti sono i codici fiscali, più quello del frontespizio. Mentre in formato spool verranno prodotti 3 soli file :  uno per il frontespizio, uno con tutti i dati anagrafici dei soggetti ed uno con tutte le somme percepite. In quest'ultimo caso sarà quindi necessario poi riaccopiare manualmente le stampe dei dati anagrafici con le corrispondenti stampe relative alle somme.

* **Cartella/File da trasmettere** :  mettendo un carattere qualsiasi nel campo, sarà possibile accedere alla maschera in cui poter indicare il nome da attribuire al file da trasmettere all'agenzia delle entrate, e la cartella in cui porlo. NOTA BENE :  in tale cartella verranno posti anche gli eventuali pdf dei modelli.

* **Dettaglio stampa log** :  indica che campi stampare nella stampa log. Di default vengono stampati solo i dati valorizzati o quelli con segnalazioni, ma è anche possibile stampare lo schema completo  dei campi.

* **Tipologia invio** :  determina che dati vengono elaborati :  da trasmettere per la prima volta, da annullare, da sostituire. Tali dati vengono riconosciuti a seconda della valorizzazione del campo "Stato" presente sul record delle somme del percipiente.
Ad eccezione della trasmissione normale per tutte le altre tipologie di invio oltre allo stato dovranno essere indicati anche il protocollo telematico e del documento attribuiti dall'agenzia delle entrate in fase di trasmissione. Questi gli stati che sono previsti : 
** Stato bianco indica che il dato è ancora da trasmettere
** Stato DSO è da sostituire
** Stato DAN è da annullare
** Stato NNN viene esclusa dalla trasmissione

* **Modalità** :  indica se l'elaborazione è provvisoria, definitiva o si vuole annullare una definitiva.
** In definitiva sui dati verranno aggiornati due campi : 
***  Lo data di trasmissione (assume data odierna)
***  Lo stato, che passa a TRA (trasmessa) o ANN (annullata), a seconda che la tipologia invio sia normale/sostitutiva o annullamento.
** In annullamento di una definitiva, verrà chiesta la data da annullare, sulla base della quale verranno filtrati i dati da elaborare e verrà cambiato lo stato, che a seconda della tipologia di invio verrà riportato al valore precedente all'esecuzione definitiva.

* **Solo certificazioni con competenza anno precedente** :  se valorizzato verranno elaborati solo i dati per i quali è presente questa informazione, al fine di poter produrre una certificazione separata per questi dati, da inviare ai percipienti. Si veda anche la documentazione relativa all'estrazione.

* **Dati Responsabile Trasmissione** :  va indicato il soggetto che si occupa della trasmissione (se non va indicata l'azienda stessa)

