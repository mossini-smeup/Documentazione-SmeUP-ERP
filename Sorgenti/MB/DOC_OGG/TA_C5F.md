# C5F - Istituti di credito aziendali

## OBIETTIVO
Definire gli istituti di credito aziendali associando a ciascuno di essi un conto contabile e un numero di conto corrente.

## CONTENUTO DEI CAMPI
 :  : FLD T$DESC **Descrizione**
Descrive l'istituto di credito.
 :  : FLD T$C5FA **Codice Banca**
Viene indicato il codice ABI/CAB che identifica la banca e che deve essere codificato come oggetto CNBAN.
 :  : FLD T$C5FC **Autorizzazione num.**

 :  : FLD T$C5FD **Data**

 :  : FLD T$C5FE **Prov.**

 :  : FLD T$C5FH **gg Intervallo Riba**
Identifica il tempo necessario alla banca in oggetto per ocmunicare l'esito delle Riba.
 :  : FLD T$C5FI **Numero C/C**
Identifica il numero di conto corrente bancario.
 :  : FLD T$C5FL **Conto Contabile C/C**
Definisce il conto contabile associato al conto corrente bancario.
 :  : FLD T$C5FK **Lista circuito bancario**
Indica la lista di ABI che identificano il circuito bancario cui
appartiene la banca e tramite la quale è possibile determinare la domiciliazione
delle operazioni.
 :  : FLD T$C5FM **Interm.extra-banc.**
Indica se l'istituto di credito non è una banca.
