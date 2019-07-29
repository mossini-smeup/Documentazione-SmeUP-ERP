## Descrizione
E' possibile attivare l'auditing degli accessi negati al sistema.
Questo può servire in particoalre quando vari accessi causano la disabilitazione di un utente.

### Nota
Le seguenti istruzioni valgono per un sistema in cui l'auditing non è già attivo.
Ossia per un sistema in cui i valori di sistema QAUDCTL e QAUDLVL valgono *NONE.
In altre situazioni valutare caso per caso.

## Attivazione audit
CRTJRNRCV JRNRCV(libreria/AUDRCV0001)
          THRESHOLD(100000)
          TEXT('Auditing Journal Receiver')
          AUT(*EXCLUDE)

CRTJRN JRN(QSYS/QAUDJRN)
       JRNRCV(libreria/AUDRCV0001)
       MNGRCV(*SYSTEM)
       DLTRCV(*NO)
       TEXT('Auditing Journal')
       AUT(*EXCLUDE)

CHGSECAUD QAUDLVL(*AUTFAIL) INLJRNRCV(libreria/AUDRCV0001)

CHGSYSVAL SYSVAL(QAUDCTL) VALUE(*AUDLVL)

## Interrogazione audit
CPYAUDJRNE ENTTYP(PW) OUTFILE(libreria/QAUDIT)

SELECT PWUSRN, PWRADR, PWTYPE, PWTSTP, PWJOB, PWUSER, PWNBR, PWPGM
FROM libreria/QAUDITPW


## Disattivazione audit
DLTF libreria/QAUDITPW

CHGSYSVAL SYSVAL(QAUDCTL) VALUE(*NONE)

CHGSECAUD QAUDLVL(*NONE)
          INLJRNRCV(libreria/AUDRCV0001)

DLTJRN JRN(QSYS/QAUDJRN)

DLTJRNRCV JRNRCV(libreria/AUDRCV0001)

## Significato del tipo violazione
A
APPC bind failure.

C
User authentication with the CHKPWD command failed.

D
Service tools user ID name not valid (QSYCHGDS API, CRTSSTUSR, CHGSSTUSR, DLTSSTUSR commands).

E
Service tools user ID password not valid (QSYCHGDS API, CRTSSTUSR, CHGSSTUSR, DLTSSTUSR commands).

P
Password not valid.

Q
Attempted signon (user authentication) failed because user profile is disabled.

R
Attempted signon (user authentication) failed because password was expired. This audit record might not occur for some user authentication mechanisms. Some authentication mechanisms do not check for expired passwords.

S
SQL Decryption password is not valid.

U
User name not valid.

X
Service tools user ID is disabled.

Y
Service tools user ID not valid (service tools interface).

Z
Service tools user ID password not valid (service tools interface).
