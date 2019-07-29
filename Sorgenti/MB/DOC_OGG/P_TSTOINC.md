# FUNZIONI SUI GIORNI LAVORATIVI.
INPUT
Azioni : 
- ' '  Incremento di una data di N giorni lavorativi
2    - '2'  Controllo di una data se corrisponde ad un giorno lavorat.
3    - '3'  Calcolo N giorni lavorativi compresi tra due date
Tipo risorsa : 
Tipo di risorsa gestita da tabella TRG.
Campo obbligatorio.
Data iniziale : 
Data da incrementare in Azione 1.
Data da controllare  in Azione 2.
Data di partenza     in Azione 3.
Campo obbligatorio.
Data Finale : 
Data di arrivo in Azione 2.
Campo obbligatorio in Azione 2.
Giorni di incremento : 
Giorni da incrementare alla data di pertenza in Azione 1.
Campo obbligatorio in Azione 1.
OUTPUT
Data calcolata : 
Data incrementata di N gg a partire dalla data iniziale in Azione 1.
Data di controllo ovvero data iniziale in Azione 2.
Data finale in Azione 3.
Giorni di incremento : 
Giorni incrementati alla data iniziale in Azione 1.
Giorni compresi fra data iniziale e data finale in Azione 3.
Flag di errore : 
Codice di ritorno controllo data lavorativa in Azione 2 : 
- Valore ' ' --> Data lavorativa
- Valore '1' --> Data non lavorativa.
