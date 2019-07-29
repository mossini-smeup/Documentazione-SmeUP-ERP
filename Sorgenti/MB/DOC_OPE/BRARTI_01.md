# Introduzione

L'obiettivo delle nuove navigazioni è quello di rendere la consultazione degli articoli __agevole__ dal punto di vista della raggiungibilità, e __semplice__ dal punto di vista della comprensione.
Dal punto di vista della raggiungibilità, queste schede possono essere richiamate direttamente dal modulo BRARTI, mentre dal punto di vista della comprensione queste sono semplici e intuitive perchè ripropongo l'ormai nota struttura a tre sezioni.
Ciascuna sezione ha una funzione ben precisa : 
**1.** la prima verticale a sinistra, dedicata al menù :  questa riporta tutte le azioni e navigazioni più importanti relative agli articoli
**2.** la seconda orizzontale, nella parte alta, dedicata ai filtri e alla loro impostazione
**3.** la terza, che occupa tutta la restante parte, destinata a contenere il risultato della ricerca.


![BRARTI_001](http://localhost:3000/immagini/MBDOC_OPE-BRARTI_01/BRARTI_001.png)
# Il dashboard del modulo

La prima voce di menù ci permette di accedere al cruscotto del modulo, ovvero una scheda puramente statistica che permette di visionare quanti codici articolo sono stati inseriti nel sistema.
La visualizzazione di queste informazioni è sensibile al tipo di raggruppamento, che può essere impostato mediante il campo "Forma" presente sull'input panel.
L'esempio di seguito mostra la visualizzazione di default, con il conteggio degli articoli organizzato per livello e stato.

![BRARTI_002](http://localhost:3000/immagini/MBDOC_OPE-BRARTI_01/BRARTI_002.png)
# Le navigazioni :  il SURF degli articoli

Per agevolare la consultazione dei codici articoli sono stati previsti diversi SURF. Oltre ai due di base, quello per codice articolo e per descrizione (di cui riportiamo sotto una piccola delucidazione sul funzionamento di alcuni campi), ne sono stati previsti altri per tipologia, gruppo ciclo, gruppo distinta, etc...
Tra le tante navigazioni, l'unica che si distingue è quella per  codici alternativi che consente di vedere, dato un codice articolo, l'elenco di tutti i suoi alternativi.
La modalità con cui vengono gestiti i legami tra i codici è mostrata nella sezione dei filtri :  questo campo, a differenza degli altri, non può essere modificato in quanto è solo di carattere informativo.

![BRARTI_003](http://localhost:3000/immagini/MBDOC_OPE-BRARTI_01/BRARTI_003.png)
Il risultato di questa consultazione permette di visualizzare, per tutti i codici alternativi, la loro disponibilità calcolata con il gruppo fonti impostato nella sezione dei filtri. Se omesso, la disponibilità viene calcolata con il gruppo fonti di default impostato in tabella BR1.

![BRARTI_004](http://localhost:3000/immagini/MBDOC_OPE-BRARTI_01/BRARTI_004.png)
Ciascun filtro è comunque dotato di una documentazione che ne spiega il significato, l'utilità e lo scopo.
A questa si può accedere premendo il tasto funzionale F1 dopo aver posizionato il cursore del mouse sul campo di cui si vuole leggere la documentazione.

Data l'importanza dei surf per codice e descrizione, riportiamo di seguito le istruzioni per il corretto utilizzo di alcuni campi filtro specifici di queste due navigazioni : 
** Posizionamento codice :  digitando in questo campo un codice articolo, o solo una sua parte, sarà possibile visualizzare tutti gli articoli a partire da o fino a quel valore inserito.
   Il risultato è quindi sensibile al tipo di ordinamento che si è deciso di imposatre nel campo A/D (ascendente o discendente)
** Cod/descrizione contiene :  usato in abbinamento agli altri campi, questo filtro permette di estrarre gli articoli che hanno o nel codice o nella descrizione quanto viene inserito dentro qui.

# Il popup delle opzioni :  il menù di un articolo

Dopo aver confermato i filtri nell'apposita sezione, è possibile visualizzare l'elenco degli articoli nella parte centrale della scheda. La matrice che viene caricata, indipendentemente dallo schema scelto e dal tipo di SURF, presenta sempre una colonna con una piccola icona (evidenziata in figura) che ha lo scopo di mettere a disposizione le azioni principali eseguibili sul codice articolo : 

![BRARTI_005](http://localhost:3000/immagini/MBDOC_OPE-BRARTI_01/BRARTI_005.png)
Questa icona permette di accedere direttamente al menù di popup di un articolo, nel quale sono riportate tutte le azioni di gestione e di interrogazione.
