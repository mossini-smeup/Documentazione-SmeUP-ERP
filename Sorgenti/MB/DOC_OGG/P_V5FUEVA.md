# Test analisi evadibilità
Questa funzione permette, dato un articolo o una riga documento, di determinare la sua evadibilità, cioè capire se un articolo oppure un gruppo di articoli saranno disponibili ad una certa data, per dare queste risposte utilizza le funzioni dell'analisi disponibilità replicate per ciascun articolo del gruppo.

Per ciascun articolo le indicazioni fondamentali sono : 

- Data e quantità richiesta
- Quantità disponibile da ora (Pronta)
- Quantità e data disponibili in futuro
- Quantità non disponibile


Gli impieghi principali sono per capire se un ordine di produzione, oppure uno di conto lavoro hanno tutti i fabbisogni disponibili ed eventualmente a quale data. Lo stesso tipo di utilizzo può essere fatto per le spedizioni di n. righe d'ordine oppure dei kit.

	
## Formato richiesta
Il formato di richiesta è il seguente : 

![V5_04_01](http://localhost:3000/immagini/MBDOC_OGG-P_V5FUEVA/V5_04_01.png)
_3_Nota bene; il formato precedente si utilizza solo in fase di controllo della funzione, mentre nella normale attività giornaliera l'analisi evadibilità viene lanciata direttamente attraverso pulsanti o funzioni di righe documenti e ordini di produzione.
	
## Lista prodotta
Viene emessa la lista seguente : 

![V5_04_02](http://localhost:3000/immagini/MBDOC_OGG-P_V5FUEVA/V5_04_02.png)
Le righe vengono esposte in ordine di data e sono presentate : 

- _2_prima riga, se esiste della quantità pronta e disponibile per la richiesta, la prima riga riporta nel campo data la dicitura PRONTA e nel campo qtà evadibile presenta la qtà pronta
- _2_riga origine, si vedono la quantità richiesta e la data della richiesta
- _2_righe successive, se ci sono arrivi previsti si vedono la quantità evadibile e la data prevista
- _2_ultima riga, se alla fine rimane della quantità non disponibile, l'ultima riga riporta nel campo data la dicitura N.Disp. e nel campo qtà evadibile presenta la qtà non disponibile


Usando le opzioni di riga è possibile vedere il dettaglio origine (es. la riga dell'ordine di vendita) e l'analisi disponibilità dell'articolo.
