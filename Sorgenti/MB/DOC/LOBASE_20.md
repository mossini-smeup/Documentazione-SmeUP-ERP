# Interfaccia a web service per la comunicazione con l'AT del Portogallo
_Analisi degli strumenti disponibili per la realizzazione del client_
Il documento ha lo scopo di fornire un'analisi degli strumenti a disposizione per l'implementazione del meccanismo di interfaccia fra il sistema Sme.UP ERP e l'Autorità Fiscale e Doganale del Ministero delle Finanze del Portogallo (di seguito denominata AT).
## Strumenti
Il panorama delle soluzioni a disposizione identifica due tecnologie candidate : 
* Client realizzato direttamente su iSeries
* Client SOAP realizzato in linguaggio Java e attivo su Sme.UP Provider
### Client su iSeries
Le soluzioni percorribili da questo punto di vista sono più di una.
Una prevede l'utilizzo del pacchetto HTTPAPI, che sono librerie installabili su iSeries (http://www.scottklement.com/httpapi/) e che permettono l'accesso al protocollo HTTP direttamente da Sme.UP ERP su iSeries.
Un'altra soluzione prevede l'utilizzo di un tool commerciale (IBM Web Services Client for ILE).
### Client SOAP Java
Il linguaggio Java e le JDK attuali mettono a disposizione, attraverso tecnologie della Apache Software Foundation (AXIS, AXIS2 o CXF), strumenti per la realizzazione di client SOAP per la connessione a Web Service. Tale client viene poi attivato su un'installazione Sme.UP Provider presente su server Windows.
## Criticità coinvolte
La soluzione del problema prevede vari elementi da valutare, ed in relazione a quelli capire come i due strumenti sopra riportati li affrontano.
I temi principali sul piatto sono : 
- Prerequisiti di networking
- Prerequisiti di sistema
- Specificità tecniche
-- Protocollo HTTPS
-- Messaggi SOAP.
--- gestione XML
--- standard SOAP
--- aderenza alla definizione rilasciata dal web service di AT
-- Procedure di criptatura dei dati contenuti in parte del messaggio SOAP, tramite chiave simmetrica generata a runtime ad ogni richiesta
-- Procedure di criptatura di dati con chiave pubblica, tramite algoritmo RSA
-- Codifica di dati in Base 64
- Stato di sviluppo del software
- Skill aziendali
-- Capacità di sviluppo
-- Reattività agli inconvenienti

Sulla base di questi punti tecnici vanno confrontate le soluzioni a disposizione quindi, di seguito, le due tecnologie "sul piatto" e, punto per punto, la risposta che danno ai punti di cui sopra.
### Client su iSeries
**Soluzione HTTPAPI**
- Prerequisiti di networking :  L'esecuzione diretta del software su iSeries implica l'assenza di elementi intermedi fra l'iSeries ed il web service. Di conseguenza però, prevede che l'iSeries acceda ad Internet per collegarsi ad un indirizzo pubblico.
- Prerequisiti di sistema :  E' necessario installare alcune opzioni /pacchetti aggiuntivi su iSeries : 
-- Digital Certificate Manager
-- TCP/IP Connectivity Utilities
-- IBM HTTP server for iSeries
-- IBM Crypto Access Provider
-- IBM Developer Kit for Java
- Specificità tecniche
-- Protocollo HTTPS :  E' gestito dal tool in questione
-- Messaggi SOAP : 
--- gestione XML :  HTTPAPI mette a disposizione solo il supporto al protocollo HTTP GET o POST, qualunque infrastruttura a livello di messaggio va implementata e gestita realizzandola "manualmente".
--- standard SOAP :  L'aderenza allo standard SOAP va garantita nel programma da realizzare. Anche in questo caso senza nessuna utility di supporto.
--- aderenza alla definizione rilasciata dal web service di AT :  Ogni specifica della definizione del web service AT va implementata manualmente nel programma realizzato (compresa la gestione degli header del messaggio SOAP)
-- Procedure di criptatura dei dati contenuti in parte del messaggio SOAP, tramite chiave simmetrica generata a runtime ad ogni richiesta :  Nessuna utility di supporto prevista. E' quindi necessario implementare manualmente questa funzionalità (eventualmente appoggiandosi a funzionalità di sistema esistenti o a tool di terze parti). Tutte le soluzioni possibili richiedono studio delle offerte e delle possibilità.
-- Procedure di criptatura di dati con chiave pubblica, tramite algoritmo RSA :  Nessuna utility di supporto prevista. E' quindi necessario implementare manualmente questa funzionalità (eventualmente appoggiandosi a funzionalità di sistema esistenti o a tool di terze parti). Tutte le soluzioni possibili richiedono studio delle offerte e delle possibilità.
-- Codifica di dati in Base 64 :  Nessuna utility di supporto prevista. E' quindi necessario implementare manualmente questa funzionalità (eventualmente appoggiandosi a funzionalità di sistema esistenti o a tool di terze parti). Tutte le soluzioni possibili richiedono studio delle offerte e delle possibilità.
- Stato di sviluppo del software :  E' tutto da implementare
- Skill aziendali :  Poca (pochissima) esperienza in merito all'uso di HTTPAPI. Nessuna esperienza nell'uso di funzionalità di cifratura direttamente su iSeries. Le suddette API sono scritte in C. In caso di problemi non abbiamo nessuna esperienza nel trattare (su iSeries) questi tipi di sorgente **Nota :  Le librerie HTTPAPI vengono distribuite "as is" da Sme UP. La valutazione di utilizzo delle stesse va effettuata di caso in caso. Sia esso un utilizzo nello standard, sia nelle personalizzazioni cliente.
-- Capacità di sviluppo :  I tempi di sviluppo non possono che risentire negativamente di questa mancanza di esperienza e conoscenza.
-- Reattività agli inconvenienti :  Sempre a causa dei motivi di cui sopra non siamo sicuri di poter far fronte in modo immediato ad eventuali problematiche ci si potrebbero presentare

