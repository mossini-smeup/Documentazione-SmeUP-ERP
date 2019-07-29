## Contenuto
Attività di un ordine di workflow.

## Oggettizzazione
 * £FUNT1 :  'F4'
 * £FUNP1 :  niente
 * £FUNK1 (lungo 10) :  il numero di attività (CHIAVE PRIMARIA) F4NURE.

## Impostazioni fisse
Nessuna.

## Autorizzazioni
Nessuna. Sono scritte in maniera automatica nel corso dell'esecuzione di un ordine.

## Livelli e stati
Il livello è quello "classico" di tutti gli oggetti Sme.up (0/2/8/9).
Lo stato è "blindato" in un V2 (WF_06) ed è gestito dal motore di workflow.

## /COPY
Creazione e gestione attività : 
 :  : DEC T(MB) P(QILEGEN) K(£WFC)

## Note strutturate (Tabella NSC)
Nessuna.

### Parametri (Tabella C£E)
Nessuno.

### Flussi (Tabella B£H)
Nessuno :  l'ordine stesso di workflow è un flusso "potenziato", ovvero non lineare e multi-utente. A questo non si sovrappone una gestione flussi in senso classico.
