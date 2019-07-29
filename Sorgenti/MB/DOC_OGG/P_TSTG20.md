# Obiettivo
La routine serve per reperire le informazioni di sintesi degli avanzamenti dell'oggetto Ordine di Produzione (OR) e dell'oggetto riga documento (DR)

# Funzioni e metodi
_1_Funzioni e _5_Metodi
 * _1_RIT, Ritorna le informazioni nei campi della DS £G20DS sulla base dei metodi scelti che andiamo a descrivere : 
 ** _5_LAS, Restituisce l' ultima operazione dell'oggetto. Ricordo che se il campo di tabella T$P51S è " " come ultima  operazione viene calcolata  la maggiore tra gli impegni risorse residui e l'ultima attività consuntivata, in caso contrario  la maggiore tra  l'ultima del ciclo di lavorazione e l'ultima attività consuntivata. Quest'ultima modalità (T$P51S='1') dà l'opportunità di gestire correttamente l'ultima fase anche per quelle produzioni "lunghe" in cui in corso di lavorazione si cambia l'alternativa di ciclo.
** _5_LAD, Restituisce le  seguenti date : 
*** _2_£G20D1   Utimo movimento magazzino
*** _2_£G20D2   Utima dichiarazione di avanzamento
*** _2_£G20D3   Utimo movimento assoluto  (maggiore dei precedenti)
*** _2_£G20D4   Data della prima dichiarazione di attività
** _5_FIR, Restituisce la prima fase del ciclo con l'informazione se completata	
** _5_SCH, Restituisce le date di schedulazione a capacità finita ed infinita
** _5_ALL, Restituisce tutte le informazioni dei precedenti metodi
 * _1_PRES, Ritorna le stesse informazioni dei metodi previsti dalla funzione RIT con la differenza che le presenta a video.
 * _1_SQF, Ritorna la quantità esistente alla fase di lavorazione di uno specifico ordine
** _5_BUO, Restituisce solo la fasi per cui esiste una quantità alla fase
** _5_ALL,  Restituisce tutte le fasi anche quelle per cui non esiste una quantità residua alla fase di lavorazione
 * _1_SQF_TOT, Ritorna la quantità completata e scartata per ogni fase dell'oggetto che stiamo scandendo con i seguenti metodi : 
** _5_BUO, Restituisce solo la fasi per cui è stata avanzata una quantità
** _5_ALL,  Restituisce tutte le fasi anche quelle per cui non è stato fatto avanzamento
 * _1_SQD,  Ritorna le stesse informazioni della funzione SQF con la differenza che calcola la situazione alla data impostata nella variabile £FUNDT. Il test viene fatto data di elaborazione compresa e quindi parliamo di situazione alla sera.
 * _1_SQD_TOT,  Ritorna le stesse informazioni della funzione SQF_TOT con la differenza che calcola la situazione alla data impostata nella variabile £FUNDT. Il test viene fatto data di elaborazione compresa e quindi parliamo di situazione alla sera


# Input
I dati di input oltre alla funzione e metodo sono passati tramite la DS £FUNDS1, la quale contiene il tipo oggetto parametro che deve essere processato.




# Output
La routine restituisce al programma chiamante valorizzati i campi della DS £G20DS

# Prerequisiti
Prerequisiti per l'utilizzo della routine sono le /copy : 
£G20DS
£FUNDS1


# Esempio di chiamata per scansione quantità alla fase di un ordine di produzione

>C                   MOVEL(P)  'SQF'         £G20FU
C                   MOVEL(P)  'ALL'         £FUNT1
C                   MOVEL(P)  'OR'          £FUNT1
C                   MOVEL(P)  K§NORD        £FUNK1
C                   MOVEL(P)  *BLANKS       £G20MS
C                   EXSR      £G20
C     £G20MS        DOWEQ     'CONT'
C                    ....... 	
C                    .........
C
C
C                   EXSR      £G20
C                   ENDDO


# Esempio di chiamata per ritorno informazioni di un ordine produzione

>C                   MOVEL(P)  'RIT'         £G20FU
C                   MOVEL(P)  'LAD'         £G20ME
C                   MOVEL(P)  'OR'          £FUNT1
C                   MOVEL(P)  K§NORD        £FUNK1
C                   EXSR      £G20



# Note particolari
.
