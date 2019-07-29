# Obiettivo
   Lanciare la Gestione Note Strutturate B£AMC0.
   Gestire uno spazio a formato libero dove inserire delle note di svariato genere (es. tipico documentazione), riconducibili    ad uno o più specifici oggetti esistenti sul sistema, utilizzando come chiave di identificazione da 1 a 3 livelli di    codici, generici o specifici.

# Funzioni e metodi

   B£NST1
   Con la /  : 
   verifica che l'ambiente delle Note Strutturate specificato a programma sia corretto, confrontandolo con i parametri    specificati nelle tabelle interessate per le Note Strutt.

   Con il ! o il ?  : 
   visualizza le varie opzioni che si possono eseguire in un determinato programma. Questa schiera di opzioni viene creata    controllando i valori che ci sono nei campi MODALITA' e VINCOLI

# Input

   Descrizione Campi : 
    £NSTAZ  :  Azione da eseguire  :  G = Gestione
                                  I = Interrogazione
                                  A = Annullamento
                                  S = Stampa
    £NSTRC  :  Se C=esegue controlli/decodifiche param. in entrata
    £NSTCA  :  Tipo contenitore assunto (in tabella NSC)
    £NSTA1  :  Valore assunto 1 per ripresa note
    £NSTA2  :  Valore assunto 2 per ripresa note
    £NSTA3  :  Valore assunto 3 per ripresa note

  Input : 
    £NSTTC  :  Tipo contenitore (descritto in tabella NSC)
    £NSTCx  :  Codice x
    £NSTPG  :  Nome programma chiamante
    £NSTTO  :  Tipo origine (o TA=tabella o *BLANKS)
    £NSTPO  :  Parametro origine (se non è BLANKS £NSTTO)
    £NSTEO  :  Elemento origine  (se non è BLANKS £NSTTO)
    £NSTT1  :  Tipo codice 1
    £NSTT2  :  Tipo codice 2
    £NSTT3  :  Tipo codice 3
    £NSTP1  :  Parametro codice 1
    £NSTP2  :  Parametro codice 2
    £NSTP3  :  Parametro codice 3
    £NSTMT  :  Modalità di richiamo programma

             N : B :   :  Se è = BLANKS il richiamo al programma B£NST1
                    non viene eseguito, resta la vecchia gestione
                    delle note (precedente 04/1996)

          01/11 = Immissione --> include gli elementi della tab
                  B£R che hanno i seguenti val. nel campo T$AZFU : 
                  C G S V
          02/12 = Modifica   --> include tutti gli elementi della
                  tabella B£R
          05/15 = Visualizz. --> include gli elementi della tab
                  B£R che hanno i seguenti val. nel campo T$AZFU : 
                  B I S V
    £NSTVI  :  Vincoli alle funzioni tabella B£R  : 

                 Se il campo è BLANKS tutte le funzioni della
                 B£R sono attive

                 1  = NOTE STRUTTURATE
                 2  = LISTE DI DISTRIBIZIONE
                 3  = INFORMAZIONI

             Ex. 1 ---> ho attive solo le funzioni delle
                        NOTE STRUTTURATE
                 2 ---> ho attive solo le funzioni delle
                        LISTE DI DISTRIBUZIONE
                 1/2- > ho attive le funzioni per le
                        NOTE STRUTTURATE e le LISTE DI DISTRIBUZ.
                 1/2/3 o 1/3 , etc ....

  Parametri Facoltativi : 
    £NSTIx  :  Intestazione codice x (x da 1 a 3)
              Descrive il significato del codice
              Es. ARTICOLO
              (Se i codici 1/2/3 sono di un tipo specifico il
              campo viene decodificato)
    £NSTDx  :  Decodifica per il codice x
              Es. per ARTICOLO = scatola per imballo
              (Se i codici 1/2/3 sono di un tipo specifico il
              campo viene decodificato)
    £NSTPR  :  Progressivo se si vuole andare alla riga

# Output

    £NSTRC  :  Flag return code -> Se <>blank=errore
    £NSTPA  :  Parametro azione (GC CC AC WL .....)
    £NST35  :  ON per £NSTPA sbagliato
    £NST36  :  ON per £NSTPA = ! ? /

# Prerequisiti

Nessuno

# Esempio di chiamata

  --- >  BEGSR £INIZI

     C*                  EVAL           £NSTTC= Tip_Conten
     C*                  EVAL           £NSTPG= PgmChiamante
     C*                  EVAL           £NSTTO= Tip_Origine
     C*                  EVAL           £NSTPO= Par_Origine
     C*                  EVAL           £NSTEO= Ele_Origine
     C*                  EVAL           £NSTT1= Tip_Cod1
     C*                  EVAL           £NSTT2= Tip_Cod2
     C*                  EVAL           £NSTT3= Tip_Cod3
     C*                  EVAL           £NSTP1= Par_Cod1
     C*                  EVAL           £NSTP2= Par_Cod2
     C*                  EVAL           £NSTP3= Par_Cod3
     C*                  EVAL           £NSTMT= Metodo
     C*                  EVAL           £NSTVI= Metodo

  --- >  BEGSR NOTE

     C*    £RPRF1        IFNE      *BLANKS
     C*                  EVAL      £NSTPA= Par_az
     C*                  EVAL      £NSTC1= Cod1
     C*                  EVAL      £NSTC2= Cod2
     C*                  EVAL      £NSTC3= Cod3

   Parametri facoltativi
     C*                  EVAL      £NSTTI= El_NSI
     C*                  Z-ADD     0             £NSTPR
     C*                  EVAL      £NSTI1= Int1
     C*                  EVAL      £NSTI2= Int2
     C*                  EVAL      £NSTI3= Int3
     C*                  EVAL      £NSTD1= Des1
     C*                  EVAL      £NSTD2= Des2
     C*                  EVAL      £NSTD3= Des3
     C*                  EVAL      £NSTA1= Ass1
     C*                  EVAL      £NSTA2= Ass2
     C*                  EVAL      £NSTA3= Ass3
      *
     C*                  EXSR      £NST
     C*                  EVAL      £NSTPA= £RPRF1


  ESEMPIO DI CHIAMATA PER VERIFICHE VELOCI
     C*                  EVAL      £NSTPA= VN_VD
     C*                  EVAL      £NSTTC= El_NSC
     C*                  EVAL      £NSTC1= Cod1
     C*                  EVAL      £NSTC2= Cod2
     C*                  EVAL      £NSTC3= Cod3
     C*                  EVAL      £NSTTI= El_NSI
     C*                  EXSR      £NST
     C*    £NSTRC        IFNE      *BLANKS
     C*                  ENDIF


# Note particolari

