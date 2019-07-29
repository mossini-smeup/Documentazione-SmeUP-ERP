# Impostazioni del Budget
Sono utilizzate dalla scheda di gestione budget e dai programmi di calcolo dei consutivi e confronto con il budget.
Nella definizione del budget di vendita possiamo avere il dettaglio per Articolo / Cliente o per Articolo, questo dipende dagli oggetti associati alla vista quantità di budget, se il dettaglio è per articolo deve esistere un listino di vendita con cliente ** oppure cliente blank, questo listino è quello utilizzato nelle valorizzazioni.

La valorizzazione del budget di vendita può avvenire direttamente scrivendo una vista nel corrispondente piano oppure,mediante lettura listino, nei servizi di creazione dei file da utilizzare per l'analisi del budegt e dei consuntivi.

Le analisi servono principalmente per confrontare i consuntivi con il budget, i servizi di elaborazione dati per il budget si occupano di : 
 * valorizzare il budget di vendita, come detto in precedenza la valorizzazione può essere da MPS oppure seguita nei servizi di creazione dati
 * raccogliere i consuntivi di fatturato, direttamente da documenti V5, da MPS, da statistiche V5 (file V5STAT)
 * integrare le informazioni per le analisi con dati quali il costo unitario standard o consuntivo oppure il cambio utilizzato

I valori possono poi essere consolidati in un D5COSO, in questo caso tema e contesto devono essere specificati nei parametri di impostazione.


