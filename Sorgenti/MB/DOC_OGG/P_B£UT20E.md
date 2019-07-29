# Generalità
Il programma deve essere lanciato dalla PTF di controllo, e ricevere il membro e il file della ptf stessa.

Lo script della ptf viene creato con struttura fissa ed ha il richiamo del programma nella prima parte, mentre nel seconda ha l'elenco dei file di SME.up.

# Principali caratteristiche
. Gestisce i file di gruppo (a questo proposito si ricorda che nonostante sia presente tra le
variabile la libreria dei dati, vengono analizzatii file nella libl. Quindi è obbligatorio
eseguire il controllo nell'ambiente giusto). Viene indicata per ogni file la libreria di
appartenenza, segnalando visivamente la differenza con la libreria della variabile.

. Possibilità di selezionare la "vista" desiderata.
Lo standard prevede di vedere solo le anomalie. C'è la possibilità di vedere, tutti i file, oppure
e singole segnalazioni di errore, Premendo il tasto F15.

. Possibilità, estendibile, di opzioni sui file : 
05 Visualizzazione del file (Lancia il comando F sul file in libl, se esiste ovviamente)
C  lancia il "comando" in maniera "cieca"
P  Lancia il "comando" presentando il prompt

# Tipo di comandi previsti
Oltre alla creazione dei file mancanti (opzione presente anche prima) vengono gestite anche le
modifiche dei file esistenti e precisamente : 
- nel caso dei logici viene richiesta precedentemente la conferma sulla cancellazione e
successivamente viene eseguito il comando di creazione.
- Nel caso dei fisici viene eseguito un CHGPF. Per effetturare la modifica di un file fisico sono
previsti 2 gradi di conferma in quanto NORMALEMTE è bene oltre che doveroso controllare tutte le
le ptf prima e questa come ultima.

# Segnalazione di errore
Da notare che per ogni tipologia di errore è associato un colore e che viene indicato sulla riga
del file in errore : 
- La libreria in cui viene proposta la creazione.
per i logici è la libreria del fisico
per i fisici è la libreria della variabile $LIBDAT
- La libreria in cui si trova il sorgente da utilizzare per eseguire il "comando"
ll file del sorgente è di default SRCDB e viene reperito dalla LIBL
Anche per questo motivo è doveroso eseguire questa ptf con la lista di librerie corretta





