# Obiettivo
Elencare i programmi di Fine.UP che contengono la possibilità di LOG di stampa.
La modalità di attivarla è, al solito, inserire un elemento col nome del programma nella tabella PGM e impostare a '1' il campo "LOG".

## Scelta Miglior dettaglio
 :  : DEC T(OJ) P(*PGM) K(S5SMES_11E)
Si imposta nel campo condizioni di LOG, nelle prime 5 posizioni, il numero progressivo di schedulazione del richiamo precedente a quello che si vuol esaminare. Ad esempio, se si vuol capire la scelta eseguita nel passo 5, si imposta 00004.
Viene stampato il miglior dettaglio, man mano, durante la scansione. NB :  viene stampato prima del controllo del CROR :  se passa anche quest'ultimo, viene aggiunta la sigla "OK !!" per evidenziare che è stato (provvisoriamente) scelto.

## Sovrapposizione tra livelli
 :  : DEC T(OJ) P(*PGM) K(S5SMES_28)
Permette di analizzare come viene posto il vincolo al più presto sui dettagli dell'assieme, in base agli istanti di fine dei dettagli dei componenti che aspetta.

## Log di sessione
 :  : DEC T(OJ) P(*PGM) K(S5SMES_32)
All'uscita della schedulazione stampa tutte le azioni "di massa" eseguite :  schedulazione, memorizzazioni, modifiche alle code delle risorse, riportate nella finestra in alto a destra della scheda di presentazione delle risorse (S5SMES_D3).

## Multipostazione
 :  : DEC T(OJ) P(*PGM) K(S5SMES_73)
Presenta, al termine dell'inizializzazione, la composizione effettiva del multipostazione, in base a quanto impostato in tabella :  le risorse, le loro postazioni.
Stampa inoltre gli istanti di inizio disponibilità, per ogni postazione, all'inizio e alla fine della schedulazione.

## Monitor Rsv
 :  : DEC T(OJ) P(*PGM) K(S5SMES_76)
Se si imposta '1' nella prima posizione delle condizioni di log viene stampato il numero di richiami a questo programma per ogni scelta di dettaglio.
Se si imposta '1' nella seconda posizione delle condizioni di log vengono viene stampato il dettaglio selezionato, con il suo istante al più presto dato dalle RSV.

## Scelta RSV
 :  : DEC T(OJ) P(*PGM) K(S5SMES_77)
Si imposta nel campo condizioni di LOG, nelle prime 5 posizioni, il numero progressivo di schedulazione del richiamo precedente a quello che si vuol esaminare. Ad esempio, se si vuol capire la scelta eseguita nel passo 5, si imposta 00004.
Stampa una situazione completa della scelta del miglior VPP.


## Altri Log
Sono inoltre attive le stampe nei seguenti programmi, non attivate via LOG.

S5SMES_C7
È un programma attivo solo su 5250 e richiamato nello script INT_TEC. Presenta a video, e se impostato, anche a stampa, la situazione dei gruppi prima e dopo la schedulazione di un dettaglio.

S5SMES_DE
Presentazione degli errori
In base al richiamo :  Loocup, 5250 o batch, la lista degli errori è presentata in matrice, in G18 o a stampa.

S5SMES_ER
In presenza di errori bloccanti, viene stampato l'elenco e inviato un messaggio all'utente che l'ha richiesta. Questa funzione è stata compresa nel precedente programma S5SMES_DE.
