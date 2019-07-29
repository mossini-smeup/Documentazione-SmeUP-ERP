# OBIETTIVI

Adeguare le partite in valuta al cambio di fine esercizio.

# PREREQUISITI

Utilizzo di un tipo registrazione che abbia impostato : 
 * un tipo registrazione con modello 05;
 * una causale di oscillazione cambio manuale;
 * un tipo rata che abbia nel gruppo flag il flag 15 valorizzato ad "1".

 :  : DEC T(ST) K(C5D&AZ)
 :  : DEC T(ST) K(C5V&AZ)
 :  : DEC T(ST) K(C5E&AZ)
 :  : DEC T(ST) K(B£Y)

Due conti (o anche uno solo) per la rilevazione dei costi/ricavi economici.

E' consigliabile utilizzare un tipo registrazione e conti differenti rispetto a quelli utilizzati per le rilevazioni in corso d'esercizio.

# METODI DI APPLICAZIONE

Esistono due modalità di applicazione delle differenze cambio. La scelta fra le due è definita tramite il campo della tabella C57 "metodo oscillazione". Queste le peculiarità di ciascuna : 

* Campo "metodo oscillazione" della tabella C57 a blank :  "Storico"
** Le oscillazioni di fine esercizio vengono rilevate ed immediatamente stornate al giorno successivo. In questo modo risultano rilevanti per la redazione del bilancio, ma subito annullate per effetto dello storno nel nuovo esercizio.
** Le oscillazioni sugli incassi/pagamenti in corso d'esercizio vengono sempre applicate rispetto al cambio storico delle partite, non tenendo conto degli adeguamenti degli esercizi precedenti.
** Sulla base delle due precedenti affermazioni è necessario considerare che i conti in gioco per la rilevazione delle differenza cambio (tutti confluenti nella medesima linea di riclassifica CEE D13), possono avere nella loro sommatoria un saldo corretto, ma non nella loro composizione. Per tale motivo sfruttando anche la scheda messa a disposizione nel modulo bilanci, sarà necessario effettuare delle rettifiche manuali (direttamente sui saldi totali).
* Campo "metodo oscillazione" della tabella C57 ad '1' :  "Adeguato"
** Le oscillazioni di fine esercizio vengono rilevate e mantenute.
** Le oscillazioni sugli incassi/pagamenti in corso vengono sempre applicate rispetto al cambio adeguato delle partite, alla fine dell'esercizio n-1.
** Non è rilevante quando la registrazione di fine esercizio n-1 sia già stata effettuata, ma è necessario che sia stato inserito il cambio di fine esercizio n-1 (prerequisito senza il quale non è possibile completare le registrazioni dell'esercizio n, se riferite a partite di esercizi precedenti).
** Con questo metodo non è necessario far alcuna rettifica manuale, ne a fine esercizio ne in corso d'esercizio.
** NOTA BENE :  per effetto di questo metodo, se una partita viene chiusa nell'esercizio n fin tanto che non viene effettuata la rilevazione di fine esercizio n-1, la partita sarà chiusa in valuta, ma aperta in valuta di conto (per l'importo dell'oscillazione di fine esercizio n-1).
** NOTA BENE 2 :  sempre per effetto di questo metodo, alla scrittura delle registrazione di fine esercizio n-1, il pgm lancerà anche il ricalcolo nell'esercizio n di tutte le oscillazioni riferite a partite aperte alla fine dell'esercizio n-1. Questo al fine di garantire la perfetta quadratura dei centesimi. Se questa operazione non andasse a buone fine verrebbe segnalato nel log di stampa.
** NOTA BENE 3 :  E' possibile passare da un metodo all'altro solo a partire dalla data inizio di un esercizio e solo dopo che l'esercizio precedente sarà stato chiuso. Sarà necessario riconfermare tutte le registrazioni contenenti oscillazioni cambio già registrate nell'esercizio a partire dal quale si attiva il nuovo metodo.

Qualunque sia il metodo di rilevazione delle oscillazioni si ricorda che il controllo del riallineamento civilistico/fiscale è possibile attraverso una specifica scheda posta nel menù dei bilanci.

Come nota aggiuntiva si riporta che il programma rileva le righe di differenza cambio in base al campo "Livello dettaglio" indicato nell'F17 :  di default è per rata, ma può essere opportuno adeguarlo rispetto alla scelta fatta nel campo C51 "oscillazioni" (dove è possibile specificare il livello di dettaglio delle righe di oscillazione in corso d'anno).

 :  : DEC T(TA) P(C57) K(*)
 :  : DEC T(TA) P(C51) K(*)


