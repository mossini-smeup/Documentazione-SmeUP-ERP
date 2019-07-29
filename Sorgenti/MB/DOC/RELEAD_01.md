# Lead
## Definizione
 :  : I.INC.MBR Fil(DOC_VOC) Mem(REBASE_GLO) Sec( :  : VOC) SAt(005)

## Schema relazioni
![X1MARK05A](http://localhost:3000/immagini/RELEAD_01/X1MARK05A.png)## Dati
* Codice identificativo
* Date apertura / scadenza passo successivo
* Responsabile
* Account
* Referente
* Tipo lead
* Fonte di provenienza :  evento/fiera, sito internet, newsletter, ecc
* Campagna origine

![X1MARK0502](http://localhost:3000/immagini/RELEAD_01/X1MARK0502.png)
![X1MARK0501](http://localhost:3000/immagini/RELEAD_01/X1MARK0501.png)
## Funzioni
### Creazione nuova opportunità ed assegnazione di un responsabile
Dalla navigazione lead si possono creare delle opportunità mediante il doppio click su una riga lead. Il programma apre il formato di inserimento nuove opportunità ereditando dalla lead il referente, l'account ed il responsabile. La lead finisce nella commessa di riferimento dell'opportunità, in questo modo è assicurato il legame tra opportunità, lead di riferimento e campagna.
In fase di creazione il responsabile viene ereditato dalla lead ma può essere modificando assegnando uno dei responsabili commerciali.

### Scadenzario / promemoria

### Drill down sulle attività di marketing e vendita successive o derivate : 
 * opportunità
 * offerte, ordini, fatture

### Analisi risultati lead
* Conto economico di commessa (costi diretti, margini delle commesse cliente derivate)
* NUmero caratteristici
** n. opportunità, (vinte e perse)



## Implementazione
Le lead sono sull'archivio BRCOMM0F ed hanno tipo commessa = '£R3'

### Campi utilizzati
M$COMM as "Lead;CM£R3",
M$DECM,
M$STAT,
M$CDRE as "Responsabile;CNCOL",
M$COEN as "Account;CNNOM",
M$DT01 as "Data apertura",
M$DT02 as "Scadenza passo successivo",
M$QI02 as "Qualità della lead (perc)",
M$COD3 as "Referente;RN",
M$STCM as "Tipo lead;TABSE£3",
