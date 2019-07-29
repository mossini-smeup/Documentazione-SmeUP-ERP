# Significato delle Program Call

## Programma richiamato
In Sme.UP le Program Call vengono fatte TUTTE verso il programma JAJAC0.
Questo programma gestisce moltissimi tipi di Program Call. La maggior parte di questi sono obsoleti (usati da WebUP 1). Qui descriviamo solo quelli necessari alla procedura di Login.

## Note su nomenclatura
Le Program Call Sme.UP hanno vari campi di input.
Per suddividerle per tipologia usiamo tre campi :  £JACMS, £JACFU e £JACME (omettendo eventualmente quelli vuoti più a dx).

## Quindi avremo ad esempio la Program Call INZJAC (£JACMS='INZJAC', £JACFU=blank, £JACME=blank) e la Program Call DATSES CON MAS (£JACMS='DATSES', £JACFU='CON', £JACME='MAS')

## Quali prendiamo in considerazione?
In questo documento vengono indicate e trattate solo le Program Call che riguardando il login del JOB principale dei client (LO_E).

## Significati della varie Program Call

### INZJAC
Inizializzazione del JOB delle Program Call.
Questa Program Call va assolutamente fatta una sola volta per ogni sessione e deve essere tassativamente la prima Program Call fatta.
Nel £JACK1 va specificato il CCSID del client.

### SMEVER JAC
Il client chiede quale sia la "versione" del JAJAC0. Questo è servito in passato per gestire la retrocompatibilità con versioni di JAJAC0 molto diverse tra loro.
Il server risponde con V3R1 ("JAJAC0 in versione >= V3R1").

### DATSES CON MAS
Richiesta di creazione connessione master.
Nel £JACP3 va passato l'utente di collegamento.
E' questa program call che determina la sottomissione del JOB LO_E.

### DATAMB NUM
Richiesta del numero di ambienti attivi per l'utente di cui è stata fatta DATSES CON MAS.
Gli ambienti sicuramente non validi non vengono contati.
In Looc.UP nel £JACP1 viene passato l'utente di collegamento ma viene ignorato.

### LISAMB LET
Richiesta della lista degli ambienti attivi per l'utente di cui è stata fatta DATSES CON MAS.
Gli ambienti sicuramente non validi vengono ignorati. In questa fase non c'è la certezza che gli ambienti passati siano tutti validi. Motivo per cui dopo aver specificato un ambiente sarà necessario fare una chiamata di verifica specifica.
Se il £JACK1 non è vuoto, viene fatto un posizionamento a partire da questo codice. Questo serve perché vengono restituiti 20 ambienti alla volta.
In £JACME è possibile indicare ' _SL_RP ' per dire che la lettura va fatta all'indietro. Questo è usato in Looc.UP per tornare alla "pagina precedente" quando mi viene mostrata la lista dei miei ambienti (appunto perché ne vengono mostrati 20 alla volta).

### DATAMB VER
Verifica dell'effettiva validità dell'ambiente selezionato.
In £JACK1 viene passato il progressivo dell'ambiente.
In Looc.UP nel £JACP1 viene passato l'utente di collegamento ma viene ignorato.

### DATSES CHG
Cambio ambiente verso l'ingresso utente indicato.
In £JACK3 viene passato il progressivo dell'ambiente.
In Looc.UP nel £JACP3 viene passato l'utente di collegamento ma viene ignorato.

### DATOGG VER
Effettua la DEC di un oggetto.
In £JACT1 viene passato il tipo, in £JACP1 il parametro e in J£ACK1 il codice.

