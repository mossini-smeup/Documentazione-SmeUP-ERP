# Oggettizzazione

A partire dal rilascio V2R3 è stata cambiata l'oggettizzazione degli oggetti DQ per garantirne le proprietà minime come oggetti Sme.up e standardizzarne i comportamenti : 
 * Prima :  il codice dell'oggetto era dato dal campo G§ACO1, ovvero una sottochiave del record CQDOMA. Questo non garantisce l'univocità degli oggetti, infatti si possono avere più documenti con lo stesso codice 1 (che differiscono ad esempio per il codice 2 o il livello di modifica).
 * Ora :  il codice dell'oggetto è il campo G§NUDO, che svolge le funzioni di numeratore (e quindi IDOJ) del file CQDOMA0F.

Il parametro non è cambiato, è sempre il tipo documento.

## G§NUDO
Il vincolo che il campo G§NUDO sia IDOJ del file CQDOMA0F è debole, ovvero non è forzato *UNIQUE sul file.
Questo per garantire la compatibilità con il passato :  il numeratore è calcolato dalla tabella CRNDO, nome elemento=tipo documento.
Due documenti di tipo diverso, quindi, possono fare riferimento a due elementi diversi di tabella CRN :  tipicamente gli elementi della tabella CRNDO sono compilati con il tipo documento come prefisso, ma quando non è così è possibile avere due documenti con lo stesso numeratore.
Per aggirare questo possibile problema nelle future installazioni ed evitare che l'univocità dipenda dal fatto che sia compilata bene la tabella CRNDO è stata aggiunta la possibilità di specificare in tabella CR1 un unico elemento della CRNDO da usare per generare i numeratori di TUTTI i documenti, di qualsiasi tipo.

# Stati
La gestione "classica" dei DQ prevede il settore CQ2 come "raccoglitore" di stati per le decodifiche, e una serie di sottosettori (CQ2AP, CQ2EM, CQ2RI) per specificare quali stati possono essere scelti per un documento in un determinato momento (sottoinsiemi del CQ2).
La nuova gestione prevede l'utilizzo del workflow, quindi sarà sufficiente compilare il settore CQ2 con tutti gli stati possibili, lasciando gestire al motore di workflow gli avanzamenti.

# /COPY e strumenti disponibili
È stata creata l'interfaccia £IDQ per le letture di documenti secondo le nuove modalità (codice = G§NUDO).
Sono stati inoltre rivisti ed ampliati gli OAV, sempre secondo le nuove modalità :  dato un documento è ora possibile, come tutti gli altri oggetti di Sme.up, reperirne in maniera univoca tutti gli attributi.
Il nuovo deviatore standard B£G99D tratta le operazioni di gestione (modifica, copia, cancellazione, interrogazione).

Rimangono una serie di /COPY che procedono secondo le vecchie modalità (codice = G§ACO1), con i limiti del caso :  £IFD, £CQ7...
