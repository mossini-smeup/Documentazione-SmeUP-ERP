# OBIETTIVO
Questa /COPY controlla l'esistenza di un oggetto sul sistema e ne reperisce l'eventuale descrizione

# FUNZIONI/METODI
Non previsti funzioni e metodi standard

# PREREQUISITI

---> C/COPY QILEGEN,£CKO       in coda al sorgente

#  FLUSSO
 **Input : **

- £CKON  :  Nome oggetto
- £CKOT  :  Tipo oggetto (*FILE, *PGM, *USRPRF, etc.)
- £CKOL  :  Libreria dove cercare oggetto _?/! In libreria cerca e restituisce la libreria dove si trova l'oggetto
- £CKOM  :  Membro (se file) -> se blank non controlla esistenza membro


**Output :  **

- £CKOR  :  Codice di ritorno
-- > 0=oggetto esistente
-- > 1=oggetto inesistente
-- > 2=membro inesistente
- £CKOD  :  Descrizione oggetto
- £CKOM  :  Membro (se richiesta ricerca)
- £CKOP  :  Libreria (se richiesta ricerca)
- £CKOLC :  LIVELLO DI CHIAMATA


##   ESEMPIO DI CHIAMATA
>             MOVEL <oggetto>                  £CKON
             MOVEL <tipo>                     £CKOT
             MOVEL <libreria>                 £CKOL
             MOVEL <membro>                   £CKOM
             MOVEL <livello chiamata>         £CKOLC
             EXSR         £CKO
             £CKOR        IFEQ                0
             MOVEL        £CKOD               <campo descrizione>
             END

