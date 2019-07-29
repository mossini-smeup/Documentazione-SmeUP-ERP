# Obiettivo
Permettere di proteggere il richiamo di un servizio oppure di una sua funzione.

# Effetto
Al richiamo di una qualsiasi funzione, il programma controlla l'autorizzazione utilizzando la classe LO.SER. Se mancano le autorizzazioni viene emesso un messaggio.
# Come funziona

## Dove definisco i servizi da proteggere
Di norma ogni servizio è ammesso per tutti gli utenti.
Se si vuole proteggere un servizio si deve definire il suo livello nello SCRIPT B£AUTO_SER in SCP_SET.
E' possibile assegnare un livello di autorizzazione generico per il servizio oppure specificare un livello per una sua funzione.
Sono gestiti i seguenti TAG : 
* SER = Servizio
** Nam = Nome del servizio
** Aut = Livello di autorizzazione
* FEM = Funzione.Metodo
** Nam = Nome della funzione.metodo
** Aut = Livello di autorizzazione

## Dove posso comprendere l'effetto
Accedere al modulo B£AUTO (autorizzazioni). E' presente una opzione specifica "Protezione servizi"

# Note particolare
1. Per questione di performance le condizioni vengono caricate solo all'ingresso quindi eventuali modifiche vengono recepite solo al prossimo collegamento
