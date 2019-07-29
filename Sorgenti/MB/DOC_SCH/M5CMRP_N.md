# Scheda Pianificazione - navigazione
La scheda permette la navigazione nei suggerimenti con varie possibilità di ingresso e ordinamento, la scheda si configura e cambia comportamento a seconda della modalità scelta.

## Visualizzazione per articolo e opzionalmente per oggetto di rottura
![M5CMRP_022](http://localhost:3000/immagini/MBDOC_SCH-M5CMRP_N/M5CMRP_022.png)
La scheda è composta di 4 sezioni più un bottone di selezione : 
* **sezione albero in alto a sinistra** :  viene presentata la lista dei valori trovati per l'oggetto di riferimento (attributo dell'articolo inpostato nello scenario - Tab. M5B)
* **sezione albero al centro a sinistra** :  dato un oggetto di riferimento viene presentata la lista degli articoli che gli appartengono
* **bottone "scegli articolo" in basso a sinistra** :  che consente di inserire manualmente il codice dell'articolo di cui si vogliono vedere i consigli
* **sezione matrice in alto a destra** :  lista dei consigli per articolo (tutti gli articoli oppure quello selezionato)
* **sezione matrice in basso a destra** : quadro di pianificazione per il consiglio selezionato nella sezione in alto a destra

Sotto la matrice dei consigli sono presenti dei bottoni che permettono di eseguire delle azioni sui consigli che vi vengono trascinati sopra, le azioni previste sono : 
* **Applicazione suggerimento** :  per i consigli selezionati applica il suggerimento proposto (es. creazione ordine, spostamento di data, annullamento, ...) purchè nella fonte sia impostato il relativo programma di applicazione e l'utente sia autorizzato (classe M5CMRP)
* **Applicazione suggerimento con variazioni** :  come il precedente con la differenza che prima dell'applicazione propone una finestra dove si possono approtare delle variazioni (es. qtà, data, fornitore)
* **Applicazione suggerimento + modifica rilascio** :  esegue l'applicazione e dopo presenta il formato di manutenzione ordine (o riga ordine) per eventuali modifiche successive (es variazione prezzo)
* **Applicazione suggerimento con variazioni + modifica rilascio** :  è la combinazione dei precedenti
* **Modifica rilascio** :  si applica ai consigli applicati in precedenza (liv. = 8) e presenta il formato di manutenzione
* **Annulamento** :  annulla (livello = 9)  i consigli selezionati
* **Annullamento con annullamento impegni** :  si applica ai consigli di produzione o di conto lavoro, dopo l'annullamento del consiglio annulla anche gli impengi collegati

I bottoni di azione sui consigli posso agire su un singolo consiglio oppure su gruppi di consigli selezionati, la selezione dei consigli segue le regole di selezione proprie delle righe di matrice : 
* **control + click sulla colonna di selezione riga**, oppure **control + barra spaziatrice**, per selezionare una riga della matrice. L'operazione può essere ripetuta a piacere per n. righe
* per selezionare un gruppo di righe contigue, selezionare la riga superiore con control + click oppure control + barra spaziatrice come visto sopra, poi selezionare una riga sottostante con **control + shift + click**, oppure **control + shift + barra spaziatrice**, vengono selezionate tutte le righe comprese nell'intervallo
* le righe selezionate vengono evideziate con l'ombreggiatura
* per deselezionare una riga precedentemente selezionata, rifare control + click
* per deselezionare tutte le righe, click nella sezione ma fuori della matrice, oppure barra spaziatrice

### Classe copertura
Tra le indicazioni presenti nella matrice dei consigli una particolare menzione spetta alla **classe di copertura** ed al relativo semaforo :  se attivato nello scenario (Tab M5B) il flag di classificazione delle coperture il sistema calcola anche questo attributo del consiglio e lo presenta in matrice, i valori possibili e relativi significati sono : 
**1 = Copertura presente** :  esiste giacenza
**2 = Copertura futura senza anticipi** :  esiste un ordine (produzione / acquisto / ....) che non ha necessità di essere anticipato, cioè la data fonte va bene così
**3 = Copertura futura con anticipi** :  esiste un ordine che però ha necessità di essere anticipato
**4 = Copertura pianificata non scaduta** :  esiste un consiglio di creazione di un ordine con data futura
**5 = Copertura pianificata scaduta** :  esiste un consiglio di creazione di un ordine con data scaduta
La classificazione è peggiore aumentando il valore :  1 è la condizione migliore, 5 la peggiore

