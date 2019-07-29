# EAN - Codice EAN (Barcode)
## OBIETTIVO
### Costruzione automatica codice EAN
La tabella contiene i dati utilizzati per la costruzione automatica del codice EAN. Tale costruzione è attiva nel caso in cui sia specificato nella tabella BRA e venga assegnato ad un articolo un codice errato.
_7_IMPORTANTE
Ad ogni cambio di codice costruttore, azzerare il rispettivo progressivo corrente dalla tabella CRN sottosettore EA.
## CONTENUTO DEI CAMPI
 :  : FLD T$EAN1  __Autorità Nazionale__
Rappresenta il "flag" f1 f2 (composto da due caratteri) che identifica l'autorità nazionale di codifica; ogni autorità nazionale di codifica riceve uno o più flags f1 f2; EAN è responsabile per l'assegnazione di questi flags.
 :  : FLD T$EAN2  __Costruttore EAN-8__
Rappresentano nell'EAN-8 le quattro cifre successive all'autorità nazionale che identificano il produttore.
 :  : FLD T$EAN3  __Costruttore EAN-13 (5)__
Rappresentano nell'EAN-13 le cinque cifre successive all'autorità nazionale che identificano il produttore. Questo campo deve essere utilizzato in alternativa al successivo.
 :  : FLD T$EAN4  __Costruttore EAN-13 (7)__
Rappresentano nell'EAN-13 le sette cifre successive all'autorità nazionale che identificano il produttore. Questo campo deve essere utilizzato in alternativa al precedente, qualora il codice costruttore assegnato sia di 7 caratteri.
 :  : FLD T$EANS  __Gruppo numeratori__
Rappresenta il sottosettore della tabella CRN, utizzato nell'assegnazione del progressivo all'interno del codice.
Tale progressivo è costituito da un carattere numerico per l'EAN-8 e di cinque caratteri numerici per l'EAN-13, nel caso si utilizzi il codice costruttore lungo 5 caratteri, o lungo tre caratteri numerici, nel caso si utilizzi il codice costruttore lungo 7 caratteri.
Nella tabella CRN sottosettore EA il progressivo per il codice per controllare l'esaurimento dei progressivi a disposizione.
EAN-8 deve essere definito lungo 2 e per il codice EAN-13 lungo
