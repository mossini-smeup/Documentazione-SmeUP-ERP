## Documentazione Start Demo

## Prerequisito importante
Come configurazione generale la struttura predefinita dovrebbe essere :  \serverxxx\xxximm\ dove al posto di xxx va messo il nome azienda.
Questa rappresenta la share che verrà usata in seguito nella configurazione delle tabelle.

## Tabelle
In questa sezione vengono esposte le tabelle che devono essere presenti per la corretta configurazione della Gestione della Configurazione. Nel corso di questo documento parleremo di disegni tecnici per riferimento, ma quanto verrà esposto è estendibile a qualsiasi documento. Infatti, nell'ambiente Softia oltre ai disegni, sono presenti le procedure.

Le tabelle  che devono essere presenti sono le seguenti : 
  :  : DEC T(ST) K(CQ0)
Tabella dei Tipi Documento-Gestione; devono essere presenti gli elementi del tipo DISE.

Per configurare questa tabella bisogna aver prima preparato le seguenti
  :  : DEC T(ST) K(CQY)
In cui va definita una Griglia per Disegni che prenda in considerazionegli articoli che sono gli articoli della documentazione.

Inoltre sempre nell elemento della tabella CQ0 va messo 1 sia su Gestione Modifica, che su Gestione Documento.

Vanno definiti anche due elementi nella tabella NSC delle note strutturate : 
   :  : DEC T(ST) K(NSC)
il primo elemento che comparirà nel campo Contenitore Docum. dovrà avere : 
 * __**__ appartenente alla tabella : 

 :  : DEC T(ST) K(*CNTT)

nel campo Codice 1.
 * __Q9000-DOCU__ appartenente alla tabella : 

 :  : DEC T(ST) K(NSA)

nel campo Archivio
 -__DO__ sottosettore della tabella : 

 :  : DEC T(ST) K(NSL)

nel campo S/S Lista Distrib.
 * __DCU__ appartenente alla tabella : 

 :  : DEC T(ST) K(NSC)

nel campo Capitolo/Tipo Note. ( Questo è un riferimento a se stesso per dare la struttura di capitoli)

Nella tabella **CQ0** bisogna inoltre definire il programma di visualizzazione nel campo **Pgm. visualizzaz.; questo elemento nel nostro caso si chiama CQDEVSM.!!!!!!

Ultimo campo che dev'essere compilato è il **Parametri Stato**. Questo campo viene riempito con un sottosettore della tabella **CTP** Questa mi dà lo stato del documento in questione se è rilasciato, emesso, approvato o altro.

### Presupposti

_1_Come si porta avanti una demo :  passi e concetti base
Per prima cosa v5d per mettere dentro un ordine d'acquisto up v5d. Si inserisce un ordine con le sue righe d'ordine, per la demo è meglio mettere dei numeri come 100 o 200 Poi entrata della bolla up v5a di entrata materiale Qui è importante rendersi conto che la politica di accorpamento dei lotti è molto importante perchè nella tabella

 :  : DEC T(ST) K(CQ1)

si imposta come agire a fronte di  un'entrata di articoli (se accorparli tutti insieme oppure se creare diversi lotti) per ogni entrata. Il campo in questione è Raggr. Articoli Acq.

Per dichiarare dei collaudi è necessario che esistano dei cicli di collaudo. Bisogna mettere dentro dei cicli; lo si fa con :  04 CCOL- Cicli di collaudo

  -> 1 Gestione Cicli di collaudo
Si mette il nome dell'articolo e si mettono dentro tutte le informazioni del caso come :  vedi come ha fatto roberto nella ges_de cisco760

A questo punto bisogna fare la dichiarazione di collaudo

Si stampa del benestare del collaudo che sono i dati del ciclo fusi su quello del lotto.

V R su una fase del ciclo di collaudo e poi si mettono dentro i valori rilevati

Autorizzazioni   da verificare prima di partire
 * CQNC01_SVI
 * PLC-CQNC01
 * cqnc01
 * cqri10

### Da segnalare : 
Il tipo ordine che viene riportato nella non conformità  è quello che viene riportato nel tipo lotto che non è quello della v5d che è di 3 caratteri che se vengono utilizzati tutti non si faserà mai
 cq§
 C£H
