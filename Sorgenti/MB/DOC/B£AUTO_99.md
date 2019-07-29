 :  : HEA PRIV(001)

# SSO

Il Single sign-on (SSO, traducibile come autenticazione unica o identificazione unica) è un sistema specializzato che permette ad un utente di autenticarsi una sola volta e di accedere a tutte le risorse informatiche alle quali è abilitato.

Una buona analogia è uno ski pass per il weekend valido per diversi impianti.
Si mostra lo ski pass a uno qualsiasi degli impianti (fino alla scadenza)e si riceve un biglietto di risalita per quell'impianto. Con il biglietto, si può sciare su qualsiasi pista di quell'impianto. Se il giorno successivo si va in un altro impianto, ancora una volta si mostra lo ski pass e si ottiene un altro biglietto.
La differenza è che con Kerberos sarà il sistema ad accorgersi automaticamente che si è in possesso di uno ski pass. In questo modo il sistema è possibile avviare automaticamente, in modo trasparente all'utente, il processo di richiesta e consegna del ticket per il servizio.

In SmeUp l'SSO è realizzato con Kerberos.
Questo protocollo è compatibile con i più diffusi sistemi operativi.
Ecco uno schema del suo funzionamento : 

![B£AUTO05](http://localhost:3000/immagini/B£AUTO_99/BXAUTO05.png)
Segue un dettaglio relativo alle diverse fasi di autenticazione (completamente trasparenti all'utente).


- Un programma client richiede al KDC per conto dell'utente un TGT, cioè una certificazione temporanea dell'identità dell'utente.
- Se le credenziali fornite dall'utente sono corrette il programma ottiene il TGT e lo conserva per accedere ai servizi previsti.
- Il programma client presentando il TGT richiede al KDC un TGS, cioè un permesso temporaneo di accesso a un particolare servizio.
- Il server KDC fornisce il TGS.
- Il programma client si presenta al servizio con il proprio TGS.
- Il servizio verifica l'identità del client e fornisce una prova della propria identità.


Una volta completata la verifica delle credenziali il client può usufruire del servizio (ad esempio un servizio di posta, un database ecc.).

# MANUALE UTENTE

## PREMESSA
Il 28/09/2010 è stata rilasciata la versione di test di Loocup nella quale è stato implementato il Single Sign On (SSO).

## COSA SIGNIFICA SSO
Single Sign On è una tecnologia che permette ad un utente di autenticarsi una sola volta (in dominio) e di accedere alle risorse informatiche alle quali è abilitato (es. 5250, Looc.Up, Web.Up).

## PREREQUISITI
I prerequisiti sono i seguenti : 

- PC in Dominio e collegato alla Lan aziendale;
- Server di autenticazione raggiungibile nella lan;
- Sistema Operativo  Windows XP SP2/SP3, oppure Windows 7.


Le versioni Home non supportano l'SSO con Kerberos.

NB :  L'SSO non può funzionare se il collegamento all'as400 viene effettuato via IP pubblico (es. se mi collego da casa), ma bisogna collegarsi prima attraverso il client VPN SSL, che permette una volta effettuato l'accesso di entrare a tutti gli effetti nella lan aziendale e usufruire quindi delle policy di dominio.

Abilitare l'autenticazione con Kerberos.
Per Windows 7 utilizzare il file :  attiva SSO kerberos Win-7.reg
Per Windows XP SP2 o SP3 utilizzare il file :  attiva SSO kerberos Win-XP.reg.
I due file .reg posizionati nella cartella : 
 \\smea.it\dfs_root\aziende\Divisione Sico\Progetti\SSO\Documentazione\Dominio Windows.

Per abilitare l'autenticazione e' sufficiente fare doppio click sul file corretto (necessari privilegi di amministratore).

## COME ABILITARE L'ACCESSO TRAMITE SSO

Esistono due modalità per attivare l'accesso in SSO : 

- SSO da collegamento (link) a Loocup.exe;
- SSO da finestra login Looc.Up;


### SSO da Collegamento
Creare o modificare un link verso Loocup.exe indicando soltanto  i parametri "IP iSeries" e "*SSO".  (vedi figura)
Non va indicato il parametro "utente".
Esempio :   "\percorsoServer\Loocup.exe 172.16.2.11 *SSO".

![B£AUTO06](http://localhost:3000/immagini/B£AUTO_99/BXAUTO06.png)
Con queste impostazioni, a seguito del lancio di Loocup.exe, tramite doppio click sull'icona di collegamento, l'accesso a Looc.Up sarà diretto.

N.B.
Nel caso venga indicato il parametro "utente", verrà presentata la maschera di Login di Looc.Up.

### SSO da finestra Login
Attivare il SSO dalla finestra di login di Looc.Up è sufficiente indicare l'iSeries e spuntare il checkbox  SSO.
N.B. Questa impostazione è valida a partire dalla richiesta di collegamento successiva.

![B£AUTO07](http://localhost:3000/immagini/B£AUTO_99/BXAUTO07.png)
Come noto, i parametri presentati nella finestra di Login sono determinati dai parametri presenti nel link di collegamento e passati a  Loocup.exe.

La valorizzazione di tali parametri a livello di link comporta quanto segue : 
* nel caso l'unica variabile valorizzata sia l l'iSeries, il successivo collegamento avverrà  semplicemente facendo doppio click sul collegamento.
* nel caso siano valorizzati iSeries e Utente non risulterà possibile l'accesso tramite *SSO e verrà valorizzato un messaggio di errore.

## COME DISABILITARE L'ACCESSO TRAMITE SSO

- SSO da collegamento (link) a Loocup.exe;
Modificare un link verso Loocup.exe togliendo il parametro "*SSO"
- SSO da finestra login Looc.Up;
Aprire la finestra di "About" e togliere il flag di spunta relativo al checkbox "Attiva SSO" : 


![B£AUTO08](http://localhost:3000/immagini/B£AUTO_99/BXAUTO08.png)
### NOTE

L'accesso all'ISERIES tramite SSO avviene con l'utente ISERIES associato al profilo di Windows (utente di dominio).
Per accedere con utenti differenti dal proprio va creato un altro link a Loocup nel quale si specifica come parametro l'utente con il quale si vuole accedere.

Per maggiori dettagli consultare la documentazione del modulo LOSSON

# Kerberos Iseries 5250

## PREMESSA
Il 28/09/2010 è stata rilasciata la versione di test di Loocup nella quale è stato implementato il Single Sign On (SSO).

## COSA SIGNIFICA SSO
Single Sign On è una tecnologia che permette ad un utente di autenticarsi una sola volta (in dominio) e di accedere alle risorse informatiche alle quali è abilitato (es. 5250, Looc.Up, Web.Up).

## PREREQUISITI
I prerequisiti sono i seguenti : 
* PC in Dominio e collegato alla Lan aziendale;
* Server di autenticazione raggiungibile nella lan;
* Sistema Operativo  Windows XP SP2/SP3, oppure Windows 7.
Le versioni Home non supportano l'SSO con Kerberos.

NB :  L'SSO non può funzionare se il collegamento all'as400 viene effettuato via IP pubblico (es. se mi collego da casa), ma bisogna collegarsi prima attraverso il client VPN SSL, che permette una volta effettuato l'accesso di entrare a tutti gli effetti nella lan aziendale e usufruire quindi delle policy di dominio.

## PREREQUISITI

Affinché si possa accedere ad un iseries con un client 5250 è necessario aver installato il CA versione 5.2 o successiva, che sia configurato correttamente e che il iSeries soddisfi i requisiti.


## COME ABILITARE L'ACCESSO TRAMITE KERBEROS DEL CLIENT ACCESS

Per abilitare l'accesso tramite KERBEROS, configurare una nuova sessione : 

![B£AUTO09](http://localhost:3000/immagini/B£AUTO_99/BXAUTO09.png)
oppure aprirne una esistente e selezionare la voce Comunicazioni, comparirà la finestrella mostrata di seguito : 

![B£AUTO10](http://localhost:3000/immagini/B£AUTO_99/BXAUTO10.png)
Cliccare sul pulsante Proprietà, e comparirà il popup seguente : 

![B£AUTO11](http://localhost:3000/immagini/B£AUTO_99/BXAUTO11.png)
Selezionare la voce "Utilizza nome principal kerberos, senza richiesta", confermare con il pulsante OK e poi ancora OK.

Se i prerequisiti sono soddisfatti, comparirà la videata con la scelta degli ambienti (se multipli), oppure si accederà al menù applicativo.




