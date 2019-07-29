# VERIFICHE E AZIONI PRELIMINARI

## COMPLETAMENTO TABELLE
### TABELLE COMUNI DI BASE
 * TABELLA B£2
Impostare correttamente il codice Azienda e la valuta EURO in tabella B£2
 :  : DEC T(ST) K(B£2)
 * TABELLA BRE
Riprendere la tabella Tipo contatto (BRE) per clienti/fornitori per aggiornare la natura ente
 :  : DEC T(ST) K(BRE)
 * TABELLA BRI
Verificare la presenza degli elementi £17 £18 £19 £20 £21 £24
 :  : DEC T(ST) K(BRI)
 * TABELLA BRX
Verificare la corretta impostazione di persona fisica/giuridica, percipiente intabelle BRX
 :  : DEC T(ST) K(BRX)
 * TABELLA PER
Creare gli elementi della tabella PER con sottosettore azienda tramite l'utility PE8 con funzione MAN e metodo CRE

 * TABELLA B£4
Creare gli elementi della tabella B£4

 * TABELLE VALUTE E CAMBI
Riprendere da modello la tabella delle valute e dei cambi
 :  : DEC T(ST) K(VAL)
 :  : DEC T(ST) K(TCA)
 * TABELLA B£W
Verificare presenza stai per oggetti E4, E5, RR e MH
 :  : DEC T(ST) K(B£WE4)
 :  : DEC T(ST) K(B£WE5)
 :  : DEC T(ST) K(B£WRR)
 :  : DEC T(ST) K(B£WMH)
 * TABELLA B£Y
Verificare presenza gruppo flag C5*
 :  : DEC T(ST) K(B£Y)
 * TABELLA B§L
Riprendere gli elementi C5*  di tabella per la gestione dei log

### TABELLE CONTABILI DI BASE
 * C51
Impostare la tabella : 
 :  : DEC T(ST) K(C51)

 * REGISTRI IVA
Impostare la tabella : 
 :  : DEC T(ST) K(C5R&AZ)

 * CAUSALI REGISTRAZIONI
Scandire le tabelle seguenti controllandone la completezza
 :  : DEC T(ST) K(C5D&AZ)
 :  : DEC T(ST) K(C5V&AZ)

 * PIANO DEI CONTI
Scandire gli elementi della seguente tabella oppure riprenderli dalla libreria dei modelli _4_SMEMOD
 :  : DEC T(ST) K(C5B)
Ricordarsi di impostare sui conti clienti/fornitori il tipo contatto.
Per gestire i parametri del conto in fase di post-modifica deve essere definito il flusso
 :  : DEC T(TA) P(B£H) K(M-TAC5B)
 :  : DEC T(TA) P(B£JTA) K(M002)

 * RICLASSIFICHE
Controllare e configurare le seguenti tabelle : 
 :  : DEC T(ST) K(C5N)
 :  : DEC T(ST) K(C5NCE)
 :  : DEC T(ST) K(C5NBA)
 :  : DEC T(ST) K(C5M)

 * PAGAMENTI
Scandire le tabelle seguenti controllandone la completezza
 :  : DEC T(ST) K(PAG&AZ)
 :  : DEC T(ST) K(C5I&AZ)
 :  : DEC T(ST) K(C5G&AZ)
 :  : DEC T(ST) K(C5E&AZ)

 * BANCHE
Per lo standard SME.up le banche sono di due tipi
 * Insieme di tutti gli sportelli nazionali :  sono definite come enti di tipo BAN. In presenza della tabella "BAN" si deve procedere alla deviazione : 
 :  : DEC T(ST) K(BAN)
si deve deviare impostando >OCNBAN o >OBA
 :  : DEC T(TA) P(B£I) K(BAN)

Mediante la funzione specifica è possibile importare la lista completa degli sportelli ABI-CAB dal file reperibile tramite servizi di remote banking
 :  : INI
 :  : CMD CALL C5N000G PARM('OF' 'R B' 'AZ')
 :  : FIN
E quindi fonderli nell'anagrafica aziendale
 :  : INI
 :  : CMD CALL C5N000G PARM('OF' 'X F' 'CNBAN')
 :  : FIN
 * Banche utilizzate dall'azienda
Sono definite tramite la configurazione delle tabelle : 
 :  : DEC T(ST) K(C5F)
 :  : DEC T(ST) K(C5J)

* TABELLE RITENUTE
Scandire le tabelle seguenti controllandone la completezza
 :  : DEC T(ST) K(C5P)
 :  : DEC T(ST) K(C5T)

*TABELLE TRACCIATI BANCARI
Fasare tabelle tracciati trasmissione bancaria *CNT5 : 
 :  : DEC T(TA) P(*CNT5)

## COMPLETAMENTO DATI GENERALI

### DATI AZIENDALI

 :  : INI Controllare archivio anagrafico aziende >>
 :  : CMD CALL BREN01G PARM('AZI')
 :  : FIN
 :  : INI Controllare parametri specifici aziende >>
 :  : CMA  :  : FUN PG(C£FU01X) FU(PARA) ME(GES) PS(£CA) T1(CN) P1(AZI) K1(&AZ)
 :  : FIN
 :  : DEC T(ST) K(C5Q&AZ) I(Definire le divisioni aziendali)


### DATE/PERIODI CHIUSURE/ESERCIZI
 :  : INI Verifica impostazione periodi per ogni azienda
 :  : CMD CALL C5N000G PARM('OF' 'O P' 'AZ')
 :  : FIN

### NUMERATORI E PROGRESSIVI CONTABILI
 :  : INI Verifica impostazione numeratori per azienda
 :  : CMD CALL C5N000G PARM('OF' 'O I' 'AZ')
 :  : FIN
 :  : INI Aggiornare progressivi stampa giornale >>
 :  : CMA  :  : FUN PG(C£FU01X) FU(PARA) ME(GES) PS(£CA) T1(CN) P1(AZI) K1(&AZ)
 :  : FIN

### PIANO DEI CONTI e BILANCI
 :  : INI _9_Verifica struttura e associazione a riclassifiche
 :  : CMD CALL C5N000G PARM('OF' 'W B' 'AZ')
 :  : FIN

 :  : INI Verificare presenza categoria contabile su anagrafico enti >>
 :  : CMD CALL BREN01G
 :  : FIN

### REGISTRAZIONI AUTOMATICHE
 :  : INI _9_Richiamo del programma di verifica
 :  : CMD CALL C5N000G PARM('OF' 'W A' 'AZ')
 :  : FIN


### ATTIVAZIONE CONTABILIZZAZIONE BATCH REGISTRAZIONI
- [Impostazioni contabilizz. documenti batch](Sorgenti/MB/DOC/C5C010_A)

### CALENDARIO PER FATTURAZIONE ATTIVA E PASSIVA
- [Eccezioni Date Scadenza &-x2f; Calendari](Sorgenti/MB/DOC/C5D010_B)



## PRE-ELIMINAZIONE CONTATTI E CONTI CONTABILI
_7_Definire due nuovi elementi nelle seguenti tabelle utilizzando
_7_come programma di controllo il C5PRE0 : 
 :  : DEC T(ST) K(B£JCO) I(Per i contatti)
 :  : DEC T(ST) K(B£JTA) I(Per i conti contabili)
_7_Agganciare gli elementi della tabella B£J alla B£H : 
 :  : DEC T(TA) P(B£H) K(P-CN)
 :  : DEC T(TA) P(B£H) K(P-TAC5B)

