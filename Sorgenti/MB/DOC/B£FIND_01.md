## Obiettivi del "Cerca"
Permettere la ricerca in Sme.Up interrogando differenti contesti.
Ciascun contesto indica un "luogo" o un insieme di "luoghi" in cui eseguire la ricerca.

## Funzionamento
Per eseguire una ricerca digitare nel campo di input la stringa da ricercare e selezionare il **contesto** nel quale eseguire la ricerca.
Il contesto predefinito è ANA (Anagrafiche di base).
Nel caso si inserisca una stringa di più parole, verranno ricercate voci che contengano tutti i termini (ricerca in **AND**), a meno che non si specifichi espressamente la parola chiave **OR** tra un termine e l'altro per indicare di reperire anche voci che contengano solo una delle parole digitate. E' inoltre possibile ricercare **espressioni esatte** racchiudendole tra **doppi apici**. E' inoltre possibile utilizzare delle parentesi tonde
I risultati restituiti sono limitati ai primi 1000 record.

## Parole chiave
Come impostazione predefinita il motore di ricerca non fa distinzione tra maiuscole e minuscole. Per effettuare una ricerca che consideri le maiuscole e minuscole presenti nella stringa aggiungere la parola chiave ***L** nel campo di input.
Sono disponibili anche delle parole chiave per indicare il contesto di ricerca direttamente nel campo di input :  esse si compongono tramite _* seguito dal codice del contesto_ (ad esempio *DOC per la Documentazione).

## Calcolo del Rating
Il rating di un risultato viene calcolato nel seguente modo : 

- per ogni occorrenza della stringa ricercata, se la stringa è trovata come parola esatta aggiunge 2, se invece è contenuta in un'altra parola aggiunge 1
- se la stringa corrisponde esattamente al codice dell'oggetto aggiunge 500, se invece è contenuta nel codice aggiunge 400
- se la stringa corrisponde esattamente alla descrizione aggiunge 400, se invece è contenuta nella descrizione aggiunge 300
 


## FAQ

- **Le ricerche effettuate non restituiscono nessun risultato.**
Potrebbe non essere stata effettuata la costruzione del database delle ricerche. E' necessario che un utente con le autorizzazioni di installatore lanci la ricostruzione del database delle ricerche tramite la voce presente nel tab _Set'n play_ della scheda, nella sezione _Azioni_.
- **I risultati ottenuti dalla ricerca non contengono riscontri relativi ad anagrafiche o script modificati di recente.
Il motore di ricerca mantiene una cache delle interrogazioni eseguite dall'utente durante la sessione di lavoro, al fine di velocizzarne la riesecuzione. Se si è precedentemente eseguita la medesima ricerca eliminare la cache tramite l'apposito pulsante _Distruggi cache ricerche_.
E' anche possibile che il risultato obsoleto sia dovuto al non aggiornamento del database delle ricerche. In questo caso è necessario che un utente con le autorizzazioni di installatore lanci la l'aggiornamento del database delle ricerche tramite la voce presente nel tab _Set'n play_ della scheda, nella sezione _Azioni_.




