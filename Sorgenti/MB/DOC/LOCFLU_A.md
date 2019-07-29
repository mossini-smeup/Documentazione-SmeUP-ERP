# Introduzione
Il componente flusso si occupa dell'esecuzione di una sequanza di azioni.

## Cosa si intente per azione
Con azione si intende una F o A.

## Come opera il componente
Il componente risolve le F del tipo
 :  : PAR F(01)
F(FLU;SERVIZIO_XX;METODO_YY) ....


Richiama l'AS400 e ottiene una sequenza di n azioni da compiere.

Ottenuta la sequenza inizia l'esecuzioe partendo dalla prima e procedendo fino ad aver esaurito tutte le azioni.

Le modalità di esecuzione del flusso, definita nel parametro di setup Type, sono 2 : 

STATIC :  l'XML del flusso contiene tutta la lista di funzioni del flusso, che vengono tutte eseguite fino in fondo. Il flusso
        termina quando tutte le funzioni della lista sono state eseguite. In questo caso, l'unico modo per fermare il flusso
        prima del suo termine naturale è quello di abilitare la conferma passo-passo con il parametro ShowStep="Yes" e
        rispondere NO alla richiesta di continuazione che viene visualizzata prima dell'esecusione di ogni passo.

DYNAMIC :  l'XML del flusso non contiene la lista di funzioni da eseguire ma contiene nel campo NextStepFun la funzione da richiamare
       sul server per avere la funzione o la lista di funzioni da eseguire come prossimo passo del flusso. Quando le funzioni
       tornate sono state eseguite viene nuovamente richiamato il servizio per avere le funzioni successive e così via. Il
       flusso si considera terminato quando il servizio che da le funzioni successive risponde con una lista vuota.



## Come opera un flusso
Un flusso può operare in varie modalità : 

- BATCH :  non c'è nessuna interazione con l'utente. In questa modalità eventuali errori non risultano bloccanti. Eventuali azioni presenti nel flusso che hanno grafica verranno eseguite ma il flusso non attenderà la chiusura dell'azione.
- MSG :  il flusso si blocca solo su eventuali messaggi
- ERR :  il flusso si blocca solo sui messaggi di errore
- INT :  le azioni vengono eseguite una dopo l'altra senza possibilità di interrompere il flusso.
- STEP :  dopo ogni azione viene chiesta conferma per passare all'esecuzione successiva.


## Stato di un flusso
Per accedere allo stato di un flusso si può utilizzare il servizio JA_00_21 :  restituisce una matrice c


