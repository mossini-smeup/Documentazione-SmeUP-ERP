# Obiettivo
Questo pgm permette la generazione del file per la trasmissione telematica dei dati relativi alle dichiarazioni d'intento emesse e la stampa del modello ministeriale.

# Formato di lancio
![Fig_007](http://localhost:3000/immagini/MBDOC_OGG-P_BRIN05/Fig_007.png)Nella videata impostare : 
 * Data emissione :  mettere il range di date con cui sono state emesse le dichiarazioni che si vuole trasmettere. Se ad esempio sono state emesse tra il 17/12/XX e il 31/12/XX compilare con questi due valori il primo e il secondo riquadro rispettivamente
 * Tipo trasmissione :  lasciare il campo vuoto per la trasmissione normale e compilarlo con 1 per effettuare una trasmissione integrativa (è possibile farlo solo se il fornitore non ha ancora emesso fatture riferite alla dichiarazione di intento che si sta trasmettendo)
* Parzializzazioni :  permette di parzializzare per fornitore, protocollo, ecc
* Trasferimento :  permette di impostare il percorso di salvataggio del file. Cliccando sul pulsante evidenziato in rosso è possibile impostare oltre al percorso di salvataggio il tipo di trasmissione (si consiglia di utilizzare il 5) e il nome del file.
* Dati rappresentante :  in questi campi vanno inseriti i riferimenti del fornitore/cliente con cui è codificato il rappresentante legale dell'azienda. Nel Codice carica andrà inserito 01 per indicare che il soggetto è il rappresentante legale.
* Plafond :  di default è impostato fisso, se il plafond aziendale è mobile compilare il campo con 2
* Dichiarazione presentata :  se è già stata presentata la dichiarazione IVA annuale per l'anno a cui il plafond è riferito andrà compilato questo campo con 1 e lasciati vuoti i campi a destra. In caso contrario il campo andrà lasciato vuoto e compilati uno o più dei campi a destra in funzione di come il plafond si è formato
 * Esportazioni :  compilare il campo con 1 se il plafond è stato composto anche con operazioni di questo tipo
 * Cessioni CEE :  compilare il campo con 1 se il plafond è stato composto anche con operazioni di questo tipo
 * Cessioni SM :  compilare il campo con 1 se il plafond è stato composto anche con operazioni di questo tipo
 * Assimilate :  compilare il campo con 1 se il plafond è stato composto anche con operazioni di questo tipo
 * Straordinarie :  compilare il campo con 1 se il plafond è stato composto anche con operazioni di questo tipo
 * Dati intermediario :  questi campi vanno inseriti solo le l'invio del file viene effettuato da un intermediario per conto dell'azienda (ad esempio se il file verrà trasmesso dal commercialista). In questo caso inserire i riferimenti del fornitore con cui è codificato l'intermediario e la data in cui si è impegnato a trasmettere i dati.
 * Dati fornitore (Responsabile trasmissione) :  va indicato il soggetto responsabile dell'invio telematico. In questi campi va identificato il soggetto su cui è registrata la firma digitale del software Entratel con cui verranno inviati i dati. Di conseguenza, nel caso in cui la comunicazione venga fatta dall'azienda stessa il campo andrà lasciato vuoto (verranno presi i riferimenti del rappresentante legale) mentre nel caso in cui la comunicazione venga inviata da un intermediario andrà indicato in questo campo il suo codice fornitore.
 * Tipo fornitore :  va indicata la tipologia di fornitore (assume 01 se non è indicata)
 * Stampa modelli :  impostare questo campo con 1 se si vuole ottenere la stampa del modello predisposto dall'Agenzia delle Entrate

Confermando la funzione con F06 verranno prodotti : 
 * Una stampa di controllo chiamata DIE_CTR in cui sono riportati tutti i dati della dichiarazione
 * Se si è impostato il campo _Stampa modelli_ : 
 ** La stampa della dichiarazione (che andrà consegnata al fornitore)
 ** La stampa del quadro A del modello ufficiale (che non è necessario consegnare al fornitore)
 * Se si è impostato il percorso nella _Trasmissione_ verrà creato all'interno della cartella impostata il file da inviare tramite Entratel (o al commercialista)
 * Nel caso in cui ci siano errori (es. mancanza di partita iva o altri dati obbligatori) viene prodotta una stampa con gli errori rilevati


