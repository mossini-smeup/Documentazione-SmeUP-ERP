# Ambiente demo

## Obiettivo.
Ottenere liste personalizzabili di oggetti(classi) e di loro istanze.



## Modello e Struttura.
B£SER_46 è il motore (servizio) in grado di fornire la lista delle classi.

Tra i vari metodi che il servizio espone, si notino : 
  * LIS.CLS (Lista Classi)
  * LIS.PRF (Lista Preferiti)

La base dati è fornita dagli script standard (*_STD) e personalizzati (*_PER), nella fattispecie per il contesto A£DEMO si considerano gli script : 
  * SCP_SET(A£DEMO_STD) (standard)
  * SCP_SET(A£DEMO_PER) (personalizzato)

A£DEMO_STD :  contiene l'elenco delle classi (tag ESE.CLS) e l'elenco dei preferiti (tag ESE.PRF) della
 classe referenziata mediante l'attributo Cod.

  * ESE.CLS Cod="$classe" Cat="$categoria"
  * ESE.PRF Cls="$classe" Cod="$oggettoPreferito"

    N.B :  si noti come la presenza del tag ESE.PRF, sostituisca in toto le istanze altrimenti estratte dalla API £G60 per la classe selezionata.

A£DEMO_PER :  stessa struttura di A£DEMO_STD, con la differenza che le classi presenti in questo script sono in "aggiunta"
a quelle già definite in A£DEMO_STD.
E' inoltre in grado di ridefinire una classe già presente nello script standard, effettuando un vero e proprio override della suddetta.



## Esempio.
Si prenda in esame un contesto d'esempio quale scheda OGBASE_IMG, tabsheet Set'n play. La scheda è divisa in quattro sezioni verticali che
rappresentano in ordine : 
* Immagini importanti
* Lista classi (LIS.CLS)
* Lista preferiti (LIS.PRF)
* Immagine
La selezione di un elemento nell'albero della Sez.1, comporta il caricamento (LIS.CLS) delle classi nella matrice della Sez.2.
La selezione di un elemento di classe nella Sez.2, comporta il caricamento (LIS.PRF) delle istanze nella matrice sella Sez.3.



## Limiti.
Attualmente un limite riscontrato è legato alla dimensione massima di 15Bytes degli oggetti.

