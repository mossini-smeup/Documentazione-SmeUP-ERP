# Set'n play

PRECEDURA DI INSTALLAZIONE

## Definizione coda lavori
E' consigliata una coda lavori specifica per il calcolo costi.
Come standard si suggerisce di denominarla QBATCHD0 e di metterla
nella stessa libreria della QBATCHUI e nel sottosistema QBATCH.

Per vedere in che libreria si trova la QBATCHUI usare il comando
- WO QBATCHUI
Per creare la coda QBATCHD0 usare il comando
- CRTJOBQ JOBQ(SMESYS_SM/QBATCHD0) TEXT('Coda per Costi')
  AUTCHK(*DTAAUT)
Per associare la coda al sottosistema QBATCH usare la procedura : 
1. Verficare il numero di sequenza disponible con il comando
   DSPSBSD SBSD(QBATCH)
   scegliere l'opzione 6 Voce coda lavori per visualizza le sequenze
2. Eseguire il comando : 
   ADDJOBQE SBSD(QBATCH) JOBQ(QBATCHD0) SEQNBR(XXX)
   dove XXX è la sequenza libera individuata nel passo 1)
Con UP GPE associare la coda QBATCHD0 ai programmi : 
  :  : DEC T(MB) P(D0SRC)  K(D0CO01C) I(Calcolo costi base)
  :  : DEC T(MB) P(D0SRC)  K(D0CO10B) I(Calcolo costo medio)
  :  : DEC T(MB) P(D0SRC)  K(D0UT81B) I(Costruz.ciclo - distinta prod/cto lav)
  :  : DEC T(MB) P(D0SRC)  K(D0UT01B) I(Confornto costi)
  :  : DEC T(MB) P(D0SRC)  K(D0UT02B) I(Confornto cicli)
  :  : DEC T(MB) P(D0SRC)  K(D0UT03B) I(Confornto distinte)
per tutti gli utenti

## Definizioni tabelle

_7_Tabella D0E.
E' una nuova tabella.
 :  : INI Importare la sua definizione dalla SMETAB
 :  : CMD UP FTB
 :  : FIN

_7_Tabella D0*
E' una nuova tabella.
 :  : INI Importare la sua definizione dalla SMETAB
 :  : CMD UP FTB
 :  : FIN

_7_Tabella D0J.
E' una nuova tabella.
 :  : INI Importare la sua definizione dalla SMETAB
 :  : CMD UP FTB
 :  : FIN

_7_Tabella IGI
Sono stati aggiunti i nuovi campi : 
* T$IGIS Rilcassifica C
* T$IGIT Rilcassifica D
* T$IGIU Liv.Inf.Corrispondente
 :  : INI Importare la sua definizione dalla SMETAB
 :  : CMD UP FTB
 :  : FIN

_7_Tabella TCO
Sono stati aggiunti i nuovi campi : 
* T$TCOP Liv.Costo Assunto
* T$TCOJ Costo Totale
* T$TCOK Natura costo
 :  : INI Importare la sua definizione dalla SMETAB
 :  : CMD UP FTB
 :  : FIN

_7_Tabella D0D
Sono stati aggiunti i nuovi campi : 
* D0D(19) Comp.Mat.(Liv.Inf.)
* D0D(20) Comp.Sca.(Liv.Inf.)
 :  : INI Importare la sua definizione dalla SMETAB
 :  : CMD UP FTB
 :  : FIN

## Creazione tabelle automatiche

Tutti gli elementi delle tabelle indicate sotto dovrebbero risultare inesistenti. Saranno creati da un apposito programma che si trova alla fine dell'elenco.

>TABELLE PER LA MEMORIZZAZIONE DEI PARAMETRI DI LANCIO UTENTE E BLOCCO PERIODO RICALCOLO
_7_Tabella C£E
 :  : DEC T(TA) P(C£E) K(£D0)
_7_Tabella B£G
 :  : DEC T(TA) P(B£G) K(£D0)
_7_Tabella B£N£C
 :  : DEC T(TA) P(B£N£C) K(D0A)
 :  : DEC T(TA) P(B£N£C) K(D1A)
 :  : DEC T(TA) P(B£N£C) K(D1B)
 :  : DEC T(TA) P(B£N£C) K(D9A)
 :  : DEC T(TA) P(B£N£C) K(DSA)

>TABELLE PER LA STRUTTURA STANDARD ALIQUOTE E MAPPATURA INDICI COSTO
_7_Tabella DOC££
 :  : DEC T(TA) P(D0C££) K(01)
 :  : DEC T(TA) P(D0C££) K(02)
 :  : DEC T(TA) P(D0C££) K(03)
 :  : DEC T(TA) P(D0C££) K(04)
 :  : DEC T(TA) P(D0C££) K(05)
 :  : DEC T(TA) P(D0C££) K(06)
