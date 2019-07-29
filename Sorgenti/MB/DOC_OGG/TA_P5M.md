# P5M - Tipo MFP
 :  : DEC T(ST) K(P5M)
## OBIETTIVI
Contiene i parametri che guidano la modalità di produzione MFP (material flow production), che introduce, nella "classica" gestione ad ordini di produzione, un dettaglio logistico, per aumentarne la versatilità.
## SOTTOSETTORI
Non gestiti
## CONTENUTO DEI CAMPI
 :  : FLD T$P5MA __Tipo contenitore__
Definisce il tipo contenitore che verrà assunto di default all'atto della creazione dei contenitori dell'ordine.
 :  : FLD T$P5MB __Tipo contenitore da parametri logisitici__
Se questo campo viene impostato, viene assunto il tipo contenitore PDC dai parametri logistici (valore alfanumerico del parametro C05 della categoria £P3, per l'articolo / plant)
Se invece viene lasciato in bianco, o in assenza del valore precedente, viene assunto il tipo contenitore di questa tabella.
 :  : FLD T$P5MC __Quantitè per contenitore da parametri logistici__
Se questo campo viene impostato, viene assunta la quantità per contenitore PDC dai parametri logistici (valore numerico del parametro C05 della categoria £P3, per l'articolo / plant)
Se invece viene lasciato in bianco, o in assenza del valore precedente, viene assunto il lotto multiplo  di produzione dell'articolo / plant.
 :  : FLD T$P5MD __Forma pres.wip interno__
E' un campo obbligatorio.
Si imposta una forma di presentazione per agganciare le giacenze del Wup interno.
Deve contenere il contenitore, l'articolo, il plant, l'area, il tipo giacenza e l'ubicazione.
Può contenere, opzionalmente, la fase, da inserire se la risorsa viene utilizzata per più di una fase del ciclo di lavorazione.
 :  : FLD T$P5ME __Suff.pgm. exit imp__
E' il suffisso X del programma P5MFP02_X. Viene eseguito come aggiustamento finale nella creazione degli impegni.
 :  : FLD T$P5MF __Forma pres.wip esterno__
E' un campo opzionale, da impostare quando il ciclo del contenitore prevede operazioni esterne (conto lavoro di fase).
Si inserisce una  forma di presentazione per agganciare le giacenze del Wup esterno.
Deve contenere il contenitore, l'articolo, il plant, l'area, il tipo giacenza, la fase e l'ente.
 :  : FLD T$P5MG __Controllo contenitore pieno__
Se impostato inibisce la possibilità di prelevare da un contenitore NON pieno o di versare in un contenitore già pieno.
 :  : FLD T$P5MH __Contesto alias__
E' il contesto dell'alias relativo ai contenitori.
 :  : FLD T$P5MI __Suffisso programma exit creazione contenitore__
E' il suffisso X del programma P5MFP01I_X che viene eseguito prima della creazione di un contenitore.
E' possbile intervenire sui campi calcolati :  tipo contenitore, codice contenitore, tipo unità di movimentazione e
quantità per contenitore
 :  : FLD T$P5MJ __Rifasa Quant.Ord.__
Se attivato, ad ogni azione MFP viene rifasata automaticamente la qtà dell'ordine in funzione della quantità dei contenitori (pianificati + in wip + versati).
 :  : FLD T$P5MK __Azione MFP su collegamento magazzino :  Buoni__
E' l'azione MFP eseguita nel collegamento a magazzino di una entrata merce con avanzmento di produzione (V5COL1) buoni. Flaf di riga conto lavoro R§FL10='1'.
 :  : FLD T$P5ML __Azione MFP su collegamento magazzino :  Scarti__
E' l'azione MFP eseguita nel collegamento a magazzino di una entrata merce con avanzmento di produzione (V5COL1) scarti Flaf di riga conto lavoro R§FL10='2'.
