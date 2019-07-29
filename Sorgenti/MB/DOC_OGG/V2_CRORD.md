# MOSCA     -  CRITERIO DI ORDINAMENTO
Definisce il criterio di ordinamento (dispatching rule) riportato negli impegni risorse avanzati (S5IRIS) ed utilizzato
nella schedulazione BCD.
Nell'ordinamento, questo campo viene preceduto dalla priorità manuale (nel caso di impegni di produzione o di  ciclo
esterno).

## NOTA TECNICA
I valori numerici vengono riportati nell'archivio come campi di 20 caratteri.
In ordinamento discendente viene riportato il loro complemento a  999999.
Se sono possibili valor negativi viene aggiunto un offset di 1000000

## VALORI POSSIBILI

### ' ' Nessun criterio
Il campo criterio viene lasciato in bianco.

### '1' ESD (Earliest Start Date)
Per gli impegni di produzione    - Data inizio richiesta
Per gli impegni di ciclo esterno - Data consegna richiesta
Per gli impegni pianificati      - Data suggerimento

### '2' EDD (Earliest Due Date)
Per gli impegni di produzione    - Data fine richiesta
Per gli impegni di ciclo esterno - Data consegna confermata
Per gli impegni pianificati      - Data fine pianificata

### '3' SPT (Shortest Processing Time)
Ore di carico dell'impegno (a partire dal tempo più breve)

### '4' LPT (Longest Processing Time)
Ore di carico dell'impegno (a partire dal tempo più lungo)

### '5' LWKR (Least Work Remaining)
Somma delle ore di carico delle operazioni non iniziate

### '6' TWKR (Total Work Remaining)
Somma delle ore di carico di tutte le operazioni

### '7' MSUT (Minimum Setup Time)
Ore di attrezzaggio dell'impegno

### '8' MST (Minimum Slack Time)
Slack time
Necessita la schedulazione a capacità infinita al più presto
Esso è dato dalla differenza tra i giorni disponibili (data fine richiesta - oggi) ed i giorni di
transito (data fine schedulazione a capacità infinita al più presto - (maggiore tra data inizio
richiesta e oggi)
Se positivo esprime i giorni di sicurezza per il completamento dell'ordine.
Se negativo esprime invece i giorni di ritardo.

### '9' S/OPN (Slack Time per Operation)
Slack time diviso per le operazioni non iniziate
Necessita la schedulazione a capacità infinita al più presto

### 'A' CR (Critical Ratio)
Rapporto critico
Necessita la schedulazione a capacità infinita al più presto
E' dato dal rapporto tra i giorni disponibili ed i giorni di transito (riferirsi alla documentazione del punto '8')
Se maggiore di 1 significa che l'ordine è in anticipo
Se compreso tra 0 e 1 significa che l'ordine è in ritardo (ma non scaduto)
Se minore di 0 significa che l'ordine è scaduto. In questo caso il risultato del calcolo non è un valore significativo,
in quanto a pari ritardo un valore più alto di giorni di transito, essendo al denominatore, produce un numero in valore
assoluto più alto, e quindi, essendo negativo, più basso.
Si è preferito in questo caso riportare il valore di slack time.
Per renderlo numericamente omogeneo ai valori positivi lo si divide per 10 :  un Critical Ratio di -0.3 rappresenta un
ordine scaduto con slack time di -3 giorni.

### 'B' FISF (First In The System First Served)
Impegno entrato per primo nel sistema (data creazione dell'ordine/riga di ciclo esterno).
Per i consigli di pianificazione (che entrano tutti alla data dell'MRP) si usa comunque la EDD (regola '2')

### 'C' FROP (Fewest Remaning Operation)
Minor numero di operazioni non iniziate

### 'D' MROP (Most Remaning Operation)
Maggior numero di operazioni non iniziate

### 'E' SSD (Start Schedulad Date)
Data inizio schedulata dell'ordine a capacità infinita all'indietro
Necessita la schedulazione a capacità infinita al più tardi

### 'F' SOSD (Start Operation Schedulad Date)
Data inizio schdulata di ogni operazione a capacità infinita all'indetro
Necessita la schedulazione a capacità infinita al più tardi

### 'O' OAV (Object Attribute Value) BASE
Viene ritornato l'OAV dell'oggetto intestatario dell'impegno (ordinie/riga/consiglio) impostato nel campo parametro priorità. E'usato l'OAV base (£OAVOR)

### 'P' PROGRAMA SPECIFICO INTERMDEIO
Viene eseguito un programma specifico impostato nel campo parametro priorità, lanciato duramte il completamento degli
impegni risorse.
A questo programma vengono passate le DS dell'impegno risorse e dell'oggetto intestatario dell'impegno

### 'Q' PROGRAMA SPECIFICO FINALE
Viene eseguito un programma specifico impostato nel campo parametro priorità, lanciato dopo aver costruito tutti gli
impegni e calcolato gli indici.
A questo programma vengono passate le DS dell'impegno risorse e dell'oggetto intestatario dell'impegno, ed una schiera
con i 99 numeri calcolati. In tal modo è possibile costruire criteri articolati, composti anche da indici.

### 'R' OAV (Object Attribute Value) ESTESO
Viene ritornato l'OAV dell'oggetto intestatario dell'impegno (ordinie/riga/consiglio) impostato nel campo parametro priorità. E'usato l'OAV esteso (£OAVO_VAES)
