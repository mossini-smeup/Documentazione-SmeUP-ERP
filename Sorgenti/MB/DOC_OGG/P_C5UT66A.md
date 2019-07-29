# OBIETTIVO

Questa funzione permette di impostare per ciascun anno la data consolidamento dichiarazione iva, che coincide con la comunicazione dell'iva annuale.

Quando viene impostata le fatture datate precedentemente all'anno impostato devono essere non soggette o comunque non detraibili.

# PARAMETRI

* Azienda :  azienda di riferimento
* Anno :  indicare l'anno per il quale non sarà più possibile registrare fatture detraibili
* Data dichiarazione :  data in cui viene effettuata la dichiarazione iva annuale. Solitamente corrisponde ad Aprile dell'anno +1 indicato nella voce precedente. NOTA BENE :  se la data viene lasciata vuota l'effetto è che se la dichiarazione era stata già effettuata, viene annullata.
* Credito Anno Precedente :  indica credito anno precedente.
* Rettifica :  eventuali rettifiche che vengono portate in dichiarazione iva annuale
* Credito Finale :  Credito anno precedente + Rettifiche

# OUTPUT

L'elaborazione produce due stampe : 
* Il saldo dei conti in cui convergono le operazioni iva non liquidabili
* Le eventuali registrazioni con iva non liquidabile successive alla liquidazione

La prima stampa indica i saldi che vanno stornati a seguito dell'utilizzo di tali operazioni nella dichiarazione iva.
In tale stampa è presenta anche una colonna "Saldo non dichiarabile" :  se presente indica il saldo delle operazioni con iva successive alla data della dichiarazione che verrebbero perciò escluse dal conteggio.

Il dettaglio delle operazioni corrispondenti al saldo non dichiarabile è riportato sulla seconda stampa.

In presenza di tali dati sarà necessario valutare : 
* Se spostare in avanti la data della dichiarazione al fine di includere anche le operazioni che sono rimaste fuori.
* Se invece intervenire sulle registrazioni escluse al fine di fissare un assoggettamento ad imposta a 0.


