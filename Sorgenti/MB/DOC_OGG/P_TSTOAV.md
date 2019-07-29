# OBIETTIVO
Si occupa della gestione di tutte le possibili operazioni relative agli attributi di un oggetto

# PREREQUISITI
C/COPY QILEGEN,£OAV

# PARAMETRI
## PARAMETRI DI INPUT

 - Funzione :  _campo £OAVFU_
>    GES) Gestione dizionario attributi (file B£SLOT0F)
    GEV) Gestione singolo valore attributo dell'oggetto
    SCE) Scelta valore attributo
    ATT) Funzioni sugli attributi
    ATTR) Funzioni sugli atributi/rilettura
    COS) Costruzione modello
    SCA) Scansione attributi
    SCAR) Scansione attributi per radice di categoria
    SCAG) Scansione attributi per gruppo
    SCA2) Scansione attributi
    CLO) Chiusura programma


 - Metodo :  _campo £OAVME_
    Per ogni funzioni sono definiti dei metodi specifici per qanto riguarda la gestione,
    la scelta, le funzioni e la scansione degli attributi

 - Tipo/Parametro 1  _campo £OAVT1/£OAVP1_

 - Codice 1     _campo £OAVC1_

 - Tipo/Parametro 2  _campo £OAVT2/£OAVP2_

 - Codice 2     _campo £OAVC2_

 - Attributo    _campo £OAVAT_

 - Data        _campo £OAVDA_

 - Categoria    _campo £OAVCT_

## PARAMETRI DI OUTPUT

 - Valore alfanumerico  _ campo £OAVOV_

 - Valore numerico        _campo £OAVON_

 - Data inizio/fine          _campo £OAVOD/OA_

 - Tipo/Parametro        _campo  £OAVOT/OP    _

 - Intestazione           Articolo di riferimento                  _campo £OAVIN_

 - Significato attributo     _campo £OAVSI_

 - Mess. livello trovato           Mess. valore multiplo         _campi £OAVM1/M2_

 - Nr. Esecuzioni      1 Indicatori   1               _campi   £OAV35/36/MS/FI/CM _

# ESEMPIO DI CHIAMATA

INPUT
>                       EVAL      £OAVFU='Funzione'
                       EVAL      £OAVME='Metodo'
                       EVAL      £OAVT1=Tipo_1
                       EVAL      £OAVP1=Parametro_1
                       EVAL      £OAVC1=Codice_1
                       EVAL      £OAVT2=Tipo_2
                       EVAL      £OAVP2=Parametro_2
                       EVAL      £OAVC2=Codice_2
                       EVAL      £OAVAT=Attributo
                       EVAL      £OAVDA=Data
                       EVAL      £OAVCT=Categoria
                       EXSR      £OAV

OUTPUT
>                       EVAL      Alfanumerico=£OAVOV
                       EVAL      Numerico=£OAVON
                       EVAL      Inizio=£OAVOD
                       EVAL      Fine=£OAVOA
                       EVAL      Livello=£OAVLI
                       EVAL      Tipo=£OAVOT
                       EVAL      Parametro=£OAVOP
                       EVAL      Intestazione=£OAVIN
                       EVAL      Attributo=£OAVSI
                       EVAL      Mes.live_trovato=£OAVM1
                       EVAL      Mes.val_multiplo=£OAVM2

