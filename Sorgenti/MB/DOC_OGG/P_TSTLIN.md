Programma di test della £LIN

# OBIETTIVO
Inizializzare le schiere interne ai programmi definite a tempo di compilazione nella lingua assunta specificata nella tabella B£2.

# FLUSSO
Ogni programma contenente schiere interne, nella routine £INIZI richiama una routine denominata per questioni di "convenzione standard" £INIZL, la quale per ogni schiera definita richiama la routine £LIN passandogli contenuto, nome, tipologia della schiera, viene tradotta, inserita nel database delle traduzioni  in lingua se mancante, ed infine restituito il contenuto tradotto e quindi reso disponibile al programma per l'utilizzo.

# PREREQUISITI
D/COPY QILEGEN,£LINE

## Parametri in input
- £LINFU -  funzione :  se blanks assunta TRA
- £LINME -  metodo :    blanks
- £LINNC -  nome rpg della schiera (10)
- £LINTC -  tipo schiera (V2-T$SVK) (opzionale ) se non fornito assunto TXT (15)
- £LINSC - contenuto della schiera (80 x 300 el.)
        -  riga 1 di schiera da tradurre (obbligatoria)
         -  riga 2 di schiera da tradurre
         -  riga 3 di schiera da tradurre
- £LINLD -  lingua in cui tradurre :  (opzionale) se blanks dedotta dalla tabella B£1. Il parametro viene pulito ad ogni richiamo

## Parametri output
- £LINSC - contenuto della schiera tradotto
         -   riga 1 di schiera tradotta
         -   riga 2 di schiera tradotta
         -   riga 3 di schiera tradotta
- £LINLU -   lunghezza delle costanti (quello che viene effettivamente tradotto)

_1_NOTA 1 :  la lunghezza delle schiere in input è limitata a 70 caratteri
_1_NOTA 2 :  la £LIN riceve in ingresso una schiera di max 300 elementi lunghi 80. Qui viene simulata una schiera di 3

# ESEMPIO DI CHIAMATA

(da inserire in £inizi)

C £INIZI BEGSR
* Inizializzazione schiere interne in lingua
C ££B£2I IFNE *BLANKS
C EXSR £INIZL
C ENDIF
C ENDSR
 *---------------------------------------------------------------
 * inizializzazione schiere interne in lingua
 *---------------------------------------------------------------

C £INIZL BEGSR
C MOVEL<nome sch>£LINNC P
C MOVEL<tipo sch>£LINTC P
C CLEAR£LINSC
C MOVEL<schiera> £LINSC
C EXSR £LIN
C MOVEL£LINSC <schiera>
C ENDSR
C/COPY QILEGEN,£LIN
