# Modalità trattamento fase in analisi disponibilità
La fase __non__ è una selezione facoltativa, come l'ente, la risorsa, la commessa, ma definisce un oggetto specifico :  l'articolo alla fase 10 e alla fase 20 sono due oggetti diversi, idem per l'articolo alla fase blank.

La fase __non__ viene trattata in : 
 * scorta minima
 * MPS
 * ordine produzione (esclusa in automatico)
 * impegni pianificati

Quindi quando si richiamano queste fonti con la fase la si tratta come blank.

La fase viene trattata in : 
 * impegni in corso :  è una chiave dell'archivio quindi si aggiunge in modo naturale al magazzino e all'articolo
 * richieste di acquisto :  se la fase ricevuta è diversa da quella del record la riga viene esclusa (la fase blank non fa eccezione)
 * righe V5 : 
 ** se la fase è significativa (Flag 13 diverso da blank) è come per le richieste di acquisto
 ** se la fase non è significativa (Flag 13 = blank), la riga viene esclusa quando viene impostata una fase diversa da blank :  viuol dire che la riga è della fase blank e quindi non va trattata se si vuole una fase specifica
 * giacenza : 
 ** se il tipo giacenza è per fase (ha tra i suoi codici "OP") si comporta come per le richieste di acquisto
 ** se invece non c'è la fase, la qtà viene escluisa se si è impostata una fase diversa da blank :  in pratica è lo stesso comportamento delle righe V5, la fase è significativa se è una delle key del tipo giacenza.

Normalmente l'analisi disponibilità per fase è trattata nella funzione di spedizione a terzisti, in cui si bilanciano gli impegni (__con__ fase) con la disponibilità presso i terzisti. Se non si considerasse la fase, l'oridne dell'assieme potrebbe dare disponibilità del componente (in caso di C/Lavoro di fase abbiamo stesso codice articolo e fasi diverse).
