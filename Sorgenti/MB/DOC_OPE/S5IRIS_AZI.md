# Introduzione
E' possibile eseguire azioni manuali che modificano il risultato della schedulazione :  si può scegliere l'ordinamento delle operazioni da eseguire, e/o la risorsa specifica su cui eseguirle, e di conservare tale scelta per le successive schedulazioni, memorizzandole nell'archivio di impegni risorse.
Tali azioni vanno eseguite operando manualmente nel formato di dettaglio.

Ricordo che il formato di dettaglio può essere visualizzato nei seguenti modi.

* Gantt
** Una risorsa specifica
** Tutte le risorse specifiche di una risorsa generale
** Tutte le risorse :  la riga riassuntiva delle operazioni di ciascuna risorsa è valorizzata
* Incolonnato
** Una risorsa specifica
** Tutte le risorse specifiche di una risorsa generale
** Tutte le risorse :  la riga riassuntiva delle operazioni di ciascuna risorsa è vuota

Per una descrizione completa delle modalità di presentazione riferirsi al documento : 
- [Analisi risultati](Sorgenti/MB/DOC_OPE/S5IRIS_RIS)

Le azioni eseguibili sono le seguenti : 
* Forzatura
Si fissa la risorsa specifica su cui eseguire un'operazione. La sequenza di schedulazione è demandata al motore. In pratica, questa azione corrisponde all'assegnazione di un filtro di risorsa specifica all'operazione.
* Congelamento
Si fissa che tutte le celle fino a quella selezionata, verranno eseguite su quella risorsa specifica, nell'ordine in cui sono state schedulate.
Il congelamento non fissa in modo assoluto la schedulazione, non definisce infatti l'istante in cui inizierà un'operazione, ma in modo relativo :  la sequenza in cui verranno eseguite le operazioni a partire dalla data di inizio della schedulazione. Se infatti, dopo aver congelato, non si dicharano avanzamenti, ma si rischedula a partire da una data successiva, la sequenza su di ogni risorsa sarà la stessa, ma con date più alte.
Il congelamento agisce a valle delle operazioni in corso, che sono schedulate per prime.
* Ordinamento
Si modifica l'ordine di schedulazione delle operazioni congelate

La lista delle operazioni schedulate su di una risorsa si divide in tre zone successive : 
* zona delle operazioni in corso
Se ce n'è più d'una, vengono ordinate in ordine inverso di dichiarazione (a partire dalla più recente) :  si assume infatti che le precedenti sono state interrotte per validi motivi e quindi si rispetta questa volontà.
* zona congelata
le operazioni sono ordinate nel modo deciso dll'utente, che può fissare la sequenza proposta dalla schedulazione oppure modificarla.
* zona libera
contiene sia operazioni forzate sia operazioni libere. L'ordinamento è deciso dallo schedulatore.

Una cella si trova in uno di questi stati (identificati dala forma)
* Iniziata

