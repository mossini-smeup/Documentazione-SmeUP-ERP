L'oggetto J1PWD nasce per gestire le password in LoocUp.

Quando un object field viene definito di questo tipo, l'immissione avviene con i caratteri sostituiti da asterischi.

## TODO
Va deciso il metodo di cifratura della password.

Esistono varie possibilità a livello di sicurezza differente.

 - nessuna criptatura :  nessuna sicurezza
 - cripatura sul client
 -- con chiave generata al momento dell'installazione
 -- con chiave definita nel codice
 - criptatura sul server mediante un servizio apposito

Se la password deve essere gestita sia sul server che sul client la criptatura mediante un servizio apposito è la soluzione da adottare.
Come contro vi è il passaggio in chiaro della password in risposta.
Per evitare di comunicare la password in chiaro si può pensare di replicare il meccanismo di cifratura sul client.

La chiave di cifratura potrà essere
- fissa
- differente per ogni installazione di SmeUp
- differente per ogni utente


