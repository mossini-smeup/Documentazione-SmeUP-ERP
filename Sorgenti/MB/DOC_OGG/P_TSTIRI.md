# Obiettivo
Interfacciare il programma in esecuzione con l'anagrafico risorse.
Eseguire la ricerca alfabetica relativa se richiesto


# Input

£IRIFU :  Funzione
£IRIME :  Metodo
£IRIAM :  Ambiente
£IRICO :  Contesto
£IRICD :  Codice risorsa  (se funzione = *Blanks)
£IRITR :  Tipo   risorsa  (se funzione = *Blanks)
£IRIRI :  N.ro Record di input
£IRILC :  Livello chiamata

# Output

£IRICD :  Risorsa  (se eseguita ricerca)
£IRIDE :  Descrizione
£IRIMS :  Codice messaggio ritorno
£IRIFI :  File   messaggio ritorno
£IRICM :  Ultimo Comando
£IRIRO :  N.ro record di output
*IN35  :  se On = Codice errato
*IN36  :  se On = eseguita ricerca alfabetica
BRRISO :  DS valorizzata

# Prerequisiti
D/COPY QILEGEN,£IRIDS

# Esempio di chiamata

  1) ricerca/decodifica/controllo risorsa

C*                  EVAL      £IRICD= Risorsa
C*                  EVAL      £IRITR= Tipo
C*                  EXSR      £IRI
C*                  EVAL      Descrizione= £IRIDE
C*                  EVAL      Risorsa    = £IRICD
C*                  EVAL      Record_BRRISO

 2) SETLL+READE sul logico BRRISO3L (tipo risorsa/gruppo risorsa)

C*                  CLEAR                   BRRISO
C*                  EVAL      £IRIFU='SLRE'
C*                  EVAL      £IRIME='3L'
C*                  EVAL      C§TRIS='CDL'
C*                  EVAL      C§DEPT='AAA'
C*                  DO        *HIVAL
C*                  EXSR      £IRI
C*                  IF        £IRIMS='FINE'
C*                  LEAVE
C*                  ENDIF
C*
C*                  utilizzo dei campi del BRRISO
C*
C*                  EVAL      £IRIFU='RE'
C*                  EVAL      £IRIME='3L'
C*                  ENDDO

# Note particolari

è preferibile eseguire un clear della DS BRRISO prima di ogni utilizzo.

£IRINK :  Numero di campi che si vuole utilizzare nella ricerca.
Non valorizzare £IRINK per lasciare al programma il compito di stabilire il numero di chiavi da usare. £IRINK viene inserito nell'ultimo char di £IRIME al richiamo dell'interfaccia

