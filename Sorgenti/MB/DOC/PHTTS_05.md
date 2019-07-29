# Obiettivo
Verificare la corretta installazione del modulo Fiel.up

# Verifiche oggetti
## Oggetti di sistema
 :  : DEC T(OJ) P(*USRPRF) K(TTS)
>L'utente deve essere autorizzato all'uso delle librerie

**Attenzione : **verificare che la *JOBD dell'utente TTS sia compatibile con l'ambiente su cui si sta lavorando!
Se Smeup    *JobD = QGPL/SMEUP01
Se XXX      *JobD = QGPL/XXX
 :  : DEC T(OJ) P(*FILE) K(PHMAN0V)
 :  : DEC T(OJ) P(*CTLD) K(TTSCTL)
 :  : DEC T(OJ) P(*DEVD) K(TTSDEV)

## OAV
 :  : DEC T(OG) P(OA) K(CS)

## Tabelle
 :  : DEC T(OG) P(TA) K(PH1)
 :  : DEC T(OG) P(TA) K(PHM)
 :  : DEC T(OG) P(TA) K(PHN)
 :  : DEC T(OG) P(TA) K(PHC)
 :  : DEC T(OG) P(TA) K(PHT)
 :  : DEC T(OG) P(TA) K(PHD)
 :  : DEC T(OG) P(TA) K(PHR)
 :  : DEC T(OG) P(TA) K(TT1)
 :  : DEC T(OG) P(SS) K(TT101)
 :  : DEC T(OG) P(SS) K(TT102)
 :  : DEC T(OG) P(SS) K(TT103)

## Programmi
 :  : DEC T(OJ) P(*PGM) K(PHFUIN)
>Il proprietario del programma deve essere QSECOFR, per poter svolgere tutte le funzioni di installazione, tra le quali creare profili utente.

 :  : INI _7_<<Verificare il proprietario dell'oggetto in linea,
 :  : CMD DSPOBJAUT OBJ(*LIBL/PHFUIN) OBJTYPE(*PGM)
 :  : FIN
 :  : INI _7_<<se necessario, modificare il proprietario.
 :  : CMD CHGOBJOWN OBJ(*LIBL/PHFUIN) OBJTYPE(*PGM) NEWOWN(QSECOFR)
 :  : FIN

## Verifiche fisiche
 * Master acceso e collegato in rete (il led "link" deve essere verde)
 * Slave collegati al Master
