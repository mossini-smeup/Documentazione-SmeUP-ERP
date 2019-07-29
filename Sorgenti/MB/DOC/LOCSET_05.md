# L'utilizzo dei setup nei servizi

## Matrice
Tutti i servizi, se non disabilitandone la funzione, eseguiranno sempre la comunicazione del default utente.

### Disabilitazione dell'invio del setup di default dell'utente
Per disabilitare il default bisogna eseguire le seguenti operazioni : 
* Se il servizio gestisce l'invio interno di setup programm, utilizzare il richiamo alla routine £JAX_DSET
* Se il servizio non gestisce setup interni dopo aver eseguito la routine £JAX_IMP0 impostare il campo £JAXCSC a "2"

### Gestione del setup interno al servizio
 Le routine disponibili sono : 
 £JAX_ISET, inizializza l'xml del setup program :  deve ricevere la struttura, il contesto e gli attributi da assegnare al nodo program, fatta eccezzione dell'attributo Context.
Esempio : 
C                   EVAL      £J15ST='EDT_SCH/G.SET.MAT'
C                   EVAL      £J15CO=%TRIM(£UIBFU)+'\'+%TRIM(£UIBME)+'\'
C                                   +%TRIMR(£UIBT1)+%TRIMR(£UIBP1)
C                   EVAL      £JAXCP='Title="Titolo"'
C                   EXSR      £JAX_ISET

 £JAX_ASET, Aggiunta di un setup.
Esempio : 
C                   EVAL      £JaxCP='Parent="A01" Name="Standard"'
C                   EXSR      £JAX_ASET
                    ....
                    ....
C                   EVAL      £JaxCP='Parent="A02" Name="Base"'
C                   EXSR      £JAX_ASET

 £JAX_ASETM, Aggiunta di setup multipli in un'unica chiamata
Esempio : 
C                   EVAL      £JaxCP='<Setup Parent="A01" Name="Standard" /> '
C                                   +'<Setup Parent="A02" Name="Base" />'
C                   EXSR      £JAX_ASETM

 £JAX_USET, Scrittura Setup salvati dall'utente
Esempio : 
C                   EVAL      £J15ST='EDT_SCH/G.SET.MAT'
C                   EVAL      £J15CO=%TRIM(£UIBFU)+'\'+%TRIM(£UIBME)+'\'
C                                   +%TRIMR(£UIBT1)+%TRIMR(£UIBP1)
C                   EXSR      £JAX_USET

 £JAX_DSET, Disabilita la possibilità di gestire il default utente
Esempio : 
C                   EXSR      £JAX_DSET

 L'esecuzione della £JAX_FIN0 completerà il setup con il default utente ed invierà l'intera struttura xml.                                                                                    
