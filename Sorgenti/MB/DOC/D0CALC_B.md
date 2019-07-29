# Introduzione
L'interrogazione del calcolo visualizzato si basa sugli stessi programmi e criteri dell'esecuzione normale, ma viene elaborato un solo articolo e, invece di generare una stampa, produce una schermata a video.
I parametri di lancio sono perciò i medesimi utilizzati per il calcolo normale :  un capitolo a parte va però aperto per i parametri riguardanti il pgm di stampa, che, in questa modalità, si occupa della costruzione del file work su cui si basa l'interrogazione.

# Modalità di interrogazione
Esistono due modalità di interrogazione :  semplificata e analitica. La determinazione della modalità da utilizzare dipende dalla valorizzazione del parametro relativo al pgm di stampa :  se blank, verrà attivata l'interrogazione semplificata, altrimenti l'analitica.
La differenza consiste nelle opzioni disponibili nell'interrogazione analitica, che, a differenza della semplificata, non si limita a produrre a video ciò che normalmente verrebbe stampato, ma fornisce anche le opzioni CO di ogni singola riga del subfile (cioè di ogni singolo componente) : 
 * _2_CO. La prima opzione mi permette di visualizzare la descrizione del processo che ha portato all'ottenimento del componente e l'elenco dei sottocomponenti utilizzati in esso, con la possibilità di poterne modificare / visualizzare le caratteristiche.
 * _2_AV. Questa opzione (attivata solo se richiesta la memorizzazione dell'avanzamento) non permette di visualizzare l'avanzamento dei costi a livello di ogni singolo componente.
L'interrogazione analitica non ha alcuno svantaggio rispetto alla semplificata, che corrisponde alla versione precedente del pgm di stampa e permette perciò di mantenere intatti gli eventuali pgm di personalizzazione.

A fronte di ciò, sono disponibili due pgm di stampa standard :  D0CA09_00 per la semplificata e D0CA09_01 per l'analitica.

# Personalizzazioni dell'interrogazione in modalità analitica
In seguito alle personalizzazioni attuate ai pgm può nascere l'esigenza di apportare modifiche all'analisi evidenziata dall'opzione CO (es. :  è stata modificata una metodologia di calcolo o si vogliono allineare pgm già esistenti).

Quando è attivata l'interrogazione analitica, la chiamata al pgm di stampa avviene passando una particolare DS (/COPY D0CA09_DS), così composta : 
 * _2_D§09CD. In questo campo deve essere passato il codice del componente che si sta elborando. L'elenco dei codici disponibili si trova nella schiera OGG, che è definita a livello di pgm nel D0C e che permette di  recuperare il codice e il tipo oggetto del componente
 * _2_D§09VA. In questo campo viene passato il valore del componente (nel caso sia numerico deve essere passato sotto forma di un numero lungo 21 con 6 decimali
 * _2_D§09IN. In questa schiera vengono passati i codici delle sottocomponenti utilizzate per la definizione del componente. L'elenco è definito nella schiera TPO del pgm e, come per la schiera OGG, permette la determinazione della descrizione e del tipo oggetto e sottocomponente
 * _2_D§09IV. In questa schiera vengono passati i valori dei sottocomponenti
 * _2_D§09AZ. In questo campo viene passato il codice dell'azione che ha permesso l'ottenimento del sottocomponente. L'elenco delle azioni è definito nella schiera AZI del pgm D0CA09_01, in cui è definito anche il riferimento al codice della schiera COM, attraverso il quale viene recuperato il testo di descrizione del processo dell'azione.
 * _2_D§09AT. Definisce l'attributo di visualizzazione del componente nella visualizzazione
 * _2_D§09LV. E' un campo opzionale che attribuisce un livello al componente
 * _2_D§09DE. Se passato, sostituisce la descrizione del componente definita nella schiera OGG
 * _2_D§09TP. Serve per definire il tipo di informazione che sto scrivendo e può assumere i valori "C"=commento (solo un testo che si vuole visualizzare), "E"=errore (testo di segnalazione) e "T"=totale. Per utilizzare l'interrogazione analitica in un pgm personalizzato, è necessario riempire la suddetta schiera (è comunque consigliabile prendere come spunto uno dei pgm standard), mentre per intervenire su una delle sopracitate schiere si può implementare il pgm D0CAX09 che dà la possibilità di modificare e completare le schiere in qualsivoglia modo.
