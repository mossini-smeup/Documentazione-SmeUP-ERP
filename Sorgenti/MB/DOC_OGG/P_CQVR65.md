## Formato di lancio
![CQ_VEND_26](http://localhost:3000/immagini/MBDOC_OGG-P_CQVR65/CQ_VEND_26.png)
L'esempio sopra permette la memorizzazione nell'archivio FOR/VAL/FOR dell'indice globale IVFO fino al primo livello di dettaglio per il periodo 2006 del fornitore 000460.

La storicizzazione è utile perchè permette di conservare le valutazioni fatte in passato anche se ad esempio col passare del tempo si è cambiato il valore del peso agli indici e mette a disposizione i valori degli indici in un archivio senza la necessità di farli ricalcolare al programma ogni volta che devono essere utilizzati per una particolare applicazione

Gli indici storicizzati li posso interrogare specificando la tripletta nel modulo di gestione indici dinamici (cfr INDI)

_2_Osservazione
Durante la registrazione delle Non Conformità relative ad un lotto acquistato da un dato fornitore, c'è la possibilità di non addebitare il difetto riscontrato al fornitore e di non tenerne conto nel calcolo del Vendor Rating e di qualsiasi altra statistica. Vediamo quanto detto con un esempio.

L'Ente Acquisti commette un errore :  nella stesura dell'ordine di acquisto è stata stampata una specifica non conforme con i requisiti di progetto. Nella fase di entrata del lotto il collaudo effettua le prove sui campioni selezionati come da ciclo di collaudo, e rileva il difetto. Quando viene compilata la Dichiarazione di collaudo, nella definizione dell'esito del controllo si dichiara lo "scarto con consegna regolare" del lotto, nonostante il fornitore non abbia alcuna responsabilità.
Per evitare di tenere conto di questa Non Conformità nel calcolo del Vendor Rating e nelle statistiche degli indici addebitandola a quel fornitore, il programma di gestione lotti permette, attraverso l'opzione "Azioni sul lotto"  di escludere la valutazione.

