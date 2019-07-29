# Gestire le personalizzazioni
Durante il processo di personalizzazione di Sme.up presso un cliente vi sono alcune convenzioni da seguire per far sì che il compito di manutenzione del software non si complichi sempre più con l'andare del tempo. La prima regola da seguire è quella di assegnare dei nomi standard alle librerie sviluppate per il cliente.

| SME_XXX | Libreria del cliente (dove _xxx_ indica il cliente), contentente le ---|
| personalizzazioni. Vengono salvate ogni sera. |
| XPER_xxx | Libreria del cliente (dove _xxx_ indica il cliente), portate in SME.up come ambienti di test. |
| 


La differenza tra queste due librerie è data dal fatto che mentre tutte le  PER_xxx vengono salvate con cadenza giornaliera, della libreria XPER_xxx non viene fatta nessuna copia automatica  di backup (il motivo è che queste librerie possono contenere informazioni che è consigliato non duplicare, ad esempio, i dati del cliente)
Nel caso comune in cui un cliente richieda che un programma si comporti in maniera  significativamente diversa rispetto allo standard, la strada da seguire non è quella di modificare il sorgente di quest'ultimo ma, invece, di implementare un apposito programma chiamato EXIT. I programmi di EXIT sono, infatti, dei programmi che modificano il comportamento del sistema senza intaccarne la generalità, l'estendibilità e che non interferiscono con gli aggiornamenti anche delle sezioni che li riguardano.

# Le exit
Nessun prodotto di gestione aziendale può ritenersi omnicomprensivo e immodificabile :  vi sono spesso specificità che non sono realisticamente riconducibili a funzioni standard. Per superare questo scoglio, sono stati realizzati dei programmi specifici, chiamati _'di exit'_ strutturati in ogni punto in cui si può decidere di estendere o modificare il comportamento del software. In questo modo per implementare comportamenti specifici si scrive nuovo codice personale invece di personalizzare il codice esistente, con i seguenti vantaggi.
Si realizzano piccoli programmi orientati alla soluzione del problema, che non interferiscono con il resto del codice, e diventano, inoltre, una auto documentazione dei comportamenti specifici dell'azienda, accessibile al personale tecnico.
Dato che il richiamo delle exit è comandato in tabella, si può facilmente confrontare il comportamento dell'applicazione in presenza ed assenza della exit stessa.
L'installazione di nuovi rilasci risulta velocizzata :  non bisogna riportare le personalizzazioni sulla nuova versione del codice. È naturalmente nostra cura mantenere inalterata la modalità di richiamo delle exit.
Un esempio è il programma di controlli aggiuntivi all'inserimento e variazione dell'anagrafica articoli, dove si possono eseguire, ad esempio, sia controlli incrociati sia semantici.
 * Uniformità di colloquio tra le varie funzioni, per permetterne la composizione in modo nativo
 * Rappresentazione 'profonda' dei fenomeni aziendali :  se se ne coglie la reale struttura, nuove esigenze possono essere già contemplate, perché sono manifestazioni diverse di uno stesso disegno concettuale.

Dalla tabella tabella BRZ è attivabile un pgm di exit che permette di applicare dei controlli di congruenza aggiuntivi rispetto a quelli previsti a standard. La prima cosa da prendere in considerazione passando al data entry V2 è il fatto che l'exit prevista dalla versione precedente rimane attiva, ma viene deviata su un pgm che supporta una radice ed un'entry differente. Per tale motivo per mantenere l'exit i pgm dovranno essere ridenominati e riadeguati.

 :  : DEC T(ST) P() K(BRZ)
 :  : DEC T(MB) P(BRSRC) K(BRBR23_X)

## PGM di EXIT
 - E' possibile definire dei tracciati personalizzati (generalmente si ha questa necessità se si devono gestire tracciati esteri o completare quelli esistenti). In questo caso la costruzione del file C5RR12TF dovrà essere spostata nel pgm di exit C5RR12T_E. Questo programma viene richiamato se nel tipo pagamento delle rate della pratica è definito un tipo tracciato diverso rispetto a quello standard (RB/AP per natura E, RI per R, HR per B, CF per S).
 - In ogni implementazione, inoltre, sono da determinare i valori  previsti nei parametri dalla tabella CCO, ma visto che ognuno si calcola tali valori secondo criteri specifici, tutti utilizzano le exit previste nella ripresa e nel data entry per  determinare tale valore.

Tabelle Personalizzazione : 
 :  : DEC T(TA) P(B£1) K(*)
 :  : DEC T(TA) P(CQ1) K(*)
 :  : DEC T(TA) P(CR1) K(*)
