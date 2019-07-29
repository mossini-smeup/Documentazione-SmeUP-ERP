# Obiettivo
Consultazione ed interazione con il nuovo framework Sme.UP Gateway.
In questa breve dosumentazione riprendiamo brevemente quello che più ampiamente è stato descritto nel documento "Il framework Sme.UP Gateway" consultabile nella sezione Cartella.

# Cos' è Sme.UP Gateway
E' il nuovo framework di gestione dei plugins A37/A38, basato su tecnologie web e basato su una serie di microservices.

# Come funziona
La struttura del framework SG è basata su una serie di microservices.
A livello implementativo, un microservice è una applicazione web da installare all'interno di un Application Server compatibile J2EE (si consiglia Payara ma va bene qualsiasi prodotto alternativo come Glassfish, JBoss, ecc ecc).

## Comunicazione
In questa sezione andremo a specificare in dettaglio le modalità di comunicazione
tra i microservices all'interno del framework SG. Il contenuto di questa sezione è
abbastanza tecnico e può essere tralasciato in una prima lettura del documento
senza che la cosa si ripercuota sulla comprensione dei paragrafi successivi.
I punti salienti del meccanismo di comunicazione sono i seguenti : 
* La comunicazione tra i singoli microservice si basa su chiamate REST su protocollo HTTP (righe rosse nella figura successiva)
* La comunicazione si basa sullo scambio di messaggi contenenti una serie di informazioni predefinite : 
** Chi ha originato il messaggio
** Una chiave di routing che permette ad eventuali ascoltatori di identificare il messaggio
** Un campo payload che trasporta le informazioni
* Il meccanismo di comunicazione di basa su un pattern di tipo observer. Il messaggio di suo non ha un destinatario predefinito ma è marcato con una chiave di routing. Le entità interessate alla ricezione dei messaggi si registrano sul sistema come ascoltatori dichiarando la tipologia di messaggi a cui sono interessate. Con questo meccanismo lo stesso messaggio può essere ricevuto contemporaneamente da più osservatori.

## I microservice base del framework SG
Come già detto in precedenza, per poter funzionare correttamente, il framework SG richiede che siano attivi una serie di microservizi di base. In questo paragrafo riprendiamo la figura già vista in precedenza e andiamo ora a descrivere in dettaglio i singoli microservice che compongono il framework, spiegando brevemente la loro funzione : 

**1. gtw-hub** (livello 1) :  è il cuore del framework SG e il motore che consente il funzionamento del sistema. Questo microservice ha varie funzioni : 
* Mantiene il registro dei microservices attivi sul framework;
* Si occupa dell'instradamento dei messaggi scambiati tra i microservices su canale HTTP. Come già visto, il motore di instradamento utilizza per il suo funzionamento i channel di RabbitMQ;
* Implementa i servizi di interrogazione sullo stato del sistema;
**2. gtw-logger** (livello 2) :  fornisce un servizio di log centralizzato. Tutti i microservices attivi nel framework utilizzano questo servizio per generare log di tipo informativo e di segnalazione degli errori. I file di log prodotti sono
salvato in una directory specifica e sono diversificati in funzione del microservice a cui si riferiscono. Alcuni microservice possono generare più file di log.

**3. gtw-config-manager** (livello 2) :  fornisce il servizio di lettura della configurazioni destinate agli altri microservices. Tutti i microservice del livello 3 leggono le loro configurazioni di avvio da AS400 utilizzando questo servizio.

**4. gtw-resources-manager** (livello 2) :  fornisce il servizio di upload delle risorse all'interno del sistema.

**5. gtw-smeup-adapter** (livello 2) :  fornisce al framework tutti i servizi legati alla integrazione con il gestionale Sme.UP. La comunicazione con il gestionale si attesta su richieste di funzione F() e risposte in formato XML di vario tipo.
Questo microservice non fornisce di suo alcun servizio gestionale ma fa da interfaccia tra protocolli SG e protocolli Sme.UP. Da notare che questo servizio non è legato all'AS400 ma può fare da ponte di comunicazione verso qualsiasi server in grado di implementare il protocollo di comunicazione Sme.UP.

**6. gtw-as400-adapter** (livello 2) :  microservice che gestisce la comunicazione verso il sistema AS400 su cui è installato il gestionale Sme.UP. Viene utilizzato dal microservice gtw-smeup-adapter come canale di comunicazione verso il mondo AS400, quando necessario. Il servizio mantiene un pool di connessioni verso AS400.

**7. gtw-as400-listener** (livello 2) :  microservice che raccoglie le richieste di funzione F() provenienti dal gestionale Sme.UP su AS400 e le convoglia al servizio gtw-smeup-adapter. Grazie a questo servizio, il sistema SG si può registrare sul gestionale Sme.Up come se fosse uno Smeup Provider e fornire pertanto la stessa interfaccia di accesso alle funzioni (K10)

**8. gtw-deployer** (livello 2) :  microservice che si occupa della creazione e della installazione di microservices A37 e A38, leggendo le configurazioni da script AS400 e lanciando gli script Maven necessari al build e al deploy nel sistema.

**9. gtw-A37-dispatcher** (livello 2) :  gestisce la scrittura di eventi A37 verso AS400 utilizzando un pool di connessioni specifico. Viene invocato direttamente dai microservices A37 quando devono inviare eventi verso AS400. La comunicazione verso AS400 è prevalentemente monodirezionale, visto che non sono previste risposte.

**10. gtw-service-a37-XX-YYY** (livello 3) :  microservices multipli che interfacciano un dispositivo esterno attraverso un plugin IOTSPI di tipo A37

**11.gtw-service-a38-XX-YYY** (livello 3) :  microservices multipli che interfacciano un web service esterno attraverso un plugin WSCSPI di tipo A38

**12.gtw-smeup-ws** (livello 3) :  microservice singolo che pubblica Web Service di tipo gestionale legati a Sme.UP.
