## Obiettivo
Le sintesi hanno l'obiettivo di permettere l'associazione fino a 18 caratteristiche di aggregazione ad un oggetto. I programmi abilitati all'utilizzo delle sintesi potranno riferirsi a una di queste aggregazioni.

## Utilizzi
L'utilizzo dei raggruppamenti può risultare utile in ogni situazione in cui, per esigenze particolari (calcolo, interrogazione, stampa, ecc...), si vogliano raggruppare gli oggetti secondo determinate caratteristiche.
Tale classe trova uno dei suoi maggiori impieghi nel Master Production Schedule, in cui si trattano domanda e piano di produzione, non solo a livello di dettaglio (articolo, cliente, ecc...) o a livello sommarizzato per articolo, ma anche a livello di raggruppamento di entità.
A questo scopo sono previste delle funzioni per poter attribuire ai possibili soggetti trattati nei piani MPS delle classi di famiglie, attraverso le quali creare i raggruppamenti su cui costruire o verificare i piani.

## Definizioni

- >Classi di famiglie :  sono tutte le classificazioni create per gli oggetti presenti sul sistema (appartenenti alla tabella *CNTT).

- >Raggruppamento di entità :  sono tutti gli oggetti del sistema ai quali è stata associata almeno un classe di famiglia.


# Definizione raggruppamenti
La definizione dei raggruppamenti avviene attraverso la tabella C£S, nella quale definiamo per ogni elemento (raggruppamento di entità) : 

- le classi di famiglie attraverso cui riclassificarlo (esterne all'archivio dell'oggetto);
- le classi di riclassificazione interne all'archivio di appartenenza dell'oggetto e controllabili attraverso un programma specifico;
- la data di validità della classificazione.

Poichè l'attribuzione di un elemento di un'entità a una famiglia specifica potrebbe essere variabile nel tempo (time effective), la classificazione viene memorizzata per data, rendendo possibile : 

- l'analisi della variazione della composizione delle famiglie nel tempo;
- l'aggregazione differenziata di una vista piano in famiglie in funzione della data.

Sono definibili fino a 9 classi interne e 9 esterne di famiglie di riclassificazione.

## Gestione
La gestione dei raggruppamenti di entità è svolta dalla classe C£05.
Nel menù gestione raggruppamenti sono trattate le seguenti funzioni : 

- Gestione raggruppamenti di entità;
- Interrogazione raggruppamenti di entità;
- Esplosione raggruppamenti di entità.


## Gestione raggruppamenti
Permette di attribuire delle classi di famiglie ad una delle entità gestite e per ciascun elemento dell'entità scelta è possibile attribuire i valori voluti per classe di famiglia.
Il campo tipo raggruppamento permette di selezionare l'entità a cui si vogliono associare delle classi di famiglie.
Questo campo è collegato alla tabella C£S, su cui per ciascuna entità sono definiti i tipi di classificazione e le relative caratteristiche usate per classificare quella specifica entità.
## Data di validità
Se è stata specificata l'obbligatorietà della data nella tabella C£S, ritroviamo qui un campo necessario di immissione della data.

## F15
Il tasto> F15 permette, in fase di gestione dei raggruppamenti, di vedere i collegamenti di dettaglio, ossia di fare una sorta di risalita e vedere, per l'entità riclassificata, gli eventuali raggruppamenti in cui entra, a sua volta, come classe di riclassficazione.

## Parzializzazioni
Risulta importante notare come le parzializzazioni di un'entità possano essere fatte anche sulle riclassifiche per essa definite.

## Interrogazione raggruppamenti di entita'
Permette di esaminare tutti i raggruppamenti previsti, le rispettive entità e i valori associati.

## Interrogazione per esplosione/implosione
Permette di esaminare la gerarchia dei raggruppamenti previsti, le rispettive entità e i valori associati.

## Simulazione azioni su sintesi
Normalmente le funzioni sono chiamate all'interno dei programmi. Questa funzione permette di simulare l'effetto delle impostazioni indicate nelle tabelle, al fine di validare l'effetto che si otterrà nei programmi che le utilizzano.
Sono possibili le seguenti funzioni : 

- Reperire
-- Significato
-- Valore
-- Decodifica del valore
- Selezionare la sintesi desiderata
- Visualizzare le sintesi associate ad un oggetto
- Verificare l'esistenza delle sintesi per un oggetto


## Esempio applicativo

- Immaginiamo di volere legare all'entità clienti le entità esterne nazione e holding di appartenenza;
- creiamo, se non presente, l'elemento clienti all'interno della C£S;
- associamo le classi di famiglie nazioni e holding che possono essere tabellate;
- in "gestione del raggruppamento clienti" possiamo associare ad ogni cliente una nazione e una holding di appartenenza (nota 1);
- in "interrogazione" possiamo esaminare i clienti per nazione di appartenenza e per holding;


**Nota 1**; in alternativa alla attribuzione esplicita, utilizzando questa funzione, di nazione e holding di appartenenza a ciascun cliente possiamo utilizzare gli attributi oggetto esistenti per il cliente : 
* nell'elemento di tabella C£S di cui sopra si compila il campo "Attributi oggetto" con il sottosettore della tabella C£Z dove andremo a definire quali sono questi attributi (es. CL)
* nella tabella C£Z sottosettore CL inseriamo n. elementi, uno per ciascun attributo del cliente che vogliamo usare  e nell'elemento specifichiamo del campo "Codice attributo" l'attributo stesso (es.  I/15 per la nazione e U/HOLD per l'holding di appartenenza)
* riferirsi alla documentazione delle tabelle C£S e C£Z
