# GMG - Tipo gestione ubicazione
## OBIETTIVO
Impostare liberamente la modalità di utilizzo dell'ubicazione (es. STANDARD, KANBAN, ecc.). Lo scopo è unicamente di classificazione.
## CONTENUTO DEI CAMPI
 :  : FLD T$GMGA __Met.accesso giacenza x ubicazione__
È un elemento della tabella GMF :  definisce la vista di GMQUAN che guida il reperimento della giacenza dell'ubicazione, nella scansione per tipo gestione.
 :  : FLD T$GMGB __Met.accesso giacenza x articolo__
È un elemento della tabella GMF :  definisce la vista di GMQUAN che guida il reperimento della giacenza di un articolo nelle ubicazioni di questo tipo.
 :  : FLD T$GMGC __Causale di prelievo__
È un elemento della tabella GMC, a disposizione di eventuali programmi che eseguono un prelievo da questa ubicazione.
 :  : FLD T$GMGD __Causale di versamento__
È un elemento della tabella GMC, a disposizione di eventuali programmi che eseguono un versamento in questa ubicazione.
