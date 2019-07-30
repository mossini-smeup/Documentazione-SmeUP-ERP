# OBIETTIVO

Questo servizio carica le liste di azioni associate ad un oggetto (istanza).
Viene quindi utilizzato : 
 * Per costruire i pop.up.
 * Per costruire le liste di azioni da 5250 (chiamato dalla G99, che poi presenta solo le azioni A() ).

# FUNZIONI / METODI

## FUN
Questa è la chiamata principale (standard) per la costruzione del popup di base di un oggetto (primo livello).
Automaticamente decide, in base alla tipizzazione, se interpretare lo script interno di default per tutti gli oggetti oppure se utilizzare uno script specifico di oggetto in SCP_SCHPOP.

## SCP
Sottochiamata da un pop.up, serve a costruire un sottolivello a partire da uno script specifico, eventualmente non legato all'oggetto.
I parametri di chiamata ricalcano quelli del JATRE_18C per l'apertura di schede, quindi : 
 * Nell'oggetto 1 viene passato l'oggetto a cui fa riferimento il pop.up (utilizzabile nelle variabili di script, ad esempio OG.K1).
 * Nell'oggetto 2 il nome del membro da aprire.
 * Nell'oggetto 4 l'eventuale nome del sottoscript.

## GES
Sottochiamata da un pop.up, serve a elencare le azioni di gestione disponibili per l'oggetto (modifica, copia, ...).

## UTE
Sottochiamata da un pop.up, serve a elencare le azioni dalla B£H di tipo A- del tipo oggetto considerato.

## STD
Sottochiamata da un pop.up, serve a elencare le azioni standard del tipo oggetto considerato (da B£FUN0_xx).

## M5.RIL
Sottochiamata da un pop.up, serve a elencare azioni specifiche M5 (pgm M5FUC0J).

## Altri metodi (CS1)
Sottochiamata da un pop.up, serve a elencare insiemi particolari di azioni costruiti da programmi speciali (JAPOP_xxx), come : 
 * azioni di carrello.
 * azioni di navigazione.
 * altre azioni non classificabili.
 * ...e così via.
