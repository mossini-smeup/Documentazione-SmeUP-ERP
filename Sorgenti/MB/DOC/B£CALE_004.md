# Calendario per Squadre
Le funzioni del calendario per squadre premettono di stabilire una disponibilità di risorse all'interno della giornata :  nel giorno sono possibili fino a 6 intervalli di orario in cui si definiscono il numero delle risorse presenti.

# Meccanismo di funzionamento
Per la risorsa gestita a squadre possiamo impostare intervalli orari con numero di risorse per ciascun intervallo a livello di : 
* __giorno specifico__ :  con il programma di manutenzione inseriamo i dati in un giorno specifico (es. 06/10/2012). Possiamo così impostare i giorni particolari in cui la presenza è diversa da quella consueta.
* __giorno della settimana__ :  con il programma di manutenzione inseriamo i dati in un giorno della settimana (es. giovedì). Con un massimo di 7 inserimenti possiamo descrivere così la settimana tipo della squadra.
* __generico__ :  con il programma di manutenzione inseriamo i dati generici validi in qualsiasi giorno.

La disponibilità della squadra è calcolata come l'intersezione del calendario risorsa e il numero di risorse presenti per ogni intervallo di ciascun giorno : 
* attraverso la gestione calendario consueta (calendario annuale, dati settimanali risorsa, eccezioni) si calcola l'orario lavorativo di ciascun giorno
* nel giorno lavorativo, all'interno dell'orario di lavoro (OLG), si calcola il numero di risorse presenti in accordo a quanto impostato con la gestione per squadre

# Utilizzo tipico
Il tipico utilizzo è come risorsa produttiva secondaria : 
* operai a supporto
* disponibilità utensili
* disponibiltà imballi
* ...

# Tabelle interessate
Nella tabella TRG si deve stabilire che un tipo risorsa gestita prevede anche le squadre (campo "Sviluppo squadre").
Nella tabella BRK dove sono definite le risorse produttive secondarie deve essere impostato il campo "Modo di reperimento calendario" che è un elemento della tabella BSC.
Nella tabella BSC il campo origine deve essere = 3

Riferirsi alla documentazione delle singole tabelle per informazioni più approfondite

- [TRG - Tipo risorsa gestita](Sorgenti/MB/DOC_OGG/TA_TRG)
- [BRK - Tipo risorse secondarie](Sorgenti/MB/DOC_OGG/TA_BRK)
- [BSC - Modo reperimento calendario](Sorgenti/MB/DOC_OGG/TA_BSC)
