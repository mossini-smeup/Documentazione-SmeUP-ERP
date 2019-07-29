I log di loocup sono salvati in  file locali, organizzati per sessione
## I log prodotti dal client Loocup
Alla data del 27/11/2007, versione di test di loocup, i file di log sono stati concentrati nella cartella identificata dal percorso
_7_%APPDATA%\Loocup\LOG.

La variabile di windows %APPDATA%, corrisponde alla variabile di Loocup ***APPDATA**.

Se il sistema operativo è Windows XP la variabile viene risolta in : 
C : \Documents and settings\utente_di_windows\Dati Applicazioni\Loocup\
## Durata dei log
I log vengono mantenuti per 7 giorni.
## Nomenclatura
I file hanno  il nome composto secondo due sintassi : 

Sessione_Utente_LOCComponente.estensione
Dove : 

- Sessione :  è il codice della sessione corrente, che corrisponde al numero di lavoro su AS400.
- Utente :  è il codice del'utente
- LOC :  è una costante
- Componente :  è il codice del componente Loggato (J1GRA)
- estensione può essere
-- PR :  indica log di performance (scritti dai componenti EXD e EMU)
-- ERR :  indica log di errore (scritti dai componenti EXD e EMU)
-- CMN :  indica log di comunicazione (solo per il componente EMU)
-- log :  indica log generali o di altri componenti


Sessione_Utente_LOTipoLog.log
Dove : 

- Sessione :  è il codice della sessione corrente, che corrisponde al numero di lavoro su AS400.
- Utente :  è il codice del'utente
- LO :  è una costante
- TipoLog :  è il tipo di log. Attualmente sono definiti i seguenti due tipi
-- PING :  memorizza i messaggi di ping inviati all'AS400 (sono i messaggi necessari a mantenre attivi i lavori su AS400)
-- INFO :  memorizza le informazioni di sato del client

