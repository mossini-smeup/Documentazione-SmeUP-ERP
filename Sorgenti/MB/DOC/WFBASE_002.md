### Caratteristiche dell'OR-Join
Nella descrizione dei requisiti sui luoghi, è stato segnalato che esse permettono di implementare l'OR-Join, vale a dire la riunificazione di più rami alternativi.

Normalmente ciò non è necessario, in quanto con una particolare descrizione del processo, lo si può realizzare senza definire esplicitamente requisiti sui luoghi.

Per far sì che la transizione 3 sia possibile se c'è un token nel luogo A oppure B (vale a dire che è stata eseguita la transizione 1 oppure la 2) è necessario introdurre un requisito ai luoghi sulla transizione 3 : 
![Fig_007](http://localhost:3000/immagini/WFBASE_002/Fig_007.png)

Ristrutturando il processo non è più necessario introdurre questo requisito. Dato che le transazioni 1 e 2 sono alternative (derivano da un OR-Split), soltanto una di esse verrà eseguita, e quindi nel luogo C si produrrà un token : 
![Fig_008](http://localhost:3000/immagini/WFBASE_002/Fig_008.png)Dopo di ciò il processo prosegue in modo analogo al caso precedente


### Implementazione del loop
È possibile realizzare loop sia in modalità Until (eseguito almeno una volta) sia in modalità While (eseguito anche zero volte).

Esempio di implementazione di loop Until per la transizione 1 :  si aggiunge una conseguenza ai luoghi sulla transizione 2.
In base ai parametri del processo, verrà aggiunto un token al luogo A (ripetizione del loop) o al luogo C (uscita dal loop) : 
![Fig_009](http://localhost:3000/immagini/WFBASE_002/Fig_009.png)
Esempio di implementazione di loop While per la transizione 2 :  si aggiunge una conseguenza ai luoghi sulla transizione 1.
In base ai parameri del processo, verrà aggiunto un token al luogo B (ingresso nel loop) o al luogo D (superamento del loop).
![Fig_010](http://localhost:3000/immagini/WFBASE_002/Fig_010.png)

### Biforcazioni
Una biforcazione può essere costutuita da un arco che si biforca in due (o più) luoghi
//// immagine FIG.001.DOC
oppure da un luogo che si biforca in due (o più) archi.
//// immagine FIG.002.DOC
Il primo caso rappresenta un And-Split implicito (se non impostate conseguenze sui luoghi), oppure un Or-Split  (se impostate conseguenze sui luoghi), che ne attivano uno solo in funzione del verificarsi di una condizione.
Il secondo caso invece costituisce un'anomalia o quantomeno una incertezza di comportamento. Il token sul luogo  rende pronte entambe le transizioni a valle. La prima che viene eseguita elimina il token e rende di nuovo non prota l'altra. Si produce quindi una indeterminazione di comportamento che può essere indesiderata.
Un utilizzo possibile di questa struttura può essere quello in cui le transizioni hanno requisiti esterni mutuamente esclusivi, in modo da eliminare l'indeterminazione del verificarsi di entrambi, introducendo una preferenza. (*)
Al verificarsi di uno di essi si attiva la transizione che consuma il token e rende definitivamente non pronta l'altra transizione.
Si può utilizzare questa struttura anche per modellare una transizione in cui il primo utente che la
dichiara, eliminando il token di ingresso, rende di nuovo non pronte le altre transizioni.

(*) Ad esempio, dati i requisiti R1 e R2 con preferenza R1, si completa il requisito R2 con la negazione di R2 (R2 AND NOT(R1)); in questo caso al verificarsi contemporaneo di R1 e R2 solo il primo requisito è soddisfatto.

### Riunificazione
Una riunificazione può essere costutuita da due luoghi che concorrono in una transizione.
//// immagine FIG.003.DOC
oppure da due transizioni che concorrono in un luogo.
//// immagine FIG.004.DOC
Il primo caso rappresenta un And-Join implicito (se non impostati requisiti sui luoghi), oppure un Or-Join (se impostati requisiti sui luoghi, che rendono pronta la transizione in base al requisito (Or se almeno un token presente, X-Or se solo un token presente, oppure un requisito speciale implementato ad hoc).
Il secondo caso rappresenta un Or-Join implicito, se le transizoni concorrenti provengono da due rami aperti con un Or-Split.
Se invece sono rami aperti con un And-Split questo caso rappresenta un'incongruenza nella descrizione , in quanto non è possibile controllare che entambe le transizioni siano eseguite per poter proseguire il processo.

### Apertura e chiusura rami
Dalle considerazioni precedenti si evidenzia l'importanza del corretto disegno del processo.
La figura seguente riporta i due principali esempi di processo :  rami paralleli (and) o alternativi (or).
L'unica definizione esplicita da introdurre nel processo sono le conseguenze sui luoghi applicate alla prima transizione nel caso del processo in or.
//// immagine FIG.005.DOC
