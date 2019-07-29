# Funzione = GES (Gestione)
Gestire l'anagrafico cambi in Euro o in Lire.

Campi significativi : 
 * Tipo cambio
 * codice divisa
 * data operazione.
In funzione dei campi scelti carica la parzializzazione e l'ordinamento opportuno.

## Metodo = INT (Interrogazione)
Modalita d'accesso in visualizzazione.
## Metodo = MOD (Modifica)
Modalita d'accesso in modifica.

# Funzione = GES (Gestione giornaliera)
Gestisce l'anagrafico cambi ad una data in Euro o in Lire.

Campi significativi : 
 * Tipo cambio
 * codice divisa
 * data operazione (obbligatoria)
In funzione dei campi scelti parzializza.

## Metodo = INT (Interrogazione)
Modalita d'accesso in visualizzazione.
## Metodo = MOD (Modifica)
Modalita d'accesso in modifica. E' possibile, se attiva, la fasatura della tabella valute al cambio presente nella data in essere.

# Funzione = LET (Lettura)
Restituisce il valore valido del cambio £G07CA alla data.
Campi significativi : 
 * Tipo cambio (obbligatorio)
 * codice divisa (obbligatorio)
 * data operazione (obbligatoria)

## Metodo = EURO
Viene restituito il controvalore in Euro secondo la modalità : 
Certo Euro - incerto Valuta
Es :  Euro = 1,15 Dollari
## Metodo = blank
Viene restituito il controvalore in Lire secondo la modalità : 
Certo Valuta- incerto Lira
Es :  Dollaro = 1625,32 Lire

# Funzione = CAM (Andamento del cambio)
Presenta graficamente l'andamento del cambio da una data in avanti o indietro per il periodo di un anno.
Campi significativi : 
 * Tipo cambio (obbligatorio)
 * codice divisa (obbligatorio)
 * data operazione (obbligatoria)

## Metodo = PRO (Progressione)
## Metodo = REG (Regressione)

# Funzione = CON (Conversione)
Restituisce il controvalore di una quantità da convertire dalla divisa origine a quella di destinazione.
Campi significativi : 
Campi significativi : 
 * Tipo cambio (obbligatorio)
 * codice divisa (obbligatorio)
 * data operazione (se nulla assume quella odierna)
 * Importo da convertire
 * Tipo cambio in cui convertire (se nullo assunto ''1'' o ''E'' in funzione dell'attvazione della divisa a cambio fisso)
 * Codice divisa in cui convertire( se nulla assunto default tabelle B£2, CAUCAON,..)

Con data inferiore al 01.01.99 il cambio, in anagrafico, è espresso in lire. Per la conversione tra diverse valute viene eseguita la triangolazione con la lira assunta con cambio unitario.
Dopo il 01.01.99 Il cambio è espresso in divisa(incerto). Per la conversione viene eseguita la triangolazione con l'EURO.Per valute a cambio fisse attive alla data viene autamaticamente ripreso il valore del cambio con tipo 'E' .

## Metodo = blank (Senza approssimazione)
Viene restituito il controvalore approssimato al massimo numero di decimali disponibili 6.
## Metodo = APP (Con approssimazione)
Viene restituito il controvalore approssimato al massimo numero di decimali definiti nella tabella della valuta.
