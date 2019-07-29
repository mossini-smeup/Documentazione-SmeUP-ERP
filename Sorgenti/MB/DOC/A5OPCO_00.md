E' possibile collegare la gestione cespiti alla contabilità, non solo per importare da questa i dati inerenti acquisto e vendita di cespiti, ma anche per alimentarla con registrazioni che sono la diretta conseguenza della gestione cespiti stessa (movimenti di ammortamento/fondo, plusvalenze, minusvalenze, ecc...).

Un set'n'play guida alla compilazione dei parametri per ottenere automaticamente queste registrazioni, fermo restando che questa modalità di operare non è obbligatoria, ma si può rivelare utile e/o comoda (es. :  in una realtà composta da più aziende e con numerose categorie fiscali).
Di solito, infatti, chi ha un'azienda sola e poche categorie fiscali, preferisce non effettuare questo tipo di collegamento, inserendo manualmente a fine esercizio i giroconti fondo/costo (derivando gli importi dai totali per categoria del libro cespiti), come pure le scritture che scaturiscono da una vendita/alienazione di un cespite.

Per avviare il set'n'play atto alla parametrizzazione di queste funzioni, si utilizza l'oggetto Azienda con funzione >W e metodo >F, cui fa seguito la richiesta del tipo di registrazione da pianificare :  si possono scegliere i tipi di movimenti che il programma genera automaticamente, essendo movimenti di capitale di immissione manuale o importati con apposita funzione.
Una volta selezionato il tipo di movimento, verranno richiesti : 

- Tipo registrazione
- Causale registrazione
- Conto Dare
- Conto Avere


La funzione "_2_Generazione movimenti contabili", richiamabile dal menu di gestione cespiti, consente di avviare un programma batch che, previa parzializzazioni e impostazioni, genererà movimenti contabili secondo le regole stabilite in precedenza.
Tale operazione è ripetibile ogni qualvolta lo si richieda, ricordando di annullare i movimenti eventualmente generati precedentemente (non viene eseguita alcuna verifica sull'esistenza o meno di questi movimenti sui conti interessati), a meno che non siano già stati stampati definitivamente sul giornale di contabilità del mese di registrazione.
Per questa ragione, si consiglia l'utilizzo di causali autostornanti per la generazione di questi movimenti.

Per poter utilizzare tale funzionalità, risulta necessaria l'autorizzazione alla classe A5MO06.

 :  : DEC T(TA) P(B£P) K(A5MO06)
 :  : INI  Richiamo gestione autorizzazioni
 :  : CMD CALL B£AUA0G PARM('A5MO06')
 :  : FIN

