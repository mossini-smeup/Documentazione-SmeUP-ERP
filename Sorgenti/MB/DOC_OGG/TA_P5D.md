# P5D - Tipo evento
 :  : DEC T(ST) K(P5D)
## OBIETTIVO
Questa tabella definisce il tipo evento.
## CONTENUTO DEI CAMPI
 :  : FLD T$ELEM Codice tipo evento
 :  : FLD T$DESC Descrizione tipo
 :  : FLD T$P5DA __S/s causale evento__
Identifica il sottosettore delle causali ammesse per la dichiarazione degli eventi di questo tipo
 :  : FLD T$P5DB __Causale default__
Se impostata, l'inizializzatore degli eventi (£P5E) forza questa causale del sottosettore definito nel campo precedente
 :  : FLD T$P5DC.T$P5DD __Tipo responsabile__
Il tipo e il prametro individuano l'oggetto che rappresenta il responsabile (codice da immettere nella dichiarazione dell'evento).
Se il tipo+parametro è OJ*USRPRF, l'inizializzatore degli eventi (£P5E) preimposta nel campo responsabile l'utente della sessione.
 :  : FLD T$P5DE __Categoria default__
È un elemento della P5F, serve per definire il tipo/parametro degli oggetti dell'archivio  P5EVEN0F e i parametri impliciti
 :  : FLD T$P5DF __Sottosettore stati gestiti__
È un sottosettore della B£W. Se non impostato si assume B£WEV.
 :  : FLD T$P5DG __Sottosettore categoria evento__
È un sottosettore della P5F.
 :  : FLD T$P5DH **Livello di nascita**
È un elemento della tabella B£W00 :  gli eventi di questo tipo nasceranno con il livello qui impostato, e con il primo stato di questo livello.
Se è impostato lo stato di nascita il livello viene determinato da questo stato
 :  : FLD T$P5DI **Stato di nascita**
È un elemento della tabella B£W sottosettore T$P5DF :  gli eventi di questo tipo nasceranno con questo stato.
Se è impostato lo stato di nascita il livello viene determinato da questo stato
 :  : FLD T$P5DJ __Contenitore note__
È' il contenitore delle note. Se non impostato risale alla tabella P51.
 :  : FLD T$P5DK __Categoria Fissa__
Se è impostato il flag categoria fissa, in immissione e modifica non sarà possibile variare la categoria rispetto a quella presente in T$P5DE , che, contestualmente, sarà un campo obbligatorio.
