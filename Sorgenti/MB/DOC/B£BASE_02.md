# Scheda di test per le azioni di oggetto di riga "Swipe".

## Definizione
Le azioni su un oggetto di riga sono tutte le funzioni previste quando in una matrice viene definito
un oggetto come principale. Le azioni su un oggetto riga sono state definite "swipe" perchè il primo
rilascio di queste funzioni è previsto per l'azione specifica tipica del touch screen.
L'attribuzione di un oggetto come principale in una riga avviene indicando nella relativa griglia
Fill="K01". Per esempio in questa griglia viene definito come oggetto di riga il CNNOM : 
 <Griglia>
  <Colonna Cod="ID_TP" Txt="Tipo" Tip="" Lun="12" IO="H" Ogg="OG" Dpy="" Fill="" Aut="" ETxt=""/>
  <Colonna Cod="ID_LI" Txt="Account" Lun="15" IO="O" Ogg="CNNOM" Fill="K01"/>
  <Colonna Cod="ID_DE" Txt="Descrizione" Lun="70" IO="O"/>
 </Griglia>

## Azioni
Le azioni sono state suddivise in : 
- azioni di sezione, per esempio l'inserimento di un oggetto della classe selezionata;
- azioni fisse, per esempio la visualizzazione della scheda dell'oggetto selezionato;
- azioni dinamiche, per esempio la variazione dell'oggetto selezionato o la gestione delle relative
  note se previste per l'oggetto selezionato.

### Azioni di sezione
Sono le azioni possibili nella scheda di un oggetto della classe selezionata, per
questa simulazione è necessario selezionare una classe, non è necessario selezionare un oggetto.
Tipicamente un'azione di sezione è quella che abitualmente viere richiamata nelle schede cliccando
sul pulsante inserimento o premendo F7.

### Azioni fisse
Sono le azioni fisse possibili per ogni elemento di una lista, disponibili genericamente per
qualsiasi oggetto nel caso in cui venga definito come oggetto di riga di una matrice.
Le azioni fisse sono sempre visualizzate nella matrice, non è per esempio necessario effettuare
lo "swipe". Potrebbero anche diventare colonne aggiuntive aggiunte alla matrice in modo automatico.

### Azioni dinamiche
Sono le azioni dinamiche definite per ogni elemento di una lista quando c'è definito un oggetto di
riga di una matrice, sono funzioni definite per permettere di eseguire funzioni specifiche per
l'oggetto della singola riga.

# Simulazioni swipe

## Obiettivo
Permettere di simulare tutte le funzioni previste su un oggetto di riga.

## Scelta parametri
Nelle prime 3 sottoschede è possibile selezionare : 
- una classe (obbligatoria);
- un contesto (facoltativo);
- un oggetto (obbligatorio solo per le azioni dinamiche).

## Simulazione
Dalla combinazione dei 3 parametri selezionati nelle prime 3 sottoschede risultano le azioni
disponibili.
E' necessario prima di tutto selezionare una classe, verranno pertanto visualizzate le azioni di
sezione e le azioni fisse disponibili per la classe.
E possibile selezionare poi un contesto, per visualizzare le azioni specifiche di un contesto per la
classe selezionata. Non è un parametro obbligatorio, non selezionandone nessuno il default è B£,
inoltre pur selezionandone uno se non sono state definite delle azioni specifiche per il contesto
vengono comunque visualizzate le azioni generali valide per qualsiasi contesto.
Selezionare infine un oggetto, è un parametro obbligatorio solo per le azioni dinamiche.

Nella parte bassa della scheda vengono visualizzate le azioni, cliccando su un'azione viene
visualizzata la relativa funzione di creazione, infine effettuando un doppio click sulla funzione
quest'ultima viene eseguita.

# Swipe di sezione

## Obiettivo
Questo tab ha l'obiettivo di permettere di simulare le funzioni possibili per le sezioni in cui è
previsto un oggetto master.

## Oggetto master
E' l'oggetto di riferimento di una sezione, pertanto le azioni eseguite su un oggetto possono
essere influite dall'oggetto principale della sezione.

## Simulazioni
Nelle prime 3 sottoschede la selezione dei primi 3 parametri classe, contesto e oggetto si comporta
come nelle simulazioni swipe del tab di cui sopra, il risultato è l'elenco delle azioni di sezione
senza selezionare un oggetto master è identico alle simulazioni del tab precedente.
Selezionando una classe ed un oggetto master vengono visualizzate le azioni di sezione eventualmente
modificate, se è previsto che ci sia una derivazione di informazioni dall'oggetto master.
Per esempio nella creazione di un oggetto, se l'oggetto master è un account e l'oggetto che sto
creando è un referente, l'azione visualizzata conterrà i parametri necessari a relazionare il
referente all'account.
