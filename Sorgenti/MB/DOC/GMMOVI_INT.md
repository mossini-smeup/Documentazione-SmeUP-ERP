# Causali di movimentazione
Tutti i movimenti di magazzino vengono eseguiti attraverso l'utilizzo delle >CAUSALI DI MOVIMENTAZIONE che sono codificate nella tabella>GMC.
  :  : DEC T(ST) K(GMC)

Gli elementi principali per la creazione di una causale di movimentazione sono : 
 * _2_AREA :  partizione _9_FISICA o _9_LOGICA dei propri  Magazzini. Si possono definire delle aree per Tipologia o Natura degli articoli; per processi di produzione o si può avere un'area per Stabilimento Produttivo. _R_Le aree possono avere valenza Fiscale oppure no (Depositi). In ogni caso  deve essere chiaro che più aree vengono definite,maggiore è il numero di causali di movimentazione da definire, sia per movimenti sulla stessa area (Versamenti, Prelievi), che per aree diverse (Trasferimenti).
 :  : DEC T(ST) K(GMR)
 * _2_TIPO MOVIMENTO :  definisce la natura del movimento :  se di produzione, o da documento o generico.
 * _2_SEGNO MOVIMENTO :  positivo o negativo o neutro (statistico).
 * _2_TIPO GIACENZA :  sono le chiavi di lettura della giacenza dell'area interessata dal movimento.
  :  : DEC T(ST) K(GMQ)
 * _2_FORMA PRESENTAZIONE : è l'elemento che guida la visualizzazione, gestione e annullamento interattivi di un movimento.
 :  : DEC T(ST) K(B£Q)

Per eseguire un movimento ci sono diverse modalità (vedere doc. particolari), inoltre deve essere presente almeno un plant : 
 :  : DEC T(TA) P(MAG) K(1)

Devono essere presenti almeno i numeratori : 
 * _2_REGISTRAZIONI MAGAZZINO
 :  : DEC T(TA) P(CRNGM) K(NREG)
 * _2_TRANSIZIONI   MAGAZZINO
 :  : DEC T(TA) P(CRNGM) K(NRTR)

## Attività sui movimenti
Come attività sui movimenti sono a disposizione : 
 * _2_Interrogazione movimenti,con diversi livelli di sintesi di raggruppamento dei movimenti :  per_7_Data registrazione,_7_Lotto,_7_Ubicazione,_7_Colloetc.
I dati visualizzati nelle varie interrogazioni sono definibili tramite la utility degli schemi di stampa.
 * _2_Revisione movimenti,anche'essa con diversi livelli di sintesi di raggruppamento.  La  modifica  dei singoli movimenti è subordinata alla classe di autorizzazione : 
  :  : DEC T(TA) P(B£P) K(GMTR00)
e alla forma di presentazione indicata sulla causale movimento. I dati visualizzati nelle varie revisioni sono definibili con gli Schemi.
 * _2_Stampa movimenti :  anch'essa è supportata da parzializzazioni, Livelli di ordinamento, Schemi di dati etc.
 * _2_Stampa schede articolo  :  consente la stampa delle Schede di magazzino.

# Esecuzione movimenti
Per eseguire un movimento ci sono diverse modalità. Qui di seguito ne vengono elencate alcune : 
 * _2_ESECUZIONE MANUALE, I movimenti si devono definire nella tabella>B£JGM.
  :  : DEC T(ST) K(B£JGM)
Vengono eseguiti attraverso una opportuna voce di menu. In questa modalità di registrazione diventa fondamentale la_4_FORMA DI PRESENTAZIONE.
 * _2_REGISTRAZIONE DOCUMENTO RICEVIMENTO O SPEDIZIONE, Solitamente sono definite le causali di movimentazione sui Tipi riga ( Tab.>V5BXX)
 Esempio : 
  :  : DEC T(TA) P(V5BCA) K(ART)
 I movimenti vengono creati al momento della registrazione del  documento di ricevimento o spedizione, attraverso l'attività di collegamento.
 * _2_VERSAMENTO E PRELIEVO DI PRODUZIONE DA ORDINE DI PRODUZIONE, In questo caso le causali sono definite nei parametri standard logistici, e possono essere legate all'articolo, al Centro di lavoro o altro.
 :  : DEC T(TA) P(C£E) K(£P1)
 :  : DEC T(TA) P(C£E) K(£P2)
Possono venire eseguiti attraverso attività sugli Ordini di produzione.

I movimenti possono anche essere  registrati attraverso  l'esecuzione  delle _9_RICHIESTE DI MOVIMENTAZIONE(vedi documentazione relativa - modulo ).
In questo caso è assolutamente necessario nella codifica delle  causali dare un segno alle AZIONI SU_4_QTA' ALLOCATAe su_4_QTA' ATTESA.
