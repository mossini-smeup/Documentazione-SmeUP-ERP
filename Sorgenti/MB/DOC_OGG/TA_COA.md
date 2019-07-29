# COA - Contabilizzazione di generale
 :  : DEC T(ST) K(COA)
## OBIETTIVO
Per la costruzione dei conti contabili.
Per verificare la corretta gestione della Tabella e le logiche di risalita ai Conti, è possibile utilizzare la routine 'TSTG03' con Funzione 'DOC'. I diversi metodi documentano i sottosettori e/o gli elementi da impostare, per risalire correttamente al codice di conto contabile.
Si può, infatti, risalire al Conto o da 'Riga documento', o da 'Oggetto' o altro.
Bisogna prestare particolare attenzione ad eventuali conflitti tra diversi sistemi di reperimento dei conti (Es. da COA TR ' tipo riga' piuttosto che da COA SP  'spese').
## CONTENUTO DEI CAMPI
 :  : FLD T$CCOA **Conto acquisti**
Immettere il conto acquisti legato all'elemento.
 :  : FLD T$COA1 **Costruzione conto acquisti**
È possibile indicare un programma per la costruzione del conto.
 :  : FLD T$COA2 **Metodo**
Si può specificare un metodo (parametri) da passare al programma specifico.
 :  : FLD T$COA5 **Passa DS record**
Inserendo il carattere 1 si specifica che il programma specifico necessita delle DS dei record di testata e righe documenti (il programma costruito dovrà tenere conto dei parametri aumentati).
 :  : FLD T$SCOA **Segno acquisti**
Libero.
 :  : FLD T$CCO2 **Conto Vendite**
Immettere il conto vendite legato all'elemento.
 :  : FLD T$COA3 **Costruzione conto vendite**
È possibile indicare un programma per la costruzione del conto.
 :  : FLD T$COA4 **Metodo**
Si può specificare un metodo (parametri) da passare al programma specifico.
 :  : FLD T$COA6 **Passa DS record**
Inserendo il carattere 1 si specifica che il programma specifico necessita delle DS dei record di testata e righe documenti (il programma costruito dovrà tenere conto dei parametri aumentati).
 :  : FLD T$SCO2 **Segno vendite**
Libero.
