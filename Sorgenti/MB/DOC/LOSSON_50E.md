 :  : HEA PRIV(001)

## PREMESSA
Nella release V3R1 di Loocup è presente la possibilità di eseguire l'accesso a SmeUp in SSO. Questa funzionalità non è presente in release precedenti.


## PREREQUISITI LOOCUP

Aver installato una versione V3R1 o successiva.


## PREREQUISITI PC

 * Il PC deve essere in dominio Active Directory 2003 o successivo, e deve essere raggiungibile il Domain Controller.
 * Deve utilizzare un S.O. Windows XP SP2 o SP3, oppure Windows 7. Non sono stati compiuti test con Windows Vista.
Nessuna versione Home ha il supporto per Kerberos (non sono associabili a un dominio AD).
 * Deve essere installata una JVM 6.0 (1.6.0) a 32 bit.
 * L'autenticazione Kerberos deve essere abilitata apportando una modifica al registro di Windows. L'installazione standard di Windows disabilita questa funzionalità.
Per l'attivazione sono stati predisposti due file .reg per automatizzare la modifica al registro.
Si trovano nel tool SSO_krb, scaricabile da : 
[http://erp.smeup.com/loocup_downloads/tools/krbtool.zip](http://erp.smeup.com/loocup_downloads/tools/krbtool.zip)

oppure all'interno del DVD della DEV.
Sono specifici per versione del sistema operativo : 
 ** per Windows 7 utilizzare il file :  attiva SSO kerberos Win-7.reg
 ** per Windows XP SP2 o SP3 utilizzare il file :  attiva SSO kerberos Win-XP.reg.
Per impostare la chiave è sufficiente fare doppio click sul file.


Di seguito riportiamo le modifiche da apportare al registro : 

Windows 7 : 

HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\Lsa\Kerberos\Parameters
Value Name :  allowtgtsessionkey
Value Type :  REG_DWORD
Value :  0x01  ( default is 0 )

Windows XP SP2 o SP3 : 

HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\Lsa\Kerberos\
Value Name :  allowtgtsessionkey
Value Type :  REG_DWORD
Value :  0x01


La caratteristica 32 o 64 bit non influenza l'accesso tramite Kerberos.
Nel caso di sistema operativo a 64 bit è necessario installare una JVM a 32 bit in quanto Loocup non funziona su JVM a 64 bit.
La JVM da utilizzare è la 1.6.0_xx o successiva.


## PREREQUISITI AD e I SERIES

Fare riferimento ai documenti relativi.


## COME ABILITARE UN UTENTE AD UTILIZZARE L'ACCESSO TRAMITE SSO

Fare riferimento al manuale utente.


## CONFIGURAZIONE DI LOOCUP

La configurazione di Loocup è composta da due fasi :  nella prima vanno definiti i parametri utilizzati dalle api GSS, nella seconda va abilitato l'accesso in SSO.

Definizione parametri api GSS

Una volta installata una versione di Loocup che supporti l'SSO tramite Kerberos, è necessario modificare il file krb5.conf che si trova nella cartella LOOCUP_SET\SSO\KERBEROS, all'interno della cartella di installazione di Loocup.

La modifica di questo file si compie tramite un editor di testo.

E' necessario specificare il dominio aziendale, il KDC (in un AD è il  Domain Controller) e il mappare il realm con il dominio.
Le parti da modificare sono evidenziate in verde o giallo.

Quelle in evidenziate in giallo sono case-sensitive e vanno scritte in maiuscolo : 

In questa parte sono definiti i default. Va indicato il realm di default.
 :  : PAR F(03)
[libdefaults]
        default_realm = REALM.XX
        clockskew = 300
        v4_instance_resolve = false
        v4_name_convert = {
                host = {
                        rcmd = host
                        ftp = ftp
                }
                plain = {
                        something = something-else
                }
        }
        - Set this to false to disable MIT krb5 compatibility
        - in GSSAPI get_mic/verify_mic, and become compatible
        - with older Heimdal releases instead.
        gss_mit_compat = true
   -default_etypes = des-cbc-crc
        -default_etypes_des = des-cbc-crc


In questa parte va definito il realm :  indica la macchina che distribuisce le chiavi

[realms]
    REALM.XX = {
                kdc = key_distribution_center.domain.xx
        }

In questa parte viene effettuato il mapping tra realm e KDC

[domain_realm]
        .domain.xx = REALM.XX



E' stato predisposto un programma di test scaricabile da
[http://erp.smeup.com/loocup_downloads/tools/krbtool.zip](http://erp.smeup.com/loocup_downloads/tools/krbtool.zip)

Per i dettagli fare riferimento al capitolo :  COME VERIFICARE LA CONNESSIONE SENZA INSTALLARE LOOCUP.


## Abilitazione dell'accesso in SSO

Per abilitare l'accesso in SSO a Loocup fare riferimento al manuale utente.


## COME VERIFICARE LA CONNESSIONE SENZA INSTALLARE LOOCUP

Per verificare che il file krb5.conf sia configurato correttamente si può utilizzare il programma di test descritto sopra e reperibile anche all'interno del DVD della DEV.

Va scompattato l'archivio.

Nella cartella krb sono presenti i seguenti file : 
 * Jaas.conf :  file utilizzato dalle api GSS. NON MODIFICARE
 * Jaasazn.policy :  file utilizzato dalle api GSS. NON MODIFICARE
 * Krb5.conf :  il file che configura la connessione Kerberos
 * Krb.jar :  il programma che esegue la connessione (necessita della JVM 1.6.0_xx)
 * Krb.properties :  il file che indica l'ISERIES a cui accedere e attiva la modalità di debug.
 * Leggimi.txt :  contiene informazioni su come eseguire i test

Come per Loocup, è necessario configurare il file krb5.conf, indicando il dominio e il CD.
A differenza di Loocup, per indicare l'ISERIES a cui connettersi bisogna utilizzare krb.properties. La proprietà debug=true abilita un output molto dettagliato sulla connessione.

Dopo aver configurato krb5.conf e krb.properties, lanciare krb.jar da una cartella locale o tramite un disco di rete. Kerberos non supporta l'accesso tramite UNC (\\macchina\cartella\...\krb).

Verrà generato il file di log  SSOKerberos.log contenente l'esito della connessione.
Questo riporta anche alcune informazioni del PC su cui è stato effettuato il test.

Vengono effettuati due test :  uno di connessione all'ISERIES e, se questo ha esito positivo, viene effettuato un secondo test di connessione al servizio JDBC.

Nel file di log, in modalità di debug troveremo infatti 3 tiket :  il TGT rilasciato dal server di dominio e poi altri due, uno per l'accesso all'ISERIES e uno per l'accesso al servizio JDBC.

In fondo al file di log è molto probabile che vi sia indicata un'eccezione :  viene effettuata una query al file VERAPG0F della libreria XGES_DAT.
L'eccezione non pregiudica la connessione SSO. E' dovuta alla mancanza del file/libreria.


## TROUBLESHOOTING

Se la connessione non ha successo si consiglia di utilizzare il programma di controllo.
La risposta è depositata nel file di log.

Al link seguente è disponibile una guida per identificare i codici di errore di kerberos : 
 :  : DEC T(J1) P(PATHFILE) [http://www.monitorware.com/common/en/securityreference/kerberos-failures.php](http://www.monitorware.com/common/en/securityreference/kerberos-failures.php)
Kerberos)

Al seguente invece una spiegazione delle eccezioni delle api JGSS : 
 :  : DEC T(J1) P(PATHFILE) [http://download.oracle.com/javase/1.5.0/docs/guide/security/jgss/tutorials/Troubleshooting.html+
](http://download.oracle.com/javase/1.5.0/docs/guide/security/jgss/tutorials/Troubleshooting.html+
)
) D(Troubleshooting)



## COSA E' STATO IMPLEMENTATO IN LOOCUP

In loocup è stato esteso il modulo che esegue la connessione all'ISERIES aggiungendo il supporto alla connessione SSO.
Quando è abilitato l'accesso in SSO, viene delegata una classe che per prima cosa verifica il path da cui è stato avviato Loocup.
Nel caso in cui Loocup sia avviato da una cartella indicata mediante un path UNC, ad esempio \\smea.it\aaa\bbb..., i file di configurazione vengono copiati in locale, nella cartella delle applicazioni  (%appdata%) sottocartella \Loocup\CONF\SSO\KERBEROS.
E' necessario copiare in file di configurazione in locale perché l'autenticazione Kerberos non supporta i path UNC.


## NOTE

L'accesso all'ISERIES tramite SSO avviene con l'utente ISERIES associato al profilo di Windows.
Se l'accesso all'ISERIES deve avvenire con utenti differenti bisogna predisporre almeno un altro link a Loocup nel quale si specifica l'utente con cui si vuole accedere.


L'accesso in SSO al' iSeries tramite le api JT400 richiede una versione che implementi le api GSS.
Si consiglia di utilizzare la versione 7.1 o successiva.
Per il download : 
[http://jt400.sourceforge.net/](http://jt400.sourceforge.net/)

La 5.2.0, distribuita con la versione di Loocup V2R3M091109 upgrade del 3/10/2010 NON supporta le GSS API.



