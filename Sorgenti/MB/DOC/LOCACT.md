# Componente Azione Virtuale

## Introduzione
Il componente Azione Virtuale è componente NON grafico che può essere specificato solo come componente di destinazione di una FUN.
Questo componente si aspetta di ricevere un xml che contenga una azione successiva da eseguire.

In particolare quanto segue : 
- CLOSE :  chiude la finestra corrente.
- LOAD(parametro) o RELOAD(parametro) :  ricarica la sottosezione indicata dal parametro.
- REFRESH :  ricarica la scheda corrente.
- EXECUTE :  lancia una funzione specificata nell'xml.

Normalmente ACT è utilizzato per chiedere al server quale funzione lanciare nei casi in cui non vi sia una reale necessità di implementare un flusso.

## Formato dati
Tipo di XML utilizzato :  Xml di azioni.

## Funzionalità ed attributi
Il componente ACT non essendo un componente grafico non ha setup o configurazioni particolari.

## Schede di esempio
Gli esempi del componente sono consultabili tramite la sezione : 

 :  : DEC K(Esempi) D(Sezione generale) X(F(EXD;*SCO;) 1(V2;JAGRA;ACT) 2(MB;SCP_SCH;J1GRA) 4(;;ESE)) L(1)


