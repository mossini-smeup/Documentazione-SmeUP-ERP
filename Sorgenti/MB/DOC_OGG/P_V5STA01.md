## Ripresa dei dati
Per ripresa dei dati si intende l'attività di estrazione, ai fini statistici, dei dati dagli archivi transazionali e di popolamento del file V5STAT0F.
Gli archivi transazionali sono i file che vengono gestiti dalle transazioni giornaliere, dove con transazione s'intende qualsiasi registrazione eseguita (inserimento documenti, movimenti, registrazioni contabili e quant'altro).

La prima operazione da fare per procedere alla consultazione delle statistiche è la ripresa dei dati. Ci sono vari modi per fare questo tipo di operazione.


### Ripresa batch
Questo tipo di ripresa  è un'attività manuale, che viene eseguita dall'utente qualora questo voglia aggiornare il file delle statistiche in modo estemporaneo. Può essere raggiunta dalla scheda base del modulo V5STAT, attraverso il tab "Menù del modulo", rappresentato in figura : 
![V5STAT_001](http://localhost:3000/immagini/MBDOC_OGG-P_V5STA01/V5STAT_001.png)
Come si può notare, le azioni di ripresa sono suddivise tra le 2 macrocategorie Ciclo Attivo e Ciclo Passivo, che a loro volta si distinguono in : 
 * Ripresa contabilizzato
 * Ripresa contab. No registrazione
 * Ripresa atteso
 * ecc....

Nel seguito analizzeremo una di queste azioni :  la scrittura di ripresa del contabilizzato.

L'operazione "Scrittura", è un tipo di operazione completo che permette di estrapolare i dati dalla contabilità e dai documenti mettendoli nel file delle statistiche.
Per ogni opzione l'utente può scegliere la modalità di esecuzione : 
![V5STAT_002](http://localhost:3000/immagini/MBDOC_OGG-P_V5STA01/V5STAT_002.png)
Le opzioni come si può vedere dall'immagine sono : 
 * _2_1 (stampa), con la quale viene eseguita semplicemente una stampa dei record che dovrebbero essere aggiornati. Questa modalità da sostanzialmente la possibilità di fare una verifica prima di passare all'effettiva scrittura dei dati sul database.
 * _2_3 (aggiorna base dati), viene eseguito l'aggiornamento del file delle statistiche.

In questo caso, richiamato dalla Ripresa contabilizzato in scrittura, si produrra l'aggiornamento (aggiunta, sostituzione..) dei record della statistica in base ai criteri selezionati.

Gli ulteriori criteri di selezione che definiranno l'estrazione dei dati sono :  le date limite (finale ed iniziale) e il metodo di ripresa.

I tipi di scrittura si distinguono in : 
![V5STAT_003](http://localhost:3000/immagini/MBDOC_OGG-P_V5STA01/V5STAT_003.png)
 * _2_A Globale (no filtri) :  elimina tutti i record del V5STAT, nell'intervallo impostato dalle date, e li ricrea prendendoli dalle registrazioni contabili. No filtri, in quanto non considera eventuali filtri impostati nelle parzializzazioni.
 * _2_B Normale :  è simile al criterio precedente, in quanto estrae solo i dati relativi all'intervallo scelto, ma considera anche i filtri se impostati. Cancella sul V5STAT solo i dati corrispondenti a quelli trovati nell'attuale estrazione.
 * _2_C Solo mancanti :  aggiunge in V5STAT tutti i documenti mancanti non estratti prima, senza aggiornare i preesistenti.

L'impostazione dei filtri (F13), consente di impostare delle parzializzazioni su tutti i campi del file di riferimento. In questo caso si tratta del file delle registrazioni contabili.
![V5STAT_005](http://localhost:3000/immagini/MBDOC_OGG-P_V5STA01/V5STAT_005.png)
Per quanto riguarda l'utilizzo specifico dei filtri in generale si rimanda alla documentazione relativa (cfr. Scheda oggetto filtro Q3).

### Ripresa come azioni di flusso
Questo tipo di ripresa avviene direttamente alla registrazione del documento attraverso l'inserimento di un passo di flusso che gestisce il collegamento automatico dei documenti con il modulo V5STAT, per esempio, una volta contabilizzata una fattura c'è la possibilità di aggiornare automaticamente, grazie a questo passo del flusso aggiuntivo, anche il modulo delle statistiche.
Questo permette di avere sempre una situazione aggiornata.

### Ripresa schedulata
Vi è la possibilità di schedulare (programmare) una ripresa periodica, ad esempio ogni notte. Questo per mantenere aggiornati i dati al giorno precedente.
