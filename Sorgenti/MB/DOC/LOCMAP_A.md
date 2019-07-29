# Introduzione
L'interfaccia è un elemento di comunicazione fondamentale per l'utente.
Attraverso l'interfaccia, l'utente può infatti svolgere diverse attività :  visualizzare informazioni esistenti, inserire nuovi input, modificare dati, effettuare ogni operazione di cui abbia necessità.
Tuttavia, questo strumento costituisce spesso un collo di bottiglia poiché possono essere istantaneamente percepite solo le informazioni presenti sullo schermo, mentre altri dati aggiuntivi necessitano di operazioni di ricerca in molti casi articolate.
Lo scopo del componente Map è proprio quello di fornire all'utente un mezzo diretto, intuitivo, che costituisca una guida semplice e pratica verso informazioni il cui accesso non sempre è reso facile dal sistema.
Ogni istanza di questo componente viene costruita sulla base di uno script dedicato contenuto nel file Xml ricevuto dall'AS/400.
Le azioni che si possono compiere sono operazioni di navigazione.
Spostandosi con il mouse all'interno dell'immagine, a seconda della posizione istantanea del cursore vengono evidenziate alcune aree con un contorno blu. Sono le aree attive, ad ognuna delle quali corrisponde un preciso oggetto Sme.up.

![ESE_001](http://localhost:3000/immagini/LOCMAP_A/ESE_001.png)
La navigazione avviene attraverso un solo click del mouse nell'area evidenziata.
Cliccando con il tasto sinistro del mouse l'utente può visualizzare la scheda associata all'oggetto o un'ulteriore mappa di navigazione, mentre con il tasto destro del mouse l'utente può ritrovare il menù di Popup caratteristico degli oggetti Sme.up.

![ESE_002](http://localhost:3000/immagini/LOCMAP_A/ESE_002.png)
Mostriamo un esempio applicativo di navigazione : 
        -La schermata iniziale permette di scegliere tre differenti percorsi di navigazione  :  caratteristiche di una cucina(1), navigazione all'interno dell'azienda(2), navigazione geografica(3).

![ESE_003](http://localhost:3000/immagini/LOCMAP_A/ESE_003.png)

Questa struttura è stata ottenuta mediante la definizione nello script di tre diverse sezioni indipendenti : 

![ESE_004](http://localhost:3000/immagini/LOCMAP_A/ESE_004.png)
Per ogni sezione sono indicate le posizioni relative allo schermo e le dimensioni desiderate
La sezione di interesse può essere scelta mediante un click sul tasto sinistro del mouse in corrispondenza dell'area.
Selezionando, per esempio, la sezione relativa alla navigazione geografica, si passa alla schermata successiva.

![ESE_005](http://localhost:3000/immagini/LOCMAP_A/ESE_005.png)
Ora è possibile selezionare alcune regioni :  selezionando la Lombardia ne otterremo la cartina geografica sulla quale, in particolare, è presente un'icona in corrispondenza del luogo in cui si trova il laboratorio.

![ESE_006](http://localhost:3000/immagini/LOCMAP_A/ESE_006.png)
Ci troviamo dunque ad osservare la planimetria generale della sede.
Al centro, nell'area corrispondente all'edificio principale, abbiamo applicato una fotografia che non solo ne mostra l'immagine reale, ma permette anche di proseguire con la navigazione all'interno.

![ESE_007](http://localhost:3000/immagini/LOCMAP_A/ESE_007.png)
Si accede così all'edificio principale, nel quale si può navigare tramite la selezione di un piano o di un ingresso.


![ESE_008](http://localhost:3000/immagini/LOCMAP_A/ESE_008.png)
Entrando al piano terra si accede alla pianta relativa : 

![ESE_009](http://localhost:3000/immagini/LOCMAP_A/ESE_009.png)
Osserviamo che l'area relativa ad una delle stanze può essere riempita con un colore diverso (blu).
Tale caratteristica è definita nello script ricevuto dall'AS/400, di cui ne riportiamo le istruzioni relative : 

![ESE_010](http://localhost:3000/immagini/LOCMAP_A/ESE_010.png)
L'area (denominata "Stanza RPG") ha associate diverse caratteristiche : 
- La forma è rettangolare ed è definita da coordinate espresse in millesimi rispetto alle dimensioni dello schermo;
- L'attributo Fill è settato ad "ON" ed indica infatti il riempimento dell'area con un particolare colore; gli attributi Img e Txt indicano la possibilità di associare un testo o un immagine a tale area. Queste caratteristiche possono essere sempre visibili ("ALWAYS"), possono essere visibili solo al passaggio del mouse ("MOUSEON") o non attive ("OFF")
- Posso inoltre associare un'azione da associare al click del mouse in corrispondenza di tale area.

Entrando in "Sala Java" arriviamo all'immagine reale della stanza : 

![ESE_011](http://localhost:3000/immagini/LOCMAP_A/ESE_011.png)
Ora possiamo visualizzare, per esempio, i dati relativi ai dipendenti di questa sezione dell'azienda selezionando la singola persona.

![ESE_012](http://localhost:3000/immagini/LOCMAP_A/ESE_012.png)
