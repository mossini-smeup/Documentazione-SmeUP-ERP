
### Tabelle
E' possibile abilitare/disabilitare globalmente l'invio di notifiche all'app mobile tramite il campo T$B£7K della tabella B£7
### Parametri
* E' possibile abilitare/disabilitare per un utente l'invio di notifiche all'app mobile tramite il parametro esteso dell'utente K/£U1/£00 .
* I device a cui inviare le notifiche mobile sono salvati nel parametro esteso multiplo dell'utente K/£U1/£01 .
* I device a cui non inviare le notifiche mobile sono salvati nel parametro esteso multiplo dell'utente K/£U1/£02 .

 :  : T04 Elementi da fasare rispetto al modello : 
TA C£E £U1
TA B£G £U1
SS B£N £U
TA B£N£U £00
TA B£N£U £01
TA B£N£U £02

### UP UT3
L'invio delle notifiche mobile necessita delle configurazioni (da restorare tramite UP UT3)
 /SMEDOC/SECFG/SESUB.A3801.S00.B00.cfg
 /SMEDOC/SECFG/SESUB.A3801.S00.B01.cfg
Il percorso in cui restorare i file .cfg è restituito dal pgm LOUT01.

- [](Sorgenti/MB/DOC_OGG/P_TSTK14)
- [](Sorgenti/MB/DOC_OGG/P_TSTK17)