_7_Tabella D0D
 :  : DEC T(TA) P(D0D) K(££)

>TABELLE PER LA GESTIONE DELLA DISTINTA NELLA DOCUMENTAZIONE DI CALCOLO
_7_Tabella *CNAA
 :  : DEC T(TA) P(*CNAA) K(£D)
_7_Tabella BRL
 :  : DEC T(TA) P(BRL) K(£D0)

>TABELLE GENERICHE D0
_7_Tabella D0*CI
 :  : DEC T(OG) P() K(TAD0*CI)
_7_Tabella D0*EL
 :  : DEC T(OG) P() K(TAD0*EL)
_7_Tabella D0*ER
 :  : DEC T(OG) P() K(TAD0*ER)
_7_Tabella D0*ET
 :  : DEC T(OG) P() K(TAD0*ET)
_7_Tabella D0*FA
 :  : DEC T(OG) P() K(TAD0*FA)
_7_Tabella D0*FS
 :  : DEC T(OG) P() K(TAD0*FS)
_7_Tabella D0*FT
 :  : DEC T(OG) P() K(TAD0*FT)
_7_Tabella D0*TR
 :  : DEC T(OG) P() K(TAD0*TR)

>TABELLE PER LA GESTIONE DEGLI ERRORI
_7_Tabella D0E
 :  : DEC T(OG) P() K(TAD0E)

>TABELLE PER LA GESTIONE DEI COSTI TOTALIZZATI
_7_Tabella D0J
 :  : DEC T(OG) P() K(TAD0J)

>TABELLE PER LA NUMERAZIONE DEI SALVATAGGI DEL FILE D0DOCU
_7_Tabella CRND0
 :  : DEC T(TA) P(CRND0) K(D0DOCU)

>TABELLE INDICI STANDARD COSTI
_7_Tabella D0A
 :  : DEC T(TA) P(D0A) K(£Q)
_7_Tabella IGI£S
 :  : DEC T(OG) P() K(TAIGI£S)

>TABELLE PER LA GESTIONE DEGLI STATI
_7_Tabella B£WD0
 :  : DEC T(TA) P(B£WD0) K(10)
 :  : DEC T(TA) P(B£WD0) K(80)
 :  : DEC T(TA) P(B£WD0) K(90)

>TABELLE PER LA GESTIONE DI CICLI E DISTINTE CONFIGURATE
_7_Tabella *CNAA
 :  : DEC T(TA) P(*CNAA) K(£C)
_7_Tabella BRL :  Work Sme.up per costi medi
 :  : DEC T(TA) P(BRL) K(£DW)
_7_Tabella BRL :  Work Sme.up per set'n play costi
 :  : DEC T(TA) P(BRL) K(£CW)

>TABELLE PER I CONFRONTO COSTI DEL CONTESTO AR
_7_Tabella B£QAR
 :  : DEC T(TA) P(B£QAR) K(£D0)

>TABELLE PER LA GESTIONE DI POLITICHE SPECIFICHE PER I COSTI
_7_Tabella C£L£D
 :  : DEC T(TA) P(C£L£D) K(£D0)
_7_Tabella C£H£D
 :  : DEC T(TA) P(C£H£D) K(ACQ)
 :  : DEC T(TA) P(C£H£D) K(PRO)
 :  : DEC T(TA) P(C£H£D) K(LAV)
_7_Tabella B£G
 :  : DEC T(TA) P(B£G) K(£DP)
_7_Tabella C£V£D
 :  : DEC T(TA) P(C£V£D) K(£DP)
_7_Tabella C£E
 :  : DEC T(TA) P(C£E) K(£DS)
_7_Tabella B£G
 :  : DEC T(TA) P(B£G) K(£DS)
_7_Tabella B£N£C
 :  : DEC T(TA) P(B£N£C) K(DSA)

 :  : INI Eseguire il programma di creazione automatica dei nuovi elementi fase 1
 :  : CMD C D0UTX01
 :  : FIN

Dopo aver eseguito il programma tutti gli elementi sopra indicati dovrenno risultare codificati.


## Controllare il contenuti delle seguenti tabella

_7_Tabella B£1
Tabella base interfaccie.
Il campo "Costi std" deve essere impostato a "S2"
 :  : DEC T(ST) K(B£1)

