# Componente CUB
Il componente CUB si occupa dell'esportazione dei dati di matrice in sistemi di Business Intelligence, OLAP o similari
## Sistemi destinazione supportati
Il componente CUB è pensato per essere estendibile in maniera da poter supportare esportazioni verso differenti sistemi destinatari
Allo stato attuale è in grado di esportare dati verso : 

- Databeacon
- Pentaho


### Esportazione verso Databeacon
L'esportazione verso Databeacon è accessibile dal popup di sezione di qualunque matrice sotto Visualizza come... --> Cube.up
![cubpop](http://localhost:3000/immagini/LOCCUB_01/cubpop.png)La definizione di Databeacon come destinazione dell'esportazione viene dalla presenza nel setup dell'attributo Type valorizzato come "DTB".
La destinazione Databeacon è inoltre la destinazione di default qualora il nodo Type non sia presente o sia vuoto
Per la parametrizzazione esiste un file **application.xml** nella cartella LOOCUP_SET/CFG presente nell'installazione.
In tale setup, nell'elemento **UICube**, è possibile definire i parametri che configurano le informazioni necessarie a scatenare il processo di esportazione e visualizzazione.
Tale file viene caricato all'avvio di Loocup quindi, eventuali modifiche necessitano di riavvio per essere effettive.
Tali informazioni riguardano : 

- Directory dove trovare il motore di Databeacon :  attributo di setup **databeacondir** del file di configurazione precedentemente indicato. Per motore di Databeacon si intende la cartella d'installazione di Databeacon. Qualora, come generalmente accade, l'applicazione Databeacon sia installata su un server, bisogna procedere a creare una condivisione con diritti di lettura ed esecuzione sulla cartella di installazione. Ad esempio :  se Databeacon è installato sul server **SERVER01** nella cartella **C : \Programmi\Databeacon**, andrà creata una condivisione su tale cartella (immaginiamo di chiamare la condivisione **DatabeaconShare**). A questo punto il parametro di configurazione **databeacondir** dovrà essere valorizzazione con **\\SERVER01\DatabeaconShare**.
- Directory e script da richiamare per scatenare la generazione (forniti nell'installazione standard)


Altre informazioni possono essere passate, desunte o fissate nel corso della singola chiamata di esportazione e riguardano

- Directory di output :  cartella temporanea dell'utente windows
- Cosa Aprire (file indice o file del cubo) :  attributo **Open** del setup contenuto nel XML. I valori previsti sono
-- **File** :  per aprire direttamente il cubo
-- **Idx** :  per aprire il file di indice dei cubi
-- **None** :  per non aprire nulla
- Nome del cubo da generare :  viene preso dal Titolo1 del nodo Service del documento XML contenente i dati


Alla fine del processo di generazione il cubo viene aperto utilizzando uno dei browser installati, secondo la seguente logica

- Su Windows XP o precedenti viene sempre chiamato Internet Explorer (per le caratteristiche di Databeacon Internet Explorer risulta la soluzione migliore)
- Su Windows 7 o Windows 2008 viene chiamato il browser di default.


**N.B.** :  Non sono stati riscontrati problemi particolari su qualunque sistema nel caso che il browser sia Internet Explorer o Firefox Mozilla. Nel caso si utilizzi Chrome può verificarsi che l'avvio di Databeacon impieghi diverse decine di secondi. In attesa della risoluzione di questo problema se ne tenga conto

### Esportazione verso Pentaho
La definizione di Databeacon come destinazione dell'esportazione viene dalla presenza nel setup dell'attributo Type valorizzato come "PHO".
