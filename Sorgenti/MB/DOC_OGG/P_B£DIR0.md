# OBIETTIVO
Permettere la manutenzione dell'archivio che definisce le eccezioni alla disponibilità di una risorsa, valide in determinati giorni dell'anno.
Essendo un archivio eccezioni, si immettono solo i valori che si vogliono modificare :  quelli lasciati vuoti si intendono normali e non danno luogo a modifiche.

# DETTAGLIO FORMATI
# Formato guida

![B£DIR0_01](http://localhost:3000/immagini/MBDOC_OGG-P_B£DIR0/BXDIR0_01.png)
## Tipo risorsa gestita
Codice controllato sulla tabella TRG.
## Codice risorsa
Viene controllato sull'anagrafico opportuno, in funzione del tipo di risorsa. I codici che iniziano con '**' non vengono controllati.

## Periodo
Mese e anno per cui si intendono definire delle eccezioni.

# Formato gestione

![B£DIR0_02](http://localhost:3000/immagini/MBDOC_OGG-P_B£DIR0/BXDIR0_02.png)
## Risorsa collegata
Previsto per usi futuri. Attualmente non gestito.
## Codici orario
Codici controllati sulla tabella OLG.
## Numero risorse
Indica il numero di risorse disponibili, in valore assoluto e non come differenza rispetto alla condizione normale. Pertanto non è possibile annullare il numero di risorse (dato che un'eccezionenon può avere valore 0) :  se si intende dichiarare la non disponibilità della risorsa, si deve agire tramite il codice orario.
## Percentuale utilizzo
Previsto per usi futuri. Attualmente non gestito.
# TABELLE COLLEGATE

- TRG  =    Tipo risorsa gestita
- OLG  =    Orari lavorativi

