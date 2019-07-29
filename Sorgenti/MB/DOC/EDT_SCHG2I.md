# G.SUB.SEM :  Semaforo

All'interno di una sezione è possibile definire la visualizzazione di un semaforo che faccia
da indicatore per evidenziare la situazione di un certo fenomeno.

# Dati

Supporta le funzioni dati relative ai semafori.

# Setup

Per questo tipo di subsezione è previsto un setup specifico G.SET.SEM

## FontName :  Nome FONT
Specifica quale carattere deve essere utilizzato per visualizzare l'etichetta. Il valore è una stringa di caratteri.

## FontColor :  Colore FONT
Specifica il colore con il quale mostrare il testo dell'etichetta. Il valore è espresso con una stringa di caratteri nella forma RNNNGNNNBNNN dove R, G e B sono rispettivamente le componenti di Rosso, Verde e Blu del colore scelto e NNN il valore numerico (0-255) di ogni componente.

## FontSize :  Dimensione FONT
Specifica la dimensione del carattere usato per visualizzare il testo dell'etichetta. Il valore è espresso con un numero intero.

## Text :  Mostra valore
Specifica se visualizzare il testo relativo al valore del semaforo. I valori possibili sono Yes/No. Il valore di default è Yes.

## Inv :  Inverti il semaforo
Definisce se invertire il comportamento del semaforo in base alle soglie passate. I valori possibili sono Yes/No. Il valore di default è No.

