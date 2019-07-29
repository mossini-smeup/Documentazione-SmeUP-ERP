# Obiettivo
Interrogazione DISTINTA BASE prevista nella tabella di personalizzazione applicazioni B£1

# Input

Campi fondamentali

£DIBSP   :  ' ' - inizio scansione
          '1' - continua scansione (è riempito dalla routine)
          'L' - interrompe il ramo e prosegue con l'elemento
                successivo dello stesso livello

£DIBPG   :  se non blanks lancia il programma con questo
          suffisso :  serve nel caso in cui ci siano due
          scansioni di distinta attive contemporaneamente
          nella stessa applicazione (lanciate da programmi
          diversi).

N.B. Deve essere ripulito anche in caso di gestione singolo
     legame (funzione 'GD')



# Output

  *IN35  :  se On = fine scansione

# Prerequisiti

D/COPY QILEGEN,£DIBE


# Esempio di chiamata
Esempio 1 :  scansione distinta ordine di produzione

     C*                  EVAL      £DIBSP=' '                               *BLANKS = inizio scansione
     C*                  EVAL      £DIBFU='DD'                              Funzione
     C*                  EVAL      £DIBME=' '                               Metodo
     C*                  EVAL      £DIBPG=' '                               Suffisso programma di aggiustamento
     C*                  EVAL      £DIBQT=1                                 Quantità
     C*                  CLEAR                   £DIBDT                     Data Validità
     C*                  EVAL      £DIBCG=''                                Configurazione
     C*                  EVAL      £DIBLM=0                                 Livello Massimo
     C*                  CLEAR                   £DIBIT                     Tipo Distinta
     C*                  EVAL      £DIBIC=N.ordine                          numero ordine di produzione
     C*                  EVAL      £DIBIS='10'                              Stato
     C*                  EVAL      £DIBIQ=''                                Sequenza Ciclo
     C*                  EVAL      £DIBIR=0                                 N.Record
     C*                  EVAL      £DIBI1=''                                Par.condiz.1
     C*                  EVAL      £DIBI2=''                                Par.condiz.2
     C*                  EVAL      £DIBFE=''                                Esponente Modifica
     C*                  EVAL      £DIBEI=''                                Esp.Componente
     C*
     C*                  DO        *HIVAL        $H                3 0
     C*                  EXSR      £DIB
     C*                  IF        £DIB35=*ON                               Indicatore errore
     C*                  LEAVE
     C*
     C*                  ENDIF
     C*                  EVAL      componente=£DIBCO
     C*                  EVAL      coefficente di impiego=£DIV(6)
     C*                  EVAL      configurazione componente=£DIBS2
     C*                  ENDDO

Esempio 2 :  scansione distinta di un articolo

     C*                  EVAL      £DIBSP=' '                               *BLANKS = inizio scansione
     C*                  EVAL      £DIBFU='ED'                              Funzione
     C*                  EVAL      £DIBME='3'                               Metodo
     C*                  EVAL      £DIBQT=100                               Quantità
     C*                  EVAL      £DIBIC=Codice articolo                   Codice Articolo
     C*
     C*                  DO        *HIVAL        $H                3 0
     C*                  EXSR      £DIB
     C*                  IF        £DIB35=*ON                               Indicatore errore
     C*                  LEAVE
     C*                  ENDIF
     C*
     C*                  EVAL      componente=£DIBCO
     C*                  EVAL      coefficente di impiego=£DIV(6)
     C*                  EVAL      configurazione componente=£DIBS2
     C*                  ENDDO

# Note particolari

