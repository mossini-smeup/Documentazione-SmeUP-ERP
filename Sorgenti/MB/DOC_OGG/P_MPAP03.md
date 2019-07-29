## Azioni tra due viste
### Introduzione
Partendo da due viste dello stesso oggetto, o della stessa coppia di oggetti, si ottiene una terza vista, a pari chiave, applicando un operatore alle quantità dello stesso periodo.

### Operatori PRIOR e PRIORF (Priorità vista)
 * **PRIOR** :  copia nel risultato la vista 1 se ha almeno un elemento diverso da zero, altrimenti copia la vista 2. Con questo operatore un risultato viene sempre scritto, in quanto non può verificarsi il caso di contemporanea assenza di entrambe le viste.
 * **PRIORF** :  copia nel risultato la vista 1 se presente il record, altrimenti copia la vista 2. Con questo operatore un risultato viene sempre scritto, in quanto non può verificarsi il caso di contemporanea assenza di entrambe le viste.

![MPAP03_01](http://localhost:3000/immagini/MBDOC_OGG-P_MPAP03/MPAP03_01.png)
### Operatori SIV2 e SIV2F (Selezione vista da presenza)
 * **S IV2** :  se la vista 2 ha almeno un campo diverso da zero, copia nel risultato la vista 1, a patto che quest'ultima esista. Con questo operatore non è detto che venga scritta una vista.
 * **SIV2F** :  se presente la vista 2, copia nel risultato la vista 1, a patto che quest'ultima esista. Con questo operatore non è detto che venga scritta una vista.

![MPAP03_02](http://localhost:3000/immagini/MBDOC_OGG-P_MPAP03/MPAP03_02.png)
### Operatori NOV2 e NOV2F (Selezione vista da assenza)
 * **NOV2** :  se la vista 2 esiste e ha tutti i campi uguali a zero, copia nel risultato la vista 1, a patto che quest'ultima esista. Con questo operatore non è detto che venga scritta una vista.
 * **NOV2F** :  se assente la vista 2, copia ne risultato la vista 1, a patto che quest'ultima esista. Con questo operatore non è detto che venga scritta una vista.

![MPAP03_03](http://localhost:3000/immagini/MBDOC_OGG-P_MPAP03/MPAP03_03.png)
### Operatore COLF (Completamento oltre frontiera)
Operatore che scrive, nella vista del risultato, parte delle quantità della vista 2, in base al riempimento (frontiera) della vista 1.

![MPAP03_04](http://localhost:3000/immagini/MBDOC_OGG-P_MPAP03/MPAP03_04.png)