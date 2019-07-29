# COLONNE MATRICE

## Definizione
La Matrice ha funzionalità standard e funzionalità legate al fatto che sia o meno di aggiornamento e che abbia o meno filtri a disposizione.
 :  : DEC T(MB) P(DOC_VOC) K(GLO_LO)

## Ordinamento
Per ordinare una matrice è possibile cliccare sull'intestazione della colonna scelta per l'ordinamento, che può essere ascendente o discentente. Il primo click ordina la colonna in modo ascendente, il secondo in modo discendente. Cliccando comparirà anche un triangolino grigio chiaro che punterà in basso o in alto a seconda del tipo di ordinamento. Sulle matrici raggruppate, è anche possibile ordinare più colonne contemporaneamente, selezionando le colonne interessate tenendo premuto SHIFT.

![LOCEXB_050](http://localhost:3000/immagini/MBDOC_OPE-LOCEXB_A2/LOCEXB_050.png)Valore Residuo)

## Sequenza colonne
**Modifica sequenza colonne**
Per modificare l'ordinamento delle colonne della matrice è sufficiente trascinare la colonna (tenendo cliccato sulla relativa intestazione) nella posizione in cui la si desidera visualizzare. L'immagine mostra come spostare la colonna "Ragione sociale" tra il "Tipo contatto" e la "Valuta".

![LOCEXB_051](http://localhost:3000/immagini/MBDOC_OPE-LOCEXB_A2/LOCEXB_051.png)
## Filtro
Si tratta, anche in questo caso, di una funzione opzionale; nel caso in cui i filtri siano attivi, è possibile visualizzare delle frecce nere sull'intestazione delle colonne. Cliccandovi sopra comparirà un elenco dei valori presenti e in testa le voci (All) e (Custom...) . Se presenti valori nulli avremo anche le voci (Blanks) e (Non blanks) . I filtri di una matrice funzionano come i filtri di Excel.

![LOCEXB_068](http://localhost:3000/immagini/MBDOC_OPE-LOCEXB_A2/LOCEXB_068.png)
Quando viene applicato un filtro, la freccia sull'intestazione della colonna filtrata cambia colore, da nero a blu.
È possibile applicare contemporaneamente più filtri ad una matrice. In basso a sinistra vengono evidenziati i filtri attivi, da li è possibile eliminarli contemporaneamente (cliccando sulla X, come nell'esempio in figura) oppure agendo manualmente sui singoli filtri. Come si può notare ancora nell'esempio, i filtri vengono applicati in AND.

![LOCEXB_056](http://localhost:3000/immagini/MBDOC_OPE-LOCEXB_A2/LOCEXB_056.png)'Utente creazione")


## Raggruppamento
Una funzionalità opzionale legata alla matrice è quella di poter raggruppare i record per uno o più dei suoi campi. In questi casi trascinando l'intestazione della colonna di raggruppamento nello spazio grigio sopra la matrice, i dati verranno raggruppati secondo il contenuto della colonna, ad esempio, nella figura, è stato eseguito un raggruppamento per "Ragione sociale" : 

![LOCEXB_052](http://localhost:3000/immagini/MBDOC_OPE-LOCEXB_A2/LOCEXB_052.png)Utilizzando i bottoni posizionati nella pulsantiera, è possibile aprire o chiudere la matrice (si veda il paragrafo 'Pulsanti specifici').
La figura è un esempio di raggruppamento per più di un criterio (quindi secondo più colonne), ovviamente seguendo un ordine di raggruppamento sensato.

![LOCEXB_055](http://localhost:3000/immagini/MBDOC_OPE-LOCEXB_A2/LOCEXB_055.png)Per chiudere un singolo raggruppamento è possibile cliccare due volte sul titolo del gruppo oppure selezionare il gruppo e premere la freccia sinistra o ancora cliccare sul '-' posto sull'etichetta del titolo del gruppo.


## Elimina colonne
Per rimuovere una colonna dalla visualizzazione è possibile cliccare sulla sua intestazione e, tenendo premuto, trascinarla verso l'alto al di fuori dell'area della matrice.
La colonna sarà sostanzialmente nascosta, quando invece si desidererà visualizzarla nuovamente, con F5 si potrà procedere ad aggiornare la scheda e quindi la matrice.

![LOCEXB_085](http://localhost:3000/immagini/MBDOC_OPE-LOCEXB_A2/LOCEXB_085.png)
## Funzioni di aggregazione

Sono delle funzioni abilitabili sulle colonne di tipo numerico (quelle di colore verde) cliccando con il tasto destro sull'intestazione della colonna e scegliendo _Totalizzazioni >> Abilita. Una volta abilitate le totalizzazioni comparirà una barra grigia ai piedi della matrice, a questo punto è possibile visualizzare le totalizzazioni in 2 modi : 
-- cliccando con il tasto destro sull'intestazione della colonna
-- cliccando con il tasto destro alla base della matrice sulla barra grigia appena comparsa all'altezza della colonna di cui voglio visualizzare la totalizzazione.
Ora non rimane che la scelta del tipo di totalizzazione, la scelta può ricadere su :  Somma, Minimo, Massimo, Conta o Media. Il risultato sarà visualizzato sulla barra grigia in basso.

![LOCEXB_060](http://localhost:3000/immagini/MBDOC_OPE-LOCEXB_A2/LOCEXB_060.png)
![LOCEXB_061](http://localhost:3000/immagini/MBDOC_OPE-LOCEXB_A2/LOCEXB_061.png)
## Colonne aggiuntive

Ora passiamo ad un argomento che verrà anche ripreso nella sezione "PopUp colonne", le colonne aggiuntive delle matrici.

![LOCEXB_086](http://localhost:3000/immagini/MBDOC_OPE-LOCEXB_A2/LOCEXB_086.png)
Questa funzione permette di aggiungere nella matrice, delle colonne in più, associate alle colonne tipizzate pre-esistenti. Infatti, a seconda della colonna sulla quale apro il popup (come posso vedere dalle due immagini d'esempio), avrò a disposizione diverse colonne aggiungibili, questo perchè a seconda dell'oggetto associato a quella determinata colonna avrò differenti oggetti associati.

![LOCEXB_087](http://localhost:3000/immagini/MBDOC_OPE-LOCEXB_A2/LOCEXB_087.png)
E' possibile inviare nel carrello anche tutti i campi di una colonna aggiuntiva, cliccando con il tasto destro del mouse sull'intestazione di una colonna e successivamente, nel menù a tendina che appare selezionare 'Aggiungi i record selezionati al carrello XXX'

Per degli esempi dettagliati sulle colonne aggiuntive riferirsi a
**My LoocUp --> Per lo sviluppatore --> Esempi --> Capire LoocUp --> 01.CMP --> 01.CMP.EXB :  Matrice --> Colonne - Colonne aggiuntive

## PopUp colonne
![LOCEXB_071](http://localhost:3000/immagini/MBDOC_OPE-LOCEXB_A2/LOCEXB_071.png)
Sulle colonne ci sono vari voci del PopUp : 
 * Le totalizzazioni, che sono operazioni che si possono eseguire su una colonna di tipo numerico. Queste funzioni sono :  somma, media, minimo, massimo e conta.
 * La parte relativa al grafico (Marca la colonna come asse, Marca la colonna come serie, Visualizza il grafico associato e talvolta la Funzioni statistiche della serie)
 * Colonne aggiuntive, sono le colonne che posso voler aggiungere nella matrice, quando la colonna contiene un'oggetto. Le colonne aggiuntive saranno attributi relativi all'oggetto stesso; se invece, la colonna non è tipizzata allora non c'è la possibilità di aggiungere colonne.
 * Help della colonna


## Carrello
Per tutto quello che concerne il concetto e l'utilizzo del carrello fare riferimento alla documentazione relativa.
- [Carrello](Sorgenti/MB/DOC/B£CARR)

E' possibile aggiungere al carrello utente o ad un altro carrello specifico alcuni campi o oggetti selezionati in una matrice.
Se sono disponibili più carrelli, dalla finestra popup si possono veder indicati tutti i carrelli disponibili.

![LOCEXB_083](http://localhost:3000/immagini/MBDOC_OPE-LOCEXB_A2/LOCEXB_083.png)
Attenzione :  questa funzionalità aggiunge al carrello, per le righe selezionate, la colonna su cui ho cliccato per fare uscire il popup.
Ad esempio :  nell'immagine ho selezionato 6 righe e ho cliccato sulla seconda colonna (oggetto) per avere il popup; in questo caso nel carrello
vengono inseriti i dati della seconda colonna per le righe dalla 2 alla 7 (quelle selezionate).

E' anche possibile mettere nel carrello direttamente delle intere colonne (colonne aggiuntive).
