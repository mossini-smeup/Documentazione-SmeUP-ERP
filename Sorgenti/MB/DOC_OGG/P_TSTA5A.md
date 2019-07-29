Programma di test della £A5A

# OBIETTIVO
Gestire le operazioni base del record nel tracciato A5CESP0F Anagrafica cespiti.

# FUNZIONI E METODI
## CLEAR
Inizializzazzazione dei campi del record con pulizia iniziale : 
imposta codice cespite se non ricevuto da Numeratore imposta livello/stato gruppo flag da tabella imposta data e ora di creaz.aggiornam.utente.
NON esegue la scrittura del record

## DERIV
Come funzione CLEAR con stessi metodi.
Non effettua però la pulizia iniziale del record, mantenendo il contenuto dei i campi del record passato.

## WRI
Esegue la scrittura del record con il contenuto ricevuto del formato record, senza eseguire alcun controllo formale sui campi.
Esegue il lancio del flusso di inserimento.

## UPD
Esegue l'aggiornamento del record con il contenuto ricevuto del formato record, senza eseguire alcun controllo formale sui campi.
Esegue il lancio del flusso di modifica.

## DEL
Dato il N°di Registrazione elimina il record dall'archivio C5TREG0F.
Elimina eventuali note e parametri di testata.

Esegue il lancio del flusso di cancellazione.

# NOTE TECNICHE

### PREREQUISITI
D A5CESP E DS EXTNAME(A5CESP0F)
 /COPY QILEGEN,£FUNDS1

### PARAMETRI IN INPUT

£A5APG :  Programma (per standardizzare verso £FUN)
£A5AFU :  Funzione (10 )
£A5AME :  Metodo (10 )
£FUNP1 :  Categoria cespite (6 )
£FUNK1 :  Codice cespite (15 )

### PARAMETRI IN OUTPUT
£A5AMS :  Codice messaggio ritorno (7)
£A5AFI :  File messaggio ritorno (10)
£A5ACM :  Ultimo Comando (2)
IN35 - On=Errore
*IN36 - On=Eseguita ricerca

£FUND1 :  DS generale di input

### ESEMPIO DI CHIAMATA
C MOVEL<Funzione>£A5AFU P
C MOVEL<Metodo >£A5AME P
C MOVEL<Cat.cesp>£FUNP1 P
C MOVEL<Cespite >£FUNK1 P
C EXSR £A5A
