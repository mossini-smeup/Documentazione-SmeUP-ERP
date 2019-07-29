# Generalità

Gli strumenti a disposizione per lo sviluppo di applicazioni in ambiente mobile  coincidono con gli strumenti a disposizione per lo sviluppo dell'applicazione gestionale sul client loocup (script di scheda, matrici, alberi, input panel ecc.), con specifiche limitazioni/particolarità tipiche del device mobile. Per chi ha quindi conoscenza degli strumenti a disposizione per lo sviluppo delle applicazioni sul client loocup, le principali nozioni consistono proprio nelle specificità tipiche del device mobile.

# Attivare l'Applicazione

Di seguito i passi da seguire per l'attivazione.

* Se si è ad una versione < della V4R1, riprendere dalla V4R1 la routine RLISMVA del pgm LOSER_05 e riportare la routine (e la sua chiamata) nella propria versione in linea.
Questo perche il collegamento tramite GlassFish necessita della routine per avere le informazioni iniziali (tra cui la scheda iniziale da caricare).
* Definire l'ambiente che si vorrà utilizzare per l'accesso mobile.
* Definire la funzione (scheda) che verrà utilzzata per l'accesso. Tale funzione è identificata attraverso la variabile di SCP_CLO *SMobile : 
** Dalla 4.1 nello script SCP_CLO DEFAULT è già predisposta come funzione di avvio, il lancio della scheda del menù indicato nell'UP UT5.
** Su una release precedente si consiglia di prevedere semplicemente il lancio di una scheda presenti una semplice funzione da cui avviare la navigazione (es. un albero scelta delle funzioni).
* Si consiglia di impostare a questo punto l'ambiente di test sul proprio utente o cmq su tutti gli utenti che dovranno poi gestire gli sviluppi :  su un ambiente di test, in una 4.1 è importante che sia attiva nell'SCP_CLO la variabile "*Sim_Dv" che valorizzata P/D permette di accedere a loocup simulando il corrispondente device. Inoltre per questo ambiente se è stata prevista una funzione *SMobile specifica, tale funzione dovrà essere impostata come *SFunction.
* Coadiuvato da un esperto in materia attivare su un server web un webservice dedicato.
* A questo punto (dopo che è già stata scaricata l'app), andare nelle impostazioni ed indicare il corretto server web.
* Effettuare infine il login al sistema con le proprie normali credenziali di accesso.

# Verifica della Connessione con il Webservice

Per verificare i parametri di accesso che il suddetto Web Service utilizza per effettuare la connessione al sistema AS400, aprire una finestra di browser web ed inserire l'URL.

Si aprirà una maschera del tutto simile alla seguente : 

![TEC038](http://localhost:3000/immagini/MOBASE_03/TEC038.png)
Selezionare quindi il tasto "Connection Data"

![TEC039](http://localhost:3000/immagini/MOBASE_03/TEC039.png)
Nella maschera, verranno visualizzate tutte le informazioni relative alla connessione.

Da tramite la suddetta pagina è inoltre possibile attraverso il pannello "Xml Smeup", verificare la risposta del webservice rispetto a qualisiasi funzione F lanciata sul server.
Inoltre contenando quello scrive nella prima riga di risposta, all'indirizzo della pagina è posso richiamare una url che risponde direttamente l'xml di risposta a quella particolare funzione.

# Riconoscere il device

Come verrà ripetuto più volte, gli strumenti di sviluppo per l'applicazione mobile, sono del tutto simili a quelli del client loocup, ma con alcune sostanziali specificità.

A causa di tali specificità può sorgere l'esigenza a livello di script o di programma di conoscere il tipo di device in utilizzo, al fine di applicare differenti considerazioni. A livello strutturale l'informazione di base, viene passato attraverso il parametro **"DV"** all'interno della variabile £UIBSS disponibile in qualsiasi servizio. Tale parametro è presente attualmente solo per i device mobile e può essere valorizzato a "P" o "T" a seconda che il device sia Phone o Tablet.

A partire dalla 4.1 il valore di tale variabile può essere identificata nei seguienti modi : 
* Negli script, attraverso la variabile di ambiente _&_AM.DV
* Nei programmi, attraverso il richiamo della /COPY £J18
Entrambe, funzionano anche su altri device (es. client loocup), e forniscono come risultato un'istanza dell'oggeto sme.up V2B£CDV.

Per versioni precedenti si forniscono in merito a questo le seguenti indicazioni : 
* Per gli script, di utilizzare tendenzialmente sempre script specifici, in modo da non aver l'esigenza di testare il device
* Per i programmi, se sono servizi, estrapolando il succitato parametro "DV" dalla variabile £UIBSS. Se si ha invece l'esigenza di utilizzare tale informazione in programmi richiamati dal servizio, si consiglia di utilizzare una delle seguenti possibili alternative : 
** passare l'informazione dal servizio, al programma specifico direttamente nell'entry
** sfruttare la £G00 per salvare l'informazione nel servizio e rileggerla nel pgm specifico
** utilizzare una tecnica simile a quella della £J18 (si veda pgm JAJAS1) in cui il servizio, dopo aver estrapolato l'informazione della £UIBSS chiami un pgm x, con chiusura RT e se necessario gruppo di attivazione specifico, in cui come variabile di pgm viene salvato il codice del device, in modo che poi altri pgm possano richiamare il pgm x per farsi restituire il valore memorizzato.

NOTA BENE :  se lo stesso webservice viene utilizzato sia da device tablet che phone, lo stesso job, potrebbe essere richiamato a volte con un device, a volte con l'altro. Per lo stesso motivo uno degli attributi ritornati dalla succitata /COPY £J18, indica se il device è fisso per il job o se può invece cambiare.

 :  : DEC T(OG) K(V2B£CDV) L(1)

# Sviluppo e Testing

Per lo sviluppo è consigliato di sfruttare il più possibile, l'ambiente di test :  come citato in precedenza, se sull'ambiente di test viene attivata la variabile di SCP_CLO, valorizzata a "P" o "T" è possibile avviare il client loocup, in modalità "simulazione". Qualora ci si trovi ad una release precedente viene consigliato di sfruttare qualche meccanismo al fine di poter cmq ottenere l'effetto di simulazione sul client loocup (es. testando il nome dell'ambiente o dell'utente se ne viene utilizzato uno specifico).

Questo perchè l'ambiente loocup fornisce una serie di vantaggi per controllare lo sviluppo : 
* ricarica ambiente
* visualizza xml su sezione

Tutte funzionalità assenti sui device mobile. Viceversa è vero che non permette di identificare in modo immediato la presenza di funzionalità grafiche che possono inficiare se non inibire l'esecuzione della funzione sul device mobile. Il consiglio operativo è quindi il seguente : 
* Sviluppare il più possibile attraverso il client loocup (cercando di acquisire nel frattempo la nozione di cosa è possibile o non possibile fare sul device mobile)
* Solo quando sul client si è ottenuto il risultato voluto, verificare il risultato direttamente sul device.
* Tutti gli sviluppi farli in un ambiente di test e solo una volta che tutto è stato verificato rilasciare le funzionalità sull'ambiente reale.

