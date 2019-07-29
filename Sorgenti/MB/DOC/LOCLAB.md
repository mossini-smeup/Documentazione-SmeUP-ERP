# Componente Label

## Abstract

La Label permette di posizionare all'interno di una scheda un testo, esso sia costante o varibile.

## Funzionalità
- [Visualizzare i dati](Sorgenti/MB/DOC/LOCLAB_F01)
- [Stile](Sorgenti/MB/DOC/LOCLAB_F02)
- [Lavorare con gli oggetti](Sorgenti/MB/DOC/LOCLAB_F03)
- [Dinamismi](Sorgenti/MB/DOC/LOCLAB_F04)

## Documenti applicativi
# G.SUB.LAB :  Label

All'interno di una sezione è possibile mettere in evidenza un breve testo.

# Dati

Supporta le funzioni dati relative agli alberi.

# Setup

Per questo tipo di subsezione è previsto un setup specifico G.SET.LAB

## FontName :  Nome FONT
Specifica quale carattere deve essere utilizzato per visualizzare l'etichetta. Il valore è una stringa di caratteri.
##  FontColor :  Colore FONT
Specifica il colore con il quale mostrare il testo dell'etichetta. Il valore è espresso con una stringa di caratteri nella forma RNNNGNNNBNNN dove R, G e B sono rispettivamente le componenti di Rosso, Verde e Blu del colore scelto e NNN il valore numerico (0-255) di ogni componente.
## BackColor :  Colore sfondo
Specifica il colore con in quale mostrare lo sfondo dell'etichetta. Il valore è espresso con una stringa di caratteri nella forma RNNNGNNNBNNN dove R, G e B sono rispettivamente le componenti di Rosso, Verde e Blu del colore scelto e NNN il valore numerico (0-255) di ogni componente.
## FontSize :  Dimensione FONT
Specifica la dimensione del carattere usato per visualizzare il testo dell'etichetta. Il valore è espresso con un numero intero.
## Align :  Allineamento testo
Specifica come deve essere allineato il testo all'interno dell'etichetta. I valori possibili sono CENTER/RIGHT/LEFT. Il valore di default è CENTER.


## Eventi gestiti
Il componente gestisce i seguenti eventi : 
- Init :  L'evento scatta in fase di caricamento il componente
- Click :  Serve a notificare al target che si è cliccato sulla label

## Schede di esempio
Gli esempi del componente lab sono consultabili tramite due sezioni differenti : 
- una sezione generale, che contiene esempi validi per Looc.UP e per Web.UP,
- una sezione più specifica per il web.

 :  : DEC K(Esempi) D(Sezione generale) X(F(EXD;*SCO;) 1(V2;JAGRA;LAB) 2(MB;SCP_SCH;J1GRA) 4(;;ESE)) L(1)
 :  : DEC K(Esempi) D(Sezione specifica per il web) X(F(EXD;*SCO;) 1(V2;JAGRA;LAB) 2(MB;SCP_SCH;WETEST_LAB)) L(1)
