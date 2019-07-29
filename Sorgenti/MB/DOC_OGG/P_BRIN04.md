# Obiettivo
Questo pgm ha la duplice funzione di stampare le lettere emesse dall'azienda che gode delle condizioni per poter usufruire della dichiarazione d'intento verso i suoi fornitori,  e di creare contiguamente i relativi record nel file di gestione.

# Formato di lancio
![Fig_005](http://localhost:3000/immagini/MBDOC_OGG-P_BRIN04/Fig_005.png)
Nella videata impostare : 
 * Tipo elaborazione :  se lasciato vuoto viene emessa una dichiarazione provvisoria. Questo significa che viene solo fatta una stampa di prova della dichiarazione stessa. Impostando il campo con 1 viene emessa una dichiarazione definitiva che quindi viene protocollata e scritta sugli archivi delle dichiarazioni di intento. Impostando il campo con 2 è possibile ottenere una ristampa di una dichiarazione già emessa
 * Utilizzo modulo standard :  se impostato con 1 Sì permette di ottenere la stampa sui moduli utilizzati fino al 2014
 * Ufficio IVA :  riporta la descrizione dell'ufficio IVA a cui viene emessa la dichiarazione di intento. Veniva utilizzata sui moduli usati fino al 2014. Sui nuovi moduli del 2015 non viene più emessa quindi può essere lasciata vuota.
 * Descrizione beni :  in questo campo va inserita (facoltativamente) la descrizione dei beni/servizi a cui la dichiarazione si riferisce
 * Data emissione :  inserire la data in cui la dichiarazione viene emessa
 * Anno di Riferimento :  inserire l'anno in cui le operazioni coperte da dichiarazione verranno poste in essere. Questo sarà anche l'anno utilizzato per l'assegnazione del protocollo della dichiarazione
 * Tipo dichiarazione :  compilare con 1 se si tratta di dichiarazione per singola operazione, 2 se si tratta di dichiarazione fino a concorrenza di un importo o 3 se si tratta di dichiarazione di un periodo
 * Importo :  compilare il campo con il valore dell'operazione se il campo _Tipo dichiarazione è compilato con 1 o 2
 * Periodo :  compilare con il periodo di validità della dichiarazione dell'operazione se il campo _Tipo dichiarazione_ è compilato con 3
 * Assoggettamento IVA :  indicare l'assoggettamento IVA che il sistema dovrà presentare in fase di immissione della registrazione di acquisto nel caso in cui la fattura ricada nel periodo di validità della dichiarazione
 * Destinatario :  indicare il destinatario della dichiarazione scrivendo nel primo campo FOR e nel secondo campo il codice del fornitore. Attenzione :  se il destinatario è un ufficio doganale verificare che all'interno dell'anagrafica sia indicato il rapporto fiscale _Dogana_.
 * Lista Destinatari :  se è stata preparata una lista di fornitori destinatari della dichiarazione compilare i campi con FOR e il nome della lista preparata

# Collegamento con la fatturazione
In funzione delle dichiarazioni ricevute al momento della stampa documenti del ciclo attivo (DDT e fatture immediate) viene determinato il codice assoggettamento da utilizzare.
