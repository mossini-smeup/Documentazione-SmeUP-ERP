## Introduzione
Il componente grafo (GRP) serve pre rappresentare grafi bidimensionali.

Un grafo è costituito da un insieme di nodi collegati tramite archi.

Il componente disegna gli archi sempre come rette, dotate eventualemnte di frecce.

Il componente viene alimentato da uno specifico XML che descrive questi due elementi base.

il grafo può essere statico o dinamico :  un grafo statico può ad esempio rappresentare un grafo di attività, mente uno dinamico può servire per esplorare relazioni tra molti oggetti.
Un grafo dinamico è infatti in grado di esplodere tutti i legami che partono da un grafo

## Il setup
Si possono specificare le seguenti opzioni di setup : 
- Locality :   attiva la dinamicità del grafo. valori SI/NO. Default NO
- ObjIconType :  specifica il tipo di icona da associare a un nodo di tipo SmeUp. Valori blank, STD_ICON, BOX. default blank. Il valore STD_ICON indica che verrà mostrata l'icona di default associata ll'oggetto, mentre BOX indica di rappresentare un quadrato di colore rosso


## I nodi
I nodi possono essere rappresentati mediante dei rettangoli, dei rettangoli arrotondati o degli ovali.

Ogni nodo è identificato da un ID univoco.
Possono essere oggettizzati, nel qual caso è attivo lo specifico menù di popup.

 T(Si possno specificare le seguenti cartteristiche : )
- Forma del nodo
- Etichetta
-- Testo da mostrare
-- Colore sfondo e colore testo
-- dimensione testo
- Posizione
-- cordinate X e Y
-- visibilità
- Suggerimento (HINT)
-- Testo da mostrare quando mi posiziono sul nodo con il mouse
-- Formtato HTML (true/false)
-- larghezza e altezza
- Oggetto Sme.Up




## Gli archi
Gli archi collegano un nodo ad un'altro nodo.
 T(Sono disponibili 4 tipi di nodi : )
- Tipo 0 :  Bidirezionale. E' una linea ingrossata senza frecce
- Tipo 1 :  Gerarchica a forma di freccia
- Tipo 2 :  Estensione. è una linea sottile. Mostra la gerarchia quando mi posiziono sopra con il mouse.
- Tipo 3 :  Gerarchica con freccia finale.


Nella figura seguente si vede un grafo di esempio con i 4 tipi di frecce.
![ese_01](http://localhost:3000/immagini/LOCGRP_A/ese_01.png)