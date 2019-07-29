# Installazione
Per quanto riguarda l'installazione del modulo dei numeri oggetto, le operazioni da effettuare sono le seguenti : 
 * riportare la nuova SMEDEV contenente tutti gli aggiornamenti;
 * lanciare l'estrazione dei dati per alimentare il file dei numeri oggetto;
 * aggiungere l'elemento D5NUOG (Numeri oggetto) nella tabella B£A sottosettore MO per poter accedere alla scheda D5NUOG tramite il modulo.

Inoltre, bisogna verificare che sia attivata la gestione delle "viste di database". Bisogna verificare l'esistenza del pgm B£IVD0, ed inoltre (IMPORTANTE) deve esiste l'ggetto VD nella tabella *CNTT (oggetti del sistema)

## Attivazione
L'attivazione avviene in due step : 
1) Attivare la gestione della storicizzazione dei numeri oggetti attravero la tabella B£7.
_2_TAB£7 :  Personalizzazione B£ Ambiente
 :  : DEC T(TA) P(B£7) K(*)
2) Abilitare l'oggetto alla storicizzazione dei numeri
_2_TAV5D :  Tipi documento
 :  : DEC T(TA) P(V5D) K()

