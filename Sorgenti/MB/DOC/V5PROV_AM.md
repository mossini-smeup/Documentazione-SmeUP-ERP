## Definizione

Di norma gli importi relativi ai contributi vengono calcolati a partire da quello che risulta dal modulo provvigioni. Nel qual caso contabilmente risultassero dei numeri differenti (es. l'agente non ha mandato la fattura o la manda di importo differente rispetto a quanto calcolato dal modulo provvigionale) è necessario operare alternativamente : 
* Facendo in modo che l'eventuale fatto contabile venga annullato (in quanto generato a partire da un eventuale errore/incomprensione) in modo che tale fatto venga a riproporsi secondo quanto è stato previsto dal modulo provvigionale.
* Intervenendo sulle provvigioni in modo che esse possano corrispondere ai fatti contabili

A tale approccio se ne affianca un altro quello per cui sotto vari aspetti viene attribuita validità solo ai fatti contabili. In smeup questa modalità si attiva impostando il campo della tabella V58 "applicazione master" con il valore "C".

 :  : DEC T(TA) P(V58) K(*)

Tale attivazione ha forti implicazioni, che vengono esposte qui a seguire.

## Differenze Funzionali


| Funzionalità|Applicazione Master V5|Applicazione Master C5 |
| ---|----|----|
| Contabilizzazione Costi Provvigionali|Si|Si |
| Contabilizzazione Contributi|Si|Solo per il minimale |
| Possibilità di calcolare i contributi sempre in base fatturato|Si|No |
| Contabilizzazione di più documenti pro-forma in un'unica registrazione|No|Si |
| Riallineamento Contributi CoGe-Provvigioni|Manuale|Automatico |
| Controllo Data Consolidamento Provvigioni *CP in CoGe|No|Si |
| 


## Differenze Operative

Oltre alla questione del trattamento dell'allineamento delle eventuali divergenze Coge-Provvigioni attivando l'applicazione master C5 operativamente in coge avviene questo : 
* In presenza di un agente con ritenute, sulla schermata appaiono due campi aggiuntivi : 
** Data competenza provvigioni (cioè la data relativa al periodo di liquidazione delle provvigioni che si stanno contabilizzando).
** Importo Provvigioni
* In presenza di un agente senza ritenute, si aprirà una schermata funzionalmente del tutto simile a quella ritenute con la sola differenza di presentare esclusivamente i due succitati campi.
* La data indicata verrà confrontata con la data *CP della tabella B£4 con sottosettore corrispondente a quello per azienda e sulla base di essa : 
** Non sarà possibile una data di riferimento inferiore
** Una registrazione che riporta data competenza inferiore non sarà cancellabile, nei dati relativi alle provvigioni/ritenute saranno modificabili
* Infine è importante notare che in questo caso diventa obbligatorio lanciare la funzione di contabilizzazione dei contributi, con l'opzione di elaborazione del solo minimale :  solo se il minimale viene così contabilizzato verrà, preso in considerazione per il calcolo dei contributi dei periodi successivi.

## Passaggio da Applicazione Master V5 ad Applicazione Master C5

Al momento è stata predisposta una funzione di utility che permette di attivare tale modalità.
La funzione produce una stampa di log, nella quale possono essere indicati anche eventuali interventi da fare a mano.

 :  : INI
 :  : CMD CALL V5UTX15A
 :  : FIN

Se invece si decidesse di tornare indietro, cioè tornare all'applicazione V5, sarebbe necessario intervenire manualmente. Non sono state predisposte delle utility. In questo caso la cosa più semplice consisterebbe nel ripartire da zero con i soli importi residui/progressivi validi alla data di passaggio.

E' inoltre importante che i tipi di registrazione che andranno ad essere utilizzati, supportino la gestione del controllo/bolle fatture passivo.

