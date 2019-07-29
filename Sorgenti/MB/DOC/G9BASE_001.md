# Fatture verso fornitori

Sono : 
 * Note di debito (fatture) A fornitore = note di credito DA fornitore (flag 19 :  m...q);
 * Note di credito A fornitore  = fatture DA fornitore (flag 19 :  a...e).

L'iter ricalca quello classico del ciclo attivo : 
 * Stampa fattura da emettere verso il fornitore :  è un programma specifico, che individua i documenti fornitore da fatturare e per ognuno chiama la stampa fattura (stesso programma usato per il ciclo attivo).
Il numeratore delle fatture è come sempre impostato in V5ADP.
 * Contabilizzazione fattura :  avviene dallo stesso programma del ciclo attivo. Impostando opportunamente l'autorizzazione V5FA05 è possibile abilitare il lancio della contabilizzazione passiva.
Nel caso di ciclo passivo il numero di protocollo non corrisponde al numero di fattura, ma viene ripreso dal numeratore indicato sulla registrazione contabile associata :  è così possibile tenere nello stesso registro fatture ricevute DA fornitori e inviate A fornitori.

# Impostazione

Passi minimi : 
 * Impostare in tabella G91 il tipo ente fornitore (FOR).
 * Verificare che il programma di stampa fatture sia compatibile anche con le fatture di ciclo passivo.
 * Impostare le autorizzazioni V5FA05 per chi deve lanciare la contabilizzazione di fatture passive.
