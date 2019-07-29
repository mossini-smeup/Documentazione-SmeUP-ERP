## Configurazione Virtual Servers Payara

Qualora fosse necessario l'utilizzo dei Virtual Servers di Payara (ad esempio nel caso di una applicazione web a cui si voglia accedere senza specificare context root...) è necessario eseguire le attività qui di seguito riportate.
Tipicamente questa necessità, la cui soluzione ha carattere sistemistico, viene gestita tramite Apache Webserver.


Accedere alla pagina amministrativa di payara;

Creare un virtual server impostando in Hosts l'indirizzo/nome del server e selezionando il/i listeners (http/https) da utilizzare:
![WEBASE_057](http://localhost:3000/immagini/WEBASE_014/WEBASE_057.png)
Installare (deploy) l'applicazione web selezionando il Virtual Server desiderato (in questo caso quello precedentemente creato) : 
![WEBASE_058](http://localhost:3000/immagini/WEBASE_014/WEBASE_058.png)
Modificare l'istanza del virtual server precedentemente creato, associandogli l'applicazione appena "deployata" selezionandola da "Default Web Module" : 
![WEBASE_059](http://localhost:3000/immagini/WEBASE_014/WEBASE_059.png)
Riavviare il servizio payara;

Pulire la cache del browser (CTRL+F5);

Accedere all'applicazione web senza digitare il contesto : 
![WEBASE_060](http://localhost:3000/immagini/WEBASE_014/WEBASE_060.png)
verificare che si venga ridirezionati nell'applicazione desiderata : 
![WEBASE_061](http://localhost:3000/immagini/WEBASE_014/WEBASE_061.png)
N.B. : la documentazione corrente deriva da documentazione ufficiale reperibile dai siti ufficiali.
