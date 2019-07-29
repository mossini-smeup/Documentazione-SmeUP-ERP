# Struttura delle schiere caratterizzazioni del tipo tempo 1
## INTRODUZIONE
La routine £BRT ha lo scopo di presentare, manutenere le schiere di valori presenti nell'archivio righe di ciclo, e di calcolare i dati derivati per la schedulazione ed il calcolo dei costi.
Essa riceve la schiera valori ed il tipo di tempo. Se quest'ultimo è a blanks viene assunto il tipo definito nella tabella BR1.
Vengono trattati, all'interno del programma di gestione funzioni (BRBRT0), i tipi tempo numerici (1/9).
Se ricevuto un tipo tempo 'x' alfanumerico, viene eseguita una deviazione al programma BRBRT0x, che sostituisce totalmente questo programma.
## Struttura delle schiere di caratterizzazione del tipo tempo
Per ogni tipo tempo (da 1 a 9) è definita a fine programma una schiera di 10 elementi, che fissa il significato di ciascun valore, così strutturata : 
 * Posiz.    01   20   Descrizione
 * Posiz.    21   21   Tipo Valore : 
 ** T=Tempo
 ** C=Costo
 ** P=Peso
 ** M=moltiplicatore
 ** /=divisore
 ** F=commento
 * Posiz.    22   22  Caratteristica valore : 
 ** Q se è un valore variabile per quantità (ad esempio il tempo lavoro)
 ** ' ' se è un valore fisso al variare della quantità (ad esempio un tempo di attrezzaggio)
 ** numero da 1 a 9, se il tipo valore è 'M' il numero da 1 a 9 è il fattore per cui va moltiplicato questo valore (ad esempio se questo valore è il numero di attrezzisti si indica la posizione del tempo di attrezzaggio), se il numero è blank si assume 1; se il tipo valore = '/' il numero è il divisore per cui va diviso questo valore, se il numero è blank si assume 1
 * Posiz.    23   24   Unità di misura propria forzata. Se blanks viene assunta l'unità della riga del ciclo, ricevuta nel campo £BRPUT.
 * Posiz.    25   40   Una schiera di 8 valori usata nel calcolo delle componenti di carico (vedi paragrafo relativo)
 * Posiz.    41   56   Una schiera di 8 valori usata nel calcolo delle componenti di costo (vedi paragrafo relativo)
 * Posiz.    57   57   Un valore che serve a normalizzare le componenti di costo (vedi paragrafo relativo)

 * **Funzione 'DE' - Decodifica tempi**
 ** __Metodo 'TT' - Valori utente (assunto)__; vengono ritornati i significati dei 10 valori
 ** __Metodo 'CC' - Componenti di carico__; vengono ritornati i significati dei 10 componenti di carico.
 ** __Metodo 'TC' - Componenti di costo__; vengono ritornati i significati dei 10 componenti di costo.
 ** __Metodo 'CR' - Codici di carico__; vengono ritornate le decodifiche della TA BR*CR.
 ** __Metodo 'ST' - Significato tipi tempo__; vengono ritornate le decodifiche degli elementi numerici della TA BR*ST.

![TSTBRT_01](http://localhost:3000/immagini/MBDOC_OGG-P_TSTBRT/TSTBRT_01.png)
 * **Funzione 'GE' - Gestione**
 ** __Metodo '02' - Modifica__; vengono presentati, con possibilità di modificarli, i valori del tipo tempo (fino ad un massimo di 10). Prima di presentarli, se sono di tipo 'T' e la loro unità di misura propria è blanks, (informazioni contenute nell'elemento della schiera di caratterizzazione) si assume che siano valori in secondi e quindi vengono convertiti nell'unità di misura ricevuta (£BRPUT) :  se questa è blanks viene assunto 'HR'. Dopo averli presentati, vengono ritrasformati in secondi, se soddisfano alle stesse condizioni. NB :  non viene trattata la quantità eventualmente ricevuta.
 ** __Metodo '05' - Visualizzazione__; vengono presentati, solo in visualizzazione, i valori (opportunamente convertiti) e, quelli variabili per quantità (informazione contenuta nella schiera di caratterizzazione) moltiplicati per la quantità ricevuta (£BRPQT) se diversa da 0.

 * **Funzione 'TR' - Trasformazione**
 ** __Metodo 'US' - Da unità di misura a secondi__; i valori vengono trasformati in secondi, se di tipo 'T' e con unità di misura propria a blank. Se sono variabili per quantità, vengono moltiplicati per la quantità se la quantità ricevuta non è 0.
 ** __Metodo 'SU' - Da secondi a unità di misura__; è il metodo inverso del precedente.

 * **Funzione 'CA' - Calcolo tempi/costi derivati**
 ** __Metodo 'CC' - Componenti di carico__; viene costruita la schiera di 10 valori che sono alla base della schedulazione dell'operazione. Il programma riceve il codice di carico (campo £BRPCC, della tabella BR*CR), il cui valore va da 1 a 10. Se esso è a 0, ma il programma riceve il codice della risorsa, viene assunto il codice di carico della risorsa stessa. l valore che sta all'incrocio tra la colonna corrispondente al codice di carico e la riga del valore individua il progressivo di carico (da 1 a 10) in cui viene sommato il valore (eventualmente normalizzato in ore e moltiplicato per la quantità).
 ** __Metodo 'TC' - Componenti di costo__; viene costruita la schiera di 10 valori che sono alla base della valorizzazione dell'operazione. Viene costruito il componente di costo nella stessa maniera del componente di carico, usando questa seconda schiera. Se, per l'elemento, è presente il valore di normalizzazione si ha il seguente comportamento :  Se esso vale 'P' , prima di essere totalizzato, il valore di ciclo viene diviso per il peso dell'articolo in esame.

 * **Funzione 'VI' - Visualizzazione**
 ** __Metodo 'DO' - Documentazione__; vengono visualizzate le schiere che definiscono il comportamento dei valori del tipo tempo ricevuto.
 ** __Metodo 'P1' - Passi di calcolo per carico__; dato il tipo tempo ed il codice di carico in input vengono visualizzati i calcoli delle componenti di carico per i tempi.
 ** __Metodo 'P2' - Passi di calcolo per costo__; dato il tipo tempo ed il codice di carico in input vengono visualizzati i calcoli delle componenti di carico per i costi.

 * **Funzione 'S&P' - Set'n play**
 ** __Metodo 'TCR' - Codici di carico__; simile a DE/CR.
 ** __Metodo 'TST' - Significato tipi tempo__; simile a DE/ST.
 ** __Metodo 'TCS' - Componenti di costo__; simile a DE/TC.
 ** __Metodo 'TCA' - Componenti di carico__; simile a DE/CC.
 ** __Metodo 'TDC' - Tabella di calcolo__; apre il sorgente del programma, in fondo ci sono le tabelle dei vari tipi tempo utilizzate nel calcolo.

![TSTBRT_02](http://localhost:3000/immagini/MBDOC_OGG-P_TSTBRT/TSTBRT_02.png)