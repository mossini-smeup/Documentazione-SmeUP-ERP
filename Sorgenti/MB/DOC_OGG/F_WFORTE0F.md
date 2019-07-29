## Contenuto
Dati generali di un ordine di workflow.
Ogni ordine è un'istanza di un processo di worklow (TAWFA).

## Codice Oggetto (in TA/*CNTT)
'F1'                               £FUNT1

## Chiave primaria
Codice ordine            (F1)      £FUNK1

## Altri condizionamenti facoltativi in ricerca
Processo WF              (TA/WFA)  £FUNP1

## Ulteriore chiave primaria
N.A.

## Tabella guida
Le impostazioni che condizionano questo archivio sono contenute nel settore di tabelle WFA (Processo) : 
 :  : DEC T(ST) K(WFA)
Ad ogni elemento della WFA è associato uno script di processo nel file SCP_WFA.


## Autorizzazioni
Classe WFORTE per quanto riguarda inserimento e gestione.
La funzione è il processo di WF.

## Livelli e stati
Il livello è quello "classico" di tutti gli oggetti Sme.up (0/2/8/9).
Per quanto riguarda lo stato distinguiamo vari concetti : 
 * Lo stato vero e proprio dell'ordine F1 (F1STAT) :  la gestione è "blindata" in un V2 (WF_06), perchè a seconda del valore assunto si hanno comportamenti diversi del motore di workflow. Ad esempio, a stato 21 (gestione libera) il motore di workflow non attiva automaticamente gli impegni all'avanzamento.
 * Lo stato di avanzamento (F1STAV) :  è un campo OPZIONALMENTE impostabile nello svolgimento di un workflow per indicare a oggetti esterni all'ordine (ad esempio altri ordini di workflow da questo dipendenti) lo stato LOGICO di questo ordine, dipendente dal processo.
 * Lo stato dell'oggetto master di un ordine spesso viene gestito dal workflow stesso :  ad esempio sarà il workflow di gestione di un articolo a impostare lo stato dell'articolo ad esso associato (in progettazione, in fase di ingegnerizzazione, a listino...).

Tutte queste informazioni possono essere usate per prendere decisioni nello svolgimento del workflow.

## Note strutturate (Tabella NSC)
Il contenitore note si assume dalla tabella WFW, dalla WFA relativa al processo.

## Parametri (Tabella C£E)
La categoria parametri si assume dalla tabella WFW, dalla WFA relativa al processo.
Per ora non è prevista una gestione parametri a standard.

## Flussi (Tabella B£H)
Nessuno :  l'ordine stesso di workflow è un flusso "potenziato", ovvero non lineare e multi-utente. A questo non si sovrappone una gestione flussi in senso classico.

## /COPY
Creazione e gestione degli ordini di workflow : 
 :  : DEC T(MB) P(QILEGEN) K(£WFB)

Dichiarazioni di avanzamento e funzioni tecniche : 
 :  : DEC T(MB) P(QILEGEN) K(£WFA)

## Gruppi flag
N.A.

## CONTENUTO DEI CAMPI

 :  : FLD F1LIVE **Livello**
Vedi documentazione del file, sezione "Livelli e stati".

 :  : FLD F1STAT **Stato**
Vedi documentazione del file, sezione "Livelli e stati".

 :  : FLD F1STAV **Stato di avanzamento**
Vedi documentazione del file, sezione "Livelli e stati".

 :  : FLD F1TPMA **Tipo oggetto master**
Impostato in tabella WFA.

 :  : FLD F1CDMA **Codice oggetto master**
Serve a specificare un oggetto "importante" per il workflow in questione.
Sulla base di questo è possibile prendere decisioni nel corso del flusso di workflow.

 :  : FLD F1TPOW **Tipo oggetto owner**
Impostato in tabella WFA.
Per ora l'unico caso gestito è TAB£U.

 :  : FLD F1CDOW **Codice oggetto owner**
Serve a specificare un utente "importante" per il workflow in questione, tipicamente il responsabile della sua esecuzione.

 :  : FLD F1PRIO **Priorità manuale**
Campo utilizzabile per ordinamenti in worklist.

 :  : FLD F1LTOT **Lead time totale**
Preso dalla tabella WFA, utilizzato per il calcolo della data fine richiesta dell'ordine a partire dalla data di inserimento.

 :  : FLD F1DFRI **Data fine richiesta**
Campo per ora utilizzabile per ordinamenti in worklist.

 :  : FLD F1NMAS **Numero ordine master**
Campo utilizzato per collegare ordini di workflow e ordini derivati.

 :  : FLD F1TMAS **Transizione master**
Campo utilizzato per collegare ordini di workflow e ordini derivati.

 :  : FLD F1AMAS **Attività master**
Campo utilizzato per collegare ordini di workflow e ordini derivati.
