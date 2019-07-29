# Obiettivo

Gestire in modo centralizzato la cache con la possibilità di abilitarla e disabilitarla, con l'obiettivo finale di permettere l'ottimizzazione delle prestazioni per non rileggere informazioni che non vengono aggiornate, piuttosto che decidere di ricaricare le informazioni ogni volta perchè le si stanno modificando.

I programmi che possono gestire la cache in modo centralizzato possono essere definiti
all'interno di questa API, ma possono anche essere aggiunti a run time.

Per ogni oggetto gestito (API, servizi, ecc.) viene mantenuto uno stato interno della cache che
può assumere questi valori : 
- 0 :  la cache dell'oggetto non è attiva
- 1 :  la cache dell'oggetto è attiva e valida
- 2 :  la cache è invalida :  va ricostruita

## Funzioni / Metodi
### CHK (Controllo stato della cache)
La funzione CHK restituisce lo stato della cache dell'oggetto passato in input.
Questi i valori possibili : 
1 :      la cache è valida e può essere utilizzata
blank :  la cache non è valida, va quindi ricostruita

### FRZ (Forzatura)
La funzione FRZ permette di forzare lo stato interno della cache di un oggetto.
* **ATT**
Il metodo ATT attiva la cache, se era già attiva resta tale e non restituisce errore.
(si assume che il chiamante abbia eseguito la costruzione)
* **DIS**
Il metodo DIS la disattiva, se era già disattivata resta tale e non restituisce errore.
* **CLR**
Il metodo CLR invalida la cache. Quindi alla prima richeista di stato verrà risposto
"cache non utilizzabile". A quel punto (assumendo la ricostruzione della stessa da parte del
chiamante) verrà portata a stato attivo

### CON (Scansione contesti)
La funzione CON permette di avere l'elenco dei programmi che hanno la gestione della cache centralizzata.
* **POS**
Il metodo POS si posiziona all'inizio dell'elenco.

* **LET**
Il metodo LET legge il programma successivo, alla fine restituisce l' errore "Non esistono altri valori da visualizzare".
