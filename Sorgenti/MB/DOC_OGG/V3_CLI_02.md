# CLI -  LISTENER DI CLIENT
Questo listener è utilizzato nella Business Continuity

## Il codice del listener
Il codice di questo listener è 02

## Cosa fa
TODO


## Che struttura dati passa al server AS
TODO

## I parametri specifici
TODO

## Esempi di impementazioni

 * C.LST Cod="CL" Txt="Connessione server primario" Add="localhost" Protocol="JAVA" Param="class=Smeup.smeui.uimainmodule.externallistener.java.client.UILoocupClientListener;Service=LOSER_11;server=172.16.2.161;type=MASTER" LoadOnStartup="1"

 * C.LST Cod="BK" Txt="Connessione server backup" Add="localhost" Protocol="JAVA" Param="class=Smeup.smeui.uimainmodule.externallistener.java.client.UILoocupClientListener;Service=LOSER_11;server=172.16.2.101;type=BACKUP" LoadOnStartup="1"

