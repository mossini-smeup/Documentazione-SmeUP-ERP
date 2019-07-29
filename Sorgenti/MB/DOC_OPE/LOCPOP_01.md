## Introduzione
Il Popup è il componente di Looc.UP che si propone di mostrare le azioni disponibili all'utente all'intenro di un menù a tendina che si apre cliccando con il tasto destro su un oggetto o sulla linguetta di una subsezione.

Distinguiamo due tipologie di popup : 
 * Popup di subsezione :  presenta le azioni associate al componente contenuto nella subsezione. Per visualizzarlo è sufficiente cliccare con il tasto destro sulla linguetta della subsezione : 

![LOCPOP_007](http://localhost:3000/immagini/MBDOC_OPE-LOCPOP_01/LOCPOP_007.png)
 * Popup di oggetto :  presenta le azioni associate all'oggetto di cui si visualizza il popup. Per visualizzarlo è sufficiente cliccare con il tasto destro sull'istanza dell'oggetto : 

![LOCPOP_008](http://localhost:3000/immagini/MBDOC_OPE-LOCPOP_01/LOCPOP_008.png)
## Struttura e Terminologia
Un popup si presenta generalmente come una lista di azioni eseguibili strutturata in livelli. Cliccando con il tasto destro del mouse su un oggetto o su una linguetta di subsezione viene restituito il popup di primo livello. Nel caso in cui le voci visualizzate nel popup di primo livello siano strutturate in sottolivelli viene visualizzata una freccetta a destra della voce; per accedere a un sottolivello è sufficiente posizionarsi sulla voce di livello superiore : 

![LOCPOP_009](http://localhost:3000/immagini/MBDOC_OPE-LOCPOP_01/LOCPOP_009.png)
Le azioni contenute nei popup sono sotto autorizzazione, pertanto il contenuto visualizzato da un utente potrebbe essere diverso da quello visualizzato da un altro utente.

## Popup di subsezione

Il primo livello di popup di subsezione è composto da un insieme di voci fisse, riscontrabili per qualsiasi componente contenuto nella subsezione. In particolare le azioni generalmente disponibili per gli utenti sono : 

 * Aggiorna :  permette di aggiornare il contenuto della sezione
 * Ingandisci :  apre la sezione in una nuova scheda
 * Aggiungi scheda a preferiti :  permette di aggiungere la scheda al menù dei preferiti
 * Impostazioni :  permette di accedere al sottolivello di gestione del setup del componente. Il sottolivello è composto dalle voci : 
 ** Setup utente :  se sono presenti altri setup oltre a quello di default vengono visualizzati all'interno del popup
 ** Default :  permette di visualizzare il componente con il setup di default
 ** Salva :  permette di salvare il setup attualmente visualizzato
 ** Salva setup come default :  permette di salvare il setup attualmente visualizzato e assegnarlo come default all'utente
 ** Salva con nome :  permette di salvare il setup assegnandogli un nome
 ** Gestione setup :  apre il gestore dei setup : 
![LOCPOP_011](http://localhost:3000/immagini/MBDOC_OPE-LOCPOP_01/LOCPOP_011.png) * Visualizza come :  permette di accedere al sottolivello contenente le visualizzazioni alternative disponibili per il componente
 * Stampa della sezione :  permette di stampare il contenuto della sezione
 * Screenshot della Sezione :  esegue una 'fotografia' della sezione : 
![LOCPOP_010](http://localhost:3000/immagini/MBDOC_OPE-LOCPOP_01/LOCPOP_010.png) * Help della scheda :  se è presente della documentazione legata alla scheda consente di visualizzarla

Le visualizzioni alternative disponibili per i componenti variano al variare del componente stesso. Si rimanda alla documentazione operativa dei singoli compenenti per la conoscenza delle visualizzazioni alternative disponibili.

## Popup di oggetto

Il popup di oggetto è suddiviso in un insieme di azioni standard disponibili per qualsiasi oggetto, un insieme di voci specifiche della tipolgoia di oggetto e un insieme di funzioni personalizzate per l'azienda.
Le azioni disponibili per qualsiasi oggetto sono : 
 * Preferiti :  permette di aggiungere l'istanza di oggetto al menù dei preferiti
 * Scheda XXX :  visualizza la scheda dell'oggetto che ha descrizione XXX (è l'oggetto su cui si è cliccato con il tasto destro)
 * Scheda altro YYY :  visualizza la scheda di un altro articolo di tipologia YYY. Selezionando questa azione verrà richiesto il codice dell'oggetto di cui si vuole visualizzare la scheda
 * Gestione / Workflow :  permette di accedere a un sottomenù nel quale sono riportate le azioni per la gestione dell'oggetto (modifica, copia, stampa, ecc.)
 * Specifiche azienda :  permette di accedere a un sottomenù nel quale sono riportate tutte la azioni personalizzate richieste dall'azienda. Ad esempio per l'oggetto articolo potrebbe essere inserita l'azione 'Esplosione distinta base' che consente di ottenere la distinta base dettagliata dell'articolo : 
![LOCPOP_012](http://localhost:3000/immagini/MBDOC_OPE-LOCPOP_01/LOCPOP_012.png)