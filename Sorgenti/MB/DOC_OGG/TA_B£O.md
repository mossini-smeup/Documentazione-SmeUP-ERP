# B£O - TIPO OGGETTO DEL DATA BASE
 :  : DEC T(ST) K(B£O)
## OBIETTIVO
Descrivere gli oggetti applicativi gestiti.
## SOTTOSETTORI
## CONTENUTO DEI CAMPI
 :  : FLD T$B£OA **Lunghezza campo**
È un valore che indica la lunghezza reale dell'oggetto deviato
 :  : FLD T$B£OB **Deviazione Tipo oggetto**
È l'oggetto reale che sostituisce l'oggetto indicato nell'elemento, in altre parole è il deviatore di oggetti.
 :  : FLD T$B£OC **Parametro**
È il paramentro dell'oggetto indicato nel campo "Deviazione Tipo ogg.".
Nel caso di oggetto UFO (*D) è il programma in cui è controllato l'oggetto. In questo caso il nome del programma in questione deve essere al massimo di 8 caratteri.
 :  : FLD T$B£OD **Gestione parametro UFO**
Può assumere il valore ' ' o '1'.
Nel caso si stia inserendo un oggetto UFO come deviatore, immettendo '1' in questo campo, il programma di controllo viene richiamato passando anche il parametro originale dell'oggetto.
 :  : FLD T$B£OE **Tipo Oggetto Parametro**
Permette di specificare il tipo oggetto a cui deve puntare il parametro.
 :  : FLD T$B£OF **Parametro Obbligatorio**
Se specificato permette di indicare se il parametro sia o meno obbligatorio.
