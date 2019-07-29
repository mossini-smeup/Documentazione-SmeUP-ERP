# INTRODUZIONE
I servizi interni sono funzioni esposte direttamente dall'applicativo client a differenza dell'altra grande tipologia di serivizi esposti dal server AS400 o in generale dai sever applicativi.

 T(Alcuni esempi di servizi interni sono : )
- aggiungi una funzione ai preferiti
- visualizza cronologia delle funzioni chiamate
- copia di file da una directory ad un'altra



## Gestore Funzioni Interne

![LOCBAS_037](http://localhost:3000/immagini/LOCINT_01/LOCBAS_037.png)
Le richieste effettuate dall'utente che non necessitano di informazioni ulteriori a quelle già presenti sul client sono per lo più gestite dal client stesso attraverso dei servizi java. La struttura di questi servizi è analoga a quella dei servizi RPG... hanno cioè una struttura in ingresso "funnizzata", cioè richiedono funzione, metodo,  un elenco di 6 oggetti massimo ed una stringa parametro e in uscita generano un file XML interpretabile dai componenti grafici di LoocUp.

L'elenco dei servizi, come in figura, è riportato qua sotto : 

JA_00_01 :  Gestore Setup

JA_00_02 :  Carrello

JA_00_03 :  E@mail

JA_00_04 :  ricerca

JA_00_05 :  gestore files, funzioni base

JA_00_06 :  gestore cronologia

JA_00_07 :  wizard

JA_00_08 :  comunicazione

JA_00_09 :  doc.html

JA_00_10 :  gestore menù

JA_00_11 :  gestore alias

JA_00_12 :  menù tab delphi

JA_00_13 : 

JA_00_14 : 

JA_00_15 :  apertura files, esec. cmd di sistema

JA_00_16 :  listener

JA_00_17 :  server

JA_00_18 :  Getore finestre
