## Obiettivo

Attraverso questa voce di menù è possibile caricare a sistema le informazioni contenute all'interno di flussi di dati ricevuto tramite i servizi di remote banking.

**NOTA BENE** :  per i movimenti di riguardanti i flussi di estratto conto, quando il file viene generato dal servizio del remote banking, va sempre applicata l'opzione che permette di scaricare solo i movimenti che non lo sono ancora stati.

## Formato guida

Al lancio della funzione viene mostrata la seguente schermata guida : 

![EDMAIL_001](http://localhost:3000/immagini/MBDOC_OGG-P_EDAP00/EDMAIL_001.png)
Al suo interno è necessario impostare : 
 * Azienda
 * Metodo :  varia al variare del flusso ricevuto. Le scelte dispnibili sono :  Movimenti C/C (nel caso in cui si vogliano registrare i movimenti di conto corrente), Avvisi pagamento (nel caso in cui si vogliano registrare pagamenti passivi) e  Esito effetti attivi (nel caso in cui si voglia procedere alla registrazione dell'esito di effetti attivi come riba o cambiali)
* Modalità :  è disponibile solo l'interrogazione

Confermando il formato guida compare una schermata in cui viene richiesta la memorizzazione dati da utilizzare : 

![EDMAIL_002](http://localhost:3000/immagini/MBDOC_OGG-P_EDAP00/EDMAIL_002.png)
All'interno della memorizzazioni sono riportate informazioni quali il nome della cartella su cui risiede il flusso e la sua collocazione.
L'impostazione del percorso di ricezione del flusso viene effettuata lasciando blank il campo Memorizzazione e dando invio :  in questo modo compare la schermata per la definizione del percorso del file dei flussi : 

![EDMAIL_004](http://localhost:3000/immagini/MBDOC_OGG-P_EDAP00/EDMAIL_004.png)
Impostando / nel campo Nome File il file prenderà lo stesso nome del file ricevuto mentre flaggando 'Cancella file da IFS' si otterrà la cancellazione del file da IFS al termine dell'acquisizione.
Una volta compilata la schermata è possibile memorizzarla in modo da poterla semplicemente selezionare nella schermata delle memorizzazioni.


Confermando il nome della memorizzazione il sistema procederà all'acquisizione del file indicato.



