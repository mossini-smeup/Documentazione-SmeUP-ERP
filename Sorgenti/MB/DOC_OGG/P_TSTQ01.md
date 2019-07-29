# ESECUZIONE B£QQ01

## OBIETTIVI
 Gestire l'utilizzo del comando B£QQ01 centralizzando le operazione da eseguire in un unico punto.

**Si ricorda che come tutte le nuove routine i parametri di INPUT sono cancellati ad ogni
**esecuzione.
**Che sono presenti 2 ds, una di input e una di output


## UTILIZZO DELLA ROUTINE
La routine è utilizzata principalmente per eseguire i comandi di B£QQ01 dal pgm _2_LANCIANTE
ma anche dal programma _4_LANCIATO per leggere i parametri di input e scrivere quelli di output.
Sono previste numerovoli repliche per utilizzare contemporaneamente più lavori
Per la spiegazione del flusso "normale" delle funzioni è scritto in fondo alla documentazione un
esempio. E' presente anche un esempio di _2_LANCIANTE e _4_LANCIATO vedi B£Q010I e B£Q011O in
SMESRC

## FUNZIONI E METODI

### INZ       Inizializzazione routine
**E' obbligatoria per ogni inizio ciclo di comandi nel programma _2_LANCIANTE**, reperisce in
**automatico il UUID dell'esecuzione del comando


### CMD       Esecuzione comando
**Con la funzione CMD si lancia un comando nell'ambiente specificato.
_1_.          .Comando singolo
Nell'esecuzione singola viena lanciato  un solo comando e quando questo ha finito l'esecuzione
il lavoro sottomesso termina.
_1_.INZ       .Apertura lavoro batch e 1° comando
_1_.CMD       .Ripetizione comando
_1_.END       .Chiusura lavoro batch
Se si vuole eseguire più volte un comando (anche diverso uno dall'altro) ma lasciare il lavoro
sottomesso in attesa dei successivi bisogna operare come segue : 
metodo **INZ** al primmo comando
metodo **CMD** ai successivi
Metodo **END** dopo l'ultimo (att.ne questo metodo non esegue comandi)

_3_ATTENZIONE
_3_Lanciare il metodo CMD/END senza avere fatto un CMD/INZ manda il lavoro in loopp in
_3_quanto viene scritta una coda dopo di chè il programma aspetta una risposta che nessuno darà,
_3_quindi viene creato un loop (in realtà un attesa infinita).
_3_Lanciare il metodo CMD/INZ senza fare il metedo CMD/END lascia aperto e quindi attivo il
_3_lavoro sottomesso

### WRIPAR    Scrittuara Parametri
_1_.INP       .Dati di Input
Viene utilizzato dal programma_2_LANCIANTEper scrivere i parametri che dovranno essere
letti dal programma _4_LANCIATO
_1_.OUT       .Dati di Output
Viene utilizzato dal programma _4_LANCIATOper scrivere i parametri che dovranno essere
letti dal programma _2_LANCIANTE

### LETPAR    Lettura Parametri
_1_.INP       .Dati di Input
Viene utilizzato dal programma _4_LANCIATOper leggere i parametri scritti dal programma
_2_LANCIANTE
_1_.OUT       .Dati di Output
Viene utilizzato dal programma _2_LANCIANTEper leggere i parametri scritti dal programma
_4_LANCIATO_

### UUID      Universally unique identifier
_1_.          .Generazione
Viene generato un UUID che può essere utilizzato da qualsiasi programma
Implementa DCE version 1 UUID , basato su MAC address e calcolo dell'istante con precisione al nanosecondo.
_1_.JOB       .Recupero UUID del job
**Questo metodo è utilizzato all'inizio dal programma _4_LANCIATO** per recuperare l' UUID del
**programma _2_LANCIANTE**


_3_ Usare una replica per ogni lavoro (ambiente diverso) sottomesso


## ESEMPIO DI FLUSSO ESECUZIONE CON PARAMETRI IN INPUT E OUTPUT

_2_Programma lanciante

          **inizio lavoro
          FUNZIONE   _3_INZ
          METODO     _1_.
          £Q01I_LC='A'

          **Scrivo parametri da passare al pgm _4_LANCIATO
          FUNZIONE   _3_WRIPAR
          METODO     _1_.INP
          £Q01I_LC='A'

          **Eseguo primo comando ambiente A
          FUNZIONE   _3_CMD
          METODO     _1_.INZ
          £Q01I_LC='A'

          _4_PROGRAMMA CHIAMATO       ----->    **Recupero UUID
                                                FUNZIONE   _3_UUID
                                                METODO     _1_.JOB
                                                £Q01I_LC=' '

                                                **leggo parametri passati dal _2_LANCIANTE**
                                                FUNZIONE   _3_LETPAR
                                                METODO     _1_.INP
                                                £Q01I_LC=' '


                                                **Eseguo programma

                                                **Scrivo parametri da passare Al _2_LANCIANTE**
                                                FUNZIONE   _3_WRIPAR
                                                METODO     _1_.OUT
                                                £Q01I_LC=' '


          **leggo parametri passati  <-----    _2_PROGRAMMA LANCIANTE
          FUNZIONE   _3_LETPAR
          METODO     _1_.OUT
          £Q01I_LC=' '

          **dal secondo lancio di comando eseguire
          FUNZIONE   _3_CMD
          METODO     _1_.CMD
          £Q01I_LC='A'


          **Alla chiusura dei lanci eseguire
          FUNZIONE   _3_CMD
          METODO     _1_.END
          £Q01I_LC='A'


          **Attenzione se si lancia il metodo _1_END senza aver lanciato almeno un _1_INZ**
          **il programma va in loopo

          **Attenzione se non si lancia il metodo _1_END dopo aver lanciato il _1_INZ**
          **il lavoro sottomesse _1_NON VIENE PIU' chiuso**


