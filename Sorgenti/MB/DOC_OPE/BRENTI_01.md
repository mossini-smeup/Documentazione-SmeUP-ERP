# Introduzione

L'obiettivo delle nuove navigazioni è quello di rendere la consultazione sulle anagrafiche degli enti (fornitori, clienti, vettori, ecc) più agevole, semplice e migliorarne così la comprensione.
Dal punto di vista della raggiungibilità, queste schede possono essere richiamate direttamente dal modulo relativo.

Una delle novità introdotte riguarda proprio il modulo BRENTI, che prima riguardava in modo generico tutti gli enti (indistintamente), ora si è articolato in tanti piccolo moduli a seconda della natura del soggetto ai quali si riferiscono. Con questa riorganizzazione infatti avremo la seguente situazione : 
- Il BRENTI0 :   è dedicato all'archivio dei contatti.
- Il BRENTI1 :   è dedicato all'analisi e interrogazione dei Clienti.
- Il BRENTI2 :   riguarda i Fornitori.
- Il BRENTI3 :   per le Aziende.
- Il BRENTI4 :   per l'anagrafico delle Banche.
- Il BRENTI5 :   per gestire e interrogare gli indirizzi.
- Il BRENTI6 :   per i Nominativi.

## Struttura della scheda
La scheda è conforme allo standard adottato anche dalle altre schede, ovvero ripropone l'ormai nota struttura a tre sezioni.
Ciascuna sezione ha una funzione ben precisa : 
**1.** la prima verticale a sinistra, dedicata al menù :  questa riporta tutte le azioni e navigazioni più importanti relative ai cicli di lavoro
**2.** la seconda orizzontale, nella parte alta, dedicata ai filtri e alla loro impostazione
**3.** la terza, che occupa tutta la restante parte, destinata a contenere il risultato della ricerca.

