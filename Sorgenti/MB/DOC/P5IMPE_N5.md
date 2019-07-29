# Struttura conto lavoro pieno
 * **Riga d'ordine**, nel tipo riga ci deve essere un elemento V5L che caratterizza la riga di conto lavoro e associa un tipo impegno P5I. Si devono creare dei flussi di inserimento, modifica, annullamento per gli impegni di lavorazione. Programma P5FIMT con le seguenti funzione/metodo : 
 ** __inserimento__, CRE / NUOV
 ** __modifica__, CRE / NETT
 ** __annullamento__, CAN
 * **Spedizione in C/Lavoro**, la gestione attuale esegue un bilancio (non datato) sul fornitore in base al gruppo fonti impostato nell'elemento di V5L (cfr paragrafo Spedizioni in conto lavorazione)
 * **Movimentazioni materiali al/dal terzista**, influenzano direttamente il fabbisongo del terzista stesso (ogni proposta di spedizione tiene conto dell'ultima transazione fatta, compresa quella in attesa spedizione :  bisogna impostare le fonti in modo opportuno :  la bolla come carico per il terzista)
 * **Rientro assieme a fronte di ordine**, è un normale ricevimento da ordine, il collegamento a magazzino scarica i componenti dal terzista e carica l'assieme in azienda. L'assieme è in attesa entrata fino al collegamento mentre i componenti sono impegnati.
 * **Spedizione per rilavorazione**, si imposta un tipo impegno materiali che impegna se stesso (OJ nel tipo impegno)
 * **Ricevimento assieme extraordine**, si imposta un tipo impegno materiali che scarica senza aver prima costruito gli impegni. è importante definire correttamente nella P5I il modo di scarico dei materiali : 
 ** **IM**, se scarico automatico di tutti i componenti impegnati (se ricevimento a fronte di ordine)
 ** **DO**, se scarico secondo distinta senza creazione preventiva degli impegni (se ricevimento a NON fronte di ordine)
 * **Recuperi (sfridi, ....)**, sono componenti a coefficiente di impiego negativo. Vengono caricati presso il terzista : 
 ** come recupero, se c'è la causale in P5I
 ** come scarico negativo se manca

# Spedizioni in conto lavorazione
Bisogna impostare un flusso di entrata/uscita con : 
 * nella V5G obbligatori
 ** tipo documento partenza e arrivo
 ** modello documento arrivo :  questo perchè è il primo modello che si assume nella catena delle priorità (se assente viene segnalato in dettaglio come errore bloccante), se si impostasse un documento con questo campo vuoto il programma tenterebbe di derivare il modello di destinazione (che è la bolla entrata merci) dal documento origine, il tipo riga è quello assunto del modello
 * primo passo, V5AT11E (passo di richiesta ente).
 ** la funzione è NEWDOC
 ** il metodo è NOB (se si impostassero altri metodi sarebbe lo stesso perchè non vengono sentiti dal programma successivo) il numero documento non serve infatti
 * passo di estrazione, V5AT40L, con le seguenti posizioni in £FUNPS : 
 ** "1"
 *** blank = presenta solo gli impegni residui
 *** "X" presenta tutti gli impegni, anche quelli coperti
 ** "2"
 *** blank = non imposta la qtà residua da spedire
 *** "X" imposta la qtà residua da spedire
 ** "3", gruppo fonti per analisi disponibilità articolo (default "**")
