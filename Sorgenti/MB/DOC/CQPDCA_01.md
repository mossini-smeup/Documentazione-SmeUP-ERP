# Scopo
 * Supportare l' utilizzo dei Piani di Campionamento standardizzati (UNI-4842/75 e Military Standard MIL 105D
 * Permettere la definizione di specifici campionamenti della Azienda
 * Supportare la definizione ed utilizzo delle Regole di attribuzione del Piano di Campionamento al lotto.

# Definizioni
 * _2_Piano di Campionamento, identifica attraverso una sigla di 3 posizioni una regola di definizione di un campione (e del n. di rifiuto/accettazione) a fronte di un lotto sottoposto al controllo. Nella normativa UNI 4842/75, il piano di campionamento coincide con un prospetto da utilizzare (campionamento semplice ordinario, campionamento semplice rinforzato, ...)
 * _2_Livello di Collaudo, identifica attraverso una sigla di 3 caratteri, una suddivisione di un piano di campionamento in casistiche più specifiche. Nella normativa UNI 4842/75, la definizione di un livello di collaudo è fondamentale per la defizione della corretta curva di rischio da applicare all' interno di un prospetto di (piano di campionamento) definito.

# Tabelle utilizzate dal modulo
### CQP Piano di Campionamento (3 caratteri)
classifica i diversi prospetti da utilizzare (ad esempio, prospetto primario, prospetto secondario, ...), e le regole di definizione ed utilizzo.
 :  : DEC T(ST) K(CQP)

### CQ*SE Livelli di Collaudo
codifica i diversi livelli di collaudo applicabili sui Piani di Campionamento.
 :  : DEC T(ST) K(CQ*SE)

È importante sottolineare che i Piani UNI 4842/75 e MIL 105 D sono precaricati, e rappresentano un importante riferimento nella creazioni di propri piani personalizzati.

# Processo di avviamento ed utilizzo
Non esiste uno specifico percorso di avviamento ed utilizzo nel caso di utilizzo dei piani precaricati.
Nel caso di definizione di propri piani, è ovviamente necessario definirli prima dell' utilizzo durante la creazione del lotto e gestione benestare di collaudo.
