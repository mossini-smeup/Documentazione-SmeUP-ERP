# Scopo
 * Gestione della FMEA per la pianificazione di progetti o processi di particolare importanza
 * Gestione della FMEA per lo sviluppo di progetti  o processi di particolare importanza

# Definizioni
 * _2_Leader, identifica il il leader del team di studio che esegue la FMEA sul progetto
 * _2_'X' Partecipante, identifica da chi è composto il team di studio
 * _2_Gruppo, identifica attraverso una sigla il livello superiore in distinta base, del componente su cui viene eseguita la FMEA
 * _2_Componente, identifica attraverso una sigla il componente su cui viene eseguita la FMEA
 * _2_Funzione, identifica la funzione del componente (vedi tabella CQ*FM)
 * _2_Difetto, identifica attraverso una sigla uno dei possibili e/o riscontrati difetti, relativi al gruppo/componente su cui si esegue l'analisi (vedi tabella CQD)
 * _2_Causa, identifica attraverso una sigla una delle possibili e/o riscontrate cause, relative ad un particolare difetto (vedi tabella CQC)
 * _2_Effetto, identifica attraverso una sigla uno dei possibili e/o riscontrati effetti, relativi ad un particolare difetto (vedi tabella CQ*EF)
 * _2_Indice di Rilevabilità, è un punteggio assegnato in funzione della  rilevabilità del difetto (vedi tabella CQ7)
 * _2_Indice di Gravità, è un punteggio assegnato in funzione della  gravità dell'effetto relativo ad un particolare difetto (vedi tabella CQ6)
 * _2_Indice di Probabilità, è un punteggio assegnato in funzione della  probabilità della causa relativa ad un particolare difetto (vedi tabella CQ5)
 * _2_Indice di Priorità di rischio, È un indice il cui valore è dato dal prodotto degli indici di gravità, rilevabilità e probabilità. Permette di discriminare su quali particolari eseguire la "continuos analisys"
 * _2_"Continuos Analisys", modalità d'analisi per cui il team di studio analizzando gli istogrammi delle cause sceglie quella con indice di priorità di maggiore ripetendo iterativamente questo processo fino a che gli indici non si sono abbassati sotto il livello minimo voluto

# Tabelle utilizzate dal modulo : 
### CQY - TIPO GRIGLIA  CONTROLLI
Descrive il significato dei campi legati alla griglia. Collegare questi campi alle tabelle o ad archivi dati.
 :  : DEC T(ST) K(CQY)

### CQ* Controlli generici (15 caratteri)
il subsettore FM identifica la funzione del componente
il subsettore EF identifica l'effetto  del modo di guasto
il subsettore MP identifica le misure previste
il subsettore ED identifica la criticità del difetto
 :  : DEC T(ST) K(CQ*FM)
 :  : DEC T(ST) K(CQ*EF)
 :  : DEC T(ST) K(CQ*MP)
 :  : DEC T(ST) K(CQ*ED)

### CQ5 Probabilità del guasto (2 caratteri)
identifica il punteggio di riferimento della probabilità di verificarsi del guasto
 :  : DEC T(ST) K(CQ5)

### CQ6 Gravità del guasto (2 caratteri)
identifica il punteggio di riferimento della gravità del guasto visto come influsso che questo ha verso il cliente
 :  : DEC T(ST) K(CQ6)

### CQ7 Rilevabilità del guasto (2 caratteri)
identifica il punteggio di riferimento della rilevabilità del difetto
 :  : DEC T(ST) K(CQ7)

### CQC Causa Difetti (15 caratteri)
codifica le cause imputabili ai difetti
 :  : DEC T(ST) K(CQC)

### CQD  Difetti (15 caratteri)
codifica i difetti riscontrabili nei componenti
 :  : DEC T(ST) K(CQD)

### CQ0  Tipo Documento (15 caratteri)
codifica il tipo di documento su cui eseguire la FMEA ed il tipo griglia
 :  : DEC T(ST) K(CQ0)


# Processo di avviamento ed utilizzo
## Attività iniziale
 * inserimento delle tabelle relative al modulo
 * inserimento articolo/gruppo/componente
 * inserimento difetti per gruppo/componente
 * inserimento effetti per gruppo/componente/difetto
 * inserimento cause per gruppo/componente/difetto
 * assegnazione degli indici di valutazione
 * calcolo priorità di rischio

## Attività periodica
 * emissione delle richieste di intervento per modifica di progetto o processo
 * gestione della rivalutazione delle priorità di rischio ad intervento effettuato
 * stampa della griglia della FMEA o FMECA
