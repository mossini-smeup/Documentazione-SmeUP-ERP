# Scopo
 * Interfaccia le funzioni di entrata materiali e lanci di produzione con i controlli e collaudi eseguiti in Azienda
 * Gestisce le procedure e  le modalità di controllo definite (cicli di collaudo) integrando le informazioni di gestione con i dati propri del Sistema Qualità
 * Gestione (stampa e/o visualizzazione ) del Benestare di Collaudo, delle BEM (bolle entrata merce), e delle targhe identificative dei lotti/contenitori
 * Gestione della accettazione e del rifiuto dei lotti in funzione dei piani di campionamento definito e delle regole di commutazione stabilite
 * Registrazione ed archiviazione delle misure di controllo effettuate sul lotto/campioni analizzati
 * Dichiarazione esito del controllo e collegamento diretto alla rilevazione di non conformità
 * Stampa i Certificati di Qualità'


# Definizioni
 * _2_Lotto, identifica attraverso una sigla l'entrata o la produzione di una quantità' di articolo, ai fini della tracciabilità degli eventi nel Sistema di Qualità
 * _2_Tipo Lotto, identifica la fonte e la natura del lotto
 * _2_Classe  funzionale Articolo, identifica attraverso una sigla la criticità di missione della parte. Alla classe funzionale sono collegabili le modalità di campionamento del lotto
 * _2_Classe  Abilitazione, identifica attraverso una sigla la abilitazione dell' ente di riferimento (fornitore, reparto interno). Alla classe di abilitazione sono collegabili le modalità di campionamento del lotto
 * _2_Numero e Data BEM, sono i riferimenti interni alla documentazione di entrata di un lotto
 * _2_Lotto Cliente/Fornitore, Certificato di Qualità', Lotto di derivazione, sono i riferimenti esterni del lotto in accettazione
 * _2_Benestare di Collaudo, è la funzione attraverso cui viene sottoposto al controllo/collaudo un lotto, integrando i ciclo di collaudo dell'articolo
 * _2_Dichiarazione di Collaudo, è la fase del benestare di collaudo in cui viene esitato il lotto
 * _2_Esito di collaudo, identifica lo stato del lotto al termine del controllo
 * _2_Quantità' dichiarata, è la quantità' dichiarata dall' ente di riferimento del lotto (fornitore, reparto) al controllo
 * _2_Quantità rilevata, è la quantità riscontrata al controllo

# Tabelle utilizzate dal modulo : 
### CQQ - Classe Funzionale Articolo
identifica il livello di criticità di immissione
 :  : DEC T(ST) K(CQQ)

### DIP - PERSONALE ANAGRAFICA-DIPENDENTI
Codifica le matricole dei dipendenti. Associa ad ogni codice di matricola tutta una serie di informazioni che concorrono a definire lo SKILL del dipendente.
 :  : DEC T(ST) K(DIP)

### *CNTT - CODICI OGGETTI APPLICATIVI
Descrive il tipo di enti che richiedono, gestiscono, evadono,ecc.. la  richiesta di intervento (direzione tecnica, direzione commerciale, ecc..)
 :  : DEC T(ST) K(*CNTT)

### CQV - Classe Abilitazione Ente
identifica il livello di abilitazione di un ente alla fornitura di un lotto
 :  : DEC T(ST) K(CQV)

### CQR - Regole di Commutazione
regolano le modalltà di alleggerimento ed appesantimento dei campionamenti.
Dovrebbero essere definite per ogni Piano e Livello di campionamento utilizzato, utilizzando come sigla la corrispondente sigla di Piano e livello.
 :  : DEC T(ST) K(CQR)

### CQB - Esito Lotto
identifica e classifica gli esiti del collaudo, ne associa il corrispondente  peso di valutazione, determina i collegamenti obbligatori alla rilevazione di misure e/o di non conformità', permette di declassare immediatamente il Piano/livello di campionamento indipendentemente dalle regole di commutazione.
 :  : DEC T(ST) K(CQB)

### CQA - Azioni sul lotto successivo
codifica azioni da controllare/segnalazioni durante il benestare di collaudo sul lotto successivo
 :  : DEC T(ST) K(CQA)

### CRV - Tipo contenitore
codifica i tipi contenitore delle quantità del lotto
 :  : DEC T(ST) K(CRV)

### CQ*PR - Priorità intervento
identifica la priorità del lotto
 :  : DEC T(ST) K(CQ*PR)

# Processo di avviamento ed utilizzo
## Attività iniziale
 * interfacciamento con le diverse movimentazioni aziendali di origine dei lotti
 * classificazione delle tipologie e delle modalità di generazione
 * classificazione delle criticità articoli, abilitazione dei fornitori, regole di commutazione e matrice CQQ/CQV (classe funzionale/classe di abilitazione) per la determinazione delle modalità di campionamento
 * classificazione delle procedure di riferimento
 * inserimento delle tabelle relative al modulo

## Attività periodica
 * gestione del benestare di collaudo ed esito dei lotti

# Gestione dei lotti (flusso informativo delle modalita di campionamento)
![CQ_LOTT_01](http://localhost:3000/immagini/CQLOTT_01/CQ_LOTT_01.png)
# Gestione dei lotti (flusso informativo)
![CQ_LOTT_02](http://localhost:3000/immagini/CQLOTT_01/CQ_LOTT_02.png)