# Obiettivo
Gestisce una serie di funzioni per ubicazione :  gestione anagrafica, interrogazione del contenuto, scansione per tipo, articolo o ubicazione, verifiche di coerenza ecc..
In alternativa alla chiamata a programma, con le stasse funzioni e metodo può essere chiamato come funizzato, passando le chiavi dovute :  per le funzioni INT usare £FUNPG=GMGMU1, per tutte le altre £FUNPG=GMGMU0

# Funzioni e metodi
 * Funzione - "GES  "    :  Gestione ubicazione
 ** Metodo   - "01"      :  Immissione
 ** Metodo   - "02"      :  Modifica
 ** Metodo   - "03"      :  Copia
 ** Metodo   - "04"      :  Annullamento
 ** Metodo   - "05"      :  Visualizza
 * Funzione - "VER  "    :  Verifiche
 ** Metodo   - "STA"     :  Stato (bloccata/vuota)
 ** Metodo   - "ART"     :  Esiste già l'articolo
 ** Metodo   - "LOT"     :  Esiste già articolo / lotto
 * Funzione - "INT  "    :  Interrogazioni
 ** Metodo   - "TPU"     :  Ubicazioni di un tipo ubicaz.
 ** Metodo   - "TPG"     :  Ubicazioni di un tipo gestione
 ** Metodo   - "UBI"     :  Contenuto dell'ubicazione
 * Funzione - "SCU  "    :  Scansioni ubicazioni
 ** Metodo   - "UBI"     :  Contenuto dell'ubicazione
 * Funzione - "SCT  "    :  Scansioni per tipo ubicazione
 ** Metodo   - "ALL"     :  Tutte
 ** Metodo   - "ALLCON"  :  Tutte con contenuto
 ** Metodo   - "VUO"     :  Vuote
 * Funzione - "SCG  "    :  Scansioni per tipo gestione
 ** Metodo   - "ALL"     :  Tutte
 ** Metodo   - "ALLCON"  :  SV - Tutte con contenuto
 ** Metodo   - "VUO"     :  Vuote
 * Funzione - "SCP  "    :  Scansioni per cod.appartenenza
 ** Metodo   - "ALL"     :  Tutte
 ** Metodo   - "ALLCON"  :  Tutte con contenuto
 ** Metodo   - "VUO"     :  Vuote
 * Funzione - "SCTUTG"   :  Scansioni per T.Ubicaz. e T.Gestione
 ** Metodo   - "ALL"     :  Tutte
 ** Metodo   - "ALLCON"  :  SV - Tutte con contenuto
 ** Metodo   - "VUO"     :  Vuote
 * Funzione - "SCA   "   :  Scansioni per articolo
 ** Metodo   - "ART"     :  Tutte

# Input
£GMUFU :  funzione
£GMUME :  metodo
£GMUMS :  Messaggio scansione/inizializzazione
£FUNT1 :  Tipo 1
£FUNP1 :  Parametro 1
£FUNK1 :  a seconda della funzione :  Tipo gestione (TAGMG), tipo Ubicazione (TAGMU) o Ubicazione (UB)
£FUNT2 :  Tipo 2
£FUNP2 :  Parametro 2
£FUNK2 :  a seconda della funzione :   Tipo gestione (TAGMG) o tipo Ubicazione (TAGMU)
£GMUMG :  Plant    (solo per alcune funz.)
£GMUAR :  Articolo (solo per alcune funz.)
£GMULT :  Lotto    (solo per alcune funz.)
£GMULC :  Livello di chiamata

# Output
£FUN35 :  Errore
£FUN36 :  Ricerca
£GMUMS :  Messaggio scansione/errore
£GMUDS :  Tutta la DS (prima parte replica tracciato GMQUAN)
£GMUAG :  Area giacenza
£GMUTG :  Tipo giacenza
£GMUMG :  Codice magazzino
£GMUAR :  Codice articolo
£GMUC1 :  Codice 1
£GMUC2 :  Codice 2
£GMUC3 :  Codice 3
£GMUC4 :  Codice 4
£GMUST :  Stato giacenza
£GMUNC :  Numero collo
£GMUGC :  Quantità giacenza
£GMUQA :  Quantità allocata
£GMUQT :  Quantità attesa
£GMULT :  Lotto
£GMUUB :  Codice ubicazione
£GMUBL :  Flag ubicaz.bloccata (<> blanks)
£GMUOC :  Flag ubicaz.occupata (<> blanks)

# Prerequisiti
/COPY £FUNDS1
/COPY £GMUDS

# Esempio di chiamata di scansione
>      *
     C                   EVAL      £GMUFU = 'SCU'
     C                   EVAL      £GMUME = 'UBI'
     C                   EVAL      £GMUMS = *BLANKS
     C                   CLEAR                   £FUND1
     C                   EVAL      £FUNT1 = 'UB'
     C                   EVAL      £FUNP1 = PLANT
     C                   EVAL      £FUNK1 = CODICE_UBICAZIONE
     *
1    C                   DO        *HIVAL
     C                   EXSR      £GMU
1    C                   IF        £GMUMS='FINE'
     C                   LEAVE
1e   C                   ENDIF
1e   C                   ENDDO

# Esempio di chiamata di gestione
>      *
     C                   EVAL      £GMUFU = 'GES'
     C                   EVAL      £GMUME = '02'
     C                   EVAL      £GMUMS = *BLANKS
     C                   CLEAR                   £FUND1
     C                   EVAL      £FUNT1 = 'UB'
     C                   EVAL      £FUNP1 = PLANT
     C                   EVAL      £FUNK1 = CODICE_UBICAZIONE
     C                   EXSR      £GMU


# Oggetti collegati
 :  : DEC T(UB)
 :  : DEC T(ST) K(GMG)
 :  : DEC T(ST) K(GMU)