**Soluzione IBM Web Services Client for ILE**
- Prerequisiti di networking :  L'esecuzione diretta del software su iSeries implica l'assenza di elementi intermedi fra l'iSeries ed il web service. Di conseguenza però, prevede che l'iSeries acceda ad Internet per collegarsi ad un indirizzo pubblico.
- Prerequisiti di sistema :  E' da valutare il costo del tool. Inoltre è necessario installare alcune opzioni /pacchetti aggiuntivi su iSeries : 
-- Extended Base Directory Support
-- Host Servers
-- Qshell
-- PASE
-- Digital Certificate Manager 4 (needed only for Web services client)
-- IBM Developer Kit for Java (J2SE 5.0 32 bit)
-- IBM HTTP Server for IBM i
- Specificità tecniche
-- Protocollo HTTPS :  E' gestito dal tool in questione
-- Messaggi SOAP : 
--- gestione XML :  E' insito nella gestione SOAP supportata dal tool in questione
--- standard SOAP :  Il tool in questione gestisce l'aderenza allo standard SOAP in modo automatico.
--- aderenza alla definizione rilasciata dal web service di AT :  E' prevista la generazione automatica di stub a partire dai WSDL forniti. Il tool presenta però alcune limitazioni (ad esempio la versione di standard SOAP). Tali limitazioni andrebbero approfondite per verificare l'effettiva applicabilità. Rappresentano comunque un possibile problema in caso di modifiche future delle specifiche da parte di AT.
-- Procedure di criptatura dei dati contenuti in parte del messaggio SOAP, tramite chiave simmetrica generata a runtime ad ogni richiesta :  Nessuna utility di supporto prevista. E' quindi necessario implementare manualmente questa funzionalità (eventualmente appoggiandosi a funzionalità di sistema esistenti o a tool di terze parti). Tutte le soluzioni possibili richiedono studio delle offerte e delle possibilità.
-- Procedure di criptatura di dati con chiave pubblica, tramite algoritmo RSA :  Nessuna utility di supporto prevista. E' quindi necessario implementare manualmente questa funzionalità (eventualmente appoggiandosi a funzionalità di sistema esistenti o a tool di terze parti). Tutte le soluzioni possibili richiedono studio delle offerte e delle possibilità.
-- Codifica di dati in Base 64 :  Nessuna utility di supporto prevista. E' quindi necessario implementare manualmente questa funzionalità (eventualmente appoggiandosi a funzionalità di sistema esistenti o a tool di terze parti). Tutte le soluzioni possibili richiedono studio delle offerte e delle possibilità.
- Stato di sviluppo del software :  E' tutto da implementare
- Skill aziendali :  Nessuna esperienza in merito all'uso di questo tool. Nessuna esperienza nell'uso di funzionalità di cifratura direttamente su iSeries. Per rispondere ai prerequisiti del web service di AT (nello specifico la modifica dell'header SOAP) è necessario scrivere programmi in C++ di cui non abbiamo esperienza su iSeries.
-- Capacità di sviluppo :  I tempi di sviluppo non possono che risentire negativamente di questa mancanza di esperienza e conoscenza.
-- Reattività agli inconvenienti :  Sempre a causa dei motivi di cui sopra non siamo sicuri di poter far fronte in modo immediato ad eventuali problematiche ci si potrebbero presentare

### Client SOAP Java
- Prerequisiti di networking :  La presenza del Client SOAP su Sme.UP Provider prevede che quest'ultimo acceda ad Internet verso l'indirizzo pubblico del web service AT. Sme.UP ERP, per la sua parte iSeries accede a Sme.UP Provider come client che inoltra una richiesta. Non è richiesto l'accesso diretto da parte di iSeries ad internet.
- Prerequisiti di sistema :  E' necessario un server Windows su cui installare Sme.UP Provider. Si rimanda alla documentazione specifica di Sme.UP Provider per maggiori dettagli sullo stesso.
- Specificità tecniche
-- Protocollo HTTPS :  Il supporto del protocollo HTTPS è gestito nativamente dalla Java Virtual Machine, previa procedura di acquisizione del certificato da eseguire una sola volta, ed in maniera trasparente dall'interfaccia SOAP.
-- Messaggi SOAP : 
--- gestione XML :  l'XML del messaggio SOAP è gestito in maniera trasparente dal client realizzato tramite wsimport.
--- standard SOAP :  Il Java Developer Kit mette nativamente a disposizione una utility (wsimport) per la costruzione automatica del client e delle strutture dati di comunicazione in base alla tecnologia preferita (AXIS, AXIS2, CXF)
--- aderenza alla definizione rilasciata dal web service di AT :  l'utility indicata (wsimport) genera automaticamente il client e le strutture dati di comunicazione sulla base del wsdl pubblicato dal web service di AT. L'accesso agli header è consentito attraverso API java appartenenti al package JAX-WS
-- Procedure di criptatura dei dati contenuti in parte del messaggio SOAP, tramite chiave simmetrica generata a runtime ad ogni richiesta :  Il package Crypto, presente nel Java Developer Kit, mette a disposizione le funzionalità e le API per le generazione delle chiavi simmetriche di criptatura.
-- Procedure di criptatura di dati con chiave pubblica, tramite algoritmo RSA :  I package Crypto e Security, presenti nel Java Developer Kit, mettono a disposizione le funzionalità e le API per la gestione della criptatura RSA
-- Codifica di dati in Base 64 :  Il Java Developer Kit mette a disposizione le funzionalità e le API per la codifica delle stringhe in Base 64, e la codifica mime (Base 64) sono "nascosti" dalle api soap
- Stato di sviluppo del software :  Sme.UP Provider utilizza funzioni e schede per il test e per il debug già sviluppate per esigenze simili. Il client SOAP è già in fase di realizzazione, ed in attesa delle credenziali del ministero necessarie per la validazione della fase di sviluppo e l'inizio della successiva fase di test.  Si rimanda alla documentazione specifica di Sme.UP Provider per maggiori dettagli sullo stesso e sull'interazione con la parte iSeries di Sme.UP ERP.
- Skill aziendali :  Il personale Sme.UP conosce già tutti gli strumenti e le tecnologie suddette, oltre che il prodotto Sme.UP Provider e le relative schede di controllo.
-- Capacità di sviluppo :  Ci aspettiamo tempi di sviluppo / manutenzione in linea con i normali tempi di sviluppo forniti nei vari ambiti di Sme.UP ERP.
-- Reattività agli inconvenienti :  Sempre per tutti i motivi di cui sopra, ci aspettiamo gli stessi livelli di reattività forniti nei vari ambiti di Sme.UP ERP.

## Conclusioni
Alla luce di quanto esposto, possiamo affermare che gli strumenti alternativi diversi da Sme.UP sono più limitati e ci vincolano a conoscenze ed esperienze che non possediamo.
Per questi motivi ci sentiamo di confermare la nostra scelta di Sme.UP Provider come soluzione per il colloquio con il Web Service di AT.
