# Azioni su documenti fatturabili

## Generalità
Può essere necessario a volte agire sui documenti in attesa di fattura (sia fatture attive che documenti di attesa fattura fornitori) per sospendere (o in seguito riattivare) la loro possibilità di essere fatturati.

La funzione che di seguito sarà descritta serve a questo scopo.

## Formato richiesta
Il formato di richiesta è il seguente : 

![V5_22_01](http://localhost:3000/immagini/MBDOC_OGG-P_V5DO21I/V5_22_01.png)
Le opzioni permettono di scegliere se si vuole agire su documenti di Clienti o Fornitori e relativi a Fatture o Note di credito.

Inoltre si deve impostare lo stato (di fatturazione) del documento, lo schema di visualizzazione e l'ente (mettere "*" se si vogliono vedere i documenti di tutti gli enti).

## Lista documenti
Fatte le opportune selezioni con INVIO si ottiene la lista dei documenti su cui si vuole agire, le opzioni possibili sono presentate in figura : 

![V5_22_02](http://localhost:3000/immagini/MBDOC_OGG-P_V5DO21I/V5_22_02.png)
L'utilizzo è intuitivo, una menzione particolare meritano le opzioni di modifica dello stato con cui si può rendere un documento non fatturabile oppure bloccarlo per il momento.

_2_Nota bene; se si è bloccato un documento sarà necessario ricordarsi che in seguito questo dovrà essere sbloccato intervenendo allo stesso modo ed inserendo nel formato richiesta il flag di blocco utilizzato.

## Gestione flag fatturazione di riga
Se si vuole intervenire su una riga singola di un documento, ad esempio per renderla non fatturabile, allora si deve intervenire sul "Flag" di fatturazione della riga stessa usando l'opzione FR, il cui comportamento è spiegato nel documento sulla stampa interattiva delle fatture (cfr. P_V5FA02 - Stampa Interattiva Fatture).
