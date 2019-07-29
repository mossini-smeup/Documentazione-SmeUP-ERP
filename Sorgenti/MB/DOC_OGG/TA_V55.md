# V55 - Par. accantonamento/spedizione
 :  : DEC T(ST) K(V55)
## OBIETTIVO
Definisce le modalità con cui si esegue, per ogni tipo documento, l'accantonamento delle quantità.
## CONTENUTO DEI CAMPI
 :  : FLD T$ELEM **Codice**
È un tipo documento (settore V5D).
 :  : FLD T$DESC **Descrizione**
 :  : FLD T$V55A **Modo accantonamento**

 :  : FLD T$V55B **Tipo documento movimentazione**
È un elemento della tabella GMO, che guida la costruzione delle righe di accantonamento. In particolare, i requisiti necessari sono tipo origine DO e tipo riga impostato, che sarà assunto dalle righe di accantonamento.
Il numeratore delle testate non è significativo,in quanto verranno generate delle righe di richiesta di movimentazione senza testate.
A questo scopo si dovrà impostare, nella tabella generale di magazzino GM1, il numeratore dell'identificativo "riga di movimentazione".
 :  : FLD T$V55C **Tipo giacenza**
È un elemento della tabella GMQ, che definisce le chiavi significative per l'accantonamento.
_9_Esempio :  se si vuole accantonare per lotto, si imposta un tipo giacenza avente come unico codice il lotto, oppure, se si desidera accantonare per lotto/ubicazione, verrà impostato un tipo giacenza contenente questi due codici.
Se si vuole accantonare unicamente per articolo, si dovrà impostare un tipo giacenza senza chiavi.
La gestione dell'accantonamento richiederà, di conseguenza, gli oggetti che sono stati impostati in questo modo.
 :  : FLD T$V55D **Sottosettore Attività**
Con l'elemento (T$V55E) viene individuato l'elemento della tabella V5G usato nelle attività connesse all'accantonamento (ad esempio, dopo la preparazione del packing list, viene eseguita la relativa attività, se impostata.)
 :  : FLD T$V55E.T$V55D **Attività (elemento)**
 :  : FLD T$V55F **Suffisso programma aggiustamento flusso**
Se impostato, prima di eseguire l'attività definita in precedenza, viene eseguito il programma 'GMPK01F_x', dove x indica
il carattere impostato in questa tabella.
_9_Esempio :  questo programma può variare l'attività da eseguire, in funzione del modello di documento che si sta trattando.
 :  : FLD T$V55G **Suffisso programma assegnazione Trim-Vg**
Se impostato, prima di eseguire l'assegnazione della riga, viene eseguito il programma 'V5AT15R_x', dove x indica il carattere impostato in questa tabella.
_9_Esempio :  questo programma può variare la riga di R.M. creata.
 :  : FLD T$V55H **No Lancio Assegnazione**
Se impostato, inibisce l'assegnazione automatica delle righe in fase di creazione R.M.
