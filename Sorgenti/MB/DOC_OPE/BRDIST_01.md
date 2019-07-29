# Introduzione

L'obiettivo delle nuove navigazioni è quello di rendere la consultazione delle distinte __agevole__ dal punto di vista della raggiungibilità, e __semplice__ dal punto di vista della comprensione.
Dal punto di vista della raggiungibilità, queste schede possono essere richiamate direttamente dal modulo BRDIST, mentre dal punto di vista della comprensione queste sono semplici perchè ripropongo l'ormai nota struttura a tre sezioni.
Ciascuna sezione ha una funzione ben precisa : 
**1.** la prima verticale a sinistra, dedicata al menù :  questa riporta tutte le azioni e navigazioni più importanti relative alle distinte
**2.** la seconda orizzontale, nella parte alta, dedicata ai filtri e alla loro impostazione
**3.** la terza, che occupa tutta la restante parte, destinata a contenere il risultato della ricerca.

![BRDIST_001](http://localhost:3000/immagini/MBDOC_OPE-BRDIST_01/BRDIST_001.png)
Come già accade per molti altri oggetti di Sme.UP, anche le distinte basi sono organizzate per tipologia, informazione obbligatoria che permette di identificare univocamente una singola distinta.
La consultazione dei dati avviene per tipologie omogenee e questo significa che, come prima cosa, occorre scegliere quale tipo di distinta si intende consultare. Questa scelta può essere sempre modificata grazie alla voce "Cambio distinta" prensente nell'Hypermenù del modulo.

![BRDIST_002](http://localhost:3000/immagini/MBDOC_OPE-BRDIST_01/BRDIST_002.png)
# Il dashboard del modulo

La prima voce di menù ci permette di accedere al cruscotto del modulo BRDIST, ovvero una scheda puramente statistica con la quale è possibile visionare quanti legami per tipo sono presenti nel sistema.
Oltre a questa informazione, si può visionare anche lo stato di utilizzo e le impostazioni di tutte le altre tipologie di distinte attraverso la scheda "situazione generale DB".

![BRDIST_003](http://localhost:3000/immagini/MBDOC_OPE-BRDIST_01/BRDIST_003.png)
# Le navigazioni :  il SURF delle distinte

A differenza di molti altri moduli in cui ha senso avere la possibilità di consultare i dati da punti di vista diversi, per quanto riguarda le distinte, esiste una sola forma di interrogazione.
Questa interrogazione può essere raggiunta o direttamente dall'Hypermenù del modulo BRDIST o, dove presente, dal FLY "Brec.UP Basic Records - Navigazione distinta".
All'apertura, la scheda si presenta strutturata, come già ricordato sopra, con le tre sezioni.
La prima cosa da fare è impostare le modalità di esplorazione con cui si vogliono consultare le distinte : 

![BRDIST_004](http://localhost:3000/immagini/MBDOC_OPE-BRDIST_01/BRDIST_004.png)
A seconda di quello che si sceglie come modalità di esplorazione, si avrà la possibilità di impostare alcuni filtri piuttosto che altri.
__1. Esplosione della distinta__
Con l'esplosione si dovrà impostare necessariamente l'assieme di partenza, dove per assieme si intende il codice padre della distinta
__2. Implosione della distinta__
Con l'implosione si dovrà invece impostare un componente di cui si vuole conoscere il padre.

I tipi di esplosione (e di conseguenza anche di implosione) che possono essere eseguiti sono le seguenti : 
a. 11=Esplosione al livello :  mostra tutti i componenti di primo livello, a prescindere dalla data di validità e dalla configurazione. Corrisponde quindi all'esplosione della distinta tecnica.
b. 12=Esplosione scalare :  mostra i componenti a tutti i livelli che sono contenuti nell'assieme. Anche questo tipo non considera le date di validità e la configurazione
c. 13=Esplosione di produzione :  mostra i componenti al primo livello non fittizio, e visualizza solamente i legami validi
d. 14=Esplosione di produzione totale :  mostra i componenti a tutti i livelli, esplodendo completamente un assieme, mostrando solo i legami validi
e. 15=Esplosione ai materiali di base :  mostra tutti e solo i componenti al livello più basso (foglie).
f. 16=Esplosione riepilogata :  percorre tutti i rami della distinta ed esegue la somma a parità di articolo
g. 17=Esplosione riepilogata ai materiali base :  esegue la somma a parità di articolo delle foglie
h. 18=Esplosione riepilogata di produzione :  come l'esplosione di produzione sommando a parità di articolo
Per quanto riguarda l'implosione la logica di funzionamento è la stessa, solo che al posto dei componenti verranno visualizzati gli assiemi a cui appartiene un legame.

Per comprendere meglio quanto appena detto, si consideri una distinta base fatta così : 
![BRDIST_007](http://localhost:3000/immagini/MBDOC_OPE-BRDIST_01/BRDIST_007.png)A seconda del tipo di navigazione impostato, si ottiene : 
a. Esplosione al livello :  A, B, C, D
b. Esplosione scalare :  A, B, C, D, E, F, G
c. Esplosione di produzione :  A, B, C, D (saltando i fittizi al primo livello e considerando solo i legami validi)
d. Esplosione di produzione totale :  A, B, C, D, E, F, G (saltando i fittizi e considerando solo i legami validi)
e. Esplosione ai materiali di base :  A, B, C, E, G.
    NB :  in questo caso, accanto ai componenti, viene presentato anche il livello cui si trovano i vari componenti, sia in formato numerico, che in formato grafico con tante tacche colorate quanti sono i livelli corrispondenti (due livelli = due tacche colorate).
![BRDIST_008](http://localhost:3000/immagini/MBDOC_OPE-BRDIST_01/BRDIST_008.png)f.  Esplosione riepilogata :  come la scalare, con in più la totalizzazione dei componenti a parità di codice.
g. Esplosione riepilogata ai materiali base :  come l'esplosione ai materiali di base, con in più la totalizzazione dei componenti a parità di codice.
h. Esplosione riepilogata di produzione :  come l'esplosione di produzione, con in più la totalizzazione dei componenti a parità di codice.

**Alcune osservazioni : **
Dal punto di vista grafico, la presenza di assiemi o componenti fittizi (ovvero codici di tipo parte 0), è segnalata dallo sfondo di colore azzurro della riga del codice stesso.
Per quanto riguarda invece gli altri campi filtro, è possibile accedere alla documentazione specifica che ne spiega il significato, l'utilità e lo scopo.
A questa si può accedere premendo il tasto funzionale F1 con il cursore del mouse posizionato sul filtro specifico : 

![BRDIST_005](http://localhost:3000/immagini/MBDOC_OPE-BRDIST_01/BRDIST_005.png)
# Il popup delle opzioni :  il menù della distinta base e le navigazioni circolari

Con le nuove schede, le distinte basi vengono visualizzate tramite un nuovo componente grafico denominato __albero con griglia__. Questo componente offre la possibilità di esplorare le distinte in modo circolare attraverso il menù di navigazione, attivabile attraverso l'icona delle opzioni presente sulla riga di ciascun legame.
Il funzionamento di queste navigazioni circolari è molto semplice : 

![BRDIST_006](http://localhost:3000/immagini/MBDOC_OPE-BRDIST_01/BRDIST_006.png)Una volta che si è aperto questo menù (come mostrato in figura) in corrispondenza di uno specifico codice, è possibile eseguire nuove esplosioni o implosioni a partire dal codice stesso. La selezione di una singola voce, non farà altro che impostare i campi del filtro con i nuovi parametri : 
** Il tipo di navigazione scelto nel popup
** Il codice che diventerà assieme o componente della nuova esplorazione.

In questo modo, è possibile percorre tutte le varie distinte dei codici sia verso l'alto che verso il basso, senza dover impostare manualmente i filtri.
