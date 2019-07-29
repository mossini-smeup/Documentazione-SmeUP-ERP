## Obiettivo

Attraverso questo programma è possibile effettuare inserimenti, modifiche e cancellazioni di movimenti black list precedentemente estratti.

## Formato guida

All'interno del formato guida è possibile compilare i seguenti campi : 
 * Opzione :  è possibile indicare inserimento (01), modifica (02), cancellazione (04) o interrogazione (05)
 * ID Movimento :  all'interno di questo campo è possibile indicare il numero progressivo del movimento all'interno del file dei movimenti black list.

![C5C020_003](http://localhost:3000/immagini/MBDOC_OGG-P_C5MB01G/C5C020_003.png)
## Formato lista

Lasciando vuoti i campi del formato guida e dando invio è possibile visualizzare la lista dei movimenti black list estratti, ordinati per data registrazione in modo decrescente : 

![C5C020_004](http://localhost:3000/immagini/MBDOC_OGG-P_C5MB01G/C5C020_004.png)
Nella parte superiore dell'elenco sono riportate le opzioni disponibili per ogni singolo record e che compariranno anche digitando un '?' all'interno della casella posta all'inizio del record stesso.

Per ognuno dei record della lista sono riportati : 
 * data registrazione, data competenza IVA, tipo e numero protocollo IVA se presenti
 * tipo ente intestatario, codice ente, ragione sociale e partita iva
 * imponibile e imposta della registrazione.

Utilizzando l'opzione 02 o 05 è possibile accedere in modifica o in interrogazione del formato dettaglio.

### Parzializzazioni

Digitando il tasto F13 o selezionando il relativo pulsante è possibile accedere alla schermata delle parzializzazioni che consentono di filtrare i record visualizzati : 

![C5C020_005](http://localhost:3000/immagini/MBDOC_OGG-P_C5MB01G/C5C020_005.png)
All'interno delle parzializzazioni è sempre disponibile il campo delle memorizzazioni che consente di salvare una particolare parzializzazione.

## Formato dettaglio

Entrando nel dettaglio di ogni singola registrazione è possibile visualizzarne le informazioni associate che verranno poi riportate all'interno delle comunicazioni black list : 

![C5C020_006](http://localhost:3000/immagini/MBDOC_OGG-P_C5MB01G/C5C020_006.png)
Nel caso in cui si entri in modifica di un movimento già trasmesso in modo definitivo verrà visualizzata una richiesta di conferma della modifica stessa.

All'interno del dettaglio del movimento black list è possibile visualizzare/modificare : 
 * Riferimenti contabili : 
 ** Numero di registrazione contabile a cui il movimento si riferisce
 ** Tipo, numero e data protocollo
 ** Numero e data documento
 ** Tipo e segno IVA
 ** Data registrazione e data competenza
 ** Validità :  se compilato con 1 il record non verrà ripreso all'interno dei dati da trasmettere all'Agenzia
 * Dati anagrafici dell'ente : 
 ** Codice ente, partita iva e codice fiscale
 ** Codice nazione, codice CVS, stato federale, provincia e contea se presenti
 ** Località e indirizzo eventualmente riportati in anagrafica dell'ente
Nel caso in cui l'ente sia una persona fisica sono riportate anche i dati della persona fisica rilevanti (nome, cognome e dati di nascita) : 

![C5C020_007](http://localhost:3000/immagini/MBDOC_OGG-P_C5MB01G/C5C020_007.png)

Nello specchietto in basso sono riportate le informazioni di dettaglio riferite alla registrazione contabile. In particolare sono riportati : 
 * Imponibile
 * Codice e descrizione assoggettamento
 * Aliquota percentuale
 * Valore dell'imposta
 * Tipologia di esenzione (ripresa dalla tabella IVA)
 * Natura operazione (ripresa dalla tabella IVA o impostata manualmente nella ripresa per movimenti non IVA)




