# CRP - INTEGRAZIONE Q9000 CON MAGAZZINO
 :  : DEC T(ST) K(CRP)
## OBIETTIVO
Questa tabella definisce le causali per l'integrazione tra Q9000 ed il magazzino.
La gestione viene attivata solo se nella tabella CQ1 è stato impostato il flag di gestione materiali attraverso tabella CRP e se, per quanto riguarda i ricevimenti di materiale, a livello di riga di bolla è stato impostato il flag "lotto di Collaudo".
## CONTENUTO DEI CAMPI
 :  : FLD T$ELEM  **Tipo lotto**
Per ogni tipo lotto è possibile indicare il comportamento logistico
 :  : FLD T$DESC  **Descrizione**
 :  : FLD CRP,01  **No Free Pass**
Questa è la causale di carico per ricevimento di un lotto di questo tipo che NON SIA in free pass. Il piano di campionamento free pass è quello riportao nella tabella CR1.
 :  : FLD CRP,02  **Free Pass**
Questa è la causale di carico per un ricevimento di un lotto di questo tipo che SIA in free pass. Il piano di campionamento free pass è quello riportao nella tabella CR1.
 :  : FLD CRP,03  **Qty Conforme**
Causale di scarico dell'area collaudo (caricata precedentemente con causale di ingresso) per la qty conforme esitata
 :  : FLD CRP,04
Causale di carico in area destinazione per la qty conforme esitata
 :  : FLD CRP,05  **Qty Non Conforme**
Causale di scarico dell'area collaudo (caricata precedentemente con causale di ingresso) per la qty NON conforme esitata
 :  : FLD CRP,06
Causale di  carico in area destinazione per la qty NON conforme esitata
 :  : FLD CRP,07  **Qty Scarto**
Causale di scarico dell'area collaudo (caricata precedentemente con causale di ingresso) per la qty SCARTO esitata
 :  : FLD CRP,08
Causale di carico in area destinazione per la qty SCARTO esitata
 :  : FLD CRP,09  **Qty Rilavorare**
Causale di scarico dell'area collaudo (caricata precedentemente con causale di ingresso) per la qty RILAVORARE esitata
 :  : FLD CRP,10
Causale di carico in area destinazione per la qty RILAVORARE esitata
 :  : FLD CRP,11  **Qty Selezionare**
Causale di scarico dell'area collaudo (caricata precedentemente con causale di ingresso) per la qty SELEZIONARE esitata
 :  : FLD CRP,12
Causale di carico in area destinazione per la qty SELEZIONARE esitata
 :  : FLD CRP,13  **Delta Dich./Ril. -**
Causale utilizzata per rettificare la giacenza in area collaudo, a seguito di un riscontro di quantità (qty rilevata) minore della quantità dichiarata inizialmente sul lotto
 :  : FLD CRP,14  **Delta Dich./Ril.**
Causale utilizzata per rettificare la giacenza in area collaudo, a seguito di un riscontro di quantità (qty rilevata) maggiore della quantità dichiarata inizialmente sul lotto
 :  : FLD CRP,15  **No Free Pass C/Fase**
Questa è la causale di carico per ricevimento di un lotto di questo tipo che NON SIA in free pass. Questa causale si usa solo nel caso di conto lavoro di fase quando sta entrando la lavorazione dell'ultima fase (sostituisce la "Causale versam.C/Lav." (T$V5BZ) della tabella V5B.
Il piano di campionamento free pass è quello riportao nella tabella CR1.
Causale utilizzata per rettificare la giacenza in area collaudo, a seguito di un riscontro di quantità (qty rilevata) maggiore della quantità dichiarata inizialmente sul lotto
 :  : FLD CRP,16  **Free Pass C/Fase**
Questa è la causale di carico per un ricevimento di un lotto di questo tipo che SIA in free pass. Questa causale si usa solo nel caso di conto lavoro di fase quando sta entrando la lavorazione dell'ultima fase (sostituisce la "Causale versam.C/Lav." (T$V5BZ) della tabella V5B.
Il piano di campionamento free pass è quello riportao nella tabella CR1.



