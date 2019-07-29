# JAL - Log di collegamento webup, loocup
## OBIETTIVO
Definire le caratteristiche e le modalità con cui tenere traccia delle operazioni effettuate da webup e dagli utenti connessi (in webup e loocup)
## CONTENUTO DEI CAMPI
 :  : FLD T$ELEM
Identifica il messaggio da loggare
 :  : FLD T$DESC
 :  : FLD T$JAL1 __Tipologia messaggio__
Identifica la tipologia del messaggio
VALORI POSSIBILI : 
- C Il Messaggio è un collegamento a loocup o webup;
- 1..9  Un qualsiasi numero può essere utilizzato come classificazione da un utente;
 :  : FLD T$JAL2 __Time out Secondi__
Solo per i messaggi di tipo 'C', imposta dopo quanti secondi il record di collegamento è da considerarsi chiuso.
 :  : FLD T$JAL3 Modalità Rid/Com
Solo per i messaggi di tipo <> DA 'C', imposta in che modo scrivere gli eventi.
Esistono 3 modalità : 
- ' ' non verrà scritto alcun evento;
- 'C' verrà scritto un evento ad ogni richiamo della routine £JAC;
- 'R' verranno raggruppati ed interpretati i richiami della routine £JAC * IN SVILUPPO **;
 :  : FLD T$JAL4 __Modalità coll__
Per gli elementi di tipo collegamento (T$JAL2='C'). Definisce se si sta scrivendo un record di webup o di loocup : 
- W = WEBUP
- L = LOOCUP
Per gli altri elementi definisce se il log è attivo per : 
- W = WEBUP
- L = LOOCUP
- E = ENTRAMBI
 :  : FLD T$JAL5 __Agg collegamento__
Definisce se aggiornare o meno il collegamento per : 
- 1 = SI
- ' ' = NO
