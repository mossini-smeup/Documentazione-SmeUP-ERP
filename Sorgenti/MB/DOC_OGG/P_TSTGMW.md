# Obiettivo
Inizializzare il record del file GMTRIM0F : 
 * a. da zero
 * b. derivandolo da un altro già esistente


# Funzioni e metodi
 * Funzione - "CLEAR"   :  inizializzazione totale del record
 ** Metodo   - blanks   :  il record verrà scritto dal pgm chiamante
 ** Metodo   - "WRI"    :  il record verrà scritto dalla funzione £GMW
 * Funzione - "DERIV"   :  inizializzazione del record a partire da un altro
 ** Metodo   - blanks   :  il record verrà scritto dal pgm chiamante
 ** Metodo   - "WRI"    :  il record verrà scritto dalla funzione £GMW


# Input
£GMWFU :  funzione
£GMWME :  metodo

£GMWMG :  codice del plant
£GMWTO :  tipo di richesta di movimentazione (tabella GMO)
£GMWNR :  numero di RdM. Se non lo si indica, sarà usato il numeratore specificato in tabella GMO

GMTRIM :  record del GMTRIM0F :  se si sta usando la funzione "DERIV", deve essere il record origine da cui derivare
        quello nuovo

# Output
GMTRIM :  record inizializzato della DS del record del GMTRIM0F
£GMWMS :  Codice messaggio
£GMWFI :  File messaggio
£GMWCM :  Ultimo comando
£GMW35 :  Indicatore 35
£GMW36 :  Indicatore 36


# Prerequisiti
Definizione del record del file : 
D GMTRIM        E DS                  EXTNAME(GMTRIM0F) INZ

# Esempio di chiamata
>C                   EVAL      £GMWFU='CLEAR'
C                   EVAL      £GMWME=''
C                   EVAL      £GMWMG=<codice del plant>
C                   EVAL      £GMWTO=<tabella GMO>
C                   EVAL      £GMWNR=''
C                   EXSR      £GMW

