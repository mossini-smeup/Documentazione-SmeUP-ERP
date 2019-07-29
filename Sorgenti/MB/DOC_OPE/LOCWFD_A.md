# Il componente WFD (Workflow Designer)

## Informazioni generali

Il nuovo componente Workflow Designer si propone di realizzare l'editing degli script di workflow (WFA) in maniera grafica, attraverso una forma proprietaria del formalismo delle Reti di Petri.

E' prevista anche una modalità di sola visualizzazione, utilizzata per mostrare lo stato di un ordine.

## L'editor grafico
![LOCWFD_01](http://localhost:3000/immagini/MBDOC_OPE-LOCWFD_A/LOCWFD_01.png)
L'editor grafico è un modulo di LoocUp, come tale la sua struttura è comune a tutti gli altri moduli :  dall'alto al basso troviamo i menù, la barra del titolo, l'area specifica per ogni modulo e la barra dei pulsanti.
Ci concentreremo sull'area specifica. Questa è composta da due parti :  in alto una pulsantiera e nella parte centrale il diagramma del workflow.
La pulsantiera fornisce l'accesso a tutte le funzionalità grafiche ed è divisa in vari gruppi di pulsanti.
Analizziamo questi gruppi, procedendo da sinistra a destra.

### Gruppo pulsanti di selezione
![LOCWFD_02](http://localhost:3000/immagini/MBDOC_OPE-LOCWFD_A/LOCWFD_02.png)
E' composto da un solo pulsante. Quando questo pulsante è selezionato consente di scegliere uno o più elementi grafici. Per scegliere un solo elemento basta cliccarci sopra,  mentre se si desidera  la selezione multipla è necessario mantenere premuto il tasto sinistro del mouse e trascinare fino a selezionare gli elementi grafici di interesse. Al termine della procedura le transizioni e i luoghi selezionati presenteranno dei quadrati bianchi ai lati, mentre gli archi presenteranno dei pallini verdi.
![LOCWFD_03](http://localhost:3000/immagini/MBDOC_OPE-LOCWFD_A/LOCWFD_03.png)
 Nel centro di un arco o di una transizione selezionata comparirà un pallino rosso, posizionandosi sopra questo il mouse assumerà la forma di 4 frecce,

![LOCWFD_04](http://localhost:3000/immagini/MBDOC_OPE-LOCWFD_A/LOCWFD_04.png)
questo indica la possibilità di creare un arco di collegamento.
Quando il mouse è dentro il perimetro della figura, ma non è sopra il pallino rosso centrale, assume la forma di una mano, per indicare la possibilità di spostare l'elemento o gli elementi selezionati.
**NOTA** Nel caso in cui si desiderasse spostare elementi grafici ad un livello di zoom molto elevato, potrebbe capitare che non esista spazio per "prendere" una figura :  Il pallino rosso occuperebbe tutta l'area e l'azione diventerebbe non sposta ma crea arco. In questo caso o si riduce il livello di zoom prima di trascinare o si utilizzano le frecce di spostamento.

### Gruppo pulsanti creazione elementi grafici
![LOCWFD_05](http://localhost:3000/immagini/MBDOC_OPE-LOCWFD_A/LOCWFD_05.png)
E' composto da : 
 * Pulsante per la creazione di una transizione
 * Pulsante per la creazione di un luogo iniziale
 * Pulsante per la creazione di un luogo
 * Pulsante per la creazione di un luogo finale
 * Pulsante per la creazione di un arco.
Quando uno dei primi 4 pulsanti è selezionato consente di creare una transizioni o un arco. Per la creazione posizionarsi con il mouse nell'area del workflow e cliccare. Ad ogni click comparirà un elemento grafico del tipo selezionato. L'elemento avrà un nome e una descrizione predefinita, ad esempio TR_1 :  Nuova transizione, TR_2 ecc ecc. Si può cambiare il codice e la descrizione agendo direttamente sull'etichetta che compare sotto l'elemento grafico, tramite un doppio click, l'etichetta diventerà editabile e consentirà la modifica. Il termine della modifica averrà o con il tasto enter o cliccando esternamente. Va posta attenzione alla sintassi :  il codice termina con il simbolo dei " : " e  quanto segue è la descrizione.
Attenzione inoltre ai luoghi non collegati a transizioni :  tutti questi elementi grafici nel momento in cui il grafico viene salvato (e quindi convertito in script) vengono persi.
Per la creazione di archi si può, una volta selezionato l'apposito pulsante, posizionarsi nel centro di una transizione e un luogo, premere il tasto destro e trascinare fino al luogo o alla transizione da collegare.  Analoga procedura si può seguire quando si è in modalità di selezione.

### Gruppo pulsanti di gestione degli allineamenti
![LOCWFD_06](http://localhost:3000/immagini/MBDOC_OPE-LOCWFD_A/LOCWFD_06.png)
E' composto da : 
 * Pulsante per allineare a destra
 * Pulsante per allineare a sinistra
 * Pulsante per allineare sulla mezzeria verticale
 * Pulsante per allineare in alto
 * Pulsante per allineare in basso
 * Pulsante per allineare sulla mezzeria orizzontale
**NOTA** Tutti questi pulsanti si attivano solo quando sono stati selezionati 2 o più elementi grafici


### Gruppo di pulsanti per la gestione degli spostamenti
![LOCWFD_07](http://localhost:3000/immagini/MBDOC_OPE-LOCWFD_A/LOCWFD_07.png)
E' composto da : 
 * Sposta a sinistra
 * Sposta a destra
 * Sposta in basso
 * Sposta in alto
Questi pulsanti agiscono su uno o più elementi grafici

### Gruppo di pulsanti per la gestione delle posizioni relative
![LOCWFD_08](http://localhost:3000/immagini/MBDOC_OPE-LOCWFD_A/LOCWFD_08.png)
E' composto da : 
 * Pulsante per allontanare due o più luoghi e  o transizioni
 * Pulsante per avvicinare due o più luoghi e  o transizioni
Questi pulsanti si attivano solo se sono selezionati due o più elementi grafici, ogni click aumenta o diminuisce la distanza dal baricentro della selezione


### Altri pulsanti
![LOCWFD_09](http://localhost:3000/immagini/MBDOC_OPE-LOCWFD_A/LOCWFD_09.png)Sono 3 gruppi : 
 * Gruppo pulsanti gestione Zoom e griglia : 
 ** Pulsante per definire il fattore di Zoom.
 ** Pulsante per mostrare/nascondere la griglia di allineamento
 * Gruppo pulsanti  gestione esportazione
 ** E' composto dal pulsante per la esportazione. Consente di salvare il workflow in un file esterno all'AS400, scegliendo tra vari formati, compreso quello di SmeUp.
 * Gruppo pulsanti gestione undo e redo
 ** Undo
 ** Redo


## Il visualizzatore di ordini
![LOCWFD_10](http://localhost:3000/immagini/MBDOC_OPE-LOCWFD_A/LOCWFD_10.png)
Il componente WFD in modalità visualizzatore di ordini, aggiunge delle informazioni su ogni impegno aggiungendo due icone in basso.
In basso a sinistra troviamo l'informazione sull'esecuzione dell'impegno :  un baffo verde indica che è stato eseguito, una croce rossa indica che non è  è stato eseguito.
In basso a destra troviamo l'informazione sullo stato dell'impegno, rappresentato con un quadratino di vari colori secondo la seguente tabella : 

 :  : IMG P([IMG : V2;WF_01;1]) H(20) W(20) R(10) A(L) C(Distribuito) ImgRef(Distribuito)
 :  : IMG P([IMG : V2;WF_01;2]) H(20) W(20) R(10) A(L) C(Preso in carico) ImgRef(Preso in carico)
 :  : IMG P([IMG : V2;WF_01;3]) H(20) W(20) R(10) A(L) C(Pronto) ImgRef(Pronto)
 :  : IMG P([IMG : V2;WF_01;4]) H(20) W(20) R(10) A(L) C(Assegnabile) ImgRef(Assegnabile)
 :  : IMG P([IMG : V2;WF_01;5]) H(20) W(20) R(10) A(L) C(Non pronto) ImgRef(Non pronto)
 :  : IMG P([IMG : V2;WF_01;6]) H(20) W(20) R(10) A(L) C(Attivabile) ImgRef(Attivabile)

Lo stato eseguito è rappresentato da un baffetto verde, mentre lo stato non eseguito è rappresentato da una X bianca su sfondo rosso.


