# OBIETTIVO
Validare i dati di un articolo. Solitamente usata in abbinamento alla £IAR permette di controllare i campi di un articolo utilizzando il meccanismo del monitor-controller-video.
Questa /copy è stata pensata per i casi in cui l'inserimento o la modifica di un articolo deve essere fatta in modo batch controllandone la validità.
Il tester permette il controllo dei campi obbligatori quali il tipo articolo, il codice, la  descrizione , l'unità di misura e il tipo parte.
Per controllare altri campi specifici definire un visualizzatore specifico.
(Si veda la tabella BRA per tipo articolo)

NOTA TECNICA
Se usate la /copy £BRX in un programma assieme alla £IAR nelle specifiche dei dati basta la £IARDS
(non includere anche la definizione esterna del BRARTI0F)

# FUNZIONI E METODI

## 01 Inserimento
La funzione 01 permette la verifica prima della scrittura di un articolo. Se richiamato anche il metodo INI richiama anche la routine INIDOC specificata nel visualizzatore (std o specifico)
Vedere la sezione INDICAZIONE ERRORI per vedere come vengono segnalati i possibili errori.

## 02 Modifica
La funzione 02 permette di testare i campi prima della modifica dell'articolo.
Vedere la sezione INDICAZIONE ERRORI per vedere come vengono segnalati i possibili errori.

# INDICAZIONE ERRORI
In caso di errori viene acceso l'indicatore 35 e vengono riempite le 3 schiere WEC,WEF,WEV, le quali rispettivamente contengono : 
 * WEC i codici di messaggio per ogni campo in erroer
 * WEF i file di messaggio relativi ai codici
 * WEV i valori da impostare nel messaggio
Inoltre viene restituita una schiera DFT che contiene tutti i campi del visualizzatore.
Tramite la DS $DF ho tutti i campi della schiera tra cui menzoniamo $DFCAM che contiene il nome del campo

Di seguito un esempio esemplificativo con emissione di un possibile messaggio di errore : 

>                    FOR       $A=1 TO %ELEM(WEC)
                    IF        WEC($A)<>*BLANKS
                    EVAL      £DMSAZ='7'
                    EVAL      £DMSME=WEC($A)
                    EVAL      CODMES=WEC($A)
                    EVAL      £DMSFI=WEF($A)
                    EVAL      £DMSVA=WEV($A)
                    EXSR      £DMSG
                    EVAL      $DF=DFT($A)
 *
                    EVAL      £DMSME=''
                    EVAL      £DMSFI=''
                    EVAL      £DMSAZ='1'
                    EVAL      £DMSTI='INFO'
                    EVAL      £DMSTE=%TRIM($DFCAM)+' '+%TRIM(£DMSTE)
                    EXSR      £DMSG

