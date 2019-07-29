# Generalità
I legami consentono di creare una relazione tra due oggetti, di qualsiasi tipo, del sistema informativo. Al legame si possono associare una serie di informazioni di carattere descrittivo o controllato.

I legami permettono : 

- al >programmatore di avere a disposizione uno strumento con cui costruire con poche righe di codice RPG programmi che permettono l'immissione di dati relativi ad  oggetti correlati tra di loro. Un esempio di utilizzo dei legami è la creazione di un programma che gestisce le relazioni fra le entità aziendali (ad esempio, associando ad una mansione lavorativa in un reparto un certo indice di rischio del lavoro, ecc...)

- all'>utente di avere a disposizione uno strumento per la creazione di applicazioni senza scrivere alcuna riga di codice (ad esempio, per sintetizzare procedure di gestione del personale, gestione corsi, ecc...).


# Passi preliminari alla definizione del legame

- Definizione delle entità oggetto della relazione.
Se voglio creare un legame tra l'oggetto "dipendente" e l'oggetto "mansione", devo creare la griglia dipendente/mansione nella tabella B£G dove si definiscono le griglie di controllo entità.
Se si vogliono effettuare dei controlli sul legame e/o si vuole gestire in modo personalizzato il  legame, sarà necessario creare un programma specificato nella C£U.
- Definizione di una categoria di parametri per dare la possibilità di agganciare al legame informazioni aggiuntive al legame.
Il contenitore delle note specificato nella categoria diventerà il contenitore del legame (Riferimento :  FUNPARA.DOC)
- Controllo del documento Parametri, nella cartella FUN .. .. ecc  ecc.. .. .


# Il Legame
Ogni tipo di legame viene caratterizzato da una tabella (C£U), nella quale vanno inseriti : 

- la griglia di controllo, ovvero i tipi oggetti trattati dal legame;
- il programma di controllo del dettaglio del legame (non obbligatorio);
- la categoria dei parametri associati alla relazione;
- la  tipologia dei limiti iniziale/finale del legame, che tipicamente è una data. Tali limiti sono opzionali o obbligatori, in funzione della relazione che si vuole descrivere.

Per la costruzione di un legame vedi diagramma di flusso SEGUENTE.


![C£_LEG_01](http://localhost:3000/immagini/C£LEGA/CX_LEG_01.png)>Figura 1 - Gestione Legami

# Interrogazione Struttura dei Legami
L'interrogazione dei legami consente di analizzare contemporaneamente diversi legami, purchè logicamente concatenati tra loro.
La funzione controlla, infatti, che le scelte effettuate abbiano una compatibilità tra tipi oggetti, cioè il secondo oggetto del primo legame dovrà essere come il primo oggetto del secondo legame. Chiariamo con un esempio :  se volessimo conoscere i rischi connessi all'attività lavorativae gli strumenti con cui un dipendente si deve proteggere, dovremmo interrogare la struttura dei legami, specificando i legami dipendente/mansione, mansione/rischio e rischio/dispositivi di protezione.

![C£_LEG_02](http://localhost:3000/immagini/C£LEGA/CX_LEG_02.png)>Figura 2 -  Costruzione interrogazione  per esplosione

Se volessimo conoscere le mansioni in cui deve essere utilizzato il dispositivo di protezione e dachi esso debba essere usato, dovremmo interrogare la struttura dei legami, specificando i legamirischio/dispositivi di protezione, mansione/rischio e dipendente/mansione.

Abbiamo realizzato un software atto alla gestione dei problemi legati alla sicurezza e salute sul lavoro.
I legami sono risultati essere un valido strumento per risolvere quella parte dell'applicazione adibita all' identificazione dei dati di base (le fonti di pericolo, i rischi, le situazioni di non conformità).
In Q9000, un pacchetto che supporta la gestione della qualità, i legami sono stati utilizzati per gestire gli strumenti composti.

![C£_LEG_03](http://localhost:3000/immagini/C£LEGA/CX_LEG_03.png)>Figura 3 - Interrogazione

![C£_LEG_04](http://localhost:3000/immagini/C£LEGA/CX_LEG_04.png)>Figura 4 - Costruzione interrogazione, implosione

![C£_LEG_05](http://localhost:3000/immagini/C£LEGA/CX_LEG_05.png)>Figura 5 - Interrogazione dei Legami