![BRENTI_001](http://localhost:3000/immagini/MBDOC_OPE-BRENTI_01/BRENTI_001.png)
Come già accade per molti altri oggetti di Sme.UP anche per gli enti avremo un tipo di consultazione legata a categorie omogenee di soggetti.
Scelto il modulo da consultare (per esempio il BRENTI1 per i clienti), al primo accesso verrà proposta una scheda iniziale con l'elenco delle diverse categorie enti per la natura del modulo scelto.
Questa scelta può essere modificata in qualsiasi momento grazie alla voce "Cambio Clienti/Fornitori ..." prensente nell'Hypermenù del modulo.

![BRENTI_002](http://localhost:3000/immagini/MBDOC_OPE-BRENTI_01/BRENTI_002.png)
# Il dashboard del modulo

La prima voce di menù ci permette di accedere al cruscotto del modulo, ovvero ad informazioni di tipo statistico che permettono di capire quanti soggetti di un certo tipo sono presenti nel sistema.
L'informazione può essere vista in differenti modi a seconda della forma scelta, che ne decide anche il raggruppamento.
![BRENTI_003](http://localhost:3000/immagini/MBDOC_OPE-BRENTI_01/BRENTI_003.png)
Oltre a queste informazioni, è possibile visualizzare tramite la scheda "Situazione parametri modulo" anche la situazione degli enti per tutte le nature presenti.
![BRENTI_004](http://localhost:3000/immagini/MBDOC_OPE-BRENTI_01/BRENTI_004.png)
# Le navigazioni :  il SURF degli Enti

Essendo gli enti dotati di numerosi attribuiti e parametri, e avendo legate ad essi numerose inormazioni, le forme di interrogazione messe a disposizione sono innumerevoli.
Queste interrogazione possono essere raggiunte direttamente dall'Hypermenù del modulo BRENTIx oppure dal popup degli oggetti che sono collegati ad un oggetto ente.

![BRENTI_005](http://localhost:3000/immagini/MBDOC_OPE-BRENTI_01/BRENTI_005.png)

## Qualche esempio SURF
Vediamo ora qualche esempio di Surf, per capire le modalità di interrogazione introdotte nella scheda : 

1) Il surf per CODICE impronta la ricerca sul codice soggetto, infatti grazie al campo "Posizionamento Codice" ho la possibilità di ricercare un soggetto a partire da quelli con un determinato codice iniziale.
Posso quindi digitare un codice per intero o anche solo l'inizio del codice ente che sto cercando.
Tramite invece il campo "Codice descr. Contiene" ho la possibilità di ricercare un soggetto tramite la ragione sociale. Talvolta succede di non ricordare per intero la ragione sociale o non ci si ricorda l'ordine con il quale è scritta, al fine di facilitare l'utente nella ricerca, questo campo fa una scansione all'interno della ragione sociale permettendomi di digitare anche solo una parte della ragione sociale, e non necessariamente l'inizio.

![BRENTI_012](http://localhost:3000/immagini/MBDOC_OPE-BRENTI_01/BRENTI_012.png)
Vediamo nel dettaglio altri campi contenuti nell'input panel : 
- "Indirizzo e località contiene" permettono di fare ricerche su questi due campi, anche scrivendo parzialmente un indirizzo, per esempio : 
![BRENTI_006](http://localhost:3000/immagini/MBDOC_OPE-BRENTI_01/BRENTI_006.png)- Il campo "RIF. FISCALE CONTIENE" invece, come dice il tooltip, permette di fare una ricerca in base alla partita iva o al codice fiscale, anche scrivendone solo una parte : 
![BRENTI_007](http://localhost:3000/immagini/MBDOC_OPE-BRENTI_01/BRENTI_007.png) Il risultato sarà che verranno filtrati tutti i soggetti che contengono quella sequenza di numeri nella propria partita iva o CF.

Gli ultimi campi presenti nell'input panel, li troveremo anche in tutti gli altri SURF del modulo : 
- A/D indica l'ordinamento ascendente o discendente della matrice e ordina i dati sempre in base al codice ente.
- SCHEMA permette di visualizzare i dati in schemi preimpostati.
- NR RIGHE permette di decidere quante righe caricare ad ogni paginazione.

2) Passiamo ora al SURF per NAZIONE o REGIONE utile ad esempio per visualizzare tutti i clienti di una determinata nazione o di una certa provincia.
Dopo avere concentrato la mia ricerca sull'anagrafica tramite il filtro sulla provincia/nazione, ho anche la possibilità di restringere ulteriormente la ricerca mirando ad un certo indirizzo o ad una località precisa. Questi due campi come dice il termine "CONTIENE" mi danno la possibilità di fare una ricerca rapida e mi lasciano la libertà di indicare solo una parte della stringa da cercare.
![BRENTI_008](http://localhost:3000/immagini/MBDOC_OPE-BRENTI_01/BRENTI_008.png)
3) Per chi invece avesse attiva la gestione dei nominativi è stata aggiunto un SURF che permette di ricercare i nominativi.
Questo con lo scopo di aiutare l'utente nell'individuazione di enti collegati ad un nominativo specifico, nell'eventualità per esempio che un ente sia cliente e fornitore allo stesso tempo.
Nella prima ricerca, una volta inserito il codice nominativo che voglio visualizzare mi si presenterà l'elenco dei soli Fornitori che hanno questo nominativo collegato, se ve ne fossero.
![BRENTI_009](http://localhost:3000/immagini/MBDOC_OPE-BRENTI_01/BRENTI_009.png)
Se mi sposto nella seconda sotto scheda "Risultato per Intero Anagrafico", vedrò su quali categorie e per quali soggetti è stato usato questo nominativo : 
![BRENTI_010](http://localhost:3000/immagini/MBDOC_OPE-BRENTI_01/BRENTI_010.png)
4) Spostiamoci ora ad uno dei Surf più importanti, quello delle estensioni, dalle quali posso visualizzare tutte quelle informazioni che non son facilmente raggiungibili dalle altre interrogazioni.
Alcuni esempi possono essere le coordinate bancarie, i dati percipiente o persona fisica, i vari indirizzi alternativi e i contatti (telefoni e mail) : 
![BRENTI_011](http://localhost:3000/immagini/MBDOC_OPE-BRENTI_01/BRENTI_011.png)
Ho la possibilità di inserire una data validità dinamica.
La scheda delle estensioni si compone di 2 sottoschede, la prima riguarda i campi con scelta libera, mentre interrogando la sottoscheda "con scelta da tipi presenti" viene mostrata la sola lista di estensioni che ha dei record in essere.


5) L'ultimo esempio di Surf che analizziamo riguarda la ricerca per RAPPORTO FISCALE. Ci postiamo nel modulo dei fornitori, il BRENTI2, da quest'interrogazione posso quindi estrarre in modo rapido tutti i soggetti percipienti.

## Documentazione ed Help
Dal modulo è possibile raggiungere la documentazione relativa, sotto la voce EDUCATION > DOCUMENTAZIONE.

Inoltre, ognuno dei filtri dell'input panel è dotato di una documentazione che ne spiega il significato, l'utilità e lo scopo. A questa si può accedere premendo il tasto funzionale F1 con il cursore del mouse posizionato sul filtro specifico.
