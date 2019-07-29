# Microkernel

# Scalabilità

Nei sistemi complessi, l'incremento globale delle prestazioni e delle risorse del sistema può essere ottenuto in differenti modalità : 



- **Verticale** :  l'aumento delle prestazioni viene ottenuto incrementando le risorse a disposizione del singolo sistema.
E' la soluzione tipica dei sistemi come IBMi.
- **Orizzontale** :  l'aumento delle prestazioni viene ottenuto scalando il lavoro su più sistemi che operano in modo coordinato. E' tipico di sistemi distribuiti su larga scala ed è normalmente sviluppato tramite cluster di macchine equivalenti e replicate.
- **Distribuita** :  l'aumento delle prestazioni viene ottenuto come per il modello orizzontale, introducendo per la possibilità di delegare a sistemi specifici specifiche funzioni


L'architettura As.UP delega la modalità di tipo verticale all'hardware di riferimento e propone un modello distribuito che offre la possibilità di gestire le risorse in modo orizzontale o specializzato in funzione della necessità.

Gli obiettivi di una moderna architettura sono i seguenti : 


- **Dimensionamento** :  dimensionamento del sistema in funzione del carico di lavoro previsto
- **Load balancing** :  bilanciamento del carico sulle risorse disponibili
- **Specializzazione** :  implementazione di servizi critici demandata a contesti specifici altamente ottimizzati
- **Integrazione** :   infrastruttura ottimizzata alla comunicazione e alla integrazione con contesti esterni, anche delocalizzati
- **Continuità** :  l'infrastruttura deve essere in grado di funzionare anche in presenza di eventuali problemi localizzati su singoli
elementi


La scelta di una architettura scalabile comporta anche alcuni problemi : 


- Una architettura a scalabilità orizzontale richiede software appositamente progettato per utilizzato su rete distribuita. E' quindi
una architettura molto pervasiva anche a livello di progettazione del software.
- Ad oggi, nessun linguaggio gestisce nativamente la scalabilità e non sembra esistere uno standard universale per la
gestione di questa categoria di problemi. Ci sono molte tecnologie, diverse per ambiente e contesto ma nessuna può
essere considerata uno standard di fatto.


# Esempio di architettura

La seguente figura mostra un esempio dove singole funzionalità necessarie al funzionamento globale
del sistema vengono demandate a specifiche risorse cooperanti all'interno di una rete.

![MUOPER_17A](http://localhost:3000/immagini/MUOPER_17/MUOPER_17A.png)

# Implementazione architettura scalabile in As.UP

La seguente figura mostra a grandi linee il principio di funzionamento.

Il punto fondamentale per il corretto funzionamento di una architettura di questo tipo è che tutto il funzionamento
del framework deve essere di tipo  **service oriented**.

Questo vuol dire : 


- Le funzionalità del sistema devono essere implementate sotto forma di servizi offerti da fornitori specilaizzati
- Il singolo servizio può essere fornito da più fornitori
- Deve esistere uno standard di accesso ai servizi. Chiunque si uniforma a questo standard è in grado di
accedere al servizio offerto.
- Il sistema deve essere in grado di tenere un registro dei servizi disponibili e controllare le autorizzazioni di
accesso a tali servizi.


Su questa base è possibile pensare una proposta di questo tipo : 

![MUOPER_17B](http://localhost:3000/immagini/MUOPER_17/MUOPER_17B.png)

Vediamo gli elementi salienti di questa soluzione architetturale.


- Il sistema globale, denominati **grid**,  è formato dall'insieme di songoli elementi detti **nodi**
- Ogni singolo nodo è un elemento applicativo che implementa una serie di **servizi**. Un determinato
servizio può essere implementato da un singolo nodo o da più nodo contemporaneamente.
- La condivisione dei servizi tra i singoli nodi avviene con grazie ad un elemento infrastrutturale che consente
ai singoli nodi di condividere il registro dei servizi. Grazie a questo registro condiviso ogni singolo nodo può
sapere in ogni momento chi è il fornitore (o i fornitori) di un determinato servizio. Allo stesso modo, il singolo
nodo registra nel registro condiviso i servizi che può fornire.
- L'accesso ai servizi avviene secondo uno standard definito dal registro condiviso. In questo modo, una volta
che un nodo ha identificato il potenziale fornitore di un servizio, potrà accedere al servizio stesso secondo le
modalità definite dallo standard.



All'interno di As.UP la tecnologia scelta per l'implementazione del registro dei servizi condivisi è la tecnologia
**D-OSGI** nella sua implementazione fornita dal framework **Eclipse ECF**. La tecnologia D-OSGI è
la naturale estensione verso la condivisione dei servizi dello standard OSGI su cui è attestata tutta l'architettura
As.UP e consente l'accesso ai servizi condivisi con una modalità simile a quella utilizzata su architetture
all-in-one.

Il principio di funzionamento del protocollo D-OSGI può essere riassunto in modo semplificato con la seguente
figura : 

![MUOPER_17C](http://localhost:3000/immagini/MUOPER_17/MUOPER_17C.png)

Le funzioni svolte dal protocollo D-OSGI sono essenzialmente tre : 


- **Service discovery** :  data una richiesta di accesso ad un servizio da parte di un potenziale consumatore,
il protocollo si occupa di individuare all'interno del sistema i potenziali fornitori del servizio. In questa fase vengono
gestite eventuali autorizzazioni di accesso in modo che un consumatore possa avere visibilità dei soli servizi a cui
è autorizzato.
- **Load balancing** :  nel caso la fase di discovery identifichi più di un fornitore per il servizio richiesto, il
protocollo consente di definire delle regole per la selezione del fornitore da utilizzare tra quelli disponibili. La
possibilità di scrivere regola anche sofisticate consente di implementare politiche di bilanciamento del carico di lavoro
tra i fornitori di servizio disponibili. Queste regole di bilanciamento possono utilizzare informazioni dinamiche sui
fornitori di servizio. Caso classico, l'esecuzione di un determinato servizio viene affidata al fornitore che nel momento
della richiesta ha meno carico di lavoro. Per poter applicare questa regola è necessario che il singolo fornitore di
servizi sia in grado di notificare al load balancer il suo carico di lavoro.
- **Businness continuity** :  la possibilità che un singolo servizio possa essere fornito da più fornitori ha un forte
ripercussione sulla stabilità e sull'affidabilità del sistema globale. Evitare che un servizio critico possa essere fornito
da un solo fornitore è il primo passo per aumentare l'affidabilità globale del sistema e garantire la continuità di
funzionamento anche in presenza di eventuali problemi.


# Riepilogo


- Ogni servizio può essere fornito da più fornitori presenti nella architettura del sistema, su macchine che possono
anche essere fisicamente diverse
- Le prestazioni globali del sistema sono date dal numero di serventi presenti nel sistema e dalla loro capacità di
condividere servizi ed informazioni.
- Le prestazioni globali del sistema possono essere aumentate aumentando il numero dei fornitori di servizi.
- L'affidabilità si incrementa aumentando e diversificando i fornitori in grado di espletare servizi critici.







