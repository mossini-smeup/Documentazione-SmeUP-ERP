# C5V - Causali contabili
 :  : DEC T(ST) K(C5V)
## OBIETTIVO
Definire le caratteristiche delle causali contabili, che caratterizzano ogni riga di registrazione contabile.
## CONTENUTO DEI CAMPI
 :  : FLD T$DESC **Descrizione**
Contiene la descrizione di questa specifica causale contabile, che verrà proposta con possibilità di modifica sulla riga di registrazione.
 :  : FLD T$C5VA **Segno registrazione**
È un elemento V2/SEGNO. È il segno che viene proposto all'atto dell'immissione delle registrazioni.
Per registrazioni non IVA viene proposto se non è stato impostato il campo corrispondente a livello di conto.
Per registrazioni IVA viene proposto sulla riga dell'ente; sulle contropartite viene invece proposto il valore opposto (scambio tra DARE e AVERE).
 :  : FLD T$C5VB **Segno rate**
È un elemento V2/C5SRA. Definisce se la riga genererà rate di dovuto e di pagato. Viene usato nella generazione delle rate, ed è riportato sulle righe in modo da sfruttarlo, ad esempio, nella generazione di righe automatiche di oscillazione e abbuoni.
 :  : FLD T$C5VC **Tipologia movimento**
È un elemento V2/C5TMO. Definisce la natura della registrazione nell'ambito della classificazione impostata in Sme.up.
Questo dato non ha alcuna funzione applicativa ma solo statistica (es. stampa fatturato)
 :  : FLD T$C5VD **Gestione descrizione supplementare**
Tramite essa è possibile definire la gestione specifica che vuole essere attribuita alla descrizione supplementare.
Può assumere i seguenti valori : 
- "3"=Forza ente + data/n° documento di riferimento
- "2"=Permette la gestione a subfile mantenendo nella descrizione la decodifica della causale.
- "1"=Forzatura ente della testata se riga manuale, forzatura ente di riferimento se riga automatica.
- " "=Normale.
 :  : FLD T$C5VE **Natura transazione intra CEE**
Definisce la natura della transazione dal punto di vista della produzione dei documenti INTRASTAT, dove verrà riportata.
 :  : FLD T$C5VF **Ammesso importo a zero**
È un elemento V2/SI/NO. Se impostato, all'atto dell'inserimento della registrazione viene permesso di lasciare l'importo a zero.
È usato, ad esempio, nella registrazione di fatture in garanzia, nelle quali imponibile, importo e imposta sono obbligatoriamente a zero.
 :  : FLD T$C5VG **Condiz. scelta caus.**
È un elemento TA/C5*CR. Se impostato, definisce il criterio di selezione mediante il quale viene effettuata la ricerca ed il controllo validità sulla causale di riga di una registrazione.
 :  : FLD T$C5VH **Oscillazione Manuale**
È un elemento V2/SI/NO. Se impostato, permette l'omissione dei controlli di Cambio/Valuta sulla riga contabile cui la causale viene associata in modo da poter inserire righe di oscillazione manuali.
 :  : FLD T$C5VI **Tipologia movimento finanziario**
È un elemento V2/C5TMF. Se impostato, la riga di registrazione ha una valenza finanziaria, la cui natura è definita da questo valore, nell'ambito della classificazione impostata in Sme.up.
 :  : FLD T$C5VK **Tipo contatto pagamento**
Se impostato nelle registrazioni di incasso/pagamento sarà possibile includere solamente enti di questa tipologia; in caso contrario sarà possibile indicare manualmente la tipologia di contatto desiderata. Si consiglia, quindi la compilazione di questo campo solo per
causali usate specificamente per incassi/ pagamenti da/verso una tipologia di ente specifico (es. Saldaconto Cliente o Bonifico Fornitore).
 :  : FLD T$C5VL **Tipo pagamento**
Se indicato, nelle registrazioni di incasso/pagamento viene forzato rispetto al tipo pagamento previsto dalla scadenza originale.
E' opportuno che tale dato venga sempre indicato per tutte quelle causali che già nella descrizione identificano la tipologia del pagamento/incasso.
 :  : FLD T$C5VN **Cambio/Val. Rate**
Se impostato a 1, forza nelle registrazioni di incasso/pagamento il cambio
del documento da saldare. In questo caso nella singola riga può essere saldata un'unica scadenza a meno
che tutte le scadenze selezionate abbiano lo stesso cambio.
Se impostato a 2, attiva la gestione multivaluta, cioè la possibilità di saldare rate con valute differenti fra loro e differenti da quella dell'incasso/pagamento.
Si veda inoltre documentazione incassi/pagamenti multivaluta, al capitolo "Abbuoni, Sconti, Oscillazioni e Altri Automatismi" del modulo "Incassi/Pagamenti".
