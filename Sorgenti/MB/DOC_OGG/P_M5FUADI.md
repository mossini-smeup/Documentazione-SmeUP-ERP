# Generalità
L'analisi disponibilità è uno degli strumenti fondamentali usati in azienda per sapere lo stato di un articolo in termini di richieste e conferimenti datati nel tempo.

Ad esempio può essere usato per fornire ad un cliente una situazione di un determinato articolo : 

- quanto è disponibile in giacenza
- se e quando sarà prodotto
- quanti e quali ordini di vendita (o di produzione o di acquisto) sono al momento in corso
- quando sono previste le consegne.


## Formato richiesta
L'analisi disponibilità parte dal seguente formato : 

![M5_02_01](http://localhost:3000/immagini/MBDOC_OGG-P_M5FUADI/M5_02_01.png)
Con scelta fonti si inserisce il gruppo fonte con il quale eseguire l'analisi.

## Funzioni di analisi disponibilità
La funzione premette diverse analisi, usare il carattere '/' per visualizzarle : 

![M5_02_02](http://localhost:3000/immagini/MBDOC_OGG-P_M5FUADI/M5_02_02.png)
### DET - Dettaglio per data
presenta i risultati dell'analisi disponibilità a livello di dettaglio fonte ordinati per data : 

![M5_02_03](http://localhost:3000/immagini/MBDOC_OGG-P_M5FUADI/M5_02_03.png)
da questa lista è possibile : 

_1_F18 - rilanciare la pianificazione per l'articolo
(in simulazione / esecuzione, con scrittura impegni o anche presentazione del risultato, con applicazione dei suggerimenti) : 

![M5_02_04](http://localhost:3000/immagini/MBDOC_OGG-P_M5FUADI/M5_02_04.png)
_1_F19 - Elencare gli assiemi dell'articolo

_1_F20 - Presentare le quantità per fonte sviluppate su una scala temporale,
data una periodicità ed una data di inizio periodo : 

![M5_02_05](http://localhost:3000/immagini/MBDOC_OGG-P_M5FUADI/M5_02_05.png)
### DFO - Dettaglio per fonte
presenta i risultati dell'analisi disponibilità a livello di dettaglio fonte ordinati per fonte

### RFO - Riepilogo per fonte
Presenta i risultati dell'analisi disponibilità riepilogati a livello fonte : 

![M5_02_06](http://localhost:3000/immagini/MBDOC_OGG-P_M5FUADI/M5_02_06.png)
### RDT - Riepilogo per giorno
Presenta i risultati dell'analisi disponibilità riepilogati a livello giorno : 

![M5_02_07](http://localhost:3000/immagini/MBDOC_OGG-P_M5FUADI/M5_02_07.png)
### SIN - Sviluppo su griglia date
Presenta i risultati delle quantità per fonte sviluppate su una scala temporale, data una periodicità ed una data di inizio periodo (come F20 da lista analisi disponibilità).

### SOG - Sintesi su oggetto
Se si attiva questa funzione deve essere stabilito su quale oggetto si vuole la sintesi, gli oggetti su cui è prevista la sintesi sono elencati sotto l'intestazione "Altri limiti", per definire su quale oggetto vogliamo la sintesi dobbiamo mettere la corrispondente lettera alfabetica nel campo segnalato (nell'esempio per avere la sintesi su fornitore mettere C e come tipo ente mettere FOR) : 

![M5_02_08](http://localhost:3000/immagini/MBDOC_OGG-P_M5FUADI/M5_02_08.png)
il risultato dell'interrogazione è il seguente : 

![M5_02_09](http://localhost:3000/immagini/MBDOC_OGG-P_M5FUADI/M5_02_09.png)
La colonna _3_"Altri limiti" serve anche per definire delle parzializzazioni, se vogliamo ad esempio avere un'analisi con funzione DET limitata ad un fornitore dovremo compilare l'interrogazione come segue : 

![M5_02_10](http://localhost:3000/immagini/MBDOC_OGG-P_M5FUADI/M5_02_10.png)
se inoltre è selezionato _3_"Intestazione Limiti" nella lista sarà emessa una testatina con la ragione sociale del fornitore : 

![M5_02_11](http://localhost:3000/immagini/MBDOC_OGG-P_M5FUADI/M5_02_11.png)
_3_Nota, se è stato inserito un limite per data massima la lista viene limitata alla data inserita, se oltre alla data massima viene impostato il campo "Limite impegni" la lista viene limitata solo per le fonti negative (impegni).

## Disponibilità componenti
Per l'articolo e gli eventuali limiti impostati con F11 si verifica la disponibilità dei componenti, si passa prima attraverso un formato di selezione (nota, se il campo 'Sempre disponibili' viene impostato con il valore 3 il sistema non segnala come mancanti gli articoli esclusi dalla gestione di magazzino e dalla pianificazione) : 

![M5_02_12](http://localhost:3000/immagini/MBDOC_OGG-P_M5FUADI/M5_02_12.png)
La lista presenta lo stato disponibilità dei componenti segnalando in reverse quelli mancanti e cambiando colore in funzione della politica di pianificazione (acquisto, produzione, conto lavoro) : 

![M5_02_13](http://localhost:3000/immagini/MBDOC_OGG-P_M5FUADI/M5_02_13.png)
# Stampa disponibilità
Permette di stampare l'analisi disponibilità, ottenuta con una delle funzioni viste per l'interrogazione, per tutti gli articoli appartenenti ad una lista (filtrata dalle parzializzazioni interne ed esterne degli articoli) : 

![M5_02_14](http://localhost:3000/immagini/MBDOC_OGG-P_M5FUADI/M5_02_14.png)