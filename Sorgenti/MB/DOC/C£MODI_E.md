# Scenari
I modelli dinamici sono organizzati per scenari, ciascuno di questi risponde a precisi obiettivi di documentazione : 

## Scenario APP - Applicazioni
Questo scenario serve per visualizzare tutte le relazioni che interessano tra gli oggetti principali della customizzazione di un'applicazione : 
 * tabelle
 * archivi
 * sottosettori di tabella

Per accedere al modello dinamico selezionare : 
 * Scenario = APP
 * Contesto = L'applicazione voluta tra quelle presenti nella finestra dei contesti attivi

Si presenta la scheda del modello dinamico dell'applicazione : 
![C£MODI_021](http://localhost:3000/immagini/C£MODI_E/CXMODI_021.png)
## Scenario LIB - Librerie
Questo scenario serve per visualizzare tutte le relazioni tra gli oggetti principali presenti in una libreria.

Per accedere al modello dinamico selezionare : 
 * Scenario = LIB
 * Contesto = La libreria voluta tra quelle presenti nella finestra dei contesti attivi

Si presenta la scheda del modello dinamico dell'applicazione : 

![C£MODI_023](http://localhost:3000/immagini/C£MODI_E/CXMODI_023.png)
## Scenario OGG - Oggetti
Questo scenario ha l'obiettivo di visualizzare gli ambienti (liste librerie) e le autorizzazioni applicative impostati.

Per accedere al modello dinamico selezionare : 
 * Scenario = OGG
 * Contesto = Quello desiderato tra quelli attivi

Si presenta la scheda del modello dinamico del contesto richiesto : 

![C£MODI_024](http://localhost:3000/immagini/C£MODI_E/CXMODI_024.png)
## Programmi
L'obiettivo di questo scenario è quello di analizzare le relazioni esistenti tra programmi ed applicazioni e le relazioni tra programmi e altri oggetti : 
 * archivi;
 * librerie;
 * altri programmi;
 * utenti (di creazione o di modifica dei programmi);
 * P.T.F.;
 * /copy utilizzate (dentro il memebro di file MBQILEGEN).

### API (/Copy)
Un utilizzo particolare dello scenario PRO permette di vedere l'elenco delle /Copy utilizzate dai programmi di un'applicazione : 
 * si seleziona l'applicazione;
 * si apre il Tab "Tipo Oggetto";
 * si seleziona il tipo "MB = Membro di un file" > "MBQILEGEN";
 * viene presentata la lista delle /Copy utilizzate.

![C£MODI_025](http://localhost:3000/immagini/C£MODI_E/CXMODI_025.png)
Un altro modo di raggiungere il modello dinamico di una /Copy è dalla lista generale di tutte le /Copy, che può essere ottenuta selezionando la voce "Servizi e Azioni" dal menù MyLoocUp, oppure dalla scheda di un'applicazione qualsiasi.

La scheda della /copy presenta il tab 'Modelli Dinamici', che selezionato attiva una scheda come sotto : 

![C£MODI_022](http://localhost:3000/immagini/C£MODI_E/CXMODI_022.png)
Nel riquadro "Relazioni dell'oggetto" compare l'unica relazione 'é utilizzata da' con l'elenco dei programmi che utilizzano tale routine.
Selezionando uno dei programmi in elenco, nel riquadro centrale verranno evidenziate le relazioni significative a cui è soggetto tale programma.
Dall'esempio compaiono relazioni di appartenenza, di creazione, modifica e utilizzo, ritenute significative da chi ha disegnato il modello dinamico. E' chiaro che, se si dovessero ritenere significative altre relazioni, basterebbe modificare il programma di ricostruzione del modello secondo le indicazioni date nei paragrafi precedenti.
Si noti che in basso sono sempre presenti i bottoni che consentono di ricostruire in tempo reale il modello dinamico.

_2_NOTA BENE
Lo scenario PRO viene creato direttamente in fase di compilazione dei programmi; al momento non esistono altre modalità per ricrearlo.

## Scenario W/U - Where Used
Ha l'obiettivo, di visualizzare per ciscuna applicazione quali sono gli archivi che possono contenere degli oggetti di cui si vuole tracciare il "dove usato".

Con dove usato di un oggetto applicativo si intende conoscere, data un'istanza di questo oggetto (un codice cliente, un articolo, una commessa, ecc...) di visualizzare principalmente in quali archivi di quali applicazioni dove questo codice è presente.

Una volta selezionato un archivio possiamo anche visualizzare in quali record dell'archivio stessol'oggetto è presente.

Per accedere al modello dinamico selezionare : 
 * Scenario = W/U
 * Contesto = L'applicazione voluta tra quelle presenti nella finestra dei contesti attivi

Si presenta la scheda del modello dinamico del "Dove Usato" : 

![C£MODI_026](http://localhost:3000/immagini/C£MODI_E/CXMODI_026.png)
## Scenario DOC - Documenti
L'obiettivo di questo scenario è quello di analizzare le relazioni esistenti tra i documenti.
In particolare : 
 * Tutti i source file che iniziano con DOC
 * I cataloghi delle immagini, nel soirce file DOC (Nome del Modulo con desinenza _FIG)
 * Tutti i file delle immagini contenuti nella cartella del modulo

Per accedere al modello dinamico selezionare : 
 * Scenario = DOC
 * Contesto = L'origine del documento voluto tra quelle presenti nella finestra dei contesti attivi

_2_NOTA BENE
Per poter importare i file bisogna preparare un archivio contenete l'elenco dei file attraverso le funzioni dell'oggetto PATHDIR.
Eseguire le seguenti operazioni : 
- Aprire l'oggetto J1 PATHDIR [SME.IMG]\TAB£A
- Selezionare Consultazioni - Contenuto
- Scegliere la forma libera
- Confermare la selezione escludendo i file di sistema
- Una volta ottenuta la matrice, eseguire il Pop.UP e selezionare Visualizza come - Scheda File Dati
- Selezionare Gestione - Sposta in tabella AS400
- Confermare l'esecuzione con nome tabella "FIGURE"

## Scenario SCP - Script
L'obiettivo di questo scenario è quello di analizzare le relazioni esistenti tra gli script e i servizi.
In particolare : 
 * Tutti i source file che iniziano con SCP

Per accedere al modello dinamico selezionare : 
 * Scenario = SCP
 * Contesto = L'origine del documento voluto tra quelle presenti nella finestra dei contesti attivi