Per i suggerimenti di produzione o di conto lavoro, viene anche eseguita la stessa classificazione su tutti gli impegni collegati e si presenta la situazione di quello in condizioni peggiori

![M5CMRP_023](http://localhost:3000/immagini/MBDOC_SCH-M5CMRP_N/M5CMRP_023.png)
## Visualizzazione per oggetto di riferimento e suggerimento

![M5CMRP_024](http://localhost:3000/immagini/MBDOC_SCH-M5CMRP_N/M5CMRP_024.png)
Qui è possibile scegliere il livello, l'oggetto di riferimento e successivamente il tipo di consiglio (suddiviso tra consigli di pianificazione e consigli di azione sull'esistente).

In base alla selezione seguita viene presentata la lista degli articoli congruenti, per l'articolo scelto, nella matrice della sezione in basso, sono esposti i consigli associati.

## Visualizzazione per suggerimento

![M5CMRP_025](http://localhost:3000/immagini/MBDOC_SCH-M5CMRP_N/M5CMRP_025.png)
Come il precedente senza la selezione per livello e oggetto di riferimento.

## Visualizzazione per fonte

![M5CMRP_026](http://localhost:3000/immagini/MBDOC_SCH-M5CMRP_N/M5CMRP_026.png)
In questa scheda è possibile selezionare la fonte (esistente o futura) e vedere gli articoli ad essa appartenenti. Una volta scelto l'articolo vengono mostrati in basso i suoi consigli.
Nelle altre due matrici in basso è possibile vedere la lista dei consigli relativi alle fonti selezionate.

## Visualizzazione per ente

![M5CMRP_027](http://localhost:3000/immagini/MBDOC_SCH-M5CMRP_N/M5CMRP_027.png)
In questa scheda è possibile scegliere un ente (visualizzato suddiviso per tipo di ente) e successivamente le fonti relative. Una volta scelta la fonte, è possibile vedere nella matrice i consigli relativi a quella coppia ente-fonte, è anche possibile vedere tutti i consigli relativi ad un certo ente indipendentemente dalla fonte.

In basso è presente il pulsante "Scegli l'ente" (analogo a Scegli articolo) che consente di inserire direttamente il tipo e il codice dell'ente.

## Operazioni comuni
In tutte le visualizzazione possibili sono presenti caratteristiche e operazioni comuni.

### Indicazione Scenario plant
Nella parte alta della scheda è sempre presente l'indicazione dello scenario e del plant a cui ci stiamo riferendo.

### Scheda tabelle
Nella parte bassa di ogni scheda è presente un pulsante,  associato al tasto funzionale F10, che consente di passare alla scheda degli elementi di tabella interessati :  TA MAG del plant interessato, TA M5B  dello scenario e TA M51 * delle impostazioni generali MRP.

### Data limite - Elimina data limite
Nella parte bassa di ogni scheda sono presenti questi due bottoni, che si attivano con un click nella sezione della matrice dei consigli, che permettono di impostare o eliminare un flitro sulla data del consiglio.

### Cambio schema
In ogni scheda è possibile cambiare schema di visualizzazione selezionandone uno tra quelli presenti nell'elenco sulla destra, per tornare allo schema di default selezionare il "P/01".

### Cambio plant
Nel caso di pianificazione multiplant è possibile cambiare il plant scegliendolo dalla lista sulla destra. Se è gestito un unico plant tale lista non è presente.

### Navigazioni
Nella matrici contententi tutti i consigli relativi alle voci selezionate nelle varie schede è possibile cliccare con il tasto destro sul codice del suggerimento e scegliere la navigazione più opportuna.
Questo apre un'ulteriore sottoscheda con i dati relativi a quella navigazione. E' comunque sempre possibile saltare dalla navigazione alle visualizzazioni viste precedentemente.

![M5CMRP_028](http://localhost:3000/immagini/MBDOC_SCH-M5CMRP_N/M5CMRP_028.png)