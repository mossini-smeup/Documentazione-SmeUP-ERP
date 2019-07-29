# Generalità
La stampa di una bolla (DDT) è un'azione che interessa diversi processi in un'azienda : 

- Stampa di una bolla di vendita
- Stampa di una bolla di invio merci in conto lavoro
- Stampa di una bolla di trasferimento tra sedi diverse
- ....


Tutte queste attività sono svolte in Sme.up da un unico programma che può essere lanciato individualmente oppure all'interno di un flusso di programmi.

Normalmente la stampa del DDT è la parte conclusiva di un flusso di programmi, ad esempio in una spedizione per vendita al cliente il flusso di programmi potrebbe essere : 

- selezione del cliente
- selezione degli ordini / articoli da spedire
- inserimento delle quantità e conferma		
- inserimento nella testata bolla del vettore, del numero colli e dei pesi, ecc..
- stampa bolla

Mentre il programma individuale di stampa bolle di solito è riservato alla ristampa di una bolla stampata in precedenza con un flusso.

Di seguito descriveremo il programma di stampa individuale perché riprende delle modalità che sonopresenti anche nei flussi mentre non ci preoccupiamo di descrivere i flussi perché oggetto di altra trattazione.
	
## Formato richiesta
Il formato di richiesta è il seguente : 

![V5_05_01](http://localhost:3000/immagini/MBDOC_OGG-P_V5BO01/V5_05_01.png)
Il tipo documento può essere visibile oppure nascosto (in questo secondo caso l'azione lancia il programma già con il tipo documento preimpostato).

Il tipo azione può essere : 

- Stampa, il programma assume un numero di DDT dal numeratore, stampa il modulo, aggiorna il record della testata documento inserendo numero e data bolla e impostando il flag 6 di documento stampato
- Prestampa, come la stampa con le eccezioni che non assume un numero di DDT e non aggiorna la testata documento
- Ristampa, valido solo per bolle già stampate in precedenza, ripete la stampa

Se si vuole stampare un singolo documento compilare il campo _3_"Stampa singolo documento"  conil numero di riferimento da stampare.

Altrimenti utilizzare le parzializzazioni per stampare un range di documenti.

Si possono modificare manualmente i campi data / ora di inizio trasporto che il sistema predisponea oggi ed adesso. Questi valori saranno stampati negli appositi campi del modulo DDT a meno chenon si decida di ignorare la stampa (_3_"1" nel campo apposito).

In casi particolari può essere necessario forzare un numero di DDT ad un valore diverso da quello che il sistema propone (vedi riga in basso), in questo caso con il tasto F10 si può intervenire direttamente sulla tabella dei numeratori.

F6 lancia la stampa.
