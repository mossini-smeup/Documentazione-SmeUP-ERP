
# Obiettivo

Stampare e trasmettere i dati relativi alle comunicazioni liquidazioni periodiche iva


# Parametri di esecuzione

* **Anno** :  anno di riferimento dei dati da trasmettere
* **Trimestre** :  trimestre di riferimento dei data da trasmettere
* **Liquidazione Del Gruppo** :  indicare se si sta creando la comunicazione liquidazione iva   del gruppo
* **Stampa modelli** :   in formato pdf, verranno prodotti i modelli nella cartella specificata   nel punto successivo. In spool verranno creati i modelli in spool.   Se non viene indicato nulla verrà creato solo il file XML nella cartella   specificata nel punto successivo
* **Cartella/File da trasmettere** :  mettendo un carattere qualsiasi nel campo, sarà possibile   accedere alla maschera in cui poter indicare il percorso ove verranno depositati i file della   comunicazione da inviare all'agenzia delle entrate. In tale cartella verranno   posti anche gli eventuali pdf dei modelli   Il nome del file verrà composto nel seguente modo :    IT + CodiceFiscale +_LI_+ Anno+Trimestre.XML
* **Modalità** :  indica se l'elaborazione è provvisoria, definitiva o si vuole annullare una definitiva.
** In definitiva sui dati verranno aggiornati due campi : 
***  Lo data di trasmissione (assume data odierna)
***  Lo stato, che passa a TRA (trasmessa) o ANN (annullata), a seconda che la tipologia invio sia normale/sostitutiva o annullamento.
** In annullamento di una definitiva, verrà chiesta la data da annullare, sulla base della quale verranno filtrati i dati da elaborare e verrà cambiato lo stato, che a seconda della tipologia di invio verrà riportato al valore precedente all'esecuzione definitiva.

