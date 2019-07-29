# Obiettivo
Costruzione di un carattere "attributo di visualizzazione"
Questo permette di colorare le righe, ad esempio, dei subfile.

# Input/Output
 FUNZIONE = 'LIC'
 METODO   =  nn  (con nn=01-15)
   OUTPUT  :  £ATRVA del Livello nn (vedi TSTATR + F9)

 FUNZIONE = 'ATTVI'
   INPUT   :  codice V2/ATTVI nel primo elemento di £AT
   OUTPUT  :  £ATRVA del codice

 FUNZIONE = Blank o altro
   INPUT   :  Schiera £AT di 4 elementi con : 
    Attributi
           N  :  Normale
           R  :  Reverse
           H  :  Alta intensità
           U  :  Sottolineata
           B  :  Lampeggiamento
           C  :  Column Separator
           I  :  Non visualizzabile
    Colori
           0  :  MONOCROMATICO (DEFAULT)
           1  :  BLU
           2  :  VERDE
           3  :  ROSA
           4  :  ROSSO
           5  :  TURCHESE
           6  :  BIANCO
           7  :  GIALLO
   OUTPUT  :  £ATRVA con l'attributo composto.




# Prerequisiti
Copy £ATRE per definizione schiera
/COPY QILEGEN,£ATRE


# Esempio di chiamata

1)
Per colorare le righe, ad esempio, di una G18 : 
        -chiamare nella £INIZI la £ATR senza specificare nessun campo.
        -inserire nel campi £G18RI l'attributo £G18PU(XXXX) e la riga cambierà colore da quel punto in poi.
        esempio : 
        EVAL    £G18RI='parte corolara normale'+£ATRPU(4RU)+'parte in rosso reverse sottolineato'

2) chimata standard

*C                     MOVEL     valore1   £AT,1
*C                     MOVEL     valore2   £AT,2
*C                     MOVEL     valore3   £AT,3
*C                     MOVEL     valore4   £AT,4
*C                     EXSR      £ATRC
*C                     MOVEL     £ATRVA    ATR

# Note particolari

Ci sono delle combinazioni del parametro di £ATRPU che si possono visualizzare nel TST premendo F7, F8, F9 o F11
di ognuna di queste composizione è mostrato il risultato.

Per tornare alla normale visualizzazione del carattere basta inserire nella riga £ATRPU(0N)

Ogni cambio di colore utilizza un byte della stringa.
