# Obiettivo
Interfacciare il programma in esecuzione con l'ANAGRAFICO
UBICAZIONI delle diverse applicazioni previste nella
tabella di personalizzazione applicazioni B£1
Eseguire la ricerca alfabetica relativa se richiesto

# Input
££UBI  :  Codice ubicazione
££UBIM :  Codice magazzino

# Output
*IN35  :  se On = Ubicazione   errata
*IN36  :  se On = eseguita ricerca alfabetica
££UBI  :  codice Ubicaz.  scelta (se eseguita ricerca)
££UBID :  descrizione Ubicazione
....... da estendere in seguito
££UBUR  Ubicazione riferimento                        0
££UBTG  Tipo gestione
££UBTU  Tipo ubicazione
££UBCA  Codice appartenenza
££UBSU  Stato ubicazione
££UBUB  Ubicazione bloccata
££UBUM  Data ultimo movimento
££UBPO  % occupazione
££UBTC  Tipo contenitore
££UBMI  Gest. multi item
££UBML  Gest. multi lotti

# Prerequisiti

/COPY QILEGEN,£RITES

DGMUBIC         E DS                  EXTNAME(GMUBIC0F)

# Esempio di chiamata

C                     MOVEL       <Ubicaz>       ££UBI
C                     MOVEL       <Magazz>       ££UBIM
C                     EXSR        £IFUBI
C  N35 36             MOVEL       ££UBI          <campo Ubicaz.>
C  N35                MOVEL       ££UBID         <campo descrizione>
C                     MOVEL       ££UBUR         <Ubicazione riferimento>   0
C                     MOVEL       ££UBTG         <TipoMgestione>
C                     MOVEL       ££UBTU         <TipoMubicazione>
C                     MOVEL       ££UBCA         <Codice appartenenza>
C                     MOVEL       ££UBSU         <Stato ubicazione>
C                     MOVEL       ££UBUB         <Ubicazione bloccata>
C                     Z-ADD       ££UBUM         <DataMultimo movimento>
C                     Z-ADD       ££UBPO         <%Uoccupazione>
C                     MOVEL       ££UBTC         <TipoMcontenitore>

# Note particolari


