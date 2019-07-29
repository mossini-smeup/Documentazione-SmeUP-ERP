Qui sotto elenchiamo alcune caratteristiche della nuova routine : 

- il mittente può essere impostato (anche un nome inventato) ed assume l'indirizzo del utente che invia la mail (in questo caso è, in maniera fissa, l'oav J/I01 dell'oggetto TA B£U), immettendo la
costante '*BLANKS' assume l'indirizzo di default della £G53
- La lista di distribuzione può essere sostituita da un indirizzo singolo specificato nei parametri
- L'oggetto ed il testo possono essere passati esplicitamente oppure possono essere creati dei messaggi standard, utilizzando la gestione messaggi con tipo contenitore £98.
-- il tipo contenitore £98 (creato in automatico dal TSTG98) è costituito dal 1) codice messaggio (tabella B£*TE), 2) Tipo messaggio (nuovo oggetto V2B£G98), 3) Lingua (che può essere passata ed assume la ££B£2F)
-- Per la gestione del testo e oggetto variabile è possibile utilizzare dei campi della DS per passare delle variabili, sono stati creati i campi : 
--- £G9801 (articolo) da utilizzare nel testo/oggetto con la sigla _&_A
--- £G9802 (Ordine/Oggetto) da utilizzare nel testo/oggetto con la sigla _&_O
--- £G9803 (ente cliente o fornitore) da utilizzare nel testo/oggetto con la sigla _&_E
--- £G9804 (Testo) da utilizzare nel testo/oggetto con la sigla _&_D
       Ovviamente bisogna impostare nella gestione commenti il testo inserendo le sigle (es. _&_A il programma sostituirà automaticamente _&_A con il contenuto del campo £G9801
-- Per il campo Testo è possibile oltre ai precedenti 2 metodi passare un percorso in cui si trova il file (txt o HTML) con il testo (percorso di IFS)
- E' possibile indicare un allegato
- Il programma assume il lancio in coda (che si può specificare) è possibile fare eseguire il pgm anche in interattivo
- E' possibile,in caso di lista con più destinatari, specificare se la mail debba essere una con tutti i destinatari oppure inviare una mail ad ogni destinatario
- per quanto riguarda la creazione della lista di distribuzione si ricorda quando segue : 
- L'elemento della tabella è solo un numeratore progressivo
- l'indirizzo può essere inserito in maniera esplicita nel campo descrizione (es. info@smeup.com) oppure essere l'oav J/I01 se inseriti i campi "T$TCEL Tipo codice" e "T$PCEL Parametro codice"
- In caso venga passato nel campo  T$TCEL il valore 'CN' e nel campo T$PCEL il tipo ente, è possibile inserire nel campo descrizione la scritta _&_BRIxxxxxx dove xxxxxx è il codice elemento della tabella BRI specificato nelle estensioni di tipo £16 dell'ente passato nel campo £G9803 (questa funzione è utile, per esempio nel caso di invio fattura a lista di distribuzione,  se si vogliono indicare oltre ad indirizzi interni più indirizzi legati al cliente ed opzionali).
Nel caso in cui sia attiva la gestione dei referenti (Oggetto RN), al posto del BRESCO0F (£BRI), bisogna invece inserire nello stesso campo descrizione la scritta _&_RNcccpppxxxxxx dove ccc è il codice della categoria del parametro e ppp il codice del parametro che si vuole utilizzare per indicare le liste a cui il referente è inscritto (a standard è prevista la categoria £RN e il Parametro A01) e xxxxxx è invece il codice dell'elemento del parametro specificato in questa stessa stringa e per il quale si vuole filtrare la lista. Ad esempio la lista a cui spedire una fattura potrebbe essere _&_RN£RNA01FATT.
- Si ricorda che è possibile (tramite il campo £G98T3) inserire la forzatura del campo T$PCEL nel caso sia variabile (a parità di lista di distribzione)
- i file contenenti i testi e gli indirizzi vengono creati nella cartella //Smedoc/allegati/testi che il programma (B£G98G) provvede a creare in loro mancanza, tuttavia si consiglia di crearle manualmente per impostarle con le autorizzazioni che si ritengano più opportune.

