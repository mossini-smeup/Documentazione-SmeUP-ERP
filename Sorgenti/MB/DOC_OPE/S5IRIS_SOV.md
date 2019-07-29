# Introduzione
Quando viene schedulata un'operazione, la successiva viene dichiarata pronta (e quindi entra in competizione per essere schedulata) e le viene assegnato un istante (data/ora) di vincolo al più presto, vale a dire l'istante minimo a cui essa può iniziare.

In assenza di specificazioni ulteriori, questo istante è la fine dell'operazione precedente (compreso il tempo di attesa successiva che, ricordo, è calcolato in giorni solari, e che fa avanzare l'operazione senza  occupare la risorsa, e serve per descrivere situazioni quali il tempo di raffreddamento, di riposo, ecc...)

E' possibile che l'operazione successiva inizi non al termine della precedente, ma quando in quest'ultima è stata prodotta una quantità sufficiente per ailmentarla (ad esempio quella per riempire un contenitore).

# Descrizione operativa
Nella schedulazione BCD è possibile rappresentare questa situazione, in diverse modalità.

Definizioni : 
OP - Operazione precedente
RP - Risorsa generale dell'operazione precedente
OS - Operazione successiva
RS - Risorsa generale dell'operazione successiva

Condizione necessaria perchè si applichi la sovrapposizione, è che sia RP sia RS siano schedulate a capacità finita.

Si deve poi impostare nello scenario che è attiva la sovrapposizione :  in questo modo si disaccoppia l'introduzione delle informazioni dal loro utilizzo.

Si impostano le seguenti informazioni, nella tabella del tipo risorsa (BRM) di RS
TS - Tipo sovrapposizione  (attualmente è attivo il tipo 'A', in ore)
HI - Ore iniziali di sovrapposizione
HF - Ore finali di sovrapposizione

I valori HI e HF possono essere inseriti anche a livello di ciclo. In questo caso essi vengono riportati nei comnponenti di carico N.4 e N.8

La sovrapposizione si calcola se TS vale 'A'

Si possono verificare i seguenti casi : 

A) Sovrapposizione dalla fine - se HI=0 e HF>0
OS deve terminare dopo HF da quando termina OP. Si controlla che non inizi prima dell'inizio di OP oppure dopo la sua fine

B) Sovrapposizione dall'inizio - se HI>0 e HF=0
OS deve iniziate dopo HI da quando inizia OP. Si controlla che non finisca prima della fine di OP e che non inizi dopo la sua fine

C) Sovrapposizione dall'inizio e dalla fine - se HI>0 e HF>0
OS deve iniziate almeno dopo HI da quando inizia OP e finire almeno dopo HF da quando finisce OP. Si utilizza il vincolo più restrittivo

Ricordo che HI e HF vengono controlati allo stesso livello (prima i valori del ciclo, poi quelli della tabella BRM).