## Parametri lancio elaborazioni e schede
* Tipo piano budget (TA MP*TP)
* Prefisso piano budget (**) (per la scheda budget si preimposta il piano che ha il prefisso indicato e l'anno prossimo, se manca si usa l'anno corrente; per le analisi consuntive si preimposta il piano con il prefisso indicato e l'anno corrente)
* Vista quantità budget (TA MPC)
* Vista valore budget (TA MPC) (se compilata i servizi di creazione analisi consuntive la usano per i valori totali, altrimenti la valorizzazione avviene con i dati di listino)
* Flusso principale creazione Budget di vendita (TA B£H) è il flusso che partendo dalla vista budget a quantità popola il resto delle viste del budget, può essere lanciato dalla scheda MPS
* Listino di vendita (TA C£L) alternativo alla vista valore budget
* Sezione listino di vendita (TA C£Vxx) alternativo alla vista valore budget
* Tipo documento fatture attive da V5 (TA V5D) (per la raccolta dati consuntivi di vendita)
* Vista qtà consuntivi di vendita (TA MPC) alternativa alla raccolta consuntivi da V5
* Vista valori consuntivi di vendita (TA MPC) alternativa alla raccolta consuntivi da V5
* Tipo record statistiche V5STAT, (V2 V5STA) alternativa alla raccolta consuntivi da V5
* Tipo costo standard (TA TCO)
* Livello costo standard (TA D0B)
* Contesto D5COSO (TA  D5S) se compilato è utilizzato per consolidare il confronto consutivi / budget di vendita
* Tema D5COSO (TA D5Oxx) come sopra

## Campi considerati
Nelle analisi budget <> consuntivi si considerano i campi seguenti che possono avere provenienze diverse : 

|  Nam="Campi per analisi consuntivi" R="99" |
| 
| .COL Txt="C." LunAut=" " A="L" |
| ---|----|
| 
| .COL Txt="Descrizione" LunAut=" " A="L" |
| 
| .COL Txt="Formula" LunAut=" " A="L" |
| 
| .COL Txt="Nota" LunAut="1" A="L" |
|   01 | Qtà Budget | | È la quantità che viene letta nella vista piano del budget |
|   02 | Importo totale Budget | | È l'importo corrispondente alla quantità del campo precedente, può essere letta da una vista piano oppure calcolata (es. valorizzando la qtà totale con un listino) |
|   03 | Prezzo unitario Budget | | può essere calcolato come divisione dell'importo totale fratto la qtà totale oppure letto direttamente (es. da un listino) |
|   04 | Componente prezzo 1 Budget | | Il campo viene usato quando il prezzo di vendita è l'insieme di n. componenti di cui si vuole controllare la varianza (es. acciaio, lavorazioni esterne, attrezzaggio, trasporto, ...) a standard sono previste fino a 8 componenti di prezzo, per un numero superiore devono essere sviluppate delle personalizzazioni |
|   05 | Comp. prezzo 2 Budget | | Vedi sopra |
|   06 | Comp. prezzo 3 Budget | | Vedi sopra |
|   07 | Comp. prezzo 4 Budget | | Vedi sopra |
|   08 | Comp. prezzo 5 Budget | | Vedi sopra |
|   09 | Comp. prezzo 6 Budget | | Vedi sopra |
|   10 | Comp. prezzo 7 Budget | | Vedi sopra |
|   11 | Comp. prezzo 8 Budget | | Vedi sopra |
|   15 | Cambio di Budget | | Il cambio utilizzato nel periodo tra la valuta corrente e quella del cliente |
|   16 | Costo unitario | | Costo standard da utilizzarenel calcolo margini |
|   17 | Margine totale Budget | V02 - (V01*V16) | Calcolato |
|   31 | Qtà Consuntivo | | Letta dai documenti di vendita |
|   32 | Importo totale Consuntivo | | Letto dai documenti di vendita |
|   33 | Prezzo unitario Consuntivo | | Può essere calcolato come divisione dei due valori precedenti oppure letto dai documenti di vendita |
|   34 | Componente prezzo 1 Consuntivo | | Vedi sopra |
|   35 | Comp. prezzo 2 Consuntivo | | Vedi sopra |
|   36 | Comp. prezzo 3 Consuntivo | | Vedi sopra |
|   37 | Comp. prezzo 4 Consuntivo | | Vedi sopra |
|   38 | Comp. prezzo 5 Consuntivo | | Vedi sopra |
|   39 | Comp. prezzo 6 Consuntivo | | Vedi sopra |
|   40 | Comp. prezzo 7 Consuntivo | | Vedi sopra |
|   41 | Comp. prezzo 8 Consuntivo | | Vedi sopra |
|   45 | Cambio Consuntivo | | Letto dai documenti di vendita |
|   47 | Margine totale Consuntivo | V32 - (V31*V16) | Calcolato |
|   51 | Delta Quant.  Cons.-Budget | V31 - V01 | Calcolato |
|   52 | Delta Importo Cons.-Budget | V32 - V02 | Calcolato |
|   53 | Delta Margine Cons.-Budget | V32 - (V31*V16) | Calcolato |
|   56 | Inc.% Quant.  Cons.-Budget | (V31-V01) * 100/V01 | Calcolato |
|   57 | Inc.% Importo Cons.-Budget | (V32-V02) * 100/V02 | Calcolato |
|   58 | Inc.% Margine Cons.-Budget | (V47-V17) * 100/V17 | Calcolato |
|   61 | Varianza quantità | (V31-V01) * V03 | Calcolata |
|   63 | Varianza prezzo | (V33-V03) * V31 | Calcolata |
|   71 | Varianza componente prezzo 1 | (V34-V04)*V31 | Vedi sopra |
|   72 | Varianza comp. prezzo 2 | (V35-V05) * V31 | Vedi sopra |
|   73 | Varianza comp. prezzo 3 | (V36-V06) * V31 | Vedi sopra |
|   74 | Varianza comp. prezzo 4 | (V37-V07) * V31 | Vedi sopra |
|   75 | Varianza comp. prezzo 5 | (V38-V08) * V31 | Vedi sopra |
|   76 | Varianza comp. prezzo 6 | (V39-V09) * V31 | Vedi sopra |
|   77 | Varianza comp. prezzo 7 | (V40-V10) * V31 | Vedi sopra |
|   78 | Varianza comp. prezzo 8 | (V41-V11) * V31 | Vedi sopra |
| 

I valori di cui sopra vengono rilevati sia nel periodo che progressivi nell'anno (year to date).

## Anagrafici di supporto
Per le elaborazioni si possono utilizzare gli stessi anagrafici usati per la produzione oppure si possono usare degli anagrafici ad hoc, in particolare : 
* distinte di budget (tipo BDG)
* cicli di budget (tipo BDG)
* listini vendita di budget (sezione B01)
* listini acquisto di budget (sezione B02)
* listini conto lavoro di budget (sezione B03)
* cambi di budget (tipo cambio "2")
* scenario pianificazione MRP di budget
* scelta fornitore preferenziale di budget :  nella pianificazione MRP la scelta del fornitore preferenziale in genere ha il suo utilizzo per la determinazione dei suggerimenti che vengono rilasciati con un orizzonte a breve, in questo caso l'archivio dove viene fissato il fornitore preferenziale non ha bisogno di date di validità e si usa il BRARES. Per la pianificazione MRP di budget può essere necessario avere fonitori diversi a date diverse, in questo caso l'archivio da utilizzare è il C£LIST con listino / sezione ad hoc e bisogna intervenire nella politica di pianificazione (tab. M5A) ed in particolare nell'esecuzione della routine £V5U che è condizionata da come sono impostati i campi "Modo di assegnazione ente"  "Parametro di assegnazione ente".
