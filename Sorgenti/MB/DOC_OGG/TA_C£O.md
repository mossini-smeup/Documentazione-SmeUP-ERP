# C£O - Descrizione in lingua
 :  : DEC T(ST) K(C£O)
## OBIETTIVI
-    Permettere di definire passi mediante i quali ottenere descrizioni estese, attraverso la concatenazione di attributi tradotti nelle lingue di interesse.
_9_Esempio :  abbiamo associato le caratteristiche di una cornice ponendo nei parametri il colore "ROSSO" e il vetro "ANTIRIFLESSO", potremo tradurre in inglese, francese, ecc. le sole parole di cui sopra ottenendo le descrizioni complete.
Si costruiscono le descrizioni delle lingue per le quali è richiesto in tabella LIN.
## COMPORTAMENTO DEL PROGRAMMA DI CALCOLO
Il programma recupera la struttura in base a "TIPO/PARAMETRO" (es. ARCINTU dove CINTU = Tipologia dell'articolo). Se non esiste un algoritmo specifico utilizza il solo tipo (Es. AR).
Il programma di calcolo è una funzione delle descrizioni estese e sarà richiamato da un passo del flusso.
Per la comprensione del calcolo della descrizione, fare riferimento alla funzione di simulazione presente nell'insieme delle funzioni.
## SOTTOSETTORI
Non significativi
## CONTENUTO DEI CAMPI
 :  : FLD T$ELEM **Codice**
Il codice è organizzato secondo la seguente struttura xxyyyyynnnnlll dove : 
xx = tipo oggetto (AR=Articolo ecc).
yyyyy = parametro oggetto (se tipo = CN avremo CLI=Cliente) se bianco è il default per tutti i tipi
nnnn = progressivo del passo
lll = codice lingua (passo valido solo per lingua lll) se bianco vale per tutte le lingue
 :  : FLD T$C£OA **Metodo**
Definisce come ottenere la variabile da tradurre ed aggiungere alle descrizioni. Abbiamo i seguenti metodi : 
1.   COS = Costante
Definisce una parola che sarà eventualmente tradotta nella lingua trattata.
_9_Es.  SEDIA
2.   OAV = Attributo oggetto
Indica un attributo dell'oggetto definito nei primi due caratteri del codice. Si utilizzerà la decodifica in lingua di
tale attributo.
_9_Es.  Classe merceologica dell'articolo
Il parametro specifica l'attributo
3.   PAR = Parametro
Come sopra ma per parametri.
Il parametro specifica categoria e codice del parametro
4.   DEV = Deviato
Permette di fare riferimento ad altro passo definito in questa stessa tabella. In tale modo si possono codificare liberamente dei passi e in questa fase sequenziarli oppure utilizzare, per un tipo articolo, il passo di un altro tipo.
 :  : FLD T$C£OB **Parametro del metodo**
In funzione del metodo come specificato sopra
 :  : FLD T$C£OC **Tipo/parametro oggetto**
Codice utilizzato per recuperare la descrizione in lingua dell'attributo richiesto dal metodo. Se non specificato e se possibile, si recupera il tipo dell'attributo o del parametro.
 :  : FLD T$C£OE **Lunghezza stringa ridotta**
Se non specificato, non viene aggiunto alcun carattere alla descrizione ridotta. La descrizione ridotta viene ripresa dalla descrizione ridotta ottenuta dal passo.
 :  : FLD T$C£OF **Separatore stringa ridotta**
Indica il numero di caratteri bianchi da inserire come separatori.
 :  : FLD T$C£OG **Lunghezza stringa estesa**
Come sopra. La descrizione estesa viene ottenuta dalla descrizione estesa del passo.
 :  : FLD T$C£OH **Separatore stringa estesa**
Come sopra. Indica il numero di caratteri bianchi da inserire come separatori.
 :  : FLD T$C£OJ **Usare il valore per descrizione ridotta**
Invece di usare la descrizione in lingua o base, si richiede di utilizzare il valore stesso (il codice)
 :  : FLD T$C£OK **Usare il valore per descrizione estesa**
Come sopra.
