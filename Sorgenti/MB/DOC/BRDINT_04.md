## Installazione

Al fine di poter utilizzare la gestione delle dichiarazioni d'intento è necessario disporre e completare i seguenti oggetti : 

### File
  :  : DEC T(OJ) P(*FILE) K(BRDINT0F) I(·)
  :  : DEC T(OJ) P(*FILE) K(BRDINT0L) I(·)
  :  : DEC T(OJ) P(*FILE) K(BRDINT1L) I(·)
  :  : DEC T(OJ) P(*FILE) K(BRDINT2L) I(·)
  :  : DEC T(OJ) P(*FILE) K(BRTDCI0F) I(·)

### Programmi
  :  : DEC T(OJ) P(*PGM) K(BRIN01G) D(Gestione dichiarazioni) O(GOKD)
  :  : DEC T(OJ) P(*PGM) K(BRIN01GV) D(Gestione dichiarazioni-video) O(GOKD)
  :  : DEC T(OJ) P(*PGM) K(BRIN01D) D(Gestione dichiarazioni) O(GOKD)
  :  : DEC T(OJ) P(*PGM) K(BRIN01DV) D(Gestione dichiarazioni-video) O(GOKD)
  :  : DEC T(OJ) P(*PGM) K(BRIN01D_X) D(Gestione dichiarazioni-Exit per flussi post modifica) O(GOKD)
Il programma gestisce l'alimentazione del file **BRDINT0F**. Inoltre richiama al suo interno un programma di __exit** che si occupa della scrittura/aggiornamento sul **BRENTI0F** dei campi : 

- E§CDIN codice dichiarazione
- E§DDIN Data dichiarazione
- E§DVES Data Valid.Esenzione


  :  : DEC T(OJ) P(*PGM) K(BRIN02A) D(Stampa registri dichiarazioni-lancio) O(GOKD)
  :  : DEC T(OJ) P(*PGM) K(BRIN02AV) D(Stampa registri dichiarazioni-lancio) O(GOKD)
  :  : DEC T(OJ) P(*PGM) K(BRIN02B) D(Stampa registri dichiarazioni-esecuzione) O(GOKD)

  :  : DEC T(OJ) P(*PGM) K(BRIN03A) D(Trasmissione dichiarazioni-lancio) O(GOKD)
  :  : DEC T(OJ) P(*PGM) K(BRIN03B) D(Trasmissione dichiarazioni-esecuzione) O(GOKD)
  :  : DEC T(OJ) P(*PGM) K(BRIN03T) D(Trasmissione dichiarazioni-esecuzione) O(GOKD)

  :  : DEC T(OJ) P(*PGM) K(BRIN04A) D(Emissione dichiarazioni-lancio) O(GOKD)
  :  : DEC T(OJ) P(*PGM) K(BRIN04B) D(Emissione dichiarazioni-esecuzione) O(GOKD)

__NB__. : Il programma BRIN04B oltre ad effettuare la stampa della lettera d'intento, effettua anche la scrittura/cancellazione del file BRDINT0F e del BRENTI0F.


