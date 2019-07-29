# Esempio costruzione guidata del codice
In questo esempio costruiremo i codici articolo in base a delle caratteristiche definite in fase di creazione articolo, le stesse caratterisitche saranno in parte riportate automaticamente nel record dell'articolo e in parte inserite nei parametri. La categoria parametri è specifica per titpo articolo e di conseguenza anche l'elenco dei parametri stessi.
L'esempio ha uno scopo puramente esemplficativo, quindi certi passaggi sono presneti a questo scopo mentre in una situazione reale potevano essere saltati.

## Regole codifica
Nell'esempio consideriamo di avere due tipologie di articoli : 
 * **Cuscinetti**, in cui il codice articolo è lungo 10, il prefisso e la classe materiali hanno entrambi il valore fisso "E3", nel codice articolo abbiamo poi 2 digit che sono il tipo schermo, altri 2 che rappresentano la geometria del foro ed infine c'è un progressivo lungo 4. La descrizione articolo invece viene presa dalla tabella tipo cuscinetto.
 * **Dadi**, in cui il codice articolo è lungo 30, il prefisso e la classe materiali hanno entrambi il valore fisso "E4", nel codice articolo abbiamo poi 7 digit che sono pari al codice UNI/ISO ed infine c'è un progressivo lungo 4. La descrizione articolo invece contiene nei primi 18 caratteri la descrizione del codice UNI/ISO, seguono 8 digit come codice tipo dimensione ed infine 2 digit come codice classe resistenza.

Vedi rappresentazione schematica
![BRARTI_00](http://localhost:3000/immagini/BRARTI_011/BRARTI_00.png)
## Flusso generale
Di seguito il flusso generale che mostra una panoramica delle varie azioni : 
![BRARTI_01](http://localhost:3000/immagini/BRARTI_011/BRARTI_01.png)
### Attivazione flusso
Il flusso costruzione codice viene attivato se nella tabella tipo articolo (BRA) è presente la domanda iniziale per il lancio del flusso costruzione codice (tabella B£F) : 
![BRARTI_02](http://localhost:3000/immagini/BRARTI_011/BRARTI_02.png)
### Lancio flusso
L'elemento della tabella B£F determina quale sottosettore / elemento della tabella B£C costituisce la domanda iniziale, inoltre viene stabilito se il flusso è automatico (attivato con INVIO) oppure se deve essere lanciato esplicitamente con F10 : 
![BRARTI_03](http://localhost:3000/immagini/BRARTI_011/BRARTI_03.png)
### Impostazione prefisso
In questo esempio la prima domanda fissa il prefisso del codice articolo e passa ad un elemento fisso (AAA) della tabella nel sottosettore AR : 
![BRARTI_04](http://localhost:3000/immagini/BRARTI_011/BRARTI_04.png)
### Assegnazione classe materiale
Tecnicamente questo passo poteva essere evitato e inglobato nel passo precedente, lo abbiamo introdotto per far vedere l'utilizzo di una domanda implicita (assume come risultato dei valori già esistenti) e l'uso della derivazione del passo successivo (l'elemento a cui andare è derivato dai dati presenti nella matrice base che è la matrice risultante dai passi precedenti) : 
![BRARTI_05](http://localhost:3000/immagini/BRARTI_011/BRARTI_05.png)
### Gruppo di domande per articoli "E3"
Proseguendo l'esempio ipotizziamo che la scelta precedente abbia indicato gli articoli "E3",  questo passo attiva un gruppo di domande in un altro sottosettore, le domande vengono presentate tutte contemporaneamente, alla fine si ritorna a questo passo di flusso per determinare il successivo : 
![BRARTI_06](http://localhost:3000/immagini/BRARTI_011/BRARTI_06.png)
### Domanda appartenente al gruppo "E3"
Questa è una delle domande del gruppo per gli articoli E3, l'ipostazione che prevede che alla fine dell'inserimento la risposta venga anche memorizzata come parametro dell'articolo che si sta codificando : 
![BRARTI_07](http://localhost:3000/immagini/BRARTI_011/BRARTI_07.png)
### Verifica univocità
Per evitare di codificare nuovi articoli con caratteristiche uguali ad altri articoli codificati in passato è opportuno verificare l'univocità di queste caratteristiche. Qesto è un esempio di come attivare questo controllo : 
![BRARTI_08](http://localhost:3000/immagini/BRARTI_011/BRARTI_08.png)
### Progressivo da numeratore
Il flusso si conclude con l'ultimo passo che assegna al codice un progressivo da numeratore : 
![BRARTI_09](http://localhost:3000/immagini/BRARTI_011/BRARTI_09.png)
## Memorizzazione parametri
Allafine della codifica articolo, per memorizzare nei parametri le risposte fornite in sede di codifica, bisogna inserire nei flussi inserimento oggetto un'azione contenente il programma "B£B£C10" con funzione = "APP" : 
![BRARTI_10](http://localhost:3000/immagini/BRARTI_011/BRARTI_10.png)