# Obiettivo
Restituire la giacenza ad una certa data

# Funzioni e metodi
 * Funzione - "INI  "   :  A inizio giornata
 ** Metodo   - "AVA"    :  In avanti da 0  a data richiesta
 ** Metodo   - "IND"    :  Da oggi a data richiesta
 * Funzione - "FIN  "   :  A fine  giornata
 ** Metodo   - "AVA"    :  In avanti da 0  a data richiesta
 ** Metodo   - "IND"    :  Da oggi a data richiesta

# Input
Attenzione :  mettere '*' sulle chiavi giacenza 1/4 se si vuole considerare tutti i valori!
£GMCFU :  funzione
£GMCME :  metodo
£FUNK2 :  Articolo
£FUNK1 :  Magazzino
£FUNDT :  Data richiesta
£GMDAR :  Area
£GMDTG :  Tipo giacenza
£GMDDA :  Gruppo area
£GMDA1 :  Aree int/est/tutte
£GMDA2 :  Aree prop/non prop/tutte
£GMDA3 :  Aree Trattamento fiscale Fiscale/Non Fiscale/Tutte
£GMDT1 :  Tipo codice   1
£GMDP1 :  Param. codice 1
£GMDK1 :  Codice        1
£GMDT2 :  Tipo codice   2
£GMDP2 :  Param. codice 2
£GMDK2 :  Codice        2
£GMDT3 :  Tipo codice   2
£GMDP3 :  Param. codice 3
£GMDK3 :  Codice        3
£GMDT4 :  Tipo codice   4
£GMDP4 :  Param. codice 4
£GMDK4 :  Codice        4

# Output
£GMCMS :  Codice messaggio ritorno (7)
£GMCFI :  File   messaggio ritorno (10)
£GMCCM :  Ultimo Comando
£FUN35 :  Indicatore errore
£FUN36 :  Indicatore ricerca
£FUNQT :  Giacenza alla data

# Prerequisiti
/COPY QILEGEN,£FUNDS1
/COPY QILEGEN,£GMDDS

# Esempio di chiamata
>     C                   CLEAR                   £GMDDS
     C                   MOVEL(P)  'FIN'         £GMCFU
     C                   MOVEL(P)  'IND'         £GMCME
     C                   MOVEL(P)  MAGAZZ        £FUNK1
     C                   MOVEL(P)  ARTICOLO      £FUNK2
     C                   Z-ADD     DATA          £FUNDT
     C                   CLEAR                   £GMDDS
     C                   EXSR      £GMC


# Oggetti collegati
 :  : DEC T(ST) K(GMQ)
 :  : DEC T(ST) K(GMC)
 :  : DEC T(ST) K(GMR)

# Note particolari

