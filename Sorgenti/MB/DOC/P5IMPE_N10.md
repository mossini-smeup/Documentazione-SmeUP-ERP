# Attribuzione modalità di scarico impegni materiali
Si acquisisce prima di tutto la modalità di scarico (A/B/C/D) dalla tecnica di gestione (GMT) contenuta nei dati magazzino / articolo.

Se codice = "A" (Nessuno scarico) non viene scritto l'impegno e si esce.

Si esamina poi il contenuto della modalità di scarico del tipo impengo (V2_MOSMA) contenuta nel tipo impegno che si sta costruendo : 
 * se è "DO" : 
 ** in fase di scarico, si scarica
 ** in fase di costruzione, si esce

Negli altri casi questa modalità, se presente, sostituisce l'altra nel seguente modo : 
>.   IM >> B
.   IC >> C
.   ID >> D

