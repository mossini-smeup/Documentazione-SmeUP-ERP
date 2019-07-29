# Obiettivo
Gestisce e recupera le informazioni gestionali della coppia Magazzino articolo.
Le informazioni vengono recuperate in base al valore del driver magazzino della tabella B£1.

# Funzioni e metodi
 * Funzione - "GES  "   :  Gestione
 ** Metodo   - "VIS"    :  Visualizzazione
 ** Metodo   - "MOD"    :  Modifica
 * Funzione - "LET  "   :  Lettura
 ** Metodo   - "ALL"    :  Tutti i dati anagrafici
Funzione - "LET_P"   :  Lettura con presentazione
 ** Metodo   - "ALL"    :  Tutti i dati anagrafici
 * Funzione - "LET_L"   :  Lettura con presentazione in loocup
 ** Metodo   - "ALL"    :  Tutti i dati anagrafici
 * Funzione - "LR   "   :  Chiusura programma

# Input
£GMAFU :  funzione
£GMAME :  metodo
.....
£FUNK2 :  Articolo
£FUNK1 :  Magazzino

# Output
£GMAMS :  Codice messaggio ritorno (7)
£GMAFI :  File   messaggio ritorno (10)
£GMACM :  Ultimo Comando
£FUN35 :  Indicatore errore
£FUN36 :  Indicatore ricerca

£GMALR :  Livello risalita
£GMAMG :  Magazzino
£GMACO :  Codice (articolo)
£GMAUB :  Ubicazione
£GMACG :  Tipo gestione
£GMAUM :  Unità movimentazione
£GMAQU :  Qtà x unità di movimentazione
£GMALS :  Criterio livello stock
£GMAPS :  Parametro di stock
£GMAOB :  Criterio obsolescenza
£GMAPO :  Parametro obsolescenza
£GMACI :  Criterio di inventario
£GMAPI :  Parametro inventario
£GMALV :  Livello stato
£GMAST :  Stato
£GMASM :  Scorta minima
£GMAPR :  Punto riordino
£GMALE :  Lotto economico
£GMACS :  Consumo stimato
£GMADI :  Data inizio utilizzo
£GMADF :  Data fine utilizzo
£GMAIN :  Data inserimento
£GMAAG :  Data agg. record
£GMAUT :  Utente ultimo agg.

Campi derivati :  dalla fine della DS all'indietro
------------------------------------------------
£GMAR1 :  Livello risalita tecnica di gestione
£GMAR2 :  Livello risalita ubicazione assunta
£GMAR3 :  Livello risalita famiglia contenitori + qta per contenitore
£GMAR4 :  Livello risalita scorta minima
£GMAR5 :  Livello risalita punto di riordino + lotto economico

# Prerequisiti
/COPY QILEGEN,£FUNDS1
/COPY QILEGEN,£GMADS

# Esempio di chiamata
>      *
     C                   MOVEL(P)  MAGAZZ        £FUNK1
     C                   MOVEL(P)  ARTICOLO      £FUNK2
     C                   MOVEL(P)  'LET'         £GMAFU
     C                   MOVEL(P)  'ALL'         £GMAME
     C                   EXSR      £GMA


# Oggetti collegati
 :  : DEC T(ST) K(C£F)
 :  : DEC T(ST) K(C£G)
 :  : DEC T(ST) K(GM1)

# Note particolari
Nel caso in cui la gestione magazzino fosse SMEUP (Quindi non deviata su altre applicazioni), il modo di recupero e scrittura dei dati magazzino articolo sono guidati dalle impostazione dell'elemento ART_MAG della tabella C£F e dal relativo elemento della tabella C£G. Inoltre a livello della tabella GM1 si puo' definire il modo di risalita specifico per campo
