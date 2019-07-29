# OBIETTIVO
Gestire le operazioni base sull'oggetto Q1 Query.

# FUNZIONI E METODI

## DEC - Decodifica
Viene eseguita la decodifica della query.

## DAT - Ritorno dati
Viene ritornata in £IQ1OU la DS £IQ1D contenente tutte le proprietà della query.

>   £IQ1DCD Codice
   £IQ1DDE Descrizione
   £IQ1DFN Fonte
   £IQ1DSC Schemi        ato
   £IQ1DFL Filtri
   £IQ1DOR Ordinamenti
   £IQ1DNE Num. elementi
   £IQ1DPF Filtro in ingresso
   £IQ1DDF Query default
   £IQ1DSD Schema di default
   £IQ1DFD Filtro di default
   £IQ1DOD Ordin. di default


## DAT : DFT - Ritorno query default
Vengono ritornati i dati della query di default.

## LIS - Lista query
Viene ritornata la sequenza delle query disponibili per l'oggetto.
Le query disponibili dipendono dalle fonti registrate per l'oggetto £IQ5(LIS)

## LIS.SCH - Lista schemi della query
Viene ritornata la sequenza degli schemi disponibili per la query.
La sequenza comprende schemi pubblici e privati della query.

## LIS.FLT - Lista filtri della query
Viene ritornata la sequenza dei filtri disponibili per la query.
La sequenza comprende filtri pubblici e privati della query.

## LIS.ORD - Lista ordinamenti della query
Viene ritornata la sequenza degli ordinamenti disponibili per la query.
La sequenza comprende ordinamenti pubblici e privati della query.

## LIS.PAR - Lista parametri della query
Di futura implementazione.
