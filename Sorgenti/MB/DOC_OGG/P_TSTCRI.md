# Obiettivo

Controllo/Gestione ricorsione

# Funzioni e metodi

 FUNZIONE    '     '  :  emette finestra con segnalaz.ricorsione e ritorna msg BAS0118

 Nelle /COPY di interfaccia viene eseguita la routine in questa modalità, ma viene lanciato il programma ritornato :   se si vuol fare eseguire la duplicazione si dovrà modificare funzione e metodo prima del lancio :  ricordare che all'uscita  della routine essi vengono puliti, quindi ritornano al default (solo controllo), e quindi, se si vuol far fare la  duplicazione in più punti bisogna impostarlo esplicitamente ogni volta.

 FUNZIONE    'NOMSG'  :  se ricorsione ritorna msg BAS0118

 FUNZIONE    'RITL'   :  ritorno del livello di chiamata
      METODO '    '   :  se non riesce emette formato e ritorna
                       msg BAS0118
             'NOMSG'  :  se non riesce ritorna solo msg BAS0118

 FUNZIONE    'ULPG'   :  ritorno l'ultimo pgm nello stack prima
                       del chiamante
      METODO '    '   :  ritorno l'ultimo pgm nello stack prima
                       del chiamante
             'BEFORE' :  ritorno del prpgramma dello stack
                       precedete quello passato in £CRIPG
           'BEFORENQ' :  ritorno del prpgramma dello stack
                       precedete quello passato in £CRIPG
                       escludendo quelli il cui nome inizia
                       per Q (pgm di sistema)

 FUNZIONE    'VIS '   :  Presenta a video lo stack delle chiamate

 Altri parametri per questa funzione
  Output £CRILC   :  livello di chiamata eseguibile

# Input
£CRIPG - Programma da controllare se esistente
£CRIFU - Funzione di controllo
£CRIME - Metodo di controllo

# Output

£CRIPG - Programma da lanciare
£CRIMS - Se non a blanks messaggio d'errore

# Prerequisiti

Nessuno

# Esempio di chiamata

 C*                  EVAL      £CRIPG=Nome_programma
 C*                  EVAL      £CRIFU='Funzione'
 C*                  EVAL      £CRIME='Metodo'
 C*                  EXSR      £CRI

# Oggetti collegati

# Note particolari
