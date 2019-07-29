# FUNZIONE DI INTERRELAZIONE GMQUAN <-> GMRRIM
# OBIETTIVO : 
Gestire tutte le funzioni di interrelazione tra le richieste di movimentazione e le giacenze.
## FUNZIONI SU GMRRIM : 
Data la richiesta di movimentazione : 
### I-A
Assegna alla quantità allocata/attesa della giacenza la quantità richiesta-evasa dell'origine/destinazione delle richieste di movimentazione solo se : 
* la quantità richiesta meno quella evasa è positiva
* il livello della richiesta è 2 (attiva)
* il FLAG 02 della richiesta è 0 (da assegnata).
In tal caso assegna la quantità e porta il flag 02 della richiesta a 2 (assegnata).

### D-D
Disassegna alla quantità allocata/attesa della giacenza la quantità richiesta-evasa dell'origine/destinazione delle richieste di movimentazione solo se : 
* la quantità richiesta-evasa è positiva
* il livello della richiesta è 2 (attiva)
* il FLAG 02 della richiesta è 2 (assegnata).
In tal caso disassegna la quantità (se diventa negativa la azzera), porta il flag 02 della richiesta a 0 (da assegnare) e pulisce le chiavi precedenti origine/destinazione della richiesta.

### A-DN
Come I-A, solo che opera unicamente sulle giacenze lasciando inalterate le richieste di movimentazione (Flag 02).

### D-DN
Come D-D, solo che opera unicamente sulle giacenze lasciando inalterate le richieste di movimentazione (Flag 02 e chiavi origine/destinazione).

## FUNZIONI DI FASATURA : 
Scandisce il file delle giacenza GMQUAN : 
### ALL
Tutto il FILE
### ARG
Per :  Area Giacenza
### KEY
Per : 
* Area Giacenza
* Tipo Giacenza
* Magazzini
* Articolo
e lo fasa sulla base dell'archivio richieste di movimentazione.

Per ogni record dell'archivio giacenza, azzera la quantità allocata e attesa. Se la quantità giacenza è nulla cancella il record e prosegue la scansione altrimenti scandisce le richieste di movimentazione per origine (allocazioni) e destinazione (attese). Per ogni record delle richieste di movimentazione trovato se il livello è attivo (2) e la quantità richiesta meno evasa è positiva  incrementa rispettivamente la quantità allocata (per origine) o attesa  (per destinazione) del GMQUAN.