_7_Tabella D01
Tabella base costi
E' obbligatorio compilare il campo "Liv.Costo assunto".
Identifica il costo totale utilizzato nel calcolo costi.
Verificare il campo "1° liv. Dist. in LIV"
Identifica se portare a livello del padre o lasciare a livello inferiore il costo dei materiali
 :  : DEC T(ST) K(D01)

_7_Tabella D0C
Tabella che gestisce la costruzione del costo delle lavorazioni interna.
Il default Sme_up è il sottosettore ££.
Verificare il legame :  aliquota - codice di carico - indice destinazione costo.
Dove l'aliquota è l'elemento della taballe e deve corripondere all'indice della IGI delle aliquote;
il codice di carico è l'indice dei tempi del ciclo (indice schiera £CRV del ciclo con scansione per componenti di costo);
l'indice di destinazione è l'indice della IGI relativa al costo che si sta calcolando.
 :  : DEC T(ST) K(D0C££)

_7_Tabella D0D
Tabella che gestisce gli indici del costo per materiali, lavorazioni esterne, ricariche.
Il default Sme_up è l'elemento ££.
Contiene gli inidici della IGI dove far confluire i costo dei materiali, delle lavorazioni esterne, e delle ricariche.
 :  : DEC T(ST) K(D0D)

_7_Tabella D5S
Tabella che gestisce i contesti dei costi.
Sone gestiti i contesti : 
* AR    Articolo.
* OR    Ordine produzione.
* DRXXX Riga documento, dove XXX è il tipo documento.
* LO    Lotto
* CC    Cetro di costo
 :  : DEC T(ST) K(D5S)

_7_Tabella D5O
Tabella che gestisce i temi dei vari contesti.
Il sottosettore è definito nella tabella del contesto. Generalmente di default si mantiene come nome del sottosettore l'oggetto del contesto.
Come standard Sme_up il tema corrisponde al tipo costo.
La procedura di costruzione del tipo costo crea in automatico anche il suo tema, con struttura di indici di default IGI£S.
 :  : DEC T(ST) K(D5OAR)
 :  : DEC T(ST) K(D5OOR)
 :  : DEC T(ST) K(D5ODR)
 :  : DEC T(ST) K(D5OLO)
 :  : DEC T(ST) K(D5OCC)

_7_Tabella PER
Tabella che gestisce i periodi di validità del costo.
 :  : DEC T(ST) K(PER)

_7_Tabella BRT
Tabella che gestisce i tipi cicli
I cicli sono un elemento portante del calcolo costi base.
Prima eseguire il calcolo costi base verificare il corretto funzionamento dei cicli
 :  : DEC T(ST) K(BRT)

_7_Tabella BRL
Tabella che gestisce i tipi distinte
Le distinte sono un elemento portante del calcolo costi base.
Prima eseguire il calcolo costi base verificare il corretto funzionamento delle distinte.
 :  : DEC T(ST) K(BRL)

_7_Tabella TCO
Tabella che gestisce i tipi costo
Il tipo costo è l'elemento base del calcolo costi.
E' stato implementato un set'n play per il controllo e la creazione di un tipo costo e di tutti i componenti coinvolti nel relativo calcolo.
 :  : DEC T(ST) K(TCO)

_7_Tabella D0E
Tabella che gestisce gli errori nel calcolo costi
Ogni errore che si presenta nel calcolo deve essere codificato in questa tabella.
Il campo "Tipologia Errore" ne determina il comportamento : 
- 0 Errore non gestito, se non si vuole gestire l'errore
- 1 Errore warning, se si vuole solo documentare l'errore
- 2 Errore vincolante, se si vuole bloccare la memorizzazione del costo (in funzione dei parametri di lancio)
 :  : DEC T(ST) K(D0E)

_7_Tabella D0J
Tabella che le fonti per l'estrazione di oggetti nel calcolo costi totalizzati.
Sono gestite le seguenti fonti : 
- 1 Movimenti magazzino
- 2 Documenti
 :  : DEC T(ST) K(D0J)

## Politiche

Nella calcolo costi base(ciclo e distinta), è possibile decidere in tabella D01 se portare il costo dei materiali(politica di acquisto) a livello del padre o lasciarli a livello inferiore.
Durante il calcolo del costo di un padre è pertanto necessario sapere la politica di ciascun componente.
Per velocizzare e rendere più precisa questa informazione si è deciso di memorizzare in un flag nel D5COSO0F la politica con cui è stato calcolato un costo.
Con seguenti valori : 
* "A" Politca acqusito
* "L" Politica lavorazione
* "P" Politica produzione
* "*" Politica mista
E' stato implementato un programma che attibuisce allo strorico di tutti i costi di tutti gli articoli presenti nel D5COSO la sua politica ad oggi.
L'aggiornamento dello storico è facoltativo. Serve solo se si fanno risalite su costi storici. Per i nuovi costi viene automaticamente aggiornata dal calcolo
 :  : INI Eseguire il programma di aggiornamento del flag 01 nel D5COSO0F
 :  : CMD C D0UTX02
 :  : FIN

