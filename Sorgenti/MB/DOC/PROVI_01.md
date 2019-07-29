# Obiettivo :  descrive la gestione degli accessi con utilizzo di Smeup provider e telecamere OCR

Una applicazione che mostra la capacità strutturale di Smeup di interagire con la domotica è stata realizzata e fatta funzionare nella sede di Erbusco.
Questa applicazione consente il controllo degli accessi al parcheggio, riconoscendo le autovetture che si presentano al cancello , la loro appartenenza ad un collaboratore di Smeup autorizzato all'ingresso e dispone l'apertura del cancello, oltre a registrare l'evento e la fotografia dell'ingresso / uscita.
Alla base di questa applicazione c'è la architettura ad oggetti di smeup, la codifica del parco autovetture ( che viene utilizzata anche per il controllo nota spese) , l'utilizzo del componente " smeup provider " che smista il traffico dati tra il server Power-I ed il resto del mondo, un dispositivo di riconoscimento ottico ( telecamera) ed un attuatore che apre il cancello elettrico.

In figura 1 è mostrato questo schema : 
* In centro alla figura c'è il componente smeup-provider  , che risiede su un server windows,  che riceve dalle telecamere l'esito del riconoscimento ottico :  targa autovettura, data , ora, direzione ( entrata o uscita) , velocità, fotografia e numero del dispositivo ( indirizzo IP) che ha realizzato l'immagine
* Questi dati vengono subito inviati  a smeup dove un programma confronta i dati con quelli dell'archivio autovetture
* Le autovetture  in Smeup sono codificate  come matricole di tipo AUT, quindi sono l'oggetto MTAUT ( vedi figura 2, scheda dell'autovettura)
* Tra i parametri dell'autovettura c'è l' utilizzatore, un collaboratore ( oggetto CNCOL) che quindi viene identificato e viene controllata la sua autorizzazione all'ingresso.
* A questo punto smeup esegue due azioni : 
** Manda a Smeup provider l'ordine di eseguire l'apertura del cancello , che diventa una stringa spedita da Smeup-Provider all'attuatore del cancello elettrico
** Scrive nell'archivio degli eventi ( vedi figura 3) il log delle entrate ed uscite.

Figura 1  :  schema della comunicazione con il campo e la domotica

![PH010](http://localhost:3000/immagini/PROVI_01/PH010.png)

Questo schema di comportamento è assolutamente generale , in quanto può essere perseguito per altre soluzioni applicative, grazie alla generalizzazione degli input e degli output : 
* L'azione che Smeup-provider svolge nei confronti dell'attuatore passa da una interfacccia standard con la domotica, che quindi può essere utilizzata per attivare altri dispositivi terminali :   pannelli luminosi, semafori, sirene,
* Smeup provider può azionare anche  AGV, robots, stampe, etc.
* Gli input a smeup-provider possono arrivare da altre fenomeni, intercettati tramite listeners :  Skype, mail, telefoni, sms
* Gli input a Smeup-provider possono arrivare anche da  PLC, dispositivi di campo, tag radiofrequenza, etc.

Appare anche chiaro che le azioni che Smeup ERP può fare sono molteplici :  scrittura di files, invio di mail, sms, etc.

Quindi questa soluzione implementata ad Erbusco serva da banco dimostrativo della validità della collaborazione tra Smeup e la domotica ed i PLC di campo.
Può essere usata per : 
* tracciare lo spostamento dei pallets dotati di tag RFID attraverso i cancelletti ( antenne radiofrequenza) nei punti nodali della micrologistica di processo ( macchine, reparti), o per creare registrazione automatiche di eventi CRM quando un cliente chiama al telefono.
* riconoscimento e smistamento dei mezzi in entrata per il carico e lo scarico con associazione ad un sistema di pesa, verifica delle masse in entrata e in uscita
* applicazione di building automation, anche senza telecamera, legata invece al riconoscimento di badge magnetici o rfid del personale o dei visitatori

Scheda di assegnazione macchina a collaboratore
![PH020](http://localhost:3000/immagini/PROVI_01/PH020.png)
Lista delle entrate e delle uscite con fotografia
![PH030](http://localhost:3000/immagini/PROVI_01/PH030.png)
NOTE TECNICHE
Nell'ambito dell'evoluzione dell'integrazione di Sme.UP ERP con i dispositivi fisici, sono stati realizzati i plug-in di Smeup-Provider per : 
* comunicazione bidirezionale con tutti i dispositivi elettrici compatibili con lo standard KNX per la building automation (controllo dell'illuminazione, gestione degli impianti di riscaldamento e ventilazione, monitoraggi degli allarmi, gestione energia, elettricità e gas, gestione di impianti audio e video); Sme.UP ERP è in grado di inviare comandi o informazioni ai dispositivi e di rilevarne lo stato in tempo reale; lo standard KNX è il primo vero standard aperto, indipendente dalla piattaforma, riconosciuto a livello europeo e mondiale e quindi adottato dai maggiori produttori di componenti elettrici (ABB, GEWISS, SCHNEIDER, SIEMENS, ect.);
* comunicazione bidirezionale con tutti i dispositivi compatibili con il protocollo OPC per la industrial automation (controllo delle macchine di produzione e dei dispositivi di segnalazione); Sme.UP ERP è in grado di inviare comandi o informazioni ai dispositivi e di rilevarne lo stato in tempo reale;  il protocollo OPC è la raccolta degli standard e delle specifiche per la comunicazione dei dati di campo in tempo reale tra dispositivi di produttori diversi (ALLEN BRADLEY, GE, MITSUBISHI OMRON, SIEMENS, WAGO, ect.);
* acquisizione delle informazioni da una telecamera ANPR (Automatic Number Plate Recognition) con sistema OCR di riconoscimento delle targhe (p.es. mod. Vega Access della Tattile Srl - www.tattile.com) con notifica dell'evento tramite messaggio TCP e archiviazione dell'immagine fotografica tramite FTP; con questo sistema Sme.UP ERP è in grado di rilevare il transito/accesso dei mezzi, identificandone la targa, la nazionalità, la direzione, la velocità, la data e l'orario.
* interfaccia di rete IP - Weinzierl 730; componente per la comunicazione bidirezionale su rete ethernet
* alimentatore, EKINEX EK-AG1-TP; alimentatore per rete KNX (30 Vdc - 640 mA) provvisto anche di alimentazione ausiliaria
* attuatore,  Gewiss GW90740 ; attuatore KNX a 4 canali, di cui 1 utilizzato per comandare l'apertura del cancello
Installazione Telecamera
![PH040](http://localhost:3000/immagini/PROVI_01/PH040.png)installazione attuatore
![PH050](http://localhost:3000/immagini/PROVI_01/PH050.png)
* Perimetro di lavoro della telecamera
![PH060](http://localhost:3000/immagini/PROVI_01/PH060.png)