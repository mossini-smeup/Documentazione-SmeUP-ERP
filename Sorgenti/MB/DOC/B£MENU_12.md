# Hypermenu

## Perchè è stato creato l'Hypermenu?
- Per razionalizzare i percorsi di accesso alle informazioni
- Per standardizzare il layout delle schede principali
- Per facilitare e rendere più intuitiva la navigazione delle informazioni
- Per riutilizzare le funzionalità evolute di :  Filtri, Schemi, Input panel, Pop up di oggetto, Accordion.

## Come si compone un Hypermenu?
Le sezioni principali di una scheda fatta con l' Hypermenu sono : 
- Una colonna a sinistra, fatta con un Accordion (uno strumento composto da una colonna che si raggruppa in verticale o si stringe in orizzontale, con il vantaggio di lasciare spazio al resto della scheda) dove compaiono le opzioni della scheda.
- Una sezione per il resto della scheda dove sono visualizzati i risultati dell'opzione selezionata nell' Accordion.

## Come sono organizzate le opzioni nell'accordion?
Sono organizzate secondo dei raggruppamenti (indicati qui di seguito come opzioni), i quali sono soggetti a livelli di autorizzazione utente (classe autorizzazione USRLVL).
I valori dei livelli di autorizzazioni assunti possono essere : 
00 = Users
01 = Key user
02 = Installatore esperto Smeup
03 = Laboratorio di sviluppo.


**Opzione K = Dashboard  -  Livello 00**
Una sola azione che mostra una sintesi delle informazioni principali della scheda.
![B£MENU_002](http://localhost:3000/immagini/B£MENU_12/BXMENU_002.png)
**Opzione N = Info  -  Livello 00**
Una sola azione che contiene i dati di base dell'oggetto della scheda (come l'F10 dell'oggetto quando richiamato in emulazione 5250).
![B£MENU_015](http://localhost:3000/immagini/B£MENU_12/BXMENU_015.png)
**Opzione E = Fly  -  Livello 00 nelle schede di oggetto  /  Livello 01 nelle schede di modulo**
Tante azioni che esplorano le informazioni collegate all'oggetto, ma uscendo dal contesto di origine.
Per esempio, partendo dalla scheda dell'ordine di produzione, nel raggruppamento FLY trovo l'interrogazione degli impegni materiali o dei movimenti di magazzino dell'ordine.
Nelle schede di modulo l'opzione FLY contiene anche le funzioni tecniche :  Set'n & Play, Prototipi, etc.
![B£MENU_009](http://localhost:3000/immagini/B£MENU_12/BXMENU_009.png)
**Opzione J =  Surf  -  Livello 00**
  Tante azioni che esplorano le informazioni analoghe all'oggetto e contestuali all'oggetto :  Per esemmpio , partendo dalla scheda dell'ordine di produzione posso vedere tutti gli ordini dello stesso articolo dell'ordine da cui sono partito.
![B£MENU_014](http://localhost:3000/immagini/B£MENU_12/BXMENU_014.png)
**Opzione Y = Mysmeup  -  Livello 00**
  Tante azioni , le stesse che sono derivate dal flusso B£H A-OG dell'oggetto , per il modulo è A-TAB£AMO (le azioni tipiche di quella azienda) , e una azione che porta alle schede personalizzate di quell'oggetto
![B£MENU_010](http://localhost:3000/immagini/B£MENU_12/BXMENU_010.png)
**Opzione F = Focus  -  Livello 00**
  Una azione che mostra una lista grafica estesa dell'oggetto
![B£MENU_022](http://localhost:3000/immagini/B£MENU_12/BXMENU_022.png)
**Opzione G = Actions  -  Livello 00**
  Tante azioni , quelle della tabella MEA riguardante il contesto
![B£MENU_008](http://localhost:3000/immagini/B£MENU_12/BXMENU_008.png)
La modifica delle voci di questa sezione di menù prevedono la modifica della tabella MEA presente nel modello relativamente all'applicazione cui il modello appartiene.
La procedura per effettuare la modifica/eliminazione/aggiunta delle **Actions** è la seguente : 

- Collegarsi all'ambiente modello (MOD)
- Modifica  della tabella MEA, sottosettore applicazione (es :  MEA, sottosettore B£)
- Modifica/inserimento/eliminazione voci, possibilmente secondo progressione numerica esistente
- Indicare su eventuale nuova voce
-- Campo modulo
-- Utilizzo=M
-  **UP FTB**  da SMEDAT£MO lettera A, a SMETAB lettera A
- Uscire da **UP FTB** e la modifica è effettiva



**Opzione D = Education  -  Livello 00**
  Ci sono due azioni :  la prima è l'accesso alla Documentazione contestuale, la seconda è l'accesso alla Formazione del modulo
![B£MENU_021](http://localhost:3000/immagini/B£MENU_12/BXMENU_021.png)
**Opzione C = Properties  -  Livello 01**
  Tante azioni che servono ad impostare il modulo  :  funzioni tecniche, associazioni ad immagini, etc.
![B£MENU_024](http://localhost:3000/immagini/B£MENU_12/BXMENU_024.png)
**Opzione S = Set'n & Play  -  Livello 01**
  Tante azioni che servono ad impostare il modulo  :  set&play, modello dinamico, etc.
![B£MENU_025](http://localhost:3000/immagini/B£MENU_12/BXMENU_025.png)
**Opzione M = Menu MGMT  -  Livello 02**
  Apre la gestione dell'hypermenu per cui un installatore esperto può modificarlo
![B£MENU_026](http://localhost:3000/immagini/B£MENU_12/BXMENU_026.png)

NOTE : 
1) La voce MySmeup non compare sempre, ma solo nei seguenti casi : 
- quando esiste una scheda personalizzata per quell'oggetto o legata a quel modulo, e se allo stesso tempo nella tabella B§K è stata scelta l'opzione 3 che permettte di mettere questa scheda agganciandola alla scheda standard attuale.
- quando esistono delle azioni (B£J) legate al modulo o all'oggetto nella tabella B£H. Rispettivamente saranno definite :  A-XX dove XX è l'oggetto o A-TAB£AMO per i moduli nella B£H e avranno delle azioni contenute rispettivamente nella B£J.

2) Focus
Nella tabella B§K si può decidere di aggiungere/togliere delle cose dalla scheda del FOCUS utilizzando un eventuale programma di aggiustamento (vedi campo EXIT FOCUS).

##  Documentazione Tecnica
la documentazione tecnica dell'Hypermenu è quella del costruttore LOA12, ossia l'oggetto V2 LOCOS A12
- [Doc.tecnica LOA12](Sorgenti/MB/DOC_OGG/V2LOCOSA12)
