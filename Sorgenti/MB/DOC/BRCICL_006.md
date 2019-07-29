# Esempio di applicazione
Analizziamo ora un esempio di applicazione delle alternative avanzate al ciclo mostrato in precedenza e ripreso qui di seguito : 

![BRCICL_01](http://localhost:3000/immagini/BRCICL_006/BRCICL_01.png)
La effettiva implementazione può essere consultata nell'ambiente "Modello" presente nel server di sviluppo.

# Costruzione del ciclo
Per semplicità abbiamo costruito un ciclo con 15 fasi tutte uguali e interne, questa impostazione è ininfluente ai fini della illustrazione di come impostare le alternative di fase e di come attivarel disattivarle.

Il ciclo precedente risulta descritto come di seguito : 

![BRCICL_14](http://localhost:3000/immagini/BRCICL_006/BRCICL_14.png)
# Impostazione delle alternative
Dalla lista il comando funzione "F15 - Costruzione alternative" apre la finestra di impostazione delle alternative : 

![BRCICL_15](http://localhost:3000/immagini/BRCICL_006/BRCICL_15.png)
La fase 010 non ha alternative quindi non necessita di impostazioni, le fasi 020 e 040 sono l'inizio di strade alternative  quindi imposteremo nelle due il primo carattere di selezione "A", la fase 020 è seguita dalla 030 e quindi andremo a collegarle mettendo lo stesso carattare dei selezione "B" sia alla fine della 020 che all'inizio della 030.
La fase 040 può essere seguita dalla 050 oppure dalla 060, il carattere di selezione della fine 040 diventerà l'inizio sia della 050 che della 060.
In questo modo abbiamo descritto tutti i percorsi alternativi del "Gruppo A" : 

![BRCICL_16](http://localhost:3000/immagini/BRCICL_006/BRCICL_16.png)
Possiamo verificare, attraverso il comando "F08 - Scelta alternative" l'effetto di questa prima impostazione : 

![BRCICL_17](http://localhost:3000/immagini/BRCICL_006/BRCICL_17.png)
Il programma ha riconosciuto che è stato definito un gruppo e che al suo interno sono possibili 3 differenti percorsi.

Proseguendo con le impostazioni del secondo gruppo otterremo : 

![BRCICL_18](http://localhost:3000/immagini/BRCICL_006/BRCICL_18.png)
Da notare la fase 120 che può essere successiva alla 090 oppure alla 110 ha due possibili inizi :  "E" "F".

# Scelta delle alternative
Una volta completato l'inserimento dei caratteri di impostazione delle alternative il ciclo si presenta come segue : 

![BRCICL_19](http://localhost:3000/immagini/BRCICL_006/BRCICL_19.png)
 "F16 - Scelta alternative" permette di sabilire, all'interno del ciclo, il percorso voluto : 

![BRCICL_20](http://localhost:3000/immagini/BRCICL_006/BRCICL_20.png)
In pratica la definizione di un percorso diventa l'attivazione (st. = 10) delle fasi richieste e la disattivazione (st. 00) di quelle non volute, per ottenere il risultato inserire una "A" di selezione nelle possibili uscite di ciascun gruppo : 

![BRCICL_21](http://localhost:3000/immagini/BRCICL_006/BRCICL_21.png)
Con "INVIO" il sistema marca con "SI" e lo stato 10 le fasi appartenenti al percorso selezionato, mentre marca con "NO" e stato 00 le fasi non selezionate.

F6 di conferma porta le variazioni sull'archivio cicli.
