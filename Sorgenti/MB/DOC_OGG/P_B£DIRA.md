# CONCETTI GENERALI


- L'orizzonte che viene coperto deve essere continuo, ossia non possono esserci dei buchi temporali, perché non avrebbero senso applicativo ( se voglio lasciare dei buchi temporali, agisco sul calendario )
- I periodi appartengono ai periodi gerarchicamente superiori, ossia i giorni appartengono ai mesi e alle settimane, le settimane appartengono ai mesi  (il criterio di appartenenza della settimana rispetto al mese, è l'appartenenza del giovedì rispetto al mese). Questo significa che c'è sempre la prima settimana di un mese e l'ultima settimana di un mese (anche la prima settimana dell'anno e l'ultima dell'anno)

Come conseguenza del punto 1, bisogna sempre saldare la fine di un periodo con l'inizio di un altro periodo, e lo si ottiene solamente andando avanti (+) o tornando indietro (-) come descritto dai flag giorni e settimane della tabella A£Q.
Il Blank (default) coincide con il valore '+'.


# LOGICA DI FUNZIONAMENTO PROGRAMMA B£DIRA

A questo punto la formazione dell'orizzonte potrebbe essere descritta dal seguente flusso : 

- Dalla data di inizio si applicano i giorni e si determina il giorno di arrivo ULTGIO
- Viene controllato se ULTGIO è la fine di un periodo del tipo periodo successivo nella A£Q (esempio :  se dopo i giorni ci sono le settimane controllo se ULTGIO è l'ultimo giorno di quella settimana, se invece ci sono i mesi, controllo che sia l'ultimo giorno di quel mese)
- Se è l'ultimo giorno lavorativo di quel tipo periodo, non è necessario né arretrare né aggiungere giorni; si prosegue quindi a costruire colonne temporali con il tipo periodo successivo nella A£Q
- Se invece NON è l'ultimo giorno lavorativo di quel tipo periodo, allora se il flag è '+' si aggiungono giorni fino ad arrivare all'ultimo giorno lavorativo di quel tipo periodo superiore. Se invece il flag è '-' allora vengono tolti giorni fino ad arrivare all'ultimo giorno del periodo precedente.
- Da quella data vengono costruite colonne con il tipo periodo successivo della A£Q


Il '-' arretra sempre, anche arrivando a togliere completamente i periodi messi.

Questo flusso può essere applicato alle settimane invece che ai giorni considerando al posto di ULTGIO la ULTSETT, ossia la settimana di arrivo e la confrontandola con l'ultima settimana del mese in cui cade.
La peridiocità a settimane ha però alcune particolarità.
Se l'ultima settimana ha la fine che non corrisponde all'ultimo lavorativo del mese : 

- Se l'ultima settimana non raggiunge la fine mese nel caso di '+' o ' ' sulle settimane vengono aggiunti periodi a completamento del mese
- Se l'ultima settimana non raggiunge la fine mese nel caso di '-' sulle settimane vengono tolti periodi (arrivando anche a toglierli tutti)
- Se l'ultima settimana è a cavallo tra due mesi e il giovedì fa parte del mese precendete viene allungata l'ultima settimana completa del mese facendola arrivare a fine mese e poi inizia il mese nuovo. (esempio dal 23/11/2015 al 30/11/2015 e poi dal 01/12/2015 al 31/1272015)
- Se l'ultima settimana è a cavallo tra due mesi e il giovedì fa parte del mese successivo nel caso di '-' sulle settimane viene allungata l'ultima settimana completa del mese facendola arrivare a fine mese e poi inizia il mese nuovo. (esempio dal 23/11/2015 al 30/11/2015 e poi dal 01/12/2015 al 31/1272015)
- Se l'ultima settimana è a cavallo tra due mesi e il giovedì fa parte del mese successivo nel caso di '+' o ' ' sulle settimane vengono aggiunte settimane a completamento del mese successivo
- Se l'ultima settimana è tutta nel mese successivo nel caso di '+' o ' ' sulle settimane vengono aggiunti periodi (settimane) a completamento del mese
- Se l'ultima settimana è tutta nel mese successivo nel caso di '-' sulle settimane vengono tolti periodi (settimane) fino alla fine del mese precedente


**E' disponibile la scheda di simulazione di massa B£SER_DA che richiama il servizio omonimo.**
**Da 5250 è possibile testare il comportamento in questo modo :  GO MP00 -> 2 -> 7.**
