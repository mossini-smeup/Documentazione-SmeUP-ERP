# MOCIR     -  MODALITÀ COSTRUZIONE IMPEGNI RISORSE
Definisce le varie modalità con cui possono essere costruiti gli impegni risorse di un oggetto (ordine di
produzione/riga di lavorazione/articolo/contenitore).

## VALORI POSSIBILI

### L1 PRODUZIONE IN LINEA A FASE UNICA
Viene trattata unicamente la fase impostata nella testata dell'ordine di produzione.

### CO CICLO OGGETTO
Viene trattato unicamente il ciclo dell'articolo intestatario del documento, del tipo impostato in tabella P5S nel
campo 'tipo ciclo origine'.

### C1 CICLO DOCUMENTO / CICLO OGGETTO
Se presente, viene trattato il ciclo del documento, intestato al
n.documento, del tipo impostato in tabella P5S nel campo 'tipo ciclo memorizzato', se assente viene assunto il ciclo
origine.

### C2 CICLO DOCUMENTO
E'come il caso precedente, senza la risalita al ciclo dell'oggetto.
