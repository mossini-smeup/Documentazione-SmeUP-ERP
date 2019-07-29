# FIL - Descrizione files
## OBIETTIVO
Definisce le caratteristiche relative a file e a eventuali trigger associati
## CONTENUTO DEI CAMPI
 :  : FLD T$ELEM Codice
Indica il file in questione
 :  : FLD T$DESC Descrizione
 :  : FLD T$FILA __Programma TRIGGER__
Indica il nome del programma da agganciare al file, il programma standard si chiama BRTRG0
 :  : FLD T$FIL1 __Ins.B/E=Pri.A/E=Dopo__
Indica in che momento deve essere richiamato il trigger quanto si sta inserendo un record del file : 
B= Prima di effettuare l'operazione.
A= Dopo aver effettuato l'operazione.
E= Prima e Dopo aver effettuato l'operazione.
 :  : FLD T$FIL2 __Ann.B/E=Pri.A/E=Dopo__
Come campo Precedente ma in cancellazione di record
 :  : FLD T$FIL3 __Agg.B/E=Pri.A/E=Dopo__
Come campo precedente ma in aggiornamento di record
 :  : FLD T$FIL0 __Ambiente specifico__
Indica il modulo verso il quale si sta facendo una fasatura.
Indica anche una parte del nome del programma richiamato da BRTRG0
 :  : FLD T$FIL4 __Parametro specifico__

 :  : FLD T$FILB __Nuova Gestione trigger__
**Vecchia modalità**
Programma chiamato XXXXXX_YY, dove XXXXXX è il file (primi 6 caratteri) e YY l'ambiente.
Viene chiamato il programma passando la DS del file triggerato (fino ad un massimo di 2000 caratteri).
Viene chiamato nei tempi definiti in tabella (prima e/o dopo l'operazione) ma in entrambi i casi il record corrente è quello successivo all'aggiornamento.
**Nuova modalità**
Programma chiamato xxxxx2_YY, dove xxxxx è il file (primi 5 caratteri) e YY l'ambiente.
Viene passata l'intera DS del file (fino ad un massimo di 32767 caratteri).
Viene passato un campo che contiene il momento di richiamo del file :  se prima o dopo l'aggiornamento.
Viene chiamato nei tempi definiti in tabella (prima e/o dopo l'operazione).
__Aggiornamento__
Si hanno sempre in linea la DS dopo l'aggiornamento (CORRENTE) e quella prima, sia che si sia in richiamo prima o dopo l'aggiornamento.
__Cancellazione__
 Si ha in linea la DS del record che si sta cancellando (CORRENTE).
__Inserimento__
 Si ha in linea la DS del record che si sta inserendo (CORRENTE).
Esempio trigger con la vecchia gestione :  **BRENTI_A7**.
Esempio trigger con la nuova gestione :  **BRENT2_A7**.
 :  : FLD T$FILC __Passaggio libreria__
Se il campo viene specificato, il programma di gestione dei trigger chiama il programma del trigger passando nei parametri anche il nome della libreria nella quale si trova il file.
Ovviamente, se questo campo viene impostato, occorre aggiungere in coda alla PARM del programma di trigger un opportuno campo lungo 10.
