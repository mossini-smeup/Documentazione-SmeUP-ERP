## Contenuto
Impegni di un ordine di workflow.
Ogni impegno deriva da una transizione (oggetto F5), specificata nello script del processo a cui l'ordine appartiene.

## Codice Oggetto (in TA/*CNTT)
'F2'                               £FUNT1

## Chiave primaria
Codice impegno           (F2)      £FUNK1

## Altri condizionamenti facoltativi in ricerca
Tipo impegno             (TA/WFI)  £FUNP1

## Ulteriore chiave primaria
N.A.

## Autorizzazioni
Chi può eseguire e chi può assegnare l'impegno :  definiti a livello di script, nella relativa transizione.

## Livelli e stati
Il livello è quello "classico" di tutti gli oggetti Sme.up (0/2/8/9).
Per quanto riguarda lo stato distinguiamo vari concetti : 
 * Lo stato del record (F2STAT) :  la gestione è "blindata" in un V2 (WF_06) e ricalca quella del relativo ordine (F1).
 * Lo stato logico dell'impegno (F2STIM) :  indica l'eseguibilità o meno di un impegno. E' un oggetto fisso V2WF_01. È molto importante, sulla base di questo stato un impegno è pronto o meno per essere eseguito.

## /COPY
Funzioni su impegni : 
 :  : DEC T(MB) P(QILEGEN) K(£WFD)

## Note strutturate (Tabella NSC)
Il contenitore note si assume dalla tabella WFW, dalla WFI relativa al tipo impegno. Tipicamente NSC=WF2.

## Parametri (Tabella C£E)
La categoria parametri si assume dalla tabella WFW, dalla WFI relativa al tipo impegno (per ora parametri non gestiti in maniera automatica).

## Flussi (Tabella B£H)
Nessuno :  l'ordine stesso di workflow è un flusso "potenziato", ovvero non lineare e multi-utente. A questo non si sovrappone una gestione flussi in senso classico.

## CONTENUTO DEI CAMPI

 :  : FLD F2LIVE **Livello**
Vedi documentazione del file, sezione "Livelli e stati".

 :  : FLD F2STAT **Stato**
Vedi documentazione del file, sezione "Livelli e stati".

 :  : FLD F2TIMP **Tipo impegno**
Utilizzato come sottoclassificazione degli impegni.

 :  : FLD F2DESC **Descrizione impegno**
Ripresa dalla descrizione della transizione corrispondente nello script del workflow, è la descrizione che viene visualizzata nelle worklist.

 :  : FLD F2STIM **Stato impegno**
Vedi documentazione del file, sezione "Livelli e stati".

 :  : FLD F2TRAN **Codice transizione**
Dice quale transizione nello script fornisce il modello per il comportamento di questo impegno.
