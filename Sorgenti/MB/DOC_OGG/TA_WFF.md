# WFF - Utenti che forzano salti
 :  : DEC T(ST) K(WFF)
## OBIETTIVO
Definire insiemi di utenti che possono forzare il salto di particolari impegni.
L'associazione di questi insiemi di utenti alle transizioni viene effettuato tramite l'attributo di transizione "Forzabilità salto da parte dell'utente".
## CONTENUTO DEI CAMPI
 :  : FLD T$ELEM __Codice insieme__
Definisce il codice dell'insieme di utenti che si sta definendo.
È il valore da inserire nell'attributo "Forzabilità salto da parte dell'utente".
Definisce il codice dell'insieme di utenti che si sta definendo.
 :  : FLD T$WFFA __Master del processo__
Gli utenti master su questo tipo processo possono forzare il salto dell'impegno.
 :  : FLD T$WFFB __Owner dell'ordine__
L'utente owner dell'ordine può forzare il salto dell'impegno.
Si ricorda che il valore di default dell'owner (salvo ridefinizioni in corso di esecuzione) è l'utente che ha fisicamente creato l'ordine di workflow.
 :  : FLD T$WFFC __Esecutori dell'impegno__
Gli utenti esecutori dell'impegno (da Classe esecutori) possono forzarne il salto.
 :  : FLD T$WFFD __Assegnatori dell'impegno__
Gli utenti assegnatori dell'impegno (da Classe assegnatori) possono forzarne il salto.
 :  : FLD T$WFFE __Tutti gli utenti__
Tutti gli utenti possono forzare il salto di questo impegno.
 :  : FLD T$WFFF __Suffisso exit__
Indica il suffisso del programma di aggiustamento tramite cui si può modificare l'insieme di utenti calcolati secondo queste regole.
Il programma richiamato è WFUTE_02suffisso e segue le stesse logiche della exit WFUTE_01x.
