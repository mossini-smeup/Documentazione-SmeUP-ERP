# GAU - Tab. utenti richieste di acquisto
## OBIETTIVO
In questa tabella dovranno obbligatoriamente essere inseriti tutti gli utenti che utilizzeranno il modulo delle Richieste di Acquisto (GARDA).
## CONTENUTO DEI CAMPI
 :  : FLD T$ELEM Elemento
Utente :  deve essere un oggetto di sistema di tipo UP
 :  : FLD T$DESC Descrizione
Descrizione .
 :  : FLD T$CCRI __Centro di Costo/Riferimento Tab GA1__
Centro di costo/riferimento a cui appartiene l'utente. Quando l'utente inserisce una richiesta, il centro di costo/riferimento richiedente verrà impostato automaticamente a questo valore.
Questo campo contiene un oggetto tipizzato nella tabella GA1 (campi tipo oggetto/parametro oggetto); se il tipo oggetto è bianco, assume il tipo 'CC' centri di costo.
 :  : FLD T$GAUB __Nome del Buyer__
È un elemento della tabella GAB :  se l'utente è anche un buyer, in questo campo viene indicato il suo nome come buyer.
 :  : FLD T$GAUN __Numeratore Richiesta__
È un elemento della tabella CRN/GA :  se impostato, le richieste di questo utente saranno numerate con questo numeratore.
 :  : FLD T$GAUS __Utente speciale__
Se impostato, l'utente, in fase di validazione, potrà modificare le parzializzazioni.
 :  : FLD T$GAUR __Tipo richiesta ass.__
È un elemento della tabella GAR :  se impostato, sarà proposto questo tipo all'atto dell'inserimento delle richieste di questo utente.
 :  : FLD T$GAU1 __Condizione 1__
Le condizioni 1/2/3 sono condizioni libere che caratterizzano l'utente :  sono utilizzabili nei programmi di controllo specifico.
 :  : FLD T$GAU2.T$GAU1 __Condizione 2__
 :  : FLD T$GAU3.T$GAU1 __Condizione 2__
 :  : FLD T$GAUI __Importo (M£)__
È un importo libero (in migliaia di lire), che può essere usato nei programmi di controllo specifico come soglia di accettabilità della richiesta.
 :  : FLD T$GAUF __Gruppo fonti__
È a disposizione dei programmi di controllo specifico, per verificare, ad esempio, la copertura della richiesta.
