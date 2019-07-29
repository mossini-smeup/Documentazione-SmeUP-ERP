# C5A - MODELLO Contab. DOCUMENTI V5
 :  : DEC T(ST) K(C5A)
## OBIETTIVO
La tabella è utilizzata per collegare i documenti V5 con la contabilità. Per chi ha installato una contabilità non SMEup, gli elementi sono le
causali contabili e normalmente la tabella è "Deviata".
Per chi ha installato Keep.UP, contiene le causali contabili abilitate ad essere utilizzate per collegare i documenti (ciclo attivo e passivo) alla contabilità.
## CONTENUTO DEI CAMPI
 :  : FLD T$DESC **Descrizione**
Descrive l'elemento (causale contabile)
 :  : FLD T$C5AA  **Tipo registrazione**
È un elemento della tabella C5D ed indica il tipo della registrazione da creare (normalmente è lo stesso nome dell'elemento). È un campo obbligatorio.
 :  : FLD T$C5AB **Causale contabile**
È un elemento della tabella C5V ed indica la causale della registrazione può essere lasciato in bianco, in questo caso viene assunta la indicata nel tipo registrazione (tabella V5D).
 :  : FLD T$C5AC  **Tipo analitica**
È un elemento della tabella C5L ed indica il tipo di causale, se gestita l'analitica. Può essere lasciato in bianco se : 
1 - Non è utilizzata l'analitica.
2 - È specificato un tipo analitica nel tipo registrazione.
 :  : FLD T$C5AD  **Suff.pgm Agg.Testata**
SV campo in sviluppo
 :  : FLD T$C5AE  **Suff.pgm Agg.Righe**
SV campo in sviluppo
 :  : FLD T$C5AF  **Suff.pgm Agg.Rate**
SV campo in sviluppo
 :  : FLD T$C5AG  **Suff.pgm Agg.Analit.**
SV campo in sviluppo
 :  : FLD T$C5AH  **Suff.pgm.Agg.Descri.**
SV campo in sviluppo
I campi sottoelencati sono riempiti normalmente dal programma che gestisce la deviazione e sono tutti campi che derivano dalla causale contabile : 
 :  : FLD T$C5A1  1=causale fornitore
 :  : FLD T$C5A2  1=causale cliente
 :  : FLD T$C5A3  Tipo Registro iva
 :  : FLD T$C5A4  Numero registro iva
 :  : FLD T$C5A5  ' ' Fatt/'1' Nota C.
 :  : FLD T$C5A6  Intra-natura trans.
 :  : FLD T$C5A7  Intra-regime stati.
 :  : FLD T$C5A8  Obbl. nr documento
 :  : FLD T$C5A9  Obbl. nr riferimento
 :  : FLD T$C5A0  Tipo Documento
