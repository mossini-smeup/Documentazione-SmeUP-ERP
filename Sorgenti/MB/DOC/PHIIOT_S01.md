# Installazione SmeUP Provider
Di seguito indichiamo i passi inziali per far comunicare SmeUp con i dispositivi di campo (PLC/BILANCE/SERIALI/MOXA ...)

**I Passi sono : **
Installazione SMEUP PROVIDER. Solitamente si apre una richiesta indicando cliente e la necessità specifica. Dopo l'apertura del ticket di assistenza si verrà contattati per avere accesso alla rete del cliente.
Per la raccolta dati di campo, è necessaria una installazione separata da altri SmeUp Provider, ad esempio quello usato da WebUp. In questo modo si ottiene una gestione separata di spazi, log e possibilità di riavvio. Ove possibile e dove si collegano più macchine si consiglia vivamente una server (anche virtuale) separato

Configurazione wrapper

Alcuni punti a cui prestare attenzione : 

-- Per l'analisi dei tempi di elaborazione è importante che all' interno del wrapper il punto : 
    set.SMEUP_PROVIDER_LOGLEVEL= DEBUG
    deve essere decommentato (togliere il -) ed impostato a DEBUG, inoltre il parametro : 
    wrapper.app.parameter.12=--loglevel : %SMEUP_PROVIDER_LOGLEVEL%
    deve essere decommentato (togliere il -)

-- Configurazione di alcune variabili fondamentali, da impostare sull' SCP_CLO dell'utente con cui è avviato il Provider : 

Cod="PROVIDER_FIELD_ENABLED" Txt="Abilita integrazione LOA37" TVal="**" Value="true"
Cod="IOTSPI_EVENT_PULSE" Txt="Tempo di estrazione eventi da coda IOTSPI" TVal="" PVal="" Value="20"
   (rappresenta la velocità con cui viene gestito l'evento all' interno del consumatore della coda dati)

IOTSPI è il nome del framework su cui lavorano i plugin

# Specifiche tecniche personale AREA IOT

Installazione di un plugin conforme all'hardware che si vuole interfacciare, nel percorso : 
 C : \SmeupProvider\libs\plugins

 Configurare la LOA37 dedicata al Plugin specifico




























