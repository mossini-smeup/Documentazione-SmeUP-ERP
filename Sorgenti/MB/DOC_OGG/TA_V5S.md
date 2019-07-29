# V5S - Spese/maggioraz/sconti testata
 :  : DEC T(ST) K(V5S)
## OBIETTIVO
Definisce le caratteristiche e le modalità di trattamento dei codici spese/maggiorazioni/sconti legati a una testata documento.
## CONTENUTO DEI CAMPI
 :  : FLD T$ELEM Codice
 :  : FLD T$DESC Descrizione
 :  : FLD T$V5SA **Sconto**
Se questo campo è '1', il codice è uno sconto, altrimenti è una spesa o una maggiorazione.
 :  : FLD T$V5SB **Importo o percentuale**
È il valore, a importo o in percentuale, della spesa (/sconto).
Viene indicato solo se si vuole legarlo in modo univoco al codice.
Se si lascia vuoto, verrà utilizzato il valore immesso sulla testata o derivabile da qualche suo codice (es :  la percentuale di sconto letta dalla tabella pagamento).
 :  : FLD T$V5SC **Tipo : Fisso/Unit/Perc/Nessuno**
Indica il tipo del coefficiente (immesso nel campo precedente o derivato dalla testata) utilizzato per il calcolo : 
 - >F = importo fisso;
- >U = importo unitario;
- >P = percentuale;
- >N = Nessuna applicazione.
 :  : FLD T$V5SD **Cod.valore applicazione**
Se il tipo del coefficiente è Unitario o Percentuale indica, tramite un codice fissato dall'applicazione, a quale valore deve essere applicato.
__Esempio__ :  se il tipo è 'P' e questo codice è 'B', l'importo verrà calcolato come percentuale sul netto merce.
Per vedere i codici previsti, utilizzare la ricerca.
 :  : FLD T$V5SE **Appl. a singolo doc.**
Questo campo è significativo solo quando si attua il raggruppamento documenti (es :  più bolle in una sola fattura).
Se questo campo è '1', la spesa viene applicata ad ogni singolo documento dove compare, altrimenti viene applicata una sola volta sull'intero gruppo.
_9_Esempio :  le spese di trasporto da addebitare per ogni bolla avranno '1' in questo campo, mentre le spese di bollo da calcolare per l'intera fattura avranno ' '.
I codici che hanno '1' vengono elaborati prima degli altri, quindi questo campo ha anche l'effetto di dividere l'elaborazione in due gruppi di codici.
 :  : FLD T$V5SF **Pgm calcolo**
In questo campo si può indicare il nome di un programma che permette di calcolare l'importo con modalità specifiche, non realizzabili con i parametri di questa tabella (es. spese di trasporto legate alla zona del cliente).
Un prototipo di tale programma è B£G04G_XX.
 :  : FLD T$V5SG **Metodo x pgm calcolo**
È il parametro (facoltativo) da passare al programma di calcolo.
Per i tipi BV se non è previsto un pgm di calcolo specifico, questo campo può essere utilizzato per indicare la data fine validità dell'elemento. La data va indicata in formato AAAAMMGG.
 :  : FLD T$V5SH **Assogg. Iva**
È il codice assoggettamento Iva da applicare alla spesa (/sconto).
Nel caso di sconto/maggiorazione percentuale da applicare alla tabella imponibili, questo campo viene ignorato.
 :  : FLD T$V5SI **Copia su righe :  pos.**
Se si indica un numero da 1 a 5 e se nella tabella V5D il campo 'Copia Ma/Sc su righe' è impostato, il valore immesso sulla testata viene riproposto su ogni nuova riga del documento nell'ennesimo campo valore. In questo modo si può ottenere, ad esempio, di copiare su tutte le righe uno sconto modalità
immesso in testata.
Naturalmente questo codice viene ignorato durante il calcolo delle spese/sconti di testata.
 :  : FLD T$V5SO **Mantieni Valore riga pos.**
Se impostato "Copia su righe" fa si che il valore Della testata non prevalga su un eventuale valore  di riga. Per esempio sconto di testata/listino articolo :  lo standard imposta nel valore di riga quello di testata, impostando questo campo verrebbe lasciato il listino quando presente
 :  : FLD T$V5SJ **Tipo spe/mag/sco**
È un codice, fissato dall'applicazione, che le permette di riconoscere le varie tipologie di spesa (/sconto), ad esempio le spese di bollo, gli sconti per pagamento, ecc.
Per vedere i codici previsti, utilizzare la ricerca.
 :  : FLD T$V5SK **Sequenza di calcolo**
È un campo di un carattere che permette di fissare la priorità di elaborazione di questo codice, all'interno del gruppo a cui appartiene (si veda il campo 'Appl. a singolo doc.').
Se, ad esempio si vuole applicare lo sconto pagamento alla tabella imponibili prima dell'addebito delle spese di bollo (in modo da escluderle dallo sconto), inserire 'A' nella tabella dello sconto e 'B' in quella delle spese.
 :  : FLD T$V5SL **Modalità contabilizzazione**
