# Obiettivo
Esegue la scansione dei movimenti di magazzino e restiuisce riepiloghi dei movimenti

# Funzioni e metodi
 * Funzione - "DET  "   :  Scansione dettagliata
 ** Metodo   - "AVA"    :  In avanti da inizio a data fine
 ** Metodo   - "IND"    :  Da data fine a data inizio
 * Funzione - "GIO  "   :  Situazione giornaliera
 ** Metodo   - "AVA"    :  In avanti da inizio a data fine
 ** Metodo   - "IND"    :  Da data fine a data inizio
 * Funzione - "RIE  "   :  Sintesi per periodo
 ** Metodo   - "   "    :  Totale
 ** Metodo   - "MOV"    :  Per tipo movimento
 ** Metodo   - "IND"    :  Indici

# Input
£GMDFU :  funzione
£GMDME :  metodo
£FUNK2 :  Articolo
£FUNK1 :  Magazzino
£GMDDI :  Data inizio
£GMDDF :  Data fine
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
£GMDGA :  Giacenza ante/movimento
£GMDPE :  Qtà progressiva entrate
£GMDPU :  Qtà progressiva uscite
£GMDSE :  Qtà periodica entrata
£GMDSU :  Qtà periodica uscita
£GMDGP :  Giacenza post/movimento in UM alternativa
£GMDAA :  Giacenza ante/movimento in UM alternativa
£GMDBE :  Qtà progressiva entrate in UM alternativa
£GMDBU :  Qtà progressiva uscite  in UM alternativa
£GMDCE :  Qtà periodica/entrata   in UM alternativa
£GMDCU :  Qtà periodica/uscita    in UM alternativa
£GMDAP :  Giacenza post/movimento in UM alternativa
£GMDQM :  Qtà movimento (um o um alt.in base al tipo giacenza)
£GMDDR :  Data registrazione/riepilogo
£GMDN1 :  N.movimenti entrata progressivi
£GMDN2 :  N.movimenti uscita  progressivi
£GMDN3 :  N.movimenti neutri  progressivi
£GMDN4 :  N.movimenti totali  progressivi
£GMDN5 :  N.movimenti entrata periodici
£GMDN6 :  N.movimenti uscita  periodici
£GMDN7 :  N.movimenti neutri  periodici
£GMDN8 :  N.movimenti totali  periodici
£GMDTC :  Tipo collo
£GMDIR :  Indice Rotazione
£GMDGM :  Giacenza Media
GMMOVI :  Record del movimento

# Prerequisiti
IGMMOVI    E DSGMMOVI0F
/COPY £FUNDS1
/COPY £GMDDS

# Esempio di chiamata
>      *
     C                   MOVEL(P)  'DET'         £GMDFU
     C                   MOVEL(P)  'AVA'         £GMDME
     C                   CLEAR                   £GMDMS
     C                   CLEAR                   £FUND1
     C                   MOVEL(P)  MAGAZZ        £FUNK1
     C                   MOVEL(P)  ARTICOLO      £FUNK2
     C                   Z-ADD     DATAINI       £GMDDI
     C                   Z-ADD     DATAFIN       £GMDDF
     *
1    C                   DO        *HIVAL
     C                   EXSR      £GMD
1    C                   IF        £GMDMS='FINE'
     C                   LEAVE
1e   C                   ENDIF
1e   C                   ENDDO


# Oggetti collegati
 :  : DEC T(ST) K(GMQ)
 :  : DEC T(ST) K(GMC)
 :  : DEC T(ST) K(GMR)

# Note particolari
I movimenti vengono presi in funzione della natura definita sulla tabella GMC
