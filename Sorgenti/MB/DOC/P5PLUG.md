# ATTIVAZIONE

## TABELLE DI BASE
 :  : DEC T(ST) K(P51)
 :  : DEC T(ST) K(P5T)

La tabella P5T identifica i tipi ordine che verranno gestiti.

Ad esempio si possono  definire ordini di Lavorazione, Montaggio,  Rilavorazione, Trasformazione, etc. Queste diverse tipologie di ordine possono distinguersi per il modo in cui vengono creati gli impegni dei materiali, gli impegni delle risorse, per come si consumano i materiali, per la gestione degli scarti, per le modalità di versamento, etc..
 :  : DEC T(ST) K(P5I)
La tabella P5I definisce il modo in cui vengono costruiti, aggiornati e consumati gli impegni dei materiali.

Le possibilità applicative che si possono realizzare implementando questa tabella sono molteplici, vediamo quelli di utilizzo più comune : 

- Costruzione degli impegni materiali : 
-- Distinta Assieme Specifica  (T$P5IE='DB')
-- Distinta Documento con eventuale risalita Assieme (T$P5IE='D1') La memorizzazione della distinta del documento si utilizza in genere per fissare materiali specifici dell'ordine. Non è opportuno memorizzarla quando non ci sono differenze rispetto a quella dell'assieme perchè modifiche successive al rilascio dell'ordine non verrebbero più recepite.
-- Distinta Documento (T$P5IE='D2')
-- Distinta Variazione E' una distinta che esprime le variazioni rispetto all'origine Si Utilizza normalmente per fare ordini di trasformazione, ad esempio lo smontaggio di un assieme.
-- Programma Utente   (T$P5IE='UT')
- Consumo dei materiali : 
-- Backflushing  (T$P5IM= 'IM') con questa tecnica i materiali vengono prelevati all'atto del versamento sulla base della distinta di produzione del codice intestatario dell'ordine. In generale si applica in ambienti in cui l'elevata  velocità del flusso produttivo rende inutile il controllo avanzamento delle fasi di lavorazione e la standardizzazione del prodotto consente il prelievo cieco dei materiali. ATTENZIONE! questa modalità non è implementabile in presenza di conto lavoro di fase.
-- Manuale  (T$P5IM=' ') tipico di realtà in cui si effettuano montaggi di prodotti su commessa specifica del cliente.
-- Fase     (T$P5IM='ID') il materiale viene prelevato in corrispondenza della specifica fase di lavoro in cui viene consumato. Un esempio è quello del grezzo che attraversa una sequenza di operazioni di lavorazione (tornitura, alesatura...) con il montaggio di alcuni componenti(guarnizioni..).


 :  : DEC T(ST) K(P5S)
La tabella P5S definisce il modo in cui vengono costruiti, aggiornati e consumati gli impegni delle risorse.

- Costruzione degli impegni risorse : 
-- Ciclo Lavorazione Assieme (T$P5SE='CO')
-- Ciclo Documento con eventuale risalita Assieme.(T$P5SE='C1') Per il ciclo memorizzato vale quanto detto per la distinta materiali memorizzata.
-- Ciclo Documento (T$P5SE='C2')
- Consumo impegni risorse
-- Impegni nettificati in base alle attivià lavorative eseguite (T$P5SO= ' ')
-- Impegni nettificati in base alla quantità versata (T$P5SO= '1')

 :  : DEC T(ST) K(CRNP5)

### Numeratori da impostare ed utilizzi

- Numeratore Attività su P51
- Numeratore Eventi   su P51
- Numeratore Ordini di produzione su P5T


 :  : DEC T(ST) K(B£WP5)
 :  : DEC T(ST) K(B£Y)
Definizione gruppo Flag Ordine Produzione su P5T
Il gruppo Flag consente di definire : 

- Stato Stampa Documento
- Gestione Quantità (sempre=1)
- Tipo Tempo nel caso di produzioni monofase si può descrivere il ciclo di lavorazione direttamente sul p5teop0f
- Definisce se sottarre al residuo la quantità versata scarta  per la determinazione degli impegni residui dei materiali. Definizione gruppo Flag Avanzamenti  su P5C


 :  : DEC T(ST) K(P5C)
La tabella P5C descrive le causali con cui si eseguono le dichiarazioni di attività.

## VERSAMENTO ORDINE PRODUZIONE
 :  : DEC T(TA) P(B£H) K(MM)
 :  : DEC T(ST) K(B£JGM)
Si devono impostare parametri del versamanto causale,controlli specifici...

## FLUSSI  ORDINE PRODUZIONE (OGGETTO OR)

### Inserimento
 :  : DEC T(TA) P(B£H) K(I-OR)

      1. Costruzione Ciclo Memorizzato

 :  : DEC T(TA) P(B£JOR) K(I010)


      2. Costruzione Distinta  Memorizzata

 :  : DEC T(TA) P(B£JOR) K(I020)


      3. Creazione  Impegni Materiali/Risorse

 :  : DEC T(TA) P(B£JOR) K(I030)


      4. Creazione  Lotto Q9000

 :  : DEC T(TA) P(B£JOR) K(I040)

### Modifica
 :  : DEC T(TA) P(B£H) K(M-OR)

      1. Modifica Ciclo con eventuale Creazione con richiesta

 :  : DEC T(TA) P(B£JOR) K(M010)

      2. Modifica Distinta con eventuale Creazione con richiesta

 :  : DEC T(TA) P(B£JOR) K(M020)

      3. Nettificazione Impegni Materiali/Risorse

 :  : DEC T(TA) P(B£JOR) K(M030)

### Pre-Cancellazione
 :  : DEC T(TA) P(B£H) K(P-OR)

      1. Cancellazione Ciclo Memorizzato (P5FUCDC;CAN;CIE)

 :  : DEC T(TA) P(B£JOR) K(P010)


      2. Cancellazione Distinta Memorizzata (P5FUDDC;CAN;CIE)

 :  : DEC T(TA) P(B£JOR) K(P020)


      3. Cancellazione Lotto Q9000 (CQP5L01;ANN;)

 :  : DEC T(TA) P(B£JOR) K(P030)

### Copia             
### Azioni            
### Visualizzazione   