Definisce la modalità di contabilizzazione dell'importo della spesa.
Se questo campo viene lasciato vuoto, la spesa verrà contabilizzata nel conto determinato dalla routine standard (£G03) di determinazione del conto contabile (nel caso delle spese verrà utilizzato il subsettore SP della tabella COA).
Impostando il campo al valore 1, l'importo della spesa verrà contabilizzato nei conti merce del documento, suddividendo l'importo in modo proporzionale all'importo di tutte le contropartite.
Impostando il campo al valore 2, l'importo della spesa verrà contabilizzato nei conti merce del documento, suddividendo l'importo in modo proporzionale all'importo delle contropartite con importi relativi a netto merce (guardando il flag 19 di riga con valori di merce).
Questa impostazione risulta utile nel caso in cui, ad esempio, non si voglia utilizzare un conto specifico per eventuali sconti, maggiorazioni o spese, ma si voglia ripartire l'importo direttamente sui conti merce.
 :  : FLD T$V5SM **Copia virtuale**
Permette di copiare in modo virtuale lo sconto/maggiorazione di testata sulle righe del documento.
Nessun campo delle righe del documento verrà modificato, ma la routine che determinana il valore delle righe dei documenti tratteranno questo sconto/maggiorazione come se fosse presente sulle righe.
Se questo campo è impostato al valore '1', la routine di determinazione del valore di riga (£V5V) riporterà virtualmente sempre il valore sulle righe, in modo che le modalità standard di utilizzo della routine £V5V (DP o CA) considerino sempre questo sconto/maggiorazione (ovvero il valore netto della riga restituito dalla routine terrà conto anche di questo valore).
Impostando il campo al valore '2', lo sconto/maggiorazione verrà copiato virtualmente sulle righe solo se la routine £V5V verrà utilizzata con la funzione specifica (DPE o CAE).
 :  : FLD T$V5SN   **Nessun accorpamento**
Inserendo il valore '1' in questo campo si specifica al programma di gestione delle spese (£V5F) che si desidera
NON raggruppare le spese con lo stesso codice gestite in documenti diversi. Lasciando bianco il programma raggruppa,
a parità di codice, la spesa. Questa funzione si rende Utile ,in presenza di spese "T$V5SE  Appl. a singolo doc."
impostato a '1', Se si vuole un dettaglio spesa per documento (esempio : spese di trasporto dettagliata per bolla in una
fattura con più bolle)
 :  : FLD T$V5SP   **Assoggetamento Iva da documento**
**Inserendo il valore '1' in questo campo si specifica al programma di gestione delle spese (£V5F)che si desidera eseguire una ripartizione della stessa riproporzionandola con gli imponibili iva del documento.
E' possibile escludere un'aliquota dalla distribuzione dichiarandone esplicitamente la sua esclusione in tabella IVA.
Condizioni di applicazione : 
1) l'imponibile della singola aliquota non deve essere superiore al totale del documento
2) Il totale del documento non deve essere 0
3) La spesa deve applicarsi al singolo documento
4) Il codice valore di applicazione non deve essere : 
   U Imponibile senza ricalcolo IVA
   S Dettaglio imponibili (iva esclusa)
   T Dettaglio imponibili (iva inclusa)
5) L'eventuale arrotondamento viene fatto sull'ultima aliquota esaminata.
6) Le aliquote sono trattate nella stessa sequenza in cui si trovano del documento.
7) Il calcolo è eseguito attraveso la sequente formula
   Per tutte le aliquote tranne l'ultima : 
     Moltiplicatore della spesa = Imponibile iva / Totale documento
     Importo iva della spesa = (Importo della spesa * Moltiplicatore)
                               Gestione dell'arrotondamento secondo le specificità della valuta
   Ultima aliquota iva elaborata
     Importo iva della spesa = Importo della spesa - Distribuito
                               Gestione dell'arrotondamento secondo le specificità della valuta
**Inserendo il valore '2' si indica al programma di gestione delle spese (£V5F) di imputare la
spesa all'assoggetamento iva maggiore nel documento

 :  : FLD T$V5SQ   **Limite di Applicazione**
E' un campo che è utilizzato per condizionare l'applicazione dell'elemento, la gestione del campo
dipende dalla tipologia della spesa (Es. Applicativo standard Il calcolo del bollo automatico per
fatture in esenzione (tipologia di spesa BV))
 :  : FLD T$V5SR   **Param.Per valore variabile**
Inserendo un parametro, che deve essere gestito tramite i parametri 'V5S' (la categoria deve essere
obbligatoriamente V5S) Si può rendere il valore (sia esso per valore, unitario o percentuale)
variabile in funzione della data di applicazione, data di applicazione che è recuperata nel solito
modo, la prima in ordine di presenza tra 1) data fattura 2) bolla 3) documento 4) "oggi"
 :  : FLD T$V5SS   **Param.Per Assoggettamento Iva**
Inserendo un parametro, che deve essere gestito tramite i parametri 'V5S' (la categoria deve essere
obbligatoriamente V5S) Si può rendere l'assoggettamento iva variabile in funzione della data di
applicazione, data di applicazione che è recuperata nel solito modo, la prima in ordine di presenza
tra 1) data fattura 2) bolla 3) documento 4) "oggi"

 :  : FLD T$V5ST   **Storno Bollo**
E' un elemento della tabella V5S.
La spesa inserita in questo campo deve essere di Tipo spe/mag/sco = 'BS' ed è inserita nella spesa
di addebito del bollo virtuale (tipo BV).
Si utilizza se si vuole imputare l'addebito del bollo ad uno specifico conto patrimoniale di bolli
virtuali, anche se non viene addebitato al cliente.
Questa spesa normalmente viene inserita in dare di un conto di costo (o abbuono).
