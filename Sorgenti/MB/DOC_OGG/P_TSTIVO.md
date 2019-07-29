# OBIETTIVI

 Questa /COPY permette di consultare le voci presenti in un contenitore.

# IL CONTESTO

 Il contenitore è il nome del membro che si intende analizzare e le
 voci sono le righe che hanno come TAG iniziale '..VOC'

# FUNZIONI/METODI

## RIC - Ricerca
      Permette all'utente di ricercare le voci nel contenitore
      selezionato.Non ha bisogno di nessun metodo ma del nome
      del contenitore; di seguito verrà richiesta la voce da ricer-
      care scegliendo tra quelle disponibili.

## DEC - Decodifica
      Controlla la presenza di una voce; non ha bisogno del metodo
      ma del nome del contenitore in cui eseguire la verifica. Se
      il campo voce è vuoto o la voce indicata non è presente
      verrà specificato 'VOCE NON PRESENTE'

## LIS - Lista
      Permette all'utente di visualizzare la lista delle voci
      all'interno del contenitore; necessita del contenitore e dopo
      aver eseguito il posizionamento mostra le voci una per volta
      fino alla fine dello stesso.

###   POS - Posiziona
      Si posiziona sulla prima voce del contenitore e la
      visualizza in uscita.

###   LET - Lettura
      Inizia a leggere le voci partendo dalla voce
      selezionata precendentemente dal POS; ad ogni esecuzione
      mostra la voce successiva fino alla fine del contenitore.

## CON - Contenuto
      Permette all'utente di visualizzare le righe di ogni
      voce.Ha bisogno del metodo, del contenitore e della voce
      su cui posizionarsi e poi leggere.

###   POS - Posiziona
      Si posiziona sulla voce indicata nel campo specifico.
      Visualizza in uscita la prima riga della voce selezionata
      se esiste all'interno di essa.

###   LET - Lettura
      Inizia a leggere le righe partendo dalla voce
      selezionata precendentemente dal POS, fino alla fine delle
      righe della voce stessa.


