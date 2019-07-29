# Obiettivi
Dal punto di vista applicativo il programma fornisce un supporto alla gestione del Rating, ad esempio consideriamo il caso di un'analisi del Vendor Rating :  nel 1994 l'azienda 'x' ha 'n' fornitori per cui con Q9000 si è  calcolata gli indici dinamici e statici, supponiamo che nel 1995 abbia n+10 fornitori l'operatore duplica se necessario modifica gli indici statici relativi agli 'n' fornitori del '94, il programma in automatico si calcola gli indici dinamici, l'operatore per sapere quali sono i fornitori nuovi su cui non ha immesso gli indici statici interroga questo programma.

## Formato guida
![CQ_VEND_19](http://localhost:3000/immagini/MBDOC_OGG-P_CQVR80/CQ_VEND_19.png)Le chiavi di accesso dell' indice globale (es. fornitore) devono corrispondere al livello di sintesi per gli indici dinamici che si seleziona. Il programma visualizzerà tutti i fornitori  (chiave dell' indice globale) per cui esistono indici dinamici dell'area/tema/livello di sintesi (che deve corrispondere alla chiave dell' indice globale) selezionato nel periodo di analisi, consentendo di discriminare per quali forntori sono stati inseriti gli indici statici.

## Formato controllo valutazioni
![CQ_VEND_20](http://localhost:3000/immagini/MBDOC_OGG-P_CQVR80/CQ_VEND_20.png)
 * se compare in visualizzazione il periodo (es. 2005) implica che per il fornitore 'xyz' sono stati inseriti gli indici dinamici e gli indici statici.
 * se non compare in visualizzazione il periodo  implica che per il fornitore 'xyz' sono stati calcolati gli indici dinamici ma non sono stati inseriti gli indici statici.
 * se compare il periodo in reverse significa che ci potrebbero essere per il fornitore 'xyz' le valutazioni statiche relative ad un'altro periodo e le valutazioni dinamiche relative al periodo in analisi
 * le opzioni presenti permettono di inserire, modificare le valutazioni statiche.

