# TRACE

## OBIETTIVI
 Gestire il trace di elaborazioni centralizzando le operazioni di calcolo della durata delle
 elaborazioni e la relativa memorizzazione. Questa API utilizza la struttura QQ per avere
 il minimo indispensabile dell'infrastruttura Sme.UP al fine di evitare possibili allocazioni
 o errori di ricorsione.

**Si ricorda che come tutte le nuove routine i parametri di INPUT sono cancellati ad ogni
**esecuzione e che sono presenti 2 ds, una di input e una di output.


## UTILIZZO DELL'API
 L'API è utilizzata per reperire il tempo iniziale dell'elaborazione, calcolare la durata
 alla fine dell'elaborazione, per infine memorizzarla nel JALOGT0F.


## FUNZIONI E METODI

### INI.CAL   Inizializzazione con calcolo del tempo iniziale
**Restituisce l'istante attuale in formato timestamp UTC, tempo coordinato universale, che
**corrisponde al fuso orario di greenwich, con accuratezza al microsecondo (milionesimo di
**secondo).

### DUR.CAL   Calcola la durata rispetto al tempo passato in input
**Restituisce la durata tra il timestamp UTC passato in input ed il timestamp attuale.

### WRI.LOG   Memorizza la durata passata in input nel JALOGT0F
**La memorizzazione della durata avviene nel campo numerico 5 (J1NUM5) e l'identificativo
**record (J1IDOG) è nel formato Q+numerojob+progressivo. Sono resi disponibili in input
**anche i campi codici 1-2-3, i numeri 1-2-3 e la descrizione, memorizzata nel campo libero J1LIBE.
