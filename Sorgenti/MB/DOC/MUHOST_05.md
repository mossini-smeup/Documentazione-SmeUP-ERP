# Descrizione

Al fine di ridurre i tempi di installazione di componenti As.UP ed avere un ambiente certo di runtime (sia esso server o client)
si rende necessario un ambiente per la gestione delle macchine virtuali.
Obiettivo e' ottenere in modo semplice le immagini in formato standard (compatibile windows / linux) per una macchina virtuale
che verra' definita in funzione delle esigenze di progetto.

## Proposta di ambiente modulare virtualizzato

Nella seguente figura viene mostrata una delle possibili architetture costruite all'interno del sistema virtuale. In
particolare, questa è l'architettura consigliata nel caso si voglia costruire un sistema che consenta la scalabilità
prestazionale.

![MUHOST_05A](http://localhost:3000/immagini/MUHOST_05/MUHOST_05A.png)
Legenda macchine : 


- **DB01**  :  database primario. E' la macchina che accoglie il DB primario del sistema.
- **DB02**  :  database secondario.
- **AS01**  :  application server As.UP (istanza 1)
- **AS02**  :  application server As.UP (istanza 2). Sono possibili più istanze di As.UP attive,
- **DK01**  :  server di sviluppo. Macchina (opzionale) utilizzata per operazioni di conversione/compilazione.
- **FS01**  :  file system condiviso e storage Flux
- **IBMi** :  sistema iSeries di origine (opzionale)
- **CO01**  :  server per connessioni connettori di comunicazione AS.UP, Looc.up Provider e server Flux. La macchina CO01 è in DMZ (vero o falso?)


Alcune note di architettura : 
- La macchina **CO01** deve essere accessibile da web su indirizzo pubblico. Solitamente è in DMZ visto che è l'unica macchina visibile
direttamente da rete pubblica.
Le porte socket da aprire su accesso pubblico sono : 

- 80
- 3000 :  Flux server
- 8023 :  shell As.UP
- 8024 :  shell As.UP in Looc.UP
- 8282 :  WebService As.UP
- 8470-8476 :  servizi AS400
- 9090 :  WebService Looc.Up Provider

- Le singole macchine virtuali possono essere sia Windows che Linux. La figura mostra una possibile distribuzione.
- La macchina **CO01** deve essere visibile dalle altre macchine e configurabile dall'interno della rete.
- La macchina **CO1** può accedere a servizi sulle macchine **AS01** e **AS02** sulle seguenti porte : 
 :  : PAR  L(PUN)
- 3787 :  porta zeroconf per ECF
- 8282 :  WebService As.UP
- 8023 :  shell As.UP
- 8024 :  shell As.UP in Looc.UP
- 8472 :  servizi DTAQ
- 8475 :  servizi RMTCMD
- 8476 :  servizi SIGNON


## Tecnologie utilizzate

In seguito un elenco delle tecnologie utilizzate in fase di sviluppo e test dell'architettura. Rappresentano la
soluzione migliore (ma non l'unica possibile).


- Sistema di virtualizzazione VMWare ESXi
- Formato macchine virtuali nativo di VMWare
- Sistemi operativi per macchine virtuali :  **Ubuntu server 14.10 64bit** e **Windows Server 2012 R2 64bit
- DBMS supportati :  **IBM DB2** (in versione Windows o Linux) e **MSSQL Server** (solo Windows)


