## Modificare la struttura di un file Sme.UP
Per modificare la struttura di un file è necessario seguire i seguenti passi : 

* Modificare il suo sorgente (presente nel source SRCDB).
* Segnare la modifica nel membro "documentativo" AAAFIL
* Adeguare e ricompilare tutti i programmi che usano quel file
* Scrivere un programma di conversione ove necessario
* Scrivere un'apposita PTF (anche a scopo documentativo)
* Scrivere un'apposita Nota Tecnica

Normalmente queste modifiche vengono fatte in fase di nuovo rilascio dell'applicativo per evitare complicazioni.

## Note sulle modifiche ai campi
I campi di un tracciato record non andrebbero MAI "accorciati". Sia essi numerici che alfanumerici.
Sono concesse alcune piccole deroghe in merito, ad esempio quando il campo è formalmente sbagliato (ad esempio un campo data lungo 9).

In generale se ci si accorge che il campo di un file ha una dimensione maggiore di analoghi campi di altri file è meglio non modificare il campo oppure "allungare" gli altri.

## Nota sulla cancellazione di campi
Nessun campo andrebbe mai cancellato da un tracciato record.







