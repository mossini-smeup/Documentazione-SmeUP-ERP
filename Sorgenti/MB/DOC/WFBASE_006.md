# Azioni associate in B£S
  :  : DEC T(ST) K(B£SWF)
# Classi di autorizzazione

## Su ordini di workflow
Mediante la classe WFORTE è possibile specificare le autorizzazioni sugli ordini di workflow, ovvero la possibilità di creare nuovi workflow di un certo tipo oppure di gestirli da utente master.
  :  : DEC T(TA) P(B£P) K(WFORTE) I( Apertura/gestione workflow >)

## Su schede del modulo
Viene utilizzata la classe standard LO.EXD per accendere/spegnere determinate sottoschede per gli utenti. Sono gestiti, oltre allo standard 05 come default su tutte le schede, i seguenti valori.
Con funzione WFUTEN, per la scheda principale del workflow : 
 * 19 per accendere gli "Impegni attivi globali";
 * 29 per accendere gli "Impegni assegnabili".
Con funzione F1_BASE, per le sottoschede della scheda di un ordine di workflow : 
 * 19 per accendere gli "Impegni attivi globali";
 * 29 per accendere gli "Impegni assegnabili".
Con funzione F2_BASE, per le sottoschede della scheda dell'impegno di workflow : 
 * 19 per accendere gli "Impegni attivi globali";
 * 29 per accendere gli "Impegni assegnabili".
Si ricorda che il default per tutte le schede dovrebbe essere 09/19/29/39/49/59/69/79/89/99, quindi di base tutte le schede sono abilitate.


## Su transizioni
E' possibile utilizzare le autorizzazioni per specificare gli insiemi di utenti che possono assegnare / eseguire impegni di workflow, in alternativa agli altri metodi di definizione di tali insiemi tramite gruppi / liste utente.

### Autorizzazioni generiche
E' possibile riciclare autorizzazioni definite per altri contesti per indicare chi può eseguire una transizione. Basta indicare nello script, nella parte relativa alla transizione, la classe, la funzione e il valore da controllare.
Per classi di autorizzazione con valori del tipo SI/NO (quindi in cui il valore non è significativo, avendo diverse risposte del tipo (SI/SI/SI...), è possibile specificare nel campo valore la posizione (riga) da controllare. Ad esempio :  POS02 controllerà che l'opzione della seconda riga abbia valore SI.

### Autorizzazioni specifiche
Classi specifiche (suggerimento di nomenclatura :  WF.nomeprocesso) compilate nel seguente modo : 

- Tabella significati :  WF.
- Riga 01 :  T1 (assegnazione).
- Riga 02 :  T2 (esecuzione).
- Tipo/param. utente :  TAB£U.
- Tipo/param. funzione :  F5nomeprocesso.