## Set'n play tipi costo
Il tipo costo è l'elemento base del calcolo costi.
Il seguente programma permette una costruzione dinamica di un tipo costo e di tutti i componenti coinvolti nel suo calcolo.
I nomi dei tipi costo proposti sono quelli assunti per default nello Sme_up. Come si potrà vedere è comunque possibile dare un proprio nome ad un tipo costo. Automaticamente il sistema lo renderà valido per tutti quei tipi costo che lo utilizzaranno nel loro set'n play.
Il programma presenta la lista dei tipi costo proposti. L'opzione "CO" gestisce la costruzione di un tipo costo. Il Tasto "F15" gestisce la ridenominazione di un tipo costo.
Si consiglia di NON costruire di massa tutti i tipi costo ma solo quelli che si intende utilizzare.
 :  : INI Eseguire set'n play per la costruzione dei tipi costo
 :  : CMD C D0UTX04A
 :  : FIN

## Tipi costo base
Il tipo costo base proposto da Sme_up è "I20".
Per i suo calcolo sono necessari cicli, distinte e  i seguenti tipi costo : 
* "A01" Aliquote
* "I01" Ultima lavorazione
* "I02" Ultimo acquisto
* "I03" Ultima lavorazione di fase
come si può vedere dal set'n play del tipo costo "I20".
Il set'n play otre ad sver costruito il tipo costo, ha generato anche tutte le sue MDV per il relativo calcolo.
Eseguendo i due programmi di calcolo D0CO01A per la simulazione, e il D0CO01B per il calcolo batch, si trovano già tutte le impostazioni memorizzate come "AR-I20"

Prima di procedere al calcolo è ncessario verificare i cicli(default tipo ciclo "ART"), le distinte(default tipo distinta "ART") e i tipi costo base che lo compongono : 

_7_ A01 Aliquote
Deve essere presente sul contesto "CC" il tipo costo "A01".
 :  : INI Verificare la presenza aliquote
 :  : CMD UP COS
 :  : FIN
Verificare con il TSTG55 se effettivamente la lettura dell'aliquota va a buon fine
 :  : INI Funzione "LET", Contesto "CC"
 :  : CMD T G55
 :  : FIN

_7_ I01 Ultima lavorazione
Verificare l'elemento "I01" della tabella "TCO"
 :  : DEC T(TA) P(TCO) K(I01)
Come default è stato proposto un costo dinamico sull'ultimo documento. Campo "Gestione eccezioni" impostato a "ULD".
Sono sicuramente da verificare i "parametri eccezione" proposti dove è presente il tipo documento. Il campo "C/to lavoro" deve rimanere a "1"
Se come lavorazione si vuole gestire un altra tipologia di costo dinamico, creare un nuovo tipo costo. Le possibli scelte sono documentate nel capitolo D0CCMC_12
- [Costo Dinamico](Sorgenti/MB/DOC/D0CCMC_12)
Verificare con il TSTG55 se effettivamente la lettura del costo va a buon fine
La documentazione specifica D0CCMC_12 spiega come come si determina il costo. Io ogni caso il programma eseguito è il B£G55S
 :  : INI Funzione "LET", Contesto "AR".
 :  : CMD T G55
 :  : FIN
Il fatto di avere come costo di ultima lavorazione un costo dinamico è solo una proposta. Il costo potrebbe benissimo essere un costo memorizzato in precedenza. Per esempio un costo medio di articolo calcolato con il G9AS10. In questo caso per verificare la lettura eseguire prima un UP COS per assicurarsi che il costo sia stato fisicamente memorizzato,  e poi un TSTG55 per assicurarsi che la lettura vada a buon fine.

_7_ I02 Ultimo acquisto
Seguire la stessa procedura del tipo costo "I01" ultima lavorazione.
Verficare l'elemento "I02" della tabella "TCO"
 :  : DEC T(TA) P(TCO) K(I02)

_7_ I03 Ultima lavorazione di faseo
Seguire la stessa procedura del tipo costo "I01" ultima lavorazione, ma con l'aggiunta nella gestione/ricerca del costo dell'oggetto FA.
Verifcare l'elemento "I03" della tabella "TCO"
 :  : DEC T(TA) P(TCO) K(I03)
