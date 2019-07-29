OBIETTIVO
 visualizzare valori/qtà per periodi

FLUSSO
 prerequisiti /COPY £G14E  (schiere)

 Parametri
 Input :   £G14FU :  Tipo Funzione (10)
                 DA = Presento 120 date
                 PE = Presento 120 periodi
         £G14ME :  Metodo  (10)
         £G14CF :  caratteristica fonte (2) per gestione £14D
                 'CO' codice (della schiera £14A)
                 'PU' puntatore schiera £14A
         £G14CD :  caratteristica data (2) per gestione £14F
                 'CO' data di £14C
                 'PU' puntatore schiera £14C
         £G14DI :  Data iniziale (8,0  AAAAMMGG)
                 (vale anche AAMMGG)
         £G14PE :  Periodicità (3) tab. A£Q
         £14A   :  Codice fonte   (RCCC)                (schiera)
                 R riclassifica
                 C codice
         £14B   :  Descrizione fonte                    (schiera)
         £14C   :  Date/periodi                         (schiera)
         £14D   :  Fonti da visualizzare                (schiera)
         £14E   :  valori da visualizzare               (schiera)
         £14F   :  Date da visualizzare                 (schiera)
campi di intestazione
         £G14I1 :  1° Intestazione SFC  (35)
         £G14I2 :  2° Intestazione SFC  (35)
         £G14AM :  ambiente (nome programma) (10)
         £G14C1 :  Codice 1  (15)
         £G14T1 :  tipo codice 1 (2)
         £G14P1 :  parametri codice 1 (10)
         £G14C2 :  Codice 2  (15)
         £G14T2 :  tipo codice 2 (2)
         £G14P2 :  parametri codice 2 (10)
         £G14C3 :  Codice 3  (15)
         £G14T3 :  tipo codice 3 (2)
         £G14P3 :  parametri codice 3 (10)

campi default
         £G14CM  Ultimo comando

Note per parametri
La schiera £14C può non essere passata, in questo caso il pgm
si occuperà di costruirla,utilizzando i campi £G14PE e £G14DI.
I campi "CF" e "DC" indicano il metodo di impostare le schiere
£14D e £14F


