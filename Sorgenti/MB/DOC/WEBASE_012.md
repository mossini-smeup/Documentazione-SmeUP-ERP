## Installazione jvm standalone

Qualora fosse necessario utilizzare una jvm diversa da quella installata nel sistema, per una questione di release o semplicemente
per una gestione separata dell'installazione, è possibile creare una directory in cui posizionare la jvm evitando quindi una
vera e propria installazione. Ovviamente occorre poi configurare opportunamente l'applicazione che usa la jvm per far si
che punti alla jvm desiderata.

La documentazione corrente è stata testata su sistema operativo Windows ma, salvo alcune piccole differenze (estensioni di files, utilities, nomenclature, separatori etc...), è valida
anche per sistemi linux (che in generale sono da preferire).

Per prima cosa occorre scaricare la versione di java relativa all'architettura interessata (per linux solitamente archivi tar.gz) : 
![WEBASE_043](http://localhost:3000/immagini/WEBASE_012/WEBASE_043.png)
Installare un software per decomprimere l'archivio exe, utilizzare ad esempio 7-Zip (nel caso di archivi tar.gz è sufficiente unzip) : 
![WEBASE_044](http://localhost:3000/immagini/WEBASE_012/WEBASE_044.png)
Si genererà un file tools, da decomprimere anch'esso, impostando il nome della directory di destinazione, nel notro caso ad esempio :  jdk8u91 : 
![WEBASE_045](http://localhost:3000/immagini/WEBASE_012/WEBASE_045.png)
Posizionare la directory appena generata e contenente il jdk in un punto a piacere (per comodità allo stesso livello della directory di Payara)
![WEBASE_046](http://localhost:3000/immagini/WEBASE_012/WEBASE_046.png)
Aprire un terminale MS-DOS (o linux), posizionarsi nella directory del jdk e terminare le operazioni di decompressione : 
![WEBASE_047](http://localhost:3000/immagini/WEBASE_012/WEBASE_047.png)
Completati con esito positivo i precedenti step, si sarà ottenuta una directory contenente un jdk standalone portabile.
Occorre quindi configurare payara perchè utilizzi tale jdk al posto di quello di sistema.

Assicurarsi che l'application server Payara non sia attivo (fermare il servizio)
Modificare con un editor di testo il file asenv.bat (nel caso di linux va modificato invece asenv.conf ) nella directory ../config di Payara aggiungendo la variabile AS_JAVA=<path_del_jdk> come in figura : 
![WEBASE_048](http://localhost:3000/immagini/WEBASE_012/WEBASE_048.png)
Avviare payara da riga comandi con il comando asadmin start-domain come in figura...
![WEBASE_049](http://localhost:3000/immagini/WEBASE_012/WEBASE_049.png)
...attendere il messaggio di avvio effettuato.
![WEBASE_050](http://localhost:3000/immagini/WEBASE_012/WEBASE_050.png)
una volta avviato l'application sever, verificare che utilizzi effettivamente il jdk installato interrogando il relativo file di log (server.log)
![WEBASE_051](http://localhost:3000/immagini/WEBASE_012/WEBASE_051.png)
terminare quindi l'istanza appena avviata di Payara in modo da non creare conflitti con quella che dev'essere avviata mediante servizio di sistema.
