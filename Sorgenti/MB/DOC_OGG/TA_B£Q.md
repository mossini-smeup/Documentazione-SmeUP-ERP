# B£Q - Forme di rappresentazione
 :  : DEC T(ST) K(B£Q)
## OBIETTIVO
Questa tabella viene utilizzata nelle seguenti diverse situazione applicative : 
1. Definire il programma di dettaglio che verrà eseguito nelle funzioni di data entry a struttura monitor/visualizzatore. In questo caso un elemento di questa tabella sarà presente nella tabella che guida la transazione (causale di magazzino, modello documento esterno, ecc..).

2. In ambito input panel di oggetto (A36_OA), allo scopo di definire layout e/o programma di controllo specifico della £K89. Anche in questo caso un elemento deid questa tabella sarà presente nella tabella che guida la transzione (causale magazzino, modello documento esterno, ecc.).

3. Parametrizzare gli 'stampatori' forniti per i vari oggetti applicativi, con una serie di specificità (ordinamenti, ulteriori informazioni di input, stampe specifiche), mantenendo la struttura fondamentale ed i servizi da essa forniti (parzializzazioni, costruzione dell'archivio di lavoro, ecc..).

## SOTTOSETTORI
I sottosettori permettono di suddividere le forme di presentazione per i vari oggetti a cui sono collegate (articoli, enti, testate o righe documenti esterni).
## CONTENUTO DEI CAMPI
 :  : FLD T$B£QP **Programma specifico**
È significativo sia per gli stampatori sia per i data entry.
Se impostato, verrà eseguito questo programma di stampa in luogo del programma previsto dallo 'stampatore'. Esso dovrà avere come 'input primario' l'archivio d'appoggio di stampa specifico per l'oggetto.
Nel caso di forma di presentazione per data entry, è il programma che gestirà il dettaglio della transazione.
 :  : FLD T$B£QR **Programma richiesta**
È significativo solo per gli stampatori ed in presenza del programma specifico.
Se impostato, all'atto della richiesta parametri, verrà eseguito anche questo programma, che verosimilmente chiederà ulteriori informazioni. Esse verranno parcheggiate nella porzione libera della 'LDA' (memoria interna del lavoro), per essere poi lette dal programma specifico di stampa, in modo da indurre comportamenti particolari.
 :  : FLD T$B£QO **Programma ordinamento**
È significativo solo per gli stampatori.
Se impostato, all'atto del lancio della funzione, verrà eseguito questo programma che forzerà specifici ordinamenti e totalizzazioni. In tal modo il programma di stampa (sia standard sia specifico) assumerà un comportamento fisso e non guidato dalle scelte dell'utente.
 :  : FLD T$B£QS **Obbligatoria conferma**
È significativo per i data entry.
Se impostato all'inserimento emette msg di conferma.
 :  : FLD T$B£QT **Rimane dopo inserimento**
È significativo per i data entry.
Se impostato dopo l'inserimento mantiene i dati.
 :  : FLD T$B£QQ **Livello Protezione**
È un elemento della tabella B£W/£Q che può essere utilizzato per autorizzare un singolo elemento di questa tabella.
Per maggiori informazioni, si rimanda all'help del programma di gestione settori, sotto il paragrafo : 
CONDIZIONAMENTO RICERCA / AUTORIZZAZIONI ALL'UTILIZZO.
