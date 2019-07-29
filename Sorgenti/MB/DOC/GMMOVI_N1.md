# B£J Per Lancio Movimenti Magazzino
Nome programmi : 
 * **GMMV01I**, lancio di una causale
 * **GMMV02I**, lancio di due causali
 * **GMMV05I**, scarico da scansione distinta

**Nota bene**; ricordare che c'è il visualizzatore standard GMMV01D_$$ in funzione delle chiavi di GMQUAN.

## Parametro 1 (Funzione)
 * **blank**, non considera la LDA ricevuta
 * **non blank**, considera la LDA ricevuta

**Struttura parametro 1 (se non blank)**
* Posizione 1-1, "_H_L", far considerare la LDA
* Posizione 2-9, se diverso da blank è il programma 2 che viene lanciato : 
 ** **GMMV01D**, default -monitor di magazzino
 ** **GMMV05G**, movimenti da aree
 ** **GMMV06G**, movimenti di un articolo

## Struttura LDA
* Posizione 1-4, causale 1
* Posizione 5-8, causale 2
Il monitor usa solo queste

Le parti seguenti sono specifiche del programma 2.

**LDA Per PGM GMMV05G**
 * Posizione 9-11, forma presentazione (tab. GMF)
 * Posizione 12-12, documento obbligatorio (N. e data) (blank = non visualizzato, 1 = Facoltativo, 2 = obbligatorio)
 * Posizione 13-13, se non blank = permessi raggruppamenti
 * Posizione 14-15, suffisso del programma di applicazione __GMMV05_xx__, (Nota :  il formato video è GMMV5xxV) attualmente esistono GMMV05_TR e GMMV05_SP, normalmente sono pure FUN, il _TR fa eccezione.

**Parti specifiche del GMMV_05_TR**
 * Posizione 26-40, articolo trasformato
