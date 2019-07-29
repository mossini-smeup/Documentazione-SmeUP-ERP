# Variabili di ambiente :  cosa sono
Le variabili di ambiente sono sostanzialmente associazioni nome=valore fatte dal sistema operativo OS400.
Esistono due tipi di variabili di sistema : 
* Job level
* System level
Le variabili di job sono associate ad un job e quindi manipolabili solo da esso. Esse vengono cancellate alla chiusura del job.
Le variabili  di sistema sono invece manipolabili da qualunque job. Esse esistono fino a che non vengono espressamente cancellate. Vengono quindi salvate e ricreate in seguito ad un IPL.
Quando un job cerca di accedere per la prima volta ad una variabile di job, il sistema la eredita da quella di sistema (se esiste). A quel punto è possibile gestire separatamente le due variabili.
Per ogni ulteriore dettaglio si rimanda alla documentazione specifica dei sistemi i.

# Uso in Sme.UP
Con la versione V3R1 di Sme.UP è stato introdotto l'uso (standard) di variabili di ambiente.
Vengono usate sia quelle a livello di sistema che di job.
E' quindi importante conoscere la loro esistenza e alcune informazioni di base.

## Quali variabili vengono usate in Sme.UP
Per vedere tutte le variabili di ambiente attualmente istanziate è sufficiente digitare
WRKENVVAR LEVEL(*JOB) (o LEVEL(*SYS))
Attualmente vengono utilizzate le seguenti variabili : 

| _1_Nome Variabile | _1_SYS/JOB | _1_significato |
| ---|----|----|
| SMESYSLIBL | SYS | librerie Sme.UP di sistema |
| SMEB£1 | JOB | campo TTLIBE di B£1 |
| SMEB£2 | JOB | campo TTLIBE di B£2 |
| SMELOC | JOB | valori relativi alla localizzazione linguistica (lingua, separatori ecc.) |
| SMEENC | JOB | dati di encoding |
| SMEENV | JOB | dati di ambiente (codice ambiente, codice univoco loocup...) |
| 

Le variabili di ambiente con livello di JOB vanno trattate come se fossero una sorta di PDS.

# Accorgimenti
## SBMJOB
Dato che le variabili di job vanno considerate come una PDS, vanno "passate" ad eventuali job sottomessi.
Nel SBMJOB è possibile impostare la copia delle variabili di ambiente da sottomettente a sottomesso. Tale opzione deve essere sempre impostata.
Quindi **IN OGNI SBMJOB effettuato, deve essere presente l'opzione CPYENVVAR(*YES)**

## Autorizzazioni
Dato che le variabili di ambiente assumono una grande importanza, è importante che gli utenti non possano cambiarle.
Vanno quindi autorizzati di conseguenza tutti i comandi che le manipolano (ADDENVVAR, CHGENVVAR, RMVENVVAR e WRKENVVAR)

