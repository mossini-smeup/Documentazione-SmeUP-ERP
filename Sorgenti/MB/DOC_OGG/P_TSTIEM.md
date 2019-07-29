# Obiettivo
La routine serve per decodificare, ricercare, validare l'esponente di modifica di un oggetto.

# Funzioni e metodi
_1_Funzioni e _5_Metodi
 * _1_Blanks, Restituisce indicatore di errore acceso se non esiste esponente di modifica dell'oggetto.
 * _1_RIC, Ricerca esponente di modifica dell'oggetto. Viene richiamato il programma di lista degli esponenti di modifica con la possibilità di scegliere l'esponente.
 * _1_VAL, Ritorna il primo esponente valido rispetto alla data impostata nel metodo
** _5_INI, alla data di validità
** _5_D01, alla data libera DT01
** _5_D02, alla data libera DT02
** _5_D0......
** _5_COD, controlla la validità rispetto al parametro passato
 * _1_CRV, Ricerca se non impostato l'esponete di modifica valido ad una data, se impostato  ne controlla la  validità. La data utilizzata è quella descritta nel metodo
** _5_INI, alla data di validità
** _5_D01, alla data libera DT01
** _5_D02, alla data libera DT02
** _5_D0......
** _5_COD, controlla la validità rispetto al parametro passato

# Input
I dati di input oltre alla funzione e metodo sono passati tramite la DS del file C£ESMO e le variabili £IEMPA(tipo esponente) e £IEMCD(codice esponente)

# Output
La routine restituisce al programma chiamante valorizzati i campi della DS del file C£ESMO e la variabile £IEMCD

# Prerequisiti
Prerequisiti per l'utilizzo della routine sono : 
IC£ESMO    E DSC£ESMO0F

# Esempio di chiamata per ricerca/controllo validità dell'esponente di modifica di un articolo al 01/07/09

>C                   EVAL      E£CODI=W$ARTI
C                   EVAL      £IEMFU='CRV'
C                   EVAL      £IEMME='INI'
C                   EVAL      £IEMPA='AR'
C                   EVAL      £IEMCD=W$ESMO
C                   EVAL      E£DTIV=20090701
C                   CLEAR     £IEMAM
C                   EXSR      £IEM
C     £IEM35        IFEQ      *ON
C                   ......
C                   ELSE
C                   EVAL      W$ESMO=£IEMCD
C                   ENDIF


# Note particolari
 * L'archivio in cui sono registrati gli esponenti di modifica di Sme.up è normalmente il C£ESMO0F   nei casi in cui è richiesto   un processo di di Work-flow di rilascio degli esponenti si può utilizzare l'archivio CQDOMA0F con   attivazione in tabella B£1.
 * In quest'ultimo caso valgono solo i metodi per data inizio validità.
