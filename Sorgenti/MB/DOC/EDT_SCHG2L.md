# G.SUB.GAU :  Cruscotto

All'interno di una sezione è possibile definire la visualizzazione di un cruscotto che faccia
da indicatore per evidenziare la situazione di un certo fenomeno.

# Dati

Supporta le funzioni dati relative ai cruscotti.

# Setup

Per questo tipo di subsezione è previsto un setup specifico G.SET.GAU

## FontName :  Nome FONT
Specifica quale carattere deve essere utilizzato per visualizzare l'etichetta. Il valore è una stringa di caratteri.

## FontColor :  Colore FONT
Specifica il colore con il quale mostrare il testo dell'etichetta. Il valore è espresso con una stringa di caratteri nella forma RNNNGNNNBNNN dove R, G e B sono rispettivamente le componenti di Rosso, Verde e Blu del colore scelto e NNN il valore numerico (0-255) di ogni componente.

## FontSize :  Dimensione FONT
Specifica la dimensione del carattere usato per visualizzare il testo dell'etichetta. Il valore è espresso con un numero intero.

## Text :  Mostra valore
Specifica se visualizzare il testo relativo ai valori del cruscotto. I valori possibili sono Yes/No. Il valore di default è Yes.

## Inv :  Inverti il cruscotto
Definisce se invertire il colori del  cruscotto in base ai valori delle soglie. I valori possibili sono Yes/No. Il valore di default è No.

## Extend :  Espandi il cruscotto
Estende il cruscotto fino ad occupare tutto il pannello che lo contiene. I valori possibili sono Yes/No. Il valore di default è No.

## Type :  Stile del cruscotto
Applica al cruscotto uno dei due stile predefiniti :   "Angular" il cruscotto visualizzato è a 180 gradi "Circle" il cruscotto viene visualizzato in modo circolare
