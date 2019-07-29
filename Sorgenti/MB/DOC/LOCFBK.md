# Componente Invio con Feedback di ritorno.

## Introduzione
Il componente FBK è un componente NON grafico che può essere specificato solo come componente di destinazione di una FUN.
Questo componente ha il suo principale utilizzo come chiamata a FUN di notifica verso il server as400 o il provider.
Come sonseguenza di ciò non ci si aspetta alcun xml di dato di ritorno ad eccezione di eventuali messaggi di conferma.

Normalmente FBK è utilizzato quando è necessario eseguire una azione sul server senza doverne controllare o aspettare il risultato.

## Formato dati
Tipo di XML utilizzato :  Solo Xml Messaggi.

## Funzionalità ed attributi
Il componente FBK non essendo un componente grafico non ha setup o configurazioni particolari.

## Schede di esempio
Gli esempi del componente sono consultabili tramite la sezione : 

 :  : DEC K(Esempi) D(Sezione generale) X(F(EXD;*SCO;) 1(V2;JAGRA;FBK) 2(MB;SCP_SCH;J1GRA) 4(;;ESE)) L(1)
