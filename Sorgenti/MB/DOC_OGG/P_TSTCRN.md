# GESTIONE NUMERATORI
# Introduzione
Tutte le azioni che si possono eseguire sui numeratori sono eseguite nella routine £CRN, che svolge le seguenti
funzioni.
# Funzioni
## Lettura
Restituisce il valore attuale del numeratore specificato.
## Incremento
Restituisce il valore incrementato
Se sulla tabella è attiva la gestione del COMMIT, la tabella stessa viene bloccata e dovrà essere sbloccato da una
successiva chiamata dell funzioni di COMMIT.
## Decremento
Decrementa il contenuto della tabella numeratore se il contenuto attuale è uguale a quello del valore di ingresso.
Si usa questa funzione ogni volta che si rinuncia (Es. F12) all'uso del numeratore proposto. Se un altro utente ha già
usato il successivo resterà un vuoto nella sequenza.
## Commit
Toglie il flag di numeratore bloccato da altro utente
## Verifica
Se si passa un valore immesso dall'utente il programma controlla la congruenza secondo le regole definite nella
tabella. Si eseguono i seguenti controlli : 
-    La parte iniziale (prefisso/separatori ecc) deve essere identica
-    La parte del progressivo fino alla lunghezza massima, deve essere non bianca e può assumere qualsiasi valore
(numero o lettera)
## Note tecniche
Per i dettagli tecnici si veda la documentazione della routine.
