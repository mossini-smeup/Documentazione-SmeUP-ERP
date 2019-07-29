# P5H - Azioni MFP
 :  : DEC T(ST) K(P5H)
## OBIETTIVI
Contiene i parametri che guidano le azioni sui contenitori di produzione MFP
## SOTTOSETTORI
Non gestiti
## CONTENUTO DEI CAMPI
 :  : FLD T$P5HA __Tipo azione__
Definisce il tipo di azione eseguita sui contenitori, cfr Tst H35 per documentazione.
- [Gestione movimentazione MFP](Sorgenti/MB/DOC_OGG/P_TSTH35)
 :  : FLD T$P5HB __Causale origine__
Definisce la causale di movimentazione relativa al contenitore origine
 :  : FLD T$P5HC __Causale destinazionee__
Definisce la causale di movimentazione relativa al contenitore destinazione
 :  : FLD T$P5HD __Causale avanzamento__
Definisce la causale di attività relativa all'avanzamento di tutte la fasi comprese tra l'ubicazione origine e
l'ubicazione destinazione
 :  : FLD T$P5HE __Suff.pgm. exit__
E' il suffisso X del programma B£H35M_X. Viene eseguito prima di ogni aggiornamento eseguito
sugli oggetti coinvolti in una azione MFP :  E1(Movimenti), E2(Attività), CZ(Colli), OR(Ordini),
 :  : FLD T$P5HF __Azione su scarto__
Definisce se l'azione agisce su contenitori per buoni o scarti
 :  : FLD T$P5HG __Causale avanzamento automatico__
Definisce la causale di attività relativa all'avanzamento di tutte la fasi automatiche. Sono tutte le dichiarazioni
comprese tra la fase origine e la fase in dichiarazione(esclusa)
In questo modo è possibile diversificare le attività sulla fase dichiarata dalle attività che hanno portato il
contenitore alla fase in dichiarazione.
Se non presente usa la Causale avanzamento
 :  : FLD T$P5HH __Tipo non conformità__
E' il tipo di non conformità generata in caso di scarti.
 :  : FLD T$P5HI __Quantità scarto NON conformità__
Definisce in quale quantità delle NON conformità viene memorizzata la quantità scarto
I valori vanno da 1 a 9 per la quantità da N§QT01 a N§QT09 e 0 per la quantità N§QT10
 :  : FLD T$P5HK __Consumo quantità pianificata__
Definisce la modalità di consumo della quantità pianificata nella prima lavorazione(1°fase).
Se non attivato significa che se si riempie un nuovo contenitore di buoni, indipendentemente dalla sua quantità,
viene consumato un intero contenitore pianficato (i contentitori pianificati sono dei fittizzi).
Se attivato con "1" significa che se si riempie un nuovo contenitore la sua quantità consuma la quantità dei contenitori pianificati. E' attivabile sia per contenitori di buoni che di scarti. Come priorità di consumo prima
sono rilevati i contenitori mai movimentiati e successivamente gli altri.
Se attivato con "2" significa che se si riempie anche un contenitore esistente la sua quantità in ecceso rispetto alla pianificata consuma la quantità dei contenitori pianificati. L'ordine di prelievo segue la stessa priorità indicata
nella modalità "1"
