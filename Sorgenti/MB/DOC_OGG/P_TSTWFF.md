# OBIETTIVO
 Effettuare le operazioni di lettura, inserimento, aggiornamento e cancellazione sul file contenente
 i promemoria di workflow (WFPROM0F).

# FUNZIONI E METODI

## CLEAR - Inizializzazione campi con pulizia
Inizializza i campi del formato record in preparazione ad un inserimento, incrementando il contatore
dei promemoria.
I campi obbligatori sono il numero dell'impegno di riferimento, tipo, parametro e codice (oggetto
TAB£U relativo all'utente a cui verrà notificato il promemoria), e il tipo promemoria (TAWFP) con le
informazioni relative all'inizializzazione.
E' possibile forzare la modalità di calcolo dell'orario del promemoria; in caso contrario viene
utilizzata quella presente sul tipo promemoria.
Le modalità di calcolo sono :  orario assoluto o relativo calcolato come tempo prima della data/ora
di riferimento impostata.
Nel tipo promemoria è definita la data/ora di riferimento da usare per il calcolo relativo : 
- Libero :  i campi F3DRIF e F3HRIF vengono valorizzati liberamente prima della scrittura
- Data attivazione impegno :  i campi F3DRIF e F3HRIF vengono valorizzati a partire dai campi
F2DPES e F2HPES del WFIMPE0F scritti all'attivazione dell'impegno
- Data rich.esec.impegno :   i campi F3DRIF e F3HRIF vengono valorizzati a partire dai campi
F2DRES e F2HRES del WFIMPE0F
- Data rich.esec.ordine :  il campo F3DRIF è valorizzato a partire dal campo F1DFRI del WFORTE0F;
F3HRIF è impostato a 0

## WRI - Scrittura record
Esegue la scrittura del record (eventualmente ricalcolando la data/ora del promemoria se la modalità
di calcolo è relativa).

## UPD - Aggiornamento record
###  - fasa promemoria
Esegue l'aggiornamento del record fasando lo stato in base allo stato dell'impegno e fasando la data
e l'ora di riferimento in base a quanto impostato nel Tipo promemoria.
### NOF - non fasa promemoria
Esegue l'aggiornamento del record così com'è.
