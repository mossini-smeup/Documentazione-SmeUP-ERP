# I.IF      - Condiziona il considerare le specifiche seguenti
      Posso gestire livelli annidati. In tal caso una specifica viene considerata
      se e solo se tutti i livelli precedenti sono abilitati
## Metodi
### .AUT - Autorizzazioni
Le autorizzazioni sono gestite dalla classe SCHEDA che ha come funzione il nome della scheda.
La tipologia è quella degli stati e degli OAV
- Numeri da 00 a 99 in 10 gruppi da 10
- Bianco = tutto autorizzato
- 36    = da 30 a 36 autorizzato, da 37 a 39 non autorizzato

Parametri
1 = Livello desiderato (se bianco assume tutto autorizzato)
### .OPE - Operatore su fattore 1 e fattore 2
Parametri
- F1 Fattore 1
- F2 Fattore 2
- OP Operatore > >= < <= <> =
- TC Tipo campo - N indica che il confronto deve essere fra numeri.
Tecnicamente la comparazione fra stringhe viene svolta dalla funzione £G83 cui si rimanda per il test e i dettagli.
### .ESI - Verifica di esistenza di un oggetto
La condizione è valida se l'oggetto indicato esiste in SME.up. L'oggetto può in particolare essere un altro script quindi ad esempio condiziono il richiamo di una sottoscheda in base all'esistenza della sua definizione.

### .END - Chiude l'ultimo livello aperto
### .ELS - Inverte la condizione del livello ultimo

# I.INC - Inclusione di uno script
## Metodi
- .MBR    - Dello script contenuto in un membro
- .PGM - Dello script generato da un programma
## Parametri
Per l'inclusione di un membro : 
      Lib :  Libreria (assume *LIBL)
      Fil :  File     (assume SCP_SCH)
      Mem :  Membro
Per l'inclusione da un programma : 
      Pgm :  Programma
      Fun :  Funzione
      Met :  Metodo
      Ent :  Formato della entry del programma
      Par :  Parametri di input al programma

NOTE :  -Ent può essere "SER" se il programma è un servizio, oppure non specificato per pgm con entry speciale (v. JASRC/LOSCH_01)
- Se il programma è un servizio Fun e Met verranno passati nello stesso campo lungo 10 come Fun.Met
- Par è lungo 512 nei pgm con entry speciale, 256 nei servizi.

# I.LOP Identificazione di un blocco da ripetere N volte con sostituzioni
A seconda della funzione, il programma costruisce (o fa costruire da altro programma) una lista di valori (VA) significati ($LO.SI) Parametri ($LO.PA).
Individua l'insieme delle  righe fino a ..END e le ripete per il numero di elementi trovati.

Valgono i seguenti limiti : 
- Massimo numero di elementi variabili            50
- Massimo numero di righe di script da ripetere   50
## Metodi
### .IMG - Lista delle immagini (Funzione SCA della API £IMM)
### .GPA - Gruppi di parametri (Lista oggetti di tipo MD OA-xx dove xx è il tipo oggetto)
### .DOC - I documenti presenti in un membro
### .OGG - Gli oggetti di un tipo specificato


# I.XML Trasferisce direttamente a XML senza trasformazione
Il primo XML viene assunto come inizio della parte da non trasformare
## Metodi
### .END - Fine del trasferimento non interpretato


# I.SCH     - Definizione di una sottoscheda
Una sottoscheda è paragonabile ad una routine di un programma. Permette di raggruppare in uno script un insieme di schede omogenee. Dall'esterno potrò richiamare direttamente una sottoscheda.
## Metodi
- .END - Fine della definizione
