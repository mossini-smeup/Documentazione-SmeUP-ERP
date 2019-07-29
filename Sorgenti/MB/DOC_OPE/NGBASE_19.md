# Creazione formula per calcolo date

In vari campi di Negoziando è possibile inserire una data calcolata dinamicamente.
Il tasto F1 su questi campi richiama la seguente feature

![CalcoloDate01](http://localhost:3000/immagini/MBDOC_OPE-NGBASE_19/CalcoloDate01.png)
che restituisce una data con il seguente meccanismo.
Partendo come base di calcolo dalla data inserita in Inizio Calcolo da Data o, se non compilata, dalla data di sistema, si seleziona : 
 * il tipo di Periodo (Giorno, Settimana, Mese o Anno);
 * il numero di periodi di spostamento;
 * Precedente o Successivo per determinare se ci si muove indietro o avanti nel tempo;
 * Inizio o Fine per indicare se la data è quella dell'inizio o della fine del periodo prescelto.

Vediamo qualche esempio.

Es. 1
con data di sistema 3/2/2016, impostiamo

![CalcoloDate02](http://localhost:3000/immagini/MBDOC_OPE-NGBASE_19/CalcoloDate02.png)
la data ritornata sarà quella dell'inizio mese di tre mesi prima del 3/2/2016, ovvero 1/11/2015.


Es. 2
ancora con data di sistema 3/2/2016, impostiamo

![CalcoloDate03](http://localhost:3000/immagini/MBDOC_OPE-NGBASE_19/CalcoloDate03.png)
La data ritornata sarà quella della fine dell'anno successivo a quello a cui appartiene il 3/2/2016, ovvero 31/12/2017.
Da notare che nel caso 1 la data restituita rimane la stessa fino a che la data di sistema appartiene al mese di febbraio 2016, nel caso 2 la data non cambia per tutto l'anno 2016. Questo permette di costruire finestre temporali "mobili".
Vediamo il seguente

Es. 3
Come impostare un periodo compreso tra due date variabili, ad esempio che comprenda la settimana completa precedente alla data di sistema.
Il programma richiede due date : 

Impostiamo la prima  data in questo modo

![CalcoloDate04](http://localhost:3000/immagini/MBDOC_OPE-NGBASE_19/CalcoloDate04.png)
e la seconda in quest'altro

![CalcoloDate05](http://localhost:3000/immagini/MBDOC_OPE-NGBASE_19/CalcoloDate05.png)
Fino a che la data di sistema rimane nella settimana n. 4 del 2016 (18-24 gennaio) il risultato delle due operazioni sarà sempre 11 e 17 Gennaio 2016, nella settimana n. 5 (25-31 Gennaio) il risultato sarà 18 e 24 Gennaio e così via.

Es. 4
Come impostare la settimana/mese/anno correnti

![CalcoloDate06](http://localhost:3000/immagini/MBDOC_OPE-NGBASE_19/CalcoloDate06.png)
Indicare il tipo di periodo e NON compilare Scostamento e Precedente/Successivo. Con data di sistema (Mercoledì) 10/2/2016 avremo rispettivamente (Lunedì) 8/2/2016 per la settimana, 1/2/2016 per il Mese e 1/1/2016 per l'Anno.

Es. 5
Come impostare n giorni a ritroso a partire da oggi

![CalcoloDate07](http://localhost:3000/immagini/MBDOC_OPE-NGBASE_19/CalcoloDate07.png)
Con data di sistema 3/2/2016 avrò come risultato 14/01/2016.
Per il Periodo Giorno il parametro Inizio/Fine non è considerato e si può omettere.

Le righe successive alla prima prendono come base di calcolo la data ritornata dalla riga precedente

Es. 6
Consideriamo la seguente impostazione con data di sistema 5/2/2016

![CalcoloDate08](http://localhost:3000/immagini/MBDOC_OPE-NGBASE_19/CalcoloDate08.png)La prima riga ritorna il 1/1/2016, per cui la seconda il 31/12/2015 e la terza il 14/12/2015

Sme.UP
Last Rev.24/05/2016
