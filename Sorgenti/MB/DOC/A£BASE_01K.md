Per tenere ordinato l'AS400 di sviluppo di SME UP, abbiamo definito le seguenti convenzioni sugli utenti.

# Utenti utilizzatori

## Utenti personali
Gli utenti personali sono quelli che hanno una corrispondenza 1 : 1 con una persona.
_Nomenclaura : _
**XXXYYY** in cui XXX sono le iniziali del cognome e YYY le iniziali del nome.
_Password : _
A discrizione dell'utente. Deve seguire le regole di scadenza impostate per il server.
Nota
_Tipologia/autorizzazioni : _
Se utente programmatore : 
Classe *USER. Con possibilità limitate. Senza autorizzazioni speciali. Gruppo QUSER.
Se utente solo utilizzatore : 
Classe *PGMR. Non con possibilità limitate. Senza autorizzazioni speciali. Gruppo QPGMR.

__Nota__
il reset di una password di questi utenti deve sempre esser fatto con impostazione di password "banale" (Es. nome utente+XX) e impostazione di password scaduta.
In questo modo l'utente si cambia la password come vuole senza bypassare le regole del sistema operativo (bypass che invece verrebe fatto impostandola direttam da CHGUSRPRF).

## Utenti di demo (???)
E' necessario avere un prefisso comune per tutti gli utenti che appartengono ad una specifica demo.
Ad esempio gli utenti per le demo di CRM, avrano tutti prefisso CRM.
Questi utenti si dividono a loro volta in due categorie : 
- finali
- di ruolo
Quelli finali sono usati per tutti gli accessi Looc.UP e per gli accessi di tipo USRPRF di Web.UP.
Quelli di ruolo sono usati per gli accessi ROLES di Web.UP.
_Nomenclaura : _
**XXX_yy** in cui XXX è il "prefisso" che raggruppa alcuni utenti
_Password : _
Nel caso di utenti di ruolo, deve essere non banale, non importa se non è "user friendly" tanto non sarà una password da imputare manualmente. Non deve avere scadenza.
Nel caso di utenti finali invece dovrebbe essere "abbastanza userfriendly" in quanto andrà inserita in fase di login.
_Tipologia/autorizzazioni : _
Classe *USER. Con possibilità limitate. Senza autorizzazioni speciali. Gruppo QUSER.

# Utenti di servizio

## Utenti Provider e gateway
Utenti da utilizzare per i vari provider o gateway.
_Nomenclaura : _
**PRVxnn**
x identifica l'AS di riferimento (L per sviluppo e C per amministrativo), nn è un progressivo.
Da notare che il nome coda va impostato uguale all'utente.
In questo modo dato il provider PRVL43, sappiamo subito che è un provider collegato a srvlab e di cui possiamo andare a vedere i JOB.
_Password : _
deve essere non banale, non importa se non è "user friendly" tanto non sarà una password da imputare manualmente. Non deve avere scadenza.
_Tipologia/autorizzazioni : _
Classe *USER. Con possibilità limitate. Senza autorizzazioni speciali. Gruppo QUSER.

## Utenti per intergrazioni esterne (???)
Utenti da utilizzare in caso di integrazioni con sistemi esterni.
_Nomenclaura : _
**SOA_xx**
_Password : _
deve essere non banale, non importa se non è "user friendly" tanto non sarà una password da imputare manualmente. Non deve avere scadenza.
_Tipologia/autorizzazioni : _
Classe *USER. Con possibilità limitate. Senza autorizzazioni speciali. Gruppo QUSER.

## Unico utente per login Web di tipo ROLES (???)
Esiste un unico utente per tutti i login di tipo ROLES.
I JOB che servono autenticazioni di tipo ROLES devono nascere e morire. Se un lavoro resta in esecuzione è un'anomalia. Quindi creiamo un utente per tute queste autenticazioni in modo da identificare più facilmente eventuali problemi.
_Nomenclaura : _
**WAU_ROL**
_Password : _
deve essere non banale, non importa se non è "user friendly" tanto non sarà una password da imputare manualmente. Non deve avere scadenza.
_Tipologia/autorizzazioni : _
Classe *USER. Con possibilità limitate. Senza autorizzazioni speciali. Gruppo QUSER.
_Ambienti di accesso : _
"Uno per ogni JAU". Le JAU del CRM staranno in un a,biente, le JAU di sviluppo in un altro, ecc.

## Unico utente per login Web di tipo FUN
_7_Da fare





__Nota generale sulle password degli utenti senza scadenza__
E' cura del creatore dell'utente memorizzarsi la password con un sistema ritenuto idoneo (es. keepass) e comunicarla a chi lo utilizzerà.
_7_Vero?
