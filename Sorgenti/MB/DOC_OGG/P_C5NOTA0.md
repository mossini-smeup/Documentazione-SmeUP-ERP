## Obiettivo
Attraverso questa voce di menù è possibile generare automaticamente le operazioni di apertura/chiusura di esercizio.

## Formato Guida
Al lancio della funzione si aprirà la seguente schermata : 

![C5C010_045](http://localhost:3000/immagini/MBDOC_OGG-P_C5NOTA0/C5C010_045.png)
Nel primo campo è necessario impostare l'esercizio in chiusura. La funzione da utilizzare è impostata in autoamatico dal sistema ( T= Apertura / Chiusura) mentre per il metodo sono disponibili tre opzioni : 
 * A :  Aggiornamento delle operazioni di chiusura di un determinato esercizio e delle operazioni di apertura dell'esercizio successivo. Nel caso di preesistenza di operazioni della medesima natura, queste non verranno cancellate ma semplicemente rettificate o integrate con nuove registrazioni e solo se ci sono conti che sono stati chiusi o aperti con saldi che si discostano da quelli reali. Se al contrario non ci sono operazioni preesistenti verranno scritte semplicemente le operazioni complete.
 * D :  Cancellazione delle operazioni di chiusura di un determinato esercizio e delle operazioni di apertura dell'esercizio successivo (tale operazione non riesce però a cancellare l'operazione di giroconto dell'utile/perdita, che dovrà essere cancellata a mano).
 * W :  Scrittura delle operazioni di apertura/chiusura. Questo metodo è una combinazione dei due precedenti :  viene infatti eseguita la cancellazione delle operazioni preesistenti e di seguito la scrittura ex-novo completa delle aperture/chiusure.

Nei campi centrali è possibile definire le date di chiusura dell'esercizio e di apertura di quello successivo.
Nel caso in cui si voglia eseguire una chiusura con data appartenente all'esercizio successivo è necessario verificare all'interno del Set'n Play "Date e Periodi" che l'esercizio in chiusura sia in sovrapposizione. Ad esempio se si vuole chiudere l'esercizio 2009 con data 20/04/10 è necessario verificare che lo stato dell'esercizio 2009 si 'In sovrapposizione'.
Più in basso si trovano Impostazioni e Parzializzazioni.
La schermata delle impostazioni si presenta nel seguente modo : 

![C5C010_046](http://localhost:3000/immagini/MBDOC_OGG-P_C5NOTA0/C5C010_046.png)
Le scelte effettuate all'interno di questa schermata modificano lievemente il comportamento del programma, senza alterarne ovviamente il concetto di base. In particolare : 
 * Dettaglio soggetti :  se impostato a '1' (Si), consente di veder sviluppati in dettaglio per codice ente i conti clienti e fornitori, per loro natura riepilogativi;
 * Max sbilancio tollerato :  permette di impostare un importo limite entro il quale arrotondare un eventuale sbilancio.
 * Scrivi sempre c/partita :  se impostato a '1' (Si), il programma effettuerà un giroconto di chiusura per ogni conto economico, patrimoniale e d'ordine, ed un giroconto di apertura per ogni conto patrimoniale e d'ordine. Ad esempio, l'esecuzione della chiusura dei conti patrimoniali porta alla scrittura di una registrazione che riporta per ogni conto che abbia saldo in dare una contropartita in avere con lo stesso importo. Il conto contabile della contropartita viene letto dall'elemento CHIPA della tabella C5U.

Attraverso le parzializzazioni è invece possibile definire un filtro sui conti contabili o sugli enti coinvolti nella registrazione : 

![C5C010_047](http://localhost:3000/immagini/MBDOC_OGG-P_C5NOTA0/C5C010_047.png)
In particolare nei primi campi è possibile dare un limite ai conti interessati. Il limite può essere assegnato indicando un range di conti da considerare oppure indicano un range di valori per un attributo :  ad esempio è possibile condiderare i conti dal 10000000 al 29999999 oppure è possibile considerare tutti i conti che abbiano riclassifica CEE compresa tra due intervalli.
Lo stesso discorso fatto sui conti contabili può essere effettuanto anche sugli enti.

Confermando il formato guida il sistema procede leggendo la tabella C5B, partendo dai conti economici e stabilendo così l'utile o la perdita d'esercizio, passa poi ai conti d'ordine ed infine quelli patrimoniali. I conti d'ordine non devono avere sbilancio tra dare e avere mentre i conti patrimoniali ed economici devono avere tra loro uno sbilancio di importo uguale ma di segno contrario. Questo sbilancio viene chiuso dalla registrazione di rilevazione del risultato di esercizio.
Nel caso in cui la funzione sia stata eseguita in modalità Interrogazione si accede al formato lista

## Formato Lista
All'interno di questa schermata viene riportato un breve report della registrazione che si sta per eseguire; sotto di esso sono indicati tutti i saldi dei conti interessati dalla registrazione : 

![C5C010_048](http://localhost:3000/immagini/MBDOC_OGG-P_C5NOTA0/C5C010_048.png)
In particolare, nel report iniziale sono riportati l'ultimo esercizio chiuso, l'esercizio in chiusura e quello in apertura e le date di chiusura e apertura. Nel caso in cui ci fossero errori (ad esempio una data non corretta) vengono segnalati all'intenro del report stesso.
Nella parte centrale vediamo i conti contabili con i rispettivi saldi :  in primo luogo sono riportati i conti economici; alla fine della lista è riportata la causale di registrazione della chiusura economica (il sistema esegue anche un controllo sulla validità della causale stessa), più in basso è riportato il giro dell'utile o della perdita dell'esercizio ed infine si trovano i conti patrimoniali  quelli d'ordine.

Se i dati riportati nel formato lista sono corretti è possibile confermare la registrazione con il tasto F18 seguito da un'ulteriore conferma con il tasto F6. Il sistema legge L'esecuzione della registrazione produce in ogni caso una stampa di controllo.

## Formato Dettaglio
Per ogni conto contabile visualizzato all'intenro del formato lista è possibile accedere al mastrino attraverso l'opziona MD posta a inizio riga : 

![C5C010_049](http://localhost:3000/immagini/MBDOC_OGG-P_C5NOTA0/C5C010_049.png)