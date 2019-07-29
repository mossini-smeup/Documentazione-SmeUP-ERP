# Introduzione
La strada che porta ad una "buona installazione" passa anche attraverso la "pulizia" del sistema operativo che supporta il sistema applicativo.

In questa sezione tratteremo : 
 * Valori di sistema
 * Completamento installazione programmi su licenza
 * Default per comandi
 * Cambio SIGNON
 * Accensioni/Spegnimenti macchina
 * Salvataggi
 * Pulizia e ottimizzazione delle risorse
 * Schedulazione lavori
 * Sottosistemi e code lavori
 * Profili utente e autorizzazioni
 * Device
 * Utilità

>N.B. :  l'applicazione dei suggerimenti che seguono deve comunque essere decisa in comunione con il responsabile del sistema presso il cliente

## Valori di sistema
Suggeriamo : 
>_1_Nome           _1_Descrizione                                    _1_Valore
QAUTOVRT          Config. autom. unità virtuali                   _5_*NOMAX
                  _3_(impostare a 0 solo se non si vuole permettere collegamenti non codificati)
_1_ cambia valore >>

 :  : INI
 :  : CMD CHGSYSVAL  SYSVAL(QAUTOVRT) VALUE(*NOMAX)
 :  : FIN
QCTLSBSD          Sottosistema di controllo                       _5_QSYS/QCTL
### cambia valore >>
 :  : INI
 :  : CMD CHGSYSVAL  SYSVAL(QCTLSBSD) VALUE('QCTL')
 :  : FIN
QDEVRCYACN        Azione errore I/E unità                         _5_*ENDJOB
                  _3_(qualora si avesse la configurazione di device a nome prefissato, si può
                  _3_ valutare di impostare il default *DSCJOB per recuperare i lavori sospesi)

### cambia valore >>
 :  : INI
 :  : CMD CHGSYSVAL  SYSVAL(QDEVRCYACN) VALUE(*ENDJOB)
 :  : FIN
QJOBMSGQFL        Azione integrale della coda messaggi di lavoro  _5_*WRAP

### cambia valore >>
 :  : INI
 :  : CMD CHGSYSVAL  SYSVAL(QJOBMSGQFL) VALUE(*WRAP)
 :  : FIN
 QLMTSECOFR       Limite accesso unità respons.riser.             _5_0

### cambia valore >>
 :  : INI
 :  : CMD CHGSYSVAL  SYSVAL(QLMTSECOFR) VALUE('0')
 :  : FIN
 QMAXSGNACN       Azione per tentativi non validi di collegamento _5_3

### cambia valore >>
 :  : INI
 :  : CMD CHGSYSVAL  SYSVAL(QMAXSGNACN) VALUE('3')
 :  : FIN
 QMAXSIGN         Num. mass. tentativi collegam.                  _5_3

### cambia valore >>
 :  : INI
 :  : CMD CHGSYSVAL  SYSVAL(QMAXSIGN) VALUE('3')
 :  : FIN
 QPWDEXPITV       Interv. scadenza par. d'ordine                  _5_120

### cambia valore >>
 :  : INI
 :  : CMD CHGSYSVAL  SYSVAL(QPWDEXPITV) VALUE('120')
 :  : FIN
 QPWDMAXLEN       Lung. mass. par. d'ordine ne                    _5_10

### cambia valore >>
 :  : INI
 :  : CMD CHGSYSVAL  SYSVAL(QPWDMAXLEN) VALUE(10)
 :  : FIN
 QPWDMINLEN       Lung. min. par. d'ordine ne                     _5>n_

### cambia valore >>
 :  : INI
 :  : CMD CHGSYSVAL  SYSVAL(QPWDMINLEN) VALUE(8)
 :  : FIN
 QPWDRQDDIF       Contr. pr. d'ordine dupl.                       _5_5 (10)
                  _3_(impostazioni sicurezza condizionate dal "documento programmatico sulla
                  _3_ sicurezza")

### cambia valore >>
 :  : INI
 :  : CMD CHGSYSVAL  SYSVAL(QPWDRQDDIF) VALUE('5')
 :  : FIN
 QSECURITY       Liv.riserv. sistema                              _5_30
                  _3_(salvo specifica richiesta)

### cambia valore >>
 :  : INI
 :  : CMD CHGSYSVAL  SYSVAL(QSECURITY) VALUE('30')
 :  : FIN
 QSTRUPPGM       Progr. di avvio                                  _5_SMESYS/B£QQQS
                  _3_(Il prototipo del programma è distribuito da SME.up e si trova nel   
                  _3_ file sorgente SMEQSM. Invitiamo a spostarlo nel file SRC_SYS della  
                  _3_ libreria SMESYS e impostare le eventuali proprie modifiche)         



### gestione valore >>
 :  : INI
 :  : CMD WRKSYSVAL  SYSVAL(QSTRUPPGM)
 :  : FIN
 QSYSLIBL        Parte sist. elenco librerie                      _5_aggiungere SMESYS
                  _3_(come da installazione durante LODRUN)

### gestione valore >>
 :  : INI
 :  : CMD WRKSYSVAL  SYSVAL(QSYSLIBL)
 :  : FIN


## Comandi collegati : 
### Gestione valori di sistema >>
 :  : INI
 :  : CMD WRKSYSVAL
 :  : FIN

### Stampa valori di sistema >>
 :  : INI
 :  : CMD WRKSYSVAL OUTPUT(*PRINT)
 :  : FIN

# Completamento installazione programmi su licenza
I nuovi sistemi normalmente pervengono già preinstallati con tutti i programmi su licenza necessari al funzionamento completo di Sme.up, però in casi particolari può essere necessario completare l'installazione di sistema operativo con : 
 * 57xxSS1 opzione 13 :  OS/400 - Include apertura del sistema
 * 57xxSS1 opzione 22 :  OS/400 - ObjectConnect
Il primo è necessario qualora si necessiti compilare programmi che utilizzano le API di sistema operativo, mentre il secondo è necessario qualora si intenda utilizzare il supporto del sistema operativo per trasferire librerie ed oggetti da un AS400 ad un altro (ad esempio per il passaggio da un vecchio sistema ad uno nuovo), utilizzando i comandi SAVRSTLIB e SAVRSTOBJ.

# Default comandi
L'ambiente di sviluppo di Sme.up, sia a livello di sviluppo standard che presso i clienti, sfrutta diverse personalizzazioni di comandi di sistema, che vengono effettuate mediante il cambiamento dei default (CHGCMDDFT).

Impostando opportunamente le variabili di ambiente : 
 :  : DEC T(TA) P(B§V) K(_&_DFTRELC) I(variabile)
**Valore attuale :  &DFTRELC
 :  : DEC T(TA) P(B§V) K(_&_DFTRELS) I(variabile)
**Valore attuale :  &DFTRELS
 :  : DEC T(TA) P(B§V) K(_&_DFTLABS) I(variabile)
**Valore attuale :  &DFTLABS

che attualmente impostano : 
 * Release di compilazione oggetti **'&DFTRELC'**
 * Release di salvataggio supporto **'&DFTRELS'**
 * Label default inizializzazione nastro **'&DFTLABS'**

**Att.ne se si effettuano modifiche alle variabili è necessario effettuare un refresh tramite F05

si potranno impostare i default dei comandi di sistema come proposti : 
> » Creazione file sorgente con lunghezza a 112 bytes (CRTSRCPF)
 :  : INI > eseguo impostazione >>
 :  : CMD CHGCMDDFT  CMD(CRTSRCPF) NEWDFT('RCDLEN(112)')
 :  : FIN
 » Nel debug si possono aggiornare i files di produzione (STRDBG, STRISDB)
 :  : INI > eseguo impostazione >>
 :  : CMD CHGCMDDFT  CMD(STRDBG) NEWDFT('UPDPROD(*YES)')
 :  : CMD CHGCMDDFT  CMD(STRISDB) NEWDFT('UPDPROD(*YES)       INVPGM(*NO)')
 :  : FIN
 » Creazione file video con riemissione formato (CRTDSPF)
 :  : INI > eseguo impostazione >>
 :  : CMD CHGCMDDFT  CMD(CRTDSPF) NEWDFT('RSTDSP(*YES)')
 :  : FIN
 » Creazione file di database con ampiezza (CRTPF)
 :  : INI > eseguo impostazione >>
 :  : CMD CHGCMDDFT  CMD(CRTPF) NEWDFT('SIZE(100000 10000 100)')
 :  : FIN
 » Inizializzazione nastro (INZTAP)
 :  : INI > eseguo impostazione >>
 :  : CMD CHGCMDDFT  CMD(INZTAP) NEWDFT('NEWVOL(&DFTLABS)       CHECK(*YES) DENSITY(*CTGTYPE) CLEAR(*NO)')
 :  : FIN
 » Salvataggio libreria (SAVLIB)
 :  : INI > eseguo impostazione >>
 :  : CMD CHGCMDDFT  CMD(SAVLIB) NEWDFT('TGTRLS(&DFTRELS) SAVACT(*LIB)')
 :  : FIN
 » Salvataggio oggetto (SAVOBJ)
 :  : INI > eseguo impostazione >>
 :  : CMD CHGCMDDFT  CMD(SAVOBJ) NEWDFT('TGTRLS(&DFTRELS) SAVACT(*LIB)')
 :  : FIN
 » Salvataggio cartella (SAVDLO)
 :  : INI > eseguo impostazione >>
 :  : CMD CHGCMDDFT  CMD(SAVDLO) NEWDFT('TGTRLS(&DFTRELS)       SAVACT(*YES) DTACPR(*YES)')
 :  : FIN
 » Opzioni di compilazione di programmi RPG (CRTRPGPGM)
 :  : INI > eseguo impostazione >>
 :  : CMD CHGCMDDFT  CMD(CRTRPGPGM) NEWDFT('TGTRLS(&DFTRELC)       USRPRF(*OWNER)')
 :  : FIN
 » Opzioni di compilazione di programmi SQL (CRTSQLRPG)
 :  : INI > eseguo impostazione >>
 :  : CMD CHGCMDDFT  CMD(CRTSQLRPG) NEWDFT('COMMIT(*NONE)       OPTION(*SOURCE) TGTRLS(&DFTRELC)')
 :  : FIN
 » Opzioni di compilazione di programmi RPGLE (CRTBNDRPG)
 :  : INI > eseguo impostazione >>
 :  : CMD CHGCMDDFT  CMD(CRTBNDRPG) NEWDFT('DFTACTGRP(*NO)       ACTGRP(*CALLER) DBGVIEW(*SOURCE) USRPRF(*OWNER)       TGTRLS(&DFTRELC)')
 :  : FIN
 » Opzioni di compilazione di programmi SQLRPGLE (CRTSQLRPGI)
 :  : INI > eseguo impostazione >>
 :  : CMD CHGCMDDFT  CMD(CRTSQLRPGI) NEWDFT('COMMIT(*NONE) DBGVIEW(*SOURCE)                       USRPRF(*OWNER) TGTRLS(&DFTRELC)')
 :  : FIN
 » Opzioni di compilazione di programmi CLP (CRTCLPGM)
 :  : INI > eseguo impostazione >>
 :  : CMD CHGCMDDFT  CMD(CRTCLPGM) NEWDFT('USRPRF(*OWNER)       TGTRLS(&DFTRELC)')
 :  : FIN
 » Opzioni di compilazione di programmi CLLE (CRTBNDCL)
 :  : INI > eseguo impostazione >>
 :  : CMD CHGCMDDFT  CMD(CRTBNDCL) NEWDFT('DFTACTGRP(*NO)       ACTGRP(*CALLER) USRPRF(*OWNER) TGTRLS(&DFTRELC)       DBGVIEW(*SOURCE)')
 :  : FIN
 » Opzioni di compilazione di programmi JAVA (CRTJVAPGM)
 :  : INI > eseguo impostazione >>
 :  : CMD CHGCMDDFT  CMD(CRTJVAPGM) NEWDFT('TGTRLS(&DFTRELC)')
 :  : FIN
 » Opzioni di fine lavoro (ENDJOB)
 :  : INI > eseguo impostazione >>
 :  : CMD CHGCMDDFT  CMD(ENDJOB) NEWDFT('OPTION(*IMMED) LOGLMT(0)')
 :  : FIN
 » Opzioni creazione profilo utente (CRTUSRPRF)
 :  : INI > eseguo impostazione >>
 :  : CMD CHGCMDDFT  CMD(CRTUSRPRF) NEWDFT('AUT(*USE)')
 :  : FIN
 » Metodo recupero azioni schedulate (ADDJOBSCDE)
 :  : INI > eseguo impostazione >>
 :  : CMD CHGCMDDFT CMD(ADDJOBSCDE) NEWDFT('RCYACN(*NOSBM)')
 :  : FIN
 » Copia variabili di ambiente in sottomissione lavori (SBMJOB)
 :  : INI > eseguo impostazione >>
 :  : CMD CHGCMDDFT CMD(SBMJOB) NEWDFT('CPYENVVAR(*YES)')
 :  : FIN


# Cambio SIGNON
L'operazione è semplice e rende gli utenti + contenti! Basta creare un file video apposito.

Si parte da>QDSIGNONsorgente contenuto in>QGPL/QDDSSRC(QDSIGNON)presente di default su tutti i sistemi AS400.
Si può modificare a piacere, con l'unica _R_accortezza di _1_non riordinare mai i campi I/O (mediante i consueti tasti F4+F6 dallo SDA), che comporterebbe la variazione del buffer di  comunicazione tra sistema e file video e non funzionerebbe più.

Una volta compilato nella libreria _7_SMESYS, bisogna abbinarlo al sottosistema _7_QINTER per renderlo attivo, seguendo la seguente procedura operativa : 
1) Assicurarsi che tutti gli utenti attivi in QINTER abbiano concluso i propri lavori e siano scollegati dal sistema
2) Collegarsi con l'utente_7_QSECOFRo alternativo, e digitare il comando_7_TFRJOB JOBQ(QCTL) per trasferire il proprio lavoro nel sottosistema di controllo.
 :  : INI >  eseguo _1_ATTENZIONE!_7_il lavoro corrente verrà riavviato.. >>>
 :  : CMD TFRJOB ?*JOBQ(QCTL)
 :  : FIN
3) Chiudere sottosistema QINTER con il comando _7_ENDSBS SBS(QINTER) OPTION(*IMMED)
 :  : INI >  eseguo >>
 :  : CMD ENDSBS ?*SBS(QINTER) ?*OPTION(*IMMED)
 :  : FIN
4) Abbinare il formato video di collegamento al sottosistema QINTER, mediante il comando _7_CHGSBSD SBSD(QINTER) SGNDSPF(SMESYS/QDSIGNONxx)
 :  : INI >  eseguo >>
 :  : CMD CHGSBSD ?*SBSD(QINTER) ??SGNDSPF(SMESYS/QDSIGNONxx)
 :  : FIN
5) Avviare sottosistema QINTER mediante il comando _7_STRSBS SBSD(QINTER)
 :  : INI >  eseguo >>
 :  : CMD STRSBS ?*SBS(QINTER)
 :  : FIN

# Accensioni/Spegnimenti macchina
Lo spegnimento e l'accensione possono dipendere da diversi fattori : 
 * GO power
 * PWRDWNSYS RESTART(*YES)
 * Sincronizzare CHGCLNUP con *SCDPWROFF

# Salvataggi
## Quando
 * Predisporre supporti specifici per LUN-MAR-MER-GIO (VEN)
 * Predisporre inoltre salvataggi di sistema almeno una volta all'anno o prima delle ferie principali

## Cosa
 * Librerie
 ** tutte le notti SMEDATxxx, SME_xxx, SMESYS
 ** ad ogni rilascio o installazione di aggiornamento SMEDEV, SMEUP_OBJ, SMESTD, SMESRC, SMEMOD, SMECON
 * Cartelle eventuali
 * Root eventuali

## Come
Utilizzo del S.o. per librerie e cartelle (già previsto da b£5)
Utilizzo del comando SAV per Root oppure QEZPWROFFP (vedi B£5)

>N.B. :  Con i salvataggi organizzati con tab. B£5 è possibile sincronizzare lo spegnimento della macchina dopo aver effettuato i salvataggi.
Nel caso in cui il lavoro che supporta il salvataggio (B£PWR..) sia in stato MSGW non rispondere al messaggio, bensì "abbattere" il lavoro con *IMMED, in modo da non SPEGNERE la macchina.

## Sospesi
Meccanismo dell'*UNLOAD

## Schedulazione lavori
 :  : INI Gestione lavori schedulati
 :  : CMD WRKJOBSCDE

_B_B£UT05A
E' fortemente consigliato di schedulare ogni notte questo programma di utility, che ha lo
scopo di controllare la dimensione di alcuni file di smeup, al fine di applicarvi un eventuale
ridimensionamento nel caso la percentuale di occupazione raggiunga il 90%. L'operazione di
ridimensionamento non comporta aumento della memoria occupata fintanto che non vengono scritti nuovi
nuovi record.
Tale lavoro schedulato deve avere una JOBD con lista librerie Sme.UP.
Nella call a questo programma va indicata la libreria da controllare : 
CALL       PGM(B£UT05A) PARM('SMEDATXXX')
Se esistono differenti ambienti, il pgm dovrebbe essere schedulato per ognuno di questi.


 :  : FIN

# Pulizia e ottimizzazione risorse
Suggeriamo : 
_B_CLEANUP

_2_IMPOSTARE
>Consentita ripulitura automatica  . . . . . . . .   Y
Orario inizio giornaliero della ripulitura  . . .   *SCDPWROFF
Numero di giorni per la conservazione di : 
Messaggi utente . . . . . . . . . . . . . . . .   1
Messaggi di sistema e di terminale  . . . . . .   1
Registrazioni lavori e altre emissioni di sistema . . . . . . . . . . . . . . . . . . .   2
Giornali di sistema e registrazioni di sistema    1


_2_NOTE
La ripulitura automatica, nel caso siano attive le personalizzazioni di sistema (tab.B£5), parte **PRIMA** delle attività di chiusura impostate in tale tabella.
L'orario di inizio giornaliero deve essere impostato ad un certo orario qualora la macchina non si spenga.

_B_ALTRE
Verificare le stampe utente e di sistema con un WRKOUTQ *ALL, elimina tutto il vecchiume (ad esempio QEZDEBUG e QEZJOBLOG possono generalmente essere svuotate);
Verificare se ci sono dei files QHST* di troppo *FILE nella QSYS
Con RCLSPLSTG *NONE si può recuperare lo spazio delle stampe cancellate

# Profili utente e autorizzazioni
Suggeriamo 3 tipologie di utenti che avranno CLASSE

- _2_*USR, Utenti finali del sistema informativo
- _2_*PGMR, Manutentori del sistema informativo
- _2_*SECOFR, Responsabile del sistema informativo


## Profili di sistema
Le impostazioni dei profili di sistema determinano le autorizzazioni di tutti gli utenti, rappresentando i profili di gruppo.
 » Verifica impostazioni profilo di gruppo UTENTI FINALI (QUSER)
 :  : INI > eseguo >>
 :  : CMM ?CHGUSRPRF USRPRF(QUSER) USRCLS(*USER) LMTCPB(*YES) SPCAUT(*USRCLS)
 :  : FIN
 » Verifica impostazioni profilo di gruppo SISTEMISTA APPLICATIVO (QPGMR)
 :  : INI > eseguo >>
 :  : CMM ?CHGUSRPRF USRPRF(QPGMR) USRCLS(*PGMR) LMTCPB(*NO) SPCAUT(*JOBCTL *SAVSYS *SPLCTL)
 :  : FIN

## Profili personali
 » Creazione profilo UTENTE FINALE (*USER/QUSER)
 :  : INI > eseguo >>
 :  : CMM ?CRTUSRPRF USRPRF(*N) USRCLS(*USER) SPCAUT(*USRCLS) JOBD(SMEJOBD) GRPPRF(QUSER) OWNER(*GRPPRF) AUT(*USE) INLPGM(*LIBL/B£QQ50) LMTCPB(*YES)
 :  : FIN
 » Creazione profilo UTENTE SISTEMISTA APPLICATVO (*PGMR/QPGMR)
 :  : INI > eseguo >>
 :  : CMM ?CRTUSRPRF USRPRF(*N) USRCLS(*PGMR) SPCAUT(*USRCLS) JOBD(SMEJOBD) GRPPRF(QPGMR) OWNER(*GRPPRF) AUT(*USE) INLPGM(*LIBL/B£QQ50)
 :  : FIN
 » Creazione profilo UTENTE RESPONSABILE RISERVATEZZA / SISTEMISTA (*SECOFR/QPGMR)
 :  : INI > eseguo >>
 :  : CMM ?CRTUSRPRF USRPRF(*N) USRCLS(*SECOFR) SPCAUT(*USRCLS) JOBD(SMEJOBD) GRPPRF(QPGMR) OWNER(*GRPPRF) AUT(*EXCLUDE) INLPGM(*LIBL/B£QQ50)
 :  : FIN

_B_Comandi correlati
 :  : INI Gestione profili
 :  : CMD WRKUSRPRF USRPRF(*ALL)
 :  : FIN
 :  : INI Stampa profili
 :  : CMD PRTUSRPRF SELECT(*USRCLS)
 :  : FIN

## Criteri di codifica del Profilo
Salvo esigenze specifiche o esistenza di norme interne all'azienda, un criterio per assegnare profili che diminuisca l'ambiguità, potrebbe essere CCCNNN, dove : 
 * CCC >> prime 3 lettere del cognome
 * NNN >> prime 3 lettere del nome

### Profilo *SECOFR
* Sarebbe opportuno avere un profilo di classe *SECOFR (oltre a QSECOFR). Questo perchè, se dimentichiamo la pwd di QSECOFR, è possibile reimpostarla con l'altro (sempre che si ricordi la pwd di quest'ultimo!!)
* Se non si ricorda e/o non è possibile ripristinare la pwd di QSECOFR è necessario ricorrere da un IPL manuale con l'opzione M del display oppure impostando il valore di sistema QIPLTYPE a 1, entrare nell'SST con utente QSECOFR e password QSECOFR (se non hai cambiato anche quella) e reimpostare la password di QSECOFR al suo default (QSECOFR).
* Non dimenticare di impostare l'autorizzaione sull'oggetto QSECOFR
*** e sopratutto l'eventuale utente creato per Backup
 :  : INI Assegna autorizazzione
 :  : CMD GRTOBJAUT OBJ(QSECOFR) OBJTYPE(*USRPRF) USER(*PUBLIC) AUT(*EXCLUDE)
 :  : FIN
 :  : INI Assegna autorizazzione utente di backup
 :  : CMD ?GRTOBJAUT OBJ(UTENTE) OBJTYPE(*USRPRF) USER(*PUBLIC) AUT(*EXCLUDE)
 :  : FIN

### Profilo QPGMR
* Non dimenticare di impostare l'autorizzazione sui seguenti oggetti : 
 :  : INI RSTOBJ
 :  : CMD GRTOBJAUT OBJ(RSTOBJ) OBJTYPE(*CMD) USER(QPGMR) AUT(*USE)
 :  : FIN
 :  : INI RSTLIB
 :  : CMD GRTOBJAUT OBJ(RSTLIB) OBJTYPE(*CMD) USER(QPGMR) AUT(*USE)
 :  : FIN
 :  : INI RST
 :  : CMD GRTOBJAUT OBJ(RST) OBJTYPE(*CMD) USER(QPGMR) AUT(*USE)
 :  : FIN

### Altre
* Disabilitare (tranne QSECOFR) tutti i profili Q*
* Tutti gli oggetti dovrebbero essere di proprietà QPGMR

# Device
## Utilità
### WRKJOB in alternativa al DSPJOB
 * Attivazione del WRKJOB in alternativa al DSPJOB per la _7_richiesta sistema(in gergo la sequenza di tasti shift+Attn o shift+Esc con la linea comandi completa), modificare il testo del messaggio CPX2313 sostituendo DSPJOB con WRKJOB

 :  : INI > eseguo >>
 :  : CMD WRKMSGD MSGID(CPX2313) MSGF(QCPFMSG)
 :  : FIN

### Query/400 con , e . invertiti
 * Inversione notazione internazionale per esecuzione Query/400 :  modificare il testo del messaggio_7_CPX2D06in modo da ottenere un testo di messaggio come quello indicato nella sottoindicata riga : 
  _2_42$11      -     2$           1112
 * se il separatore migliaia visualizzato è**,**anziché**.**, e, il separatore decimale visualizzato è**.**anziché**,**, quindi si è in una situazione di inversione dei segni separatori migliaia/decimale, si può procedere modificando la stringa iniziale del messaggio : 
     in_7_42$11
 ** la cifra a sinistra del $ governa il separatore decimale (2=, 1=.)
 ** la cifra a destra del $ governa il separatore migliaia (2=, 1=.)

 :  : INI > eseguo >>
 :  : CMD WRKMSGD MSGID(CPX2D06) MSGF(QCPFMSG)
 :  : FIN

## Debug in schermo esteso
 * Impostazione DEBUG origine ILE con schermo esteso (Widescreen), mediante l'impostazione di una variabile di ambiente a livello di sistema.

 :  : INI > eseguo >>
 :  : CMD ADDENVVAR ENVVAR(ILE_DEBUGGER_1) VALUE(ALLOW_WIDE_SCREEN) LEVEL(*SYS) REPLACE(*YES)
 :  : FIN

## Trasferimento spool tra AS400
 * Trasferimento dei file di SPOOL tra due AS400, è possibile utilizzare il comando SNDTCPSPLF per copiare dallo spool di un AS400_O in una coda di stampa di un altro AS400_D. Il comando vuole come prerequisiti il protocollo TCP attivato, una coda di stampa sull'AS400 di destinazione.

 :  : INI > eseguo >>
 :  : CMD ? SNDTCPSPLF  RMTSYS(nome) PRTQ(coda) FILE(file) JOB(job)                   DESTTYP(*AS400)  TRANSFORM(*NO)
 :  : FIN
>   SNDTCPSPLF RMTSYS(<nome>) PRTQ(<coda>) FILE(<file>) JOB(<job>)
              DESTTYP(*AS400) TRANSFORM(*NO)
   nome :  indirizzo IP o nome host AS400 (dipende da impostazione risuluzione host)
   coda :  nome della coda di stampa destnazione
   file :  nome del file da trasferire
   job  :  nome del job da trasferire


## Caratteri non stampabili
 * In casistiche in cui il programma di scrittura segnala di non essere in grado di riprodurre "caratteri non stampabili", si può ovviare modificando il printer file in modo da indurre che i caratteri non stampabili vengano sostituiti da " " (blank). I printer files di Smeup sono già impostati con tale opzione, ma qualora si necessitasse la modifica di un printer file che presenta tale problema, procedere con il seguente comando : 

 :  : INI > eseguo >>
 :  : CMD ? CHGPRTF FILE(PRT198) RPLUNPRT(*YES ' ')
 :  : FIN

# Appunti
* Disabilitare tutti i profili Q* (tranne QSECOFR)
* Creazione ambiente di test (RSTLIB post salvataggi)
* Salvataggi con *UNLOAD
