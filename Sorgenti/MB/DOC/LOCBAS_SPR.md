# Sme.UP Provider

![LOCBAS_042](http://localhost:3000/immagini/LOCBAS_SPR/LOCBAS_042.png)
# Cos'è

**Sme.UP Provider**   è il fornitore di servizi remoti per applicazioni del mondo Sme.UP.
Contiene funzionalità sviluppate nel codice di Looc.UP che non era possibile o conveniente far gestire ai nostri sistemi as400. Nacque nel 2006 dedicato principalmente alla connessione con dispositivi di campo e alla comunicazione e controllo di altri client (controllare e far eseguire funzioni). Si sviluppò in seguito per altri ambiti che dettaglieremo in questo documento. Veniva chiamato "Looc.UP server" ed utilizzato dai diretti interessati coinvolti su progetti specifici. Oggi, dato l'utilizzo sempre più diffiuso, come ad esempio la gestione delle connessioni verso Sme.UP ERP da dispositivi web e mobile, abbiamo pensato ad una giusta divulgazione, diffusione e ad un nome più corretto come "**Sme.UP Provider**".

![LOCBAS_043](http://localhost:3000/immagini/LOCBAS_SPR/LOCBAS_043.png)
**Sme.UP Provider** getta la basi per la realizzazione del modello di sviluppo applicativo completamente single-source.
Infatti garantisce un accesso unico e standardizzato, basato su FUN e XML, al sistema gestionale, mantenendo le connessioni e i job as400 e quindi l'utente applicativo.
Questo permetterà al consulente applicativo Sme.UP di sviluppare in autonomia come avviene oggi con Looc.UP

![LOCBAS_044](http://localhost:3000/immagini/LOCBAS_SPR/LOCBAS_044.png)
Il codice Looc.UP è composto da due blocchi logici, i componenti di interfaccia grafica, che interagiscono direttamente con l'utente, sviluppati quasi interamente in Delphi e i componenti (**Sme.UP Provider**) che eseguono operazioni (o servizi) e che forniscono o manipolano dati, sviluppati in java. I primi richiamano i secondi attraverso le "FUN", i secondi rispondono con XML dopo aver eseguito il compito richiesto.
**Sme.UP Provider** richiede un server dedicato, per ora con sistema operativo Windows.

# A cosa serve

![LOCBAS_045](http://localhost:3000/immagini/LOCBAS_SPR/LOCBAS_045.png)
**Sme.UP Provider** espone diversi servizi e si presta ai seguenti utilizzi : 

 :  : PAR F(01) L(PUN)
- Servizi di accesso tramite web
- Servizi di accesso tramite mobile
- Integrazione con il campo
- Accesso remoto ai file e alle cartella
- Web Service di integrazione con applicazioni terze (Negoziando, QlickView, Documentali, Altri Erp, ecc...)
- Stampe e documentazione
- Fogli di calcolo
- Grafici e immagini dinamiche
- Strumenti di base


## Servizi di accesso tramite web e mobile
**Sme.UP Provider** fa da bridge tra le Web.UP e Mob.UP e il server applicativo, mantendo le connessioni e facendo transitare le richieste (FUN) e le risposte (XML). Permette alle applicazionei Web e Mobile di collegarsi a qualunque ambiente.

![LOCBAS_046](http://localhost:3000/immagini/LOCBAS_SPR/LOCBAS_046.png)
## Integrazione con il campo
Tramite i plugin, **Sme.UP Provider** può interagire con dispositivi collegati al pc, ad esempio PLC, stampanti, bus di campo, applicazioni di comunicazione con la produzione.
Accesso remoto ai file e alle cartelle
**Sme.UP Provider** può accedere alle risorse (file) della propria rete o a risorse accessibili via http. Può quindi essere utilizzato per reperire dei PDF archiviati in un percorso di file non raggiungibile ovunque (da sede a sede, da casa a sede). Queste risorse possono essere percorsi diretti passati esplicitamente o indiretti, calcolati da Looc.UP stesso (pdf di una fattura dato il codice fattura, logo di un cliente dato il cliente, cartella contenente un file dato un file contenuto)

## Web Service di integrazione con applicazioni terze

- **Sme.UP Provider** esegue query su database esterni (qualunque database compatibile con jdbc) e permette di importare questi dati su as400 o di visualizzarli. L'importazione e la visualizzazione supportando gli oggetti. Si può, ad esempio, leggere una tabella di un database e importarla in Sme.UP
- Tramite i plugin, **Sme.UP Provider** può interagire con applicazioni esterne utilizzando il loro linguaggio. Questa interazione può configurarsi con un invio di dati, una richiesta di dati o la richiesta di esecuzione di un'operazione, in entrambe le direzioni. Gli esempi realizzati sono la connessione con Skype, la connessione con sistemi di posta, la connessione con Exchange Calendar.
- Tramite l'esecuzione di comandi shell pc, **Sme.UP Provider** può lanciare applicazioni.


## Stampe e Documentazione

- **Sme.UP Provider**  produce stampe (file PDF) partendo da qualunque matrice, con la possibiltà di applicare i setup (filtri, raggruppamenti, ecc.. ) e gli stili grafici. Le matrici possono contenere immagini (dalla fotografia dell'articolo al barcode, qrcode, grafico, gaussiana, autogenerati dai dati)
- **Sme.UP Provider**  produce stampe complesse partendo da script SCP_G53, che definiscono la struttura di un documento PDF (come si fa con gli script di scheda). Si possono creare PDF di fatture, bolle, schede cliente, report con molte tabelle e testi lunghi, contenenti anche "intelligenza" basata sulle logiche di Sme.UP (oav, oggetti, ecc..).
- **Sme.UP Provider**  genera PDF a partire da membri di documentazione. Ad esempio, si può generare il manuale di un modulo o, presso un cliente, il manuale d'uso di un articolo, che può essere poi pubblicato sul sito del cliente.
- **Sme.UP Provider**  gestisce un sito di documentazione basato su wiki, permettendo di pubblicare pagine wiki, dopo averle trattate per renderle consultabili correttamente e linkate tra loro. Può gestire, ad esempio, il wiki del cliente.
- **Sme.UP Provider**  produce pagine HTML a partire da membri di documentazione


## Ambito Fogli di Calcolo

- **Sme.UP Provider**  produce fogli di calcolo (Excel / Open Office / CSV) partendo da qualunque matrice, con la possibiltà di applicare i setup (filtri, raggruppamenti, ecc.. ) e gli stili grafici.
- **Sme.UP Provider**  legge fogli di calcolo (Excel, XLSX, Open Office, CSV) trasformandoli in forma matrice, con oggettizzazione, permettendo ad esempio di consultare un listino scritto in un folgio excel, aggiungendo poi le colonne aggiuntive, o navigando negli oggetti contenuti nel foglio excel.
- **Sme.UP Provider**  legge i fogli di calcolo e li trasferisce in file dati su AS400. Può, ad esempio, importare dati provenienti da altri sistemi.
- **Sme.UP Provider**  trasferisce file di testo su AS400.


## Grafici e Immagini dinamiche
**Sme.UP Provider**  può generare immagini di grafici o oggetti grafici generati runtime a partire dai dati che arrivano da un servizio. I grafici sono torte, gaussiane, barre, carte xr, andamenti nel tempo, diragrammi di pareto, linee, punti, reti di petri (rappresentazione workflow), gauge
Gli oggetti grafici sono QR-code, barcode di differenti tipologia, immagini di oggetti.

## Esecuzione funzioni schedulate
**Sme.UP Provider**  può eseguire funzioni schedulate su AS400 (wrkjobscde) tramite il costruttore LOA27.

## Strumenti di Base
Si tratta di funzioni trasversali a tutte le necessità applicative. Sono un po' come i B£.

### A- Colonne Aggiuntive
In **Sme.UP Provider** sono supportate le colonne aggiuntive. **Sme.UP Provider** è in grado di completare una matrice aggiugendo le colonne aggiuntive, per poi utilizzare i dati, ad esempio, in una stampa, o per visualizzarli.

### B- Reperimento Icone e Immagini
Tutte le immagini e le icone degli oggetti sono reperite attraverso un algoritmo di risalita che tiene conto del multi-azienda e delle classi, gestendo i default. Questo algoritmo è eseguito da **Sme.UP Provider**. Con immagini di oggetti si intende, di fatto, tutte le immagini :  infatti anche le azioni (Apri, Visualizza, Esegui), gli stati (Aperto, Chiuso) sono codificate come oggetti. Allo stesso modo, le immagini della documentazione sono oggetti Figura, i grafici sono l'immagine della funzione che genera il grafico, i barcode sono immagini di oggetti J4BRC.

### C- Flussi
**Sme.UP Provider** può eseguire un flusso (elenco di fun) attraverso il componente interno FLU. Oltre all'esecuzione, esistono servizi per gestire i flussi eseguiti o in esecuzione. I flussi hanno un'alta valenza applicativa :  sono come dei CL composti da fun. Si può ad esempio, con un click, ciclare sui clienti con sollecito, lanciare la generazione di un sollecito, archiviarlo in pdf e inviare un'email al cliente a al responsabile del cliente.

### D- Variabili
**Sme.UP Provider** gestisce e mantiene delle variabili che possono essere di inizializzazione o calcolate runtime :  ad esempio, se volessi sapere l'ora, potrei chiedere a **Sme.UP Provider di risolvere la variabile *NOW, se volessi sapere l'indirizzo ip dell'as400, chiederei la variabile *SERVER
Oggetti Applicativi Client
**Sme.UP Provider** gestisce oggetti che esistono solo al suo interno e che non possono essere trattati dall'AS400. In particolare, ne definisce e ritorna gli OAV. Ad esempio, si può chiedere a **Sme.UP Provider** la dimensione di un file, la cartella in cui è contento, la data di modifica, come OAV codificato (J/02, I/04 ecc...) e con servizi generici. In questo modo questi oggetti possono essere trattati allo stesso modo degli oggetti applicativi su as400.

# Checklist e soluzione ai problemi più comuni

- [Check list e soluzione problemi più comuni](Sorgenti/MB/DOC/LOCBAS_SPC)


# Installazione e configurazione

- [Sme.UP Provider&-x3a; Set and play](Sorgenti/MB/DOC/LOCBAS_SPI)

- [Prerequisiti e configurazione SSO SmeupProvider](Sorgenti/MB/DOC/LOCBAS_SPS)

# Protocollo comunicazione

- [Smeup Provider - Esempi di chiamate](Sorgenti/MB/DOC/LOCBAS_SPF)

# La versione Roma Revision 1

- [Sme.UP Provider&-x3a; La versione Roma R](Sorgenti/MB/DOC/LOCBAS_SP1)

# La versione Roma Revision 2

- [Sme.UP Provider Roma Rev.2](Sorgenti/MB/DOC/LOCBAS_SP2)

# Provider in Linux

- [Sme.UP Provider Web Application](Sorgenti/MB/DOC/LOCBAS_W00)


- [Sme.UP Provider&-x3a; Set and play](Sorgenti/MB/DOC/LOCBAS_SPI)


 :  : NPG
