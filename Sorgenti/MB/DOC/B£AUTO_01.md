# DOCUMENTAZIONE GENERALE

## Definizione
Con autorizzazione si intende la capacità che viene conferita a un utente o a un gruppo di utenti di esercitare una certa attività o di visualizzare un'informazione. Smu.UP garantisce infatti di limitare le azioni di un utente relativamente a un menù, a un anagrafico o di  una azione di modifica di un dato.
Al tema autorizzazioni è stato dedicato un intero modulo, all'interno del quale è possibile trovare gli strumenti che servono a impostare, gestire o semplicemente controllare le autorizzazioni attive per un utente su un particolare oggetto (applicazione, modulo, o anche enti, articoli, etc). Questo modulo, denominato B£AUTO e consultabile solo se lo *USERLEVEL del proprio utente è alemno 01, si trova all'interno dell'area applicativa _Architettura e servizi di base, nell'applicazione B£.

Per chiarire subito il concetto di  *USERLEVEL. riportiamo di seguito una sua breve definizione, poichè una spiegazione più approfondita verrà demanadata a un documento specifico.
Con *USERLEVEL si intende quella classe di autorizzazione che definisce il livello di utilizzo si MSe.UP da parte dell'utente. A oggi vengono gestiti quattro diversi livelli di utilizzo : 

* **00 - Operativo** :  destinato agli utilizzatori finali di SMe.UP, a chi cioè utilizza il SW solo dal punto di vista applicativo.
* **01 - Gestore EDP** :  per quegli utenti che, oltre a una visione applicativa, hanno abitualmente a che fare con azioni di gestione del sistema, dal punto di vista del suo funzionamento a livello di impostazioni generali.
* **02 - Implementatore** :  da attribuire agli installatori Sme.UP nelle installazioni dai clienti. Questo livello conferisce il massimo grado di utilizzo di Sme.UP.
* **03 - Sviluppatore (test)** :  con questo livello si attivano funzioni che sono ancora in fase di test. Questo livello è riservato a chi si occupa di sviluppare Sme.UP  in laboratorio.

_Rimandiamo al documento B£AUTO_02 per amggiori dettagli sullo *USERLEVEL._

## Lo scopo delle autorizzazioni
A seconda di chi implementa o subisce gli effetti delle autorizzazioni, queste perseguono scopi e finalità ben differenti.
>Per l'utente finale : 
* accedere solo alle funzioni che sono di suo interesse
* visualizzare su un record anagrafico solo i campi di sua competenza
* inibire l'accesso alle tabelle di parametrizzazione (riservate al presonale IT dedicato alla customizzazione dell'applicazione)
>Per il programmatore : 
* rendere indipendente il suo programma dal particolare utente che vi accede
* implementare nello stesso programma funzioni con livello di autorizzazioni diverse
* disporre di una funzione generica da introdurre nei suoi programmi
>Per il responsabile sistema informativo : 
* confidare sulla congruenza dei dati presenti nel sistema


## Architettura Applicativa
Le autorizzazini in Sme.UP vengono configurate attraverso tre valori : 

- la **CLASSE**, ovvero un elemento della tabella B£P, che definisce l'ambito applicativo sul quale l'auorizzazione deve avere effetto (applicazione, modulo, oggetto, istanza, componente, etc...).
- L'**UTENTE**, ovvero la persona sulla quale le autorizzazioni devono avere effetto. Possono essere definite autorizzazioni per utente, gruppo utente o utente generico **.
- La **FUNZIONE**, e quindi una declinazione specifica del contesto e quindi della classe sopracitata.

Le modalità con cui le autoizzazioni devono operare all'interno di ciascuna classe sono invece definite azioni (elementi della tabella B£S) e dal valore assunto da queste.
Le azioni possono essere le normali opzioni di aggiunta, modifica, copia... o azioni più complese e articolate. Ogni azione ha 10 possibili risposte. In tale modo, per ogni classe di autorizzazione, si viene a creare una sorta di tabella di dieci righe (azioni possibili :  IMMISSIONE, MODIFICA, VISUALIZZAZIONE,...) e dieci colonne (risposte valide :  01/IM, 02/MO, 05/VI,..).



