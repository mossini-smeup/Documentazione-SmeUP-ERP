 :  : HEA RESP(MAEOLI) STAT(10) USAG(FORFED) DTAG(20180919) ORAG(171500) AMBT(TE)

# Sme.UP Provider Web Application
Partendo dalla release di Sme.UP Provider Roma Rev 2, è stata sviluppata una versione che può funzionare anche all'interno di un application server (tipicamente Payara), e quindi è indipendente dal sistema operativo.

## Le versioni di Sme.UP Provider
Le versioni di Sme.UP Provider sono 3 : 
 * Sme.UP Provider Stand Alone o Provider SA :  si tratta della versione "storica", quella che funziona solo in ambiente Windows
 * Sme.UP Provider Web Application o Provider WA :   è la versione funzionante all'interno di un application server, quindi indipendente dal sistema operativo
 * Smartkit :  è la versione Provider WA distribuita in un container docker o in una macchina virtuale.


## Differenze tra Provider WA e SA
La versioni Smartkit e la WA sono le stesse, è differente il metodo di distribuzione :  la prima è "pronta all'uso", la seconda ha bisogno di un'application server.

Confronteremo pertanto la versione WA e quella SA.

### Limitazioni versione WA
Funzionando all'interno di un'application server, non è possibile eseguire i programmi SmeTray (Scheda) e SmeUIClt (Emulatore).
Questo implica, ad esempio che non è possibile far eseguire funzioni di generazione di file excel ( F(EXC,...).
Non è poossible neppure l'esecuzioni di funzioni che richiedano il richiamo di emulazioni che hanno un video.
Non si possono eseguire i flussi batch.
Non è possibile utilizzare plugin che si mettano in ascolto su una porta specifica.
Non è possibile neppure utilizzare le funzionalità relative al dialogo con i LoocUp client.

### Vantaggi versione WA
 * L'applicazione funziona a 64 bit, viene quindi superato il limite di 1024Kb(*), quindi si ha un incremento della robustezza, potendo elaborare XML molto più grossi senza problemi di esaurire la memoria.
 * Avvi e spegnimenti sono gestiti dall'application server
 * Il provider si deve preoccupare solamente della gestione delle connessioni/disconnesioni verso l'AS400
 * Può funzionare sia su Window che su Linux che su AS400

NOTA (*) In teoria sono 2048 ma a causa di limiti nella gestione della memoria sulle macchine Windows, si riesce ad arrivare al massimo a 1024Kb.

## Prerequisiti
Un application server, consigliato Payara 5 64 bit, Java 8 64 bit, una macchina con sistema operativo di tipo server con 8GB di ram minimo, consigliati 16.
Payara va configurato per essere un'applicazione server con almeno 2GB di ram (consigliati 4GB).

## L'installazione
L'installazione si compie in 3 passi.
Nel primo passo, il deploy, il provider crea i file necessari alla configurazione e al funzionamento nella home dell'utente cartella etc/provider/<contesto_del_provider>.
dopo questa operazione si potrà già interrogare il provider all'indirizzo http://localhost:8080/<contesto_del_provider>/debug, ma, non avendo ancora configurato a quale AS400 vada connessio, nella pagina di debug saranno indicati i parametri mancanti.
Il provider però non è ancora connesso all'AS400, e in questo momento non è in grado di assolvere a nessuna altra funzione.
Con il primo delpoy, vengono create nella home dell'utente le cartelle etc/provider/<nome contesto>/
qui verà posizionato il file configuration.poperties e la cartella providerfiles.

Il file configuration.poperties consente di definire un sottoinsieme delle caratteristiche configurabili tramite il file wrapper.conf.
Per prima cosa sarà necessario modificare questo file impostando le solite credenziali di autenticazione (AS400/utente/password/ambiente) e il nome del provider.

Sarà anche possibile fa funzionare il provider in un ambiente in cui su AS400 non è installato SmeUp.
In questo caso andrà lasciato l'ambiente vuoto e decommentato il parametro XMLINI=DEFAULT

Queste due impostazioni diranno al provider che l'XML iniziale dovrà essere letto dal file di default.

Se invece l'ambiente non sarà blank, allora il provider leggerà l'xml iniziale dall'ambiente SmeUp.

NOTA :  l'XML iniziale contiene la configurazione del provider.

## Accesso ai file
In un ambiente in cui il provider deve accedere a file posti su server Windows o sull'IFS sarà necessario montare delle condivisioni e informare il provider su come reperire i file.
Sarà necessario definire una mappa in cui si fà l'associazione tra percorso Windows e percorso Linux.
Poniamo ad esempio che le fatture siano posizionate sul server \\server01.dominio.com\fatture e che siano state montate in /mnt/payara/server01-fatture.
il legame tra percorso Windows e percorso linux lo posso fare agendo sul file configuration.properties.
In questo file sono state predisposte 9 MAPPING_PATH_XX=WIN() LIN()
Se ne possono usare quante ne occorrono :  il provider utilizzerà tutti i mapping path definiti.
Devono avere la forma WIN(percorso windows) LIN(percorso linux), ad esempio : 
MAPPING_PATH_01=WIN(\\server01.dominio.com\fatture) LIN( /mnt/payara/server01-fatture)

Se il provider dovrà accedere all'IFS, sarà necessario montare e mappare l'IFS.
Ad esempio se abbiamo \\AS400.dominio.com\Smedoc, montato in /mnt/payara/as400-smedoc aggiungeremo
MAPPING_PATH_02=WIN(\\AS400.dominio.com\Smedoc) LIN(/mnt/payara/as400-smedoc)

Se i percorsi che vengono passati dal provider non hanno il dominio, oppure vengono usati sia con che senza domio, esempio \\AS400\smedoc\fatture, sarà necessario inserire anche il percorso senza dominio, ad esempio : 
MAPPING_PATH_03=WIN(\\AS400\Smedoc) LIN(/mnt/payara/as400-smedoc)

Se un server espone più cartelle, esempio : 
\\server01\azienda01\cartella_clienti
\\server01\azienda01\cartella_fornitori
\\server01\azienda01\cartella_banche
posso evitare di montare tutte e tre le cartelle, e poi dover fare tre associazioni, montando direttamente la radice, in questo caso \\server01\azienda01 verrà montata in /mnt/payara/server01-azienda01

## configurazione mappa alternativa
Tutti i mapping path si possono definire in alternativa anche nell'SCP_CLO del provider, tramite la variabile PROVIDER_MAPPING, che ha come valori un insieme di coppie WIN() LIN() separate da "|",  poste all'interno dei MAP(), esempio : 
.  :  : C.VAR Cod="PROVIDER_MAPPING" TVal="J5" PVal="TPRV/A;P" Value="MAP(WIN(\\AS400.dominio.com\cartella1) LIN(/mnt/payara/cartella1)|WIN(\\AS400.dominio.com\cartella2) LIN(/mnt/payara/cartella2)|...|WIN(/mnt/payara/cartellann) LIN(/mnt/payara/cartellann))"

NOTA :  prima e dopo il "|" non ci devono essere spazi.
In caso si definiscano i mapping sia nel SCP_CLO che nel file di configurazione dello Smart Kit, vincono quelli presenti nel file di configurazione (non vengono fusi).

## Automatizzare il mount
Per semplificare il mount delle cartelle sul server Linux, si consiglia di utilizzare autofs.
Questa si occupa di montare i file sistem solamente all'occorrenza.
E' inoltre in grado di gestire situazioni in cui il server remoto vada offline, cosa che il mount non è in grado di fare.
Qui di seguito le istruzioni di base : 
sudo apt-get install autofs
in /etc si trova il auto.master.

commentare tutto quanto ed aggiungere
/mnt/payara/ /etc/auto.mnt

che significa :  in /mnt/payara monta tutto quanto specificato in auto.mnt

NOTA :  si suppone che l'utente che utilizza payara sia payara

in auto.mnt andranno specificati i mount da compiere ad esempio : 
server01-fatture -fstype=cifs,file_mode=0777,dir_mode=0777,username=utente_windows,password=password_utente_windows,domain=dominio.com,nocase  : server01.dominio.com\fatture
as400-smedoc -fstype=cifs,file_mode=0777,dir_mode=0777,username=utente_AS400,password=password_utente_AS400,domain=dominio.com,nocase  : //as400.dominio.com/smedoc

Una volta compleatato il file **auto.mnt**, o dopo ogni modifica, è necessario avviare / riavviare autofs : 
**sudo service autofs restar**t

Qui si trova la documentazione completa
[https://help.ubuntu.com/community/Autofs](https://help.ubuntu.com/community/Autofs)

## Test
Per verificare che il provider acceda ai percorsi specificati, si può utilizzare la pagina di debug.
Affinchè il provider acquisisca le modifiche apportate al file configuration.properties è necessario riavviare payara o rideployarlo.
Per far prendere le modifiche fatte negli script SCP_CLO è sufficiente invece un riavvio da pagina di debug.

Nella pagina di debug c'è il pulsante "Test PROVIDER_PATHS". con questo pulsante si possono testare tutti i mapping definiti.






