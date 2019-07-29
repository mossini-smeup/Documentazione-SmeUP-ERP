# Aggiornamenti
## Versione 22

- Salvataggio configurazioni con i numeri in formato naturale, es. 12,3. Fino alla versione 21 i numeri venivano salvati nel formato utilizzato per salvare i numeri nelle tabelle dello SmeUp.
- Gestione tabelle con codice tipizzato
- Oggettizzate le domande configurate multiple per avere l'accesso alle schede delle risposte fornite.
- Esteso il configuratore del setup (Script _R_EDT_G30)
-- e' possibile personalizzare il comportamento del tasto F6, eseguendo il salvataggio senza richiesta di conferma
-- è possibile personalizzare come le descrizioni estese vengono visualizzate
-- è possibile nascondere l'albero delle sezioni
- Gestite le descrizioni estese pre e post domanda e pre e post sezione
-- modificate le tabelle CFD e CFS per abilitare questa funzionalità
-- le descrizioni estese si inseriscono utilizzando i contenitori CFS per le sezioni e CS per le domande
-- la descrizione estesa pre va messe nel capitolo DPR
-- la descrizione estesa pos va messe nel capitolo DPO
- Modifiche al motore delle regole
-- Implementata la regola setExtDesc(domanda, testo, posizione)
-- Implementata la regola che consente di leggere le note strutturate


## Versione 23 - V2R3M091109-02B

- Domande configurate con scelta in lista :  salvate solo le risposte fornite e non tutte
- Motore regole implementata istruzione setExtDesc

- E' stata gestita la modalità sola lettura per le domande configurate a risposta multipla.
- correzione note estese domande di questionario :  da formato HTM a TXT
- corretta gestione history domande numeriche
- corretta attivazione pulsanti toolbar configuratore
-- storia esecuzione
-- storia esecuzione in formato matrice
-- avanti
-- indietro

- G30Dialog forzata chiusura su reloadForm
- gestione cache questionari caricati JA_00_07(?) VIS.CAH

- copia di elementi di tabella con subsettore diverso
- gestione ObjectField numerici senza risposta
- gestione salvataggio configurazioni di questionari Q- con due o più chiavi (NON GESTITO DA CFSER_02)





