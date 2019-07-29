# OBBIETTIVO
Eseguire il lancio funzioni LOOCUP da un sorgente RPG
# PREREQUISITI
C/COPY QILEGEN,£UIDDS

# PARAMETRI

## PARAMETRI DI INPUT

### Funzione

- ' '(*blanks)  :  Lancio di una funzione LOOCUP tramite una stringa     in cui è definita la chiamata
- FUN   :  Lancio di funzione LOOCUP tramite stringa UIBDS
- PGM   :  Lancio di funzione LOOCUP tramite programma

Le funzione hanno 3 metodi comuni : 

- **WRLOO (Esecuzione semplice)** : 
La funzione richiesta e l'emulazione lanciata funzionano in modo indipendente, l'emulazione in questo caso è ferma fintanto che non premo un tasto.
- **EXLOO (Esecuzione modale)** : 
La funzione viene eseguita ed il controllo passa alla finestra LOOCUP, quindi l'emulazione rimane bloccata fino a che non ritorno dalla funzione lanciata
- **RELOO (Esecuzione e ritorno)** : 
La funzione viene eseguita ed il controllo torna automaticamente  all'emulazione, senza il bisogno di interazione.


## Dettaglio funzioni

### 1) ' '(*blanks)
Questa funzione si occupa di lanciare una funzione LOOCUP passando in input una stringa in cui viene costruita la chiamata. La stringa viene passata alla funzione tramite il comando **COMANDO**

### 2) FUN
Questa funzione di occupa di lanciare una funzione LOOCUP ricevendo in input una stringa UIBDS che viene costruita tramite la funzione **FUN Impostazioni** in cui vengono esposti in dettaglio tutti i campi necessari per la costruzione della suddetta funzione.

### 3) PGM
Questa funzione di occupa di lanciare una funzione LOOCUP ricevendo in input la LDA o il comando di uno specifico programma.