![FIG_003](http://localhost:3000/immagini/MBDOC_OPE-S5IRIS_AZI/FIG_003.png)* Libera

![FIG_002](http://localhost:3000/immagini/MBDOC_OPE-S5IRIS_AZI/FIG_002.png)* Congelata

![FIG_001](http://localhost:3000/immagini/MBDOC_OPE-S5IRIS_AZI/FIG_001.png)* Forzata

![FIG_004](http://localhost:3000/immagini/MBDOC_OPE-S5IRIS_AZI/FIG_004.png)
Le azioni si dividono, per la modalità operativa di esecuzione in : 
* Statiche :  si eseguono puntando una cella e selezionando il menu popup.
* Dinamiche :  si eseguono trascinando una cella in una posizione significativa

# Azioni statiche
Le azioni statiche si eseguono puntando una cella e selezionando il menu popup.
Esse, a loro volta, si dividono in
* Azioni dirette :  eseguite sul primo livello di popup.
* Scelte specifiche :  eseguite scendendo a più livelli nel popup.

## Azioni dirette
Le azioni dirette si eseguono cliccando l'opzione nel popup, e sono indipendenti dalla forma di presentazione.
Le opzioni presentate dipendono dalla situzione dell'operazione selezionata
* Iniziata
** nessuna opzione
* Libera
** congelamento ON - congela la schedulazione fino all'operazione selezionata (compresa)
** forzatura ON - forza l'operazione selezionata sulla risorsa in cui si trova
* Congelata
** congelamento OFF - elimina il congelamento a partire dall'operazione selezionata (compresa) fino all'ultima congelata. Eventuali forzature successive vengono mantenute
* Forzata
** congelamento ON - congela la schedulazione fino all'operazione selezionata (compresa)
** Forzatura OFF - elimina la forzatura dall'operazione selezionata.

Dopo aver eseguito l'azione, viene ripresentato il formato di dettaglio con la forma delle celle interessate aggiornata.

Nella figura seguente viene presentata una situazione con tutte le celle libere.

![FIG_029](http://localhost:3000/immagini/MBDOC_OPE-S5IRIS_AZI/FIG_029.png)Selezionando la terza cella (414590), appare il seguente popup. SI noti che tutta la riga viene evidenziata

![FIG_030](http://localhost:3000/immagini/MBDOC_OPE-S5IRIS_AZI/FIG_030.png)Se si sceglie di congelarla, il dettaglio assumerà in modo automatico il seguente aspetto (con le celle fino a quella selezionata che diventano congelate).

![FIG_031](http://localhost:3000/immagini/MBDOC_OPE-S5IRIS_AZI/FIG_031.png)
## Scelte specifiche
Sono attivate (sia nel Gantt sia in Incolonnata) quando si è in presentazione delle risorse specifiche di una risorsa generale, ed esse sono più d'una.
Posizionandosi su di una cella, si presenta, nel pop-up, il bottone "Sposta nel gruppo" :  selezionandolo, appare un menu a tendina con le risorse specifiche del gruppo; la scelta di una di esse vi provoca la forzatura della fase corrispondente alla cella.
Viene impedita la scelta di una risorsa non del filtro se impostata la selezione solo al suo interno, e della risorsa attuale (dove è schedulata la fase). Quest'ultima azione (permessa, se la cella è libera) va eseguita con il bottone "Forzatura ON", che compare solo quando la forzatura sulla fase attuale è consentita.

Anche in questo caso, l'esecuzione dell'azione provoca il riaggiornamento automatico del formato, con spostamento dell'operazione selezionata all'ultima posizione della lista nella risorsa d'arrivo, con modifica della forma della cella, che diventa forzata, perdendo l'eventuale congelmento.

Questa azione consiste nell'eseguire in modo automatico un trascinamento obliquo a destra dell'ultima cella della risorsa d'arrivo. Si rimanda a questo
paragrafo per la rappresentazione grafica dei suoi effetti

Sono stati realizzati alcuni accorgimenti grafici per migliorare la comprensione.
* La risorsa specifica su cuila fase è schedulata è preceduta da una freccia
* Le altre risorse specifiche sono precedute dal simbolo di spunta
* Il colore verde identifica le risorse del filtro di risorse specifiche
* Il colore verde identifica le risorse non del filtro
* Il colore rosso identifica un'anomalia
* Le risorse non selezionabili sono in bassa intensità
* Le risorse del filtro sono in grassetto
* Le altre risorse (non del filtro ma selezionabili) sono in carattere normale

Nel seguito diamo alcuni esempi di queste rappresentazioni.

Se non vi sono filtri di risorse appare il seguente menu :  tutte le risorse, ad eccezione della attuale, sono selezionabili (carattere normale), ma nessuna è preferenziale (colore blu)

![FIG_023](http://localhost:3000/immagini/MBDOC_OPE-S5IRIS_AZI/FIG_023.png)
Le ulteriori forme di presentazione si differenziano in base alla scelta di impostazione :  se si possono selezionare tutte le risorse o solo quelle del filtro.

**Se sono selezionabili tutte le risorse, si presenta una delle seguenti situazioni.**

Nel seguente esempio vi sono due risorse del filtro (MOA.02, che è la risorsa attuale) e MOA.03 (segnalate in verde). L'unica risorsa non sceglibile (a bassa intensità) è la risorsa attuale.

![FIG_024](http://localhost:3000/immagini/MBDOC_OPE-S5IRIS_AZI/FIG_024.png)Nel seguente esempio l'unica risorsa del filtro è la risorsa attuale MOA.01, (freccia verde), che è l'unica non sceglibile (a bassa intensità).

![FIG_025](http://localhost:3000/immagini/MBDOC_OPE-S5IRIS_AZI/FIG_025.png)Nel seguente esempio le risorse del fitro sono MOA.02 e MOA.03 (segnale di spunta verde).
La risorsa attuale MOA.01 (unica non sceglibile, a bassa intensità) non è del filtro (freccia blu).

![FIG_026](http://localhost:3000/immagini/MBDOC_OPE-S5IRIS_AZI/FIG_026.png)
**Se sono selezionabili solo le risorse del filtro, si presenta una delle seguenti situazioni.**

Nel seguente esempio vi sono tre risorse del filtro (MOB.02, che è la risorsa attuale), MOB.05  e MOB.08 (segnalate in verde. Queste ultime sono le uniche sceglibili (le altre sono a bassa intensità).

![FIG_027](http://localhost:3000/immagini/MBDOC_OPE-S5IRIS_AZI/FIG_027.png)Nel seguente esempio L'unica risorsa del filtro è la risorsa ASA.06 (verde) che è l'unica sceglibile (le altre sono in bassa intensità).
La risorsa attuale ASA.08, non del filtro, è contrassegnata da una freccia rossa, in quanto costituisce un'anomalia :  non appartiene al filtro, ed il filtro è vincolante.
Il motivo più probabile è che è stata iniziata su di una risorsa non ammessa, oppure che il filtro è stato modificato dopo averla forzata o congelata.

![FIG_028](http://localhost:3000/immagini/MBDOC_OPE-S5IRIS_AZI/FIG_028.png)
# Azioni dinamiche
Le azioni dinamiche, ottenute per trascinamento di una cella, dipendono dal tipo di visualizzazione.
Non è permesso spostare un' operazione iniziata :  se la si punta viene emesso un messaggio d'errore.

## Modalità di trascinamento
### Trascinamento orizzontale
Si sposta una cella orizzontalmente, a sinistra o a destra, in modo che, rispettivamente, il suo inizio preceda o segua l'inizio almeno di un'altra cella. In tal modo si comunica l'intenzione di modificare l'ordine della schedulazione. Ciò si traduce nel congelamento delle celle fino a quella mossa (compresa), nell'ordine successivo allo spostamento.
Dopo l'azione, il Gantt viene riordinato :  la cella mossa si sposta verticalmente, mentre orizzontalmente rimane nella posizione in cui è stata spostata, in quanto è significativa per il congelamento la sua posizione relativa rispetto alle altre celle, e non quella assoluta, che viene calcolata dopo aver eseguito una schedulazione globale (operazione che si può lanciare dall'interno del Gantt).
Se la cella non scavalca nessun'altra cella, oppure precede una cella iniziata, lo spostamento viene impedito :  appare un messaggio di avvertimento e si ripresenta la situazione precedente allo spostamento.

Ad esempio, se si ha la seguente situazione

![FIG_032](http://localhost:3000/immagini/MBDOC_OPE-S5IRIS_AZI/FIG_032.png)
e si sposta la cella 414590 a destra della 424677 per decidere di eseguirla dopo di essa

![FIG_033](http://localhost:3000/immagini/MBDOC_OPE-S5IRIS_AZI/FIG_033.png)
al rilascio del mouse il Gantt si riaggiorna nel seguente modo, con le due celle invertite (verticalmente), e con tutte le celle congelate fino a quella mossa. Quest'ultima rimane, orizzontalmente, nella posizione in cui era stata trascinata

![FIG_034](http://localhost:3000/immagini/MBDOC_OPE-S5IRIS_AZI/FIG_034.png)
La sua posizione effettiva sarà la seguente, ottenuta dopo aver eseguito la schedulazione globale

![FIG_035](http://localhost:3000/immagini/MBDOC_OPE-S5IRIS_AZI/FIG_035.png)
L'esemipo seguente mostra invece, partendo dalla stessa situazione iniziale, lo spostamento della cella 424677 a sinistra della cella 414590  per decidere di eseguirla prima di essa.
Vengono riportati i Gantt dello spostamento, dopo il rilascio del mouse e dopo la schedulazione globale.

![FIG_036](http://localhost:3000/immagini/MBDOC_OPE-S5IRIS_AZI/FIG_036.png)
![FIG_037](http://localhost:3000/immagini/MBDOC_OPE-S5IRIS_AZI/FIG_037.png)
![FIG_038](http://localhost:3000/immagini/MBDOC_OPE-S5IRIS_AZI/FIG_038.png)
Il seguente Gantt riporta un esempio di spostamento non significativo e quindi impedito.
La cella 414590 è stata spostata a sinistra, ma, dato che non oltrepassa la cella 411490, la sua posizione nella schedulazione rimane la stessa.

![FIG_039](http://localhost:3000/immagini/MBDOC_OPE-S5IRIS_AZI/FIG_039.png)
### Trascinamento obliquo
Il trascinamento obliquo consiste nello spostamento di una cella di dettaglio a sinistra o a destra di un'altra cella di dettaglio.
Con questa azione sii ottiene il congelamento della risorsa della cella d'arrivo, rispettivamente con la cella d'arrivo esclusa o inclusa, a cui si accoda (pure congelata) la cella spostata.
Se si trascina una cella a destra dell'ultima cella di una risorsa diversa, si ha l'effetto di forzare (perdendo l'eventuale congelamento) la cella spostata sulla risorsa d'arrivo, senza nessun congelamento.
Nella rappresentazione incolonnata si ottiene lo stesso effetto di forzatura sulla risorsa d'arrivo trascinando la cella sulla riga della risorsa specifca, che, in questa rappresentazione riporta la riga riassuntiva vuota.
Se lo spostamento non è significativo (si sposta una cella dopo la precedente o prima della successiva), oppure non ammesso (prima di una cella iniziata) viene data segnalazione e si ripresenta la situazione precedente.
Anche in questo caso la riga della cella trascinata viene spostata nella posizone finale, mentre orizzontalmente è posta a metà tra le due celle in cui è stata trascinata.
Alla successiva schedulazione globale la cella verrà riposizionata in modo corretto.

Ad esempio, se si parte dalla la seguente situazione

![FIG_032](http://localhost:3000/immagini/MBDOC_OPE-S5IRIS_AZI/FIG_032.png)
e si sposta la cella 414590 a destra della 411491 per decidere di eseguirla dopo di essa. Si noti che nel trascinamento obliquo non è influente il posizionameto verticale della cella trascinata :  nell'esempio, non ha alcun significato il fatto che la cella 414590 oltrepassi anche la cella sottostante 4112492

![FIG_040](http://localhost:3000/immagini/MBDOC_OPE-S5IRIS_AZI/FIG_040.png)
al rilascio del mouse il Gantt si riaggiornerà nel seguente modo, con le due celle invertite (verticalmente), e con tutte le celle congelate fino a quella mossa. Quest'ultima è posta, orizzontalmente, a metà tra le celle 411491 e 411492.

![FIG_041](http://localhost:3000/immagini/MBDOC_OPE-S5IRIS_AZI/FIG_041.png)
La sua posizione effettiva sarà la seguente, ottenuta dopo aver eseguito la schedulazione globale

![FIG_042](http://localhost:3000/immagini/MBDOC_OPE-S5IRIS_AZI/FIG_042.png)
L'esempio seguente riporta la stessa azione eseguita sull'Incolonnato. Non viene riportata la situazione dopo una rischedulazione, in quanto in questo caso essa non modifica la posizione finale della cella.

La situazione iniziale è la seguente

![FIG_043](http://localhost:3000/immagini/MBDOC_OPE-S5IRIS_AZI/FIG_043.png)
Si esegue lo spostamento obliquo

![FIG_044](http://localhost:3000/immagini/MBDOC_OPE-S5IRIS_AZI/FIG_044.png)
Al rilascio del mouse si presenterà il seguente Incolonnato

![FIG_045](http://localhost:3000/immagini/MBDOC_OPE-S5IRIS_AZI/FIG_045.png)
L'esempio seguente mostra la forzatura di una cella su di una risorsa diversa dall'attuale,  nella presentazione incolonnata.

Da questa situazione di partenza

![FIG_046](http://localhost:3000/immagini/MBDOC_OPE-S5IRIS_AZI/FIG_046.png)
Per forzare la cella 411490 sulla risorsa specifica ASA.01, si può spostare la cella a destra dell'ultima cella della risorsa in cui la si vuole forzare (409286)

![FIG_047](http://localhost:3000/immagini/MBDOC_OPE-S5IRIS_AZI/FIG_047.png)
oppure portarla nella riga iniziale della risorsa d'arrivo, che nell'Incolonnato è vuota (questo tipo di spostamento, verso la riga riassuntiva, verrà trattato nel paragrafo successivo)

![FIG_048](http://localhost:3000/immagini/MBDOC_OPE-S5IRIS_AZI/FIG_048.png)
In entrambi i  casi il risultato finale è il seguente, con la cellla spostata che diventa forzata.  Essa viene posta in ultima posizione :  la successiva schedulazione la collocherà nella posizione definitiva.

![FIG_049](http://localhost:3000/immagini/MBDOC_OPE-S5IRIS_AZI/FIG_049.png)
### Trascinamento sulla riga riassuntiva
Ad ogni cella del Gantt corrisponde una cella sulla riga riassuntiva della stessa risorsa specifica.

Si può spostare sulla riga riassuntiva, una cella del dettaglio del Gantt o di un'altra riga riassuntiva.
Le possibilità ammesse sono le seguenti
* spostamento di una cella di una riga riassuntiva nella stessa riga riassuntiva
* spostamento di una cella di dettaglio nella propria riga riassuntiva.

Queste modalità sono equivalenti allo spostamento orizzontale di una cella, con il controllo che lo spostamento sia significativo (oltrepassi almeno un'altra cella) e valido (non preceda le fasi iniziate).

* spostamento di una cella di una riga riassuntiva in un'altra riga riassuntiva
* spostamento di una cella di dettaglio in una riga riassuntiva diversa dalla propria

In queste modalità, se la cella viene spostata a destra dell'ultima cella della riga riassuntiva, si ha l'effetto di forzarla sulla risorsa della riga riassuntiva d'arrivo.
Negli altri casi si esegue il normale congelamento, sempre sulla risorsa della riga riassuntiva d'arrivo, fino al punto in cui si ha trascinto la cella.

Il trascinamento di una cella sulla riga riassuntiva vuota (di una risorsa specifica diversa dall'attuale) provoca quindi la forzatura su quella risorsa.
Ricordiamo che nel Gantt la riga riassuntiva è vuota se la risorsa è scarica, mentre nell'incolonnato essa è sempre vuota, quindi in quest'ultimo caso questo spostamento ha sempre l'effetto di forzatura.

### Limitazioni allo spostamento
Nello spostamento obliquo ed in quello sulla riga riassuntiva, si può, tra l'altro, modificare la risorsa specifica su cui si esegue l'operazione.
In questo caso viene controllato che la nuova risorsa speciifca appartenga alla risorsa generale della fase di ciclo, ed al filtro, se esso è vincolante.

### Precisazioni sulla zona congelata
Quando si eseguono spostamenti che convolgono celle della zona congelata, vanno tenute presenti le seguenti caratteristiche.
La zona congelata non viene mai ridotta in modo automatico.
Se, ad esempio, si sposta l'ultima fase congelata a sinistra, la penultima congelata diventa l'ultima congelata. Tale spostamento non provoca l'arretramento del confine della zona congelata, che deve essere eseguito in modo esplicito con un'azione statica (dal popup della cella).
La zona congelata viene invece estesa in modo automatico.
Se, ad esempio, si sposta a destra l'ultima fase congelata, le fasi che essa supera diventano anch'esse congelate.

## Azioni dinamiche nel Gantt
Sono abilitati tutti i tipi di  trascinamento.
Nella presentazione di tutte le risorse si può eseguire solo lo spostamento tra righe riassuntive, esseno le uniche vosualizzate. Per poter eseguire gli altri spostamenti, bisogna aprire almeno una di esse, ed operare sul dettaglio.

## Azioni dinamiche nell'Incolonnato
Sono abilitati soltanto il trascinamento obliquo e quello dal dettaglio alla riga riassuntiva (in questo caso vuota), in quanto gli altri trascinamenti implicano una rappresentazione temporale, che è assente in questa forma.
Nella presentazione di tutte le risorse, dato che in questa modalità viene riportata soltanto la riga riassuntiva che, in questo caso è vuota, per poter operare sul dettaglio, è necessario aprire almeno una risorsa.

## Risorse scariche
E' possibile decidere se visualizzare o meno le risorse scariche.
La loro visualizzazione permette di forzarvi delle operazioni, trascinandovi una cella. Lo stesso risultato può essere ottenuto, selezionando la risorsa specifica nel popup delle celle.

Nella seguente situazione

![FIG_046](http://localhost:3000/immagini/MBDOC_OPE-S5IRIS_AZI/FIG_046.png)
per forzare la cella 411490 sulla risorsa ASA.04, si trascina la cella sulla riga di questa risorsa

![FIG_050](http://localhost:3000/immagini/MBDOC_OPE-S5IRIS_AZI/FIG_050.png)
Al rilascio del mouse si presenterà il seguente Incolonnato

![FIG_051](http://localhost:3000/immagini/MBDOC_OPE-S5IRIS_AZI/FIG_051.png)
## Segnalazione spostamenti
Nella rappresentazione Gantt le celle spostate sono riconoscibili, prima delle rischedulazione, dal fatto che non rispettano esattamente la sequenza temporale.
Nella rappresentazione incolonnata, invece, ciò non è possibile, perché le celle sono tutte nella stessa posizione.
Lo spostamento di una cella provoca la cancellazione, in memoria, degli istanti di inizio e fine schedulazione, che non sono più significativi. Questa caratteristica è utilizzabile per riconoiscere le celle mosse :  nello schema di presentazione si imposta di visualizzare, ad esempio, la data e l'ora di inizio e fine schedulazione.

Nell'esempio seguente, partendo dalla situazione : 

![FIG_052](http://localhost:3000/immagini/MBDOC_OPE-S5IRIS_AZI/FIG_052.png)
Se sii esegue il seguente spostamento, decidendo di eseguire la fase 428331 prima della 430892.

![FIG_053](http://localhost:3000/immagini/MBDOC_OPE-S5IRIS_AZI/FIG_053.png)
Al rilascio del mouse viene presentata la seguente situazione (nella cella mossa data e ora di inizio e fine sono in bianco).

![FIG_054](http://localhost:3000/immagini/MBDOC_OPE-S5IRIS_AZI/FIG_054.png)
Dopo la schedulazione globale questi campi sono nuovamente valorizzati.

![FIG_055](http://localhost:3000/immagini/MBDOC_OPE-S5IRIS_AZI/FIG_055.png)