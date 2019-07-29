# OBIETTIVO
Recupero di un XML da un servizio. Trasformazione di un XML restituito da un servizio in formato TXT o LATEX. Attualmente gestisce solo documenti XML di max 30000.

# PREREQUISITI
D/COPY QILEGEN,£FSRDS
D/COPY QILEGEN,£FSR

# PARAMETRI
## PARAMETRI DI INPUT
- Funzione :  _campo £FSRFU_

- GET Recupero di un XML da un servizio.
- TRX Trasformazione di un documento XML restituito da un servizio in formato TXT o LATEX.
- VIS Visualizzazione di un documeto XML restituito da un servizio in formato XML, TXT o LATEX.
- PRN Stampa di un documento XML restituito da un servizio in formato TXT o LATEX.

- Metodo :  _campo £FSRME_
Funzione GET : 

- *BLANKS Recupero di un XML da un servizio.

Funzione TRX : 

- TXT Trasformazione di un documento XML in formato TXT.
- LTX Trasformazione di un documento XML in formato LATEX.

Funzione VIS : 

- TXT Visualizzazione di un documento XML in formato TXT.
- LTX Visualizzazione di un documento XML in formato LATEX.

Funzione PRN : 

- TXT Stampa di un documento XML in formato TXT.
- LTX Stampa di un documento XML in formato LATEX.

- Funzione di chiamata di un servizio :  _campo £FSRLF_
Campo utilizzato con la funzione GET per recuperare un XML da un servizio. La sintassi della funzione è quella di chiamata di un servizio da Loocup.

- Componente :  _campo £FSRCM_
Campo utilizzato con le funzioni TRX, VIS e PRN. Specifica il tipo di componente grafico rappresentato dall'XML. Attualmente sono gestiti i valori EXB (matrice) e TRE (albero) per la trasformazione in formato testo e il valore EXB (matrice) per la trasformazione in LATEX.

- Parametri :  _campo £FSRPA_
Campo utilizzato con le funzioni TRX, VIS e PRN. Elenco di parametri da utilizzare per la funzione scelta. Attualmente sono gestiti per la componente matrice i seguenti parametri : 

- COD(COL1,COL2,..)  Specifica le colonne della matrice da visualizzare / stampare / trasformare. Valore di default tutte le colonne.
- RIG(n) Specifica il numero massimo di righe da visualizzare / stampare / trasformare. Valore di default tutte le righe.

- XML restituito dal servizio :  _campo £FSRXM_
Campo di input per le funzioni TRX, VIS e PRN. Dimensione massima 30000.

## PARAMETRI DI OUTPUT
- XML restituito dal servizio :  _campo £FSRXM_
Campo di output per la funzione GET. Contiene l'XML da visualizzare / stampare / trasformare. Dimensione massima 30000.

- Documento XML trasformato :  _campo £FSRTX_
Campo di output per la funzione TRX. Contiene l'XML trasformato in formato testo o latex. Dimensione massima 30000.

- Indicatore di errore :  _campo £FSR35 (*IN35)_
Indicatore di errore di esecuzione della /COPY.

# ESEMPI DI CHIAMATA
>EVAL      £FSRFU='GET'
EVAL      £FSRLF='F(EXB;B£SER_44;LIS.FLD) 1(OJ;*FILE;BRENTI0F) 2(;;)'
EXSR      £FSR

EVAL      £FSRFU='TRX'
EVAL      £FSRME='LTX'
EVAL      £FSRCM='EXB'
EVAL      £FSRPA='RIG(10) COD(SSTR03,SSTR04,SSTR05)'
EVAL      £FSRXM=XML restituito dal servizio
EXSR      £FSR

# NOTE
-