## Rappresentazione astratta
La funzione delle autorizzazioni può essere immaginata come uno strumento che fornisce una "RISPOSTA" rispetto alla eseguibilità di una "AZIONE" di "QUALCUNO" in un determinato "CONTESTO".
Sostituendo le parole astratte di sopra potremo avere ad esempio casi di questo genere : 

- "Paolo" può "inserire" un nuovo "cliente"?
- "Tutti gli utenti" possono "vedere il costo" nelle "interrogazioni di magazzino?

_1_Schema Astrazione delle autorizzazioni : 
![B£AUTO01](http://localhost:3000/immagini/B£AUTO_01/BXAUTO01.png)
Quindi la tecnica adottata in Sme_up può benissimo essere ripresa senza alcun problema di conflitti concettuali.

## Rappresentazione tecnica
Lo schema seguente vuole descrivere gli elementi tecnici dell'impostazione.

_1_Schema Tecnico delle autorizzazioni : 
![B£AUTO02](http://localhost:3000/immagini/B£AUTO_01/BXAUTO02.png)
La classe di autorizzazione fissa il significato di utente e funzione permettendo la scelta all'interno di un qualsiasi "Oggetto Applicativo", nonché il sottosettore da cui saranno riprese le azioni possibili.
Lo schema delle autorizzazioni rappresenta in modo semplice quello che risulta essere il comportamento dell'applicazione "Autorizzazioni" in Sme_up.
Per generare l'elenco di queste ultime devono essere scelti i parametri seguenti  : 

- Utente
- Funzione
- Classe


## Attribuzione Autorizzazioni
>Risalita
All'interno di una classe possono essere attribuite Autorizzazioni per il generico utente "U**", per la generica funzione "F**" ed il generico Gruppo "G**".
Analogamente è possibile attribuire autorizzazioni anche per l'utente specifico su qualsiasi funzione e gruppo.
Riassumiamo schematicamente le suddette Autorizzazioni a partire da un livello più basso (utente/funzione) a quello più alto (classe) : 
 :  : PAR
- Utente specifico / F**
- G** / Utente specifico
- U** / Funzione specifica
- G** / Funzione specifica
- Gruppo specifico/ U**
- Gruppo specifico / F**


_1_Schema risalita autorizzazioni : 
![B£AUTO03](http://localhost:3000/immagini/B£AUTO_01/BXAUTO03.png)
Immaginiamo ora che all'interno di un certo applicativo un utente voglia accedere ad una particolare funzione.
La richiesta d'accesso causerà la chiamata al programma B£AUA0G di gestione delle Autorizzazioni che andrà, come prima cosa, a verificare l'esistenza delle stesse relative alla funzione chiamata per l'utente chiamante.
Nel caso non siano state definite tali Autorizzazioni, il programma risalirà fino a quelle definite per l'utente generico e per la particolare funzione.
Se questo non andrà a buon fine, continuerà per quelle relative all'utente per una generica funzione all'interno della classe.
Nel caso in cui nemmeno queste siano state definite verranno prese quelle definite per default cioè U** / F** (Schema di Risalita).

_1_Esempio - Astrazione delle autorizzazioni Sme.up : 
![B£AUTO04](http://localhost:3000/immagini/B£AUTO_01/BXAUTO04.png)
Lo schema precedente vuole essere di aiuto per comprendere il grado di astrazione delle autorizzazioni in SME_UP. Si noti che la logica rimane valida qualunque sia l'ambito preso in considerazione. Nel nostro caso avremo che "QUALCUNO" diventa "Veicolo", il "CONTESTO" diventa "l'ambiente" e le "AZIONI" sono le "attività eseguibili". Mediante le autorizzazioni potrò descrivere il fatto che un ciclomotore non può viaggiare in autostrada e che il limite di una automobile su strada urbana è di 50 Km orari.

