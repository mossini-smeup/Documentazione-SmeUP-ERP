# CRB - Causali di magazzino Q9000
 :  : DEC T(ST) K(CRB)
## OBIETTIVO
La tabella CRB è organizzata in sottosettori. Viene utilizzato il sottosettore che ha il nome del tipo lotto.
---------------------------------------------------------------------
CQAM30_XX  Registrazione collaudo A magazzino
---------------------------------------------------------------------
Documentazione generale
OBIETTIVO
Aggiornare il movimento di magazzino con la quantità rilevata dalla dichiarazione di collaudo
FLUSSO
Chiamato dal pgm di dichiarazione collaudo
PARAMETRI
Numero BEM
Qtà rilevata in UM Mag
"      "     in UM Acq (ininfluente)
N. lotto
Flag di modifica dichiarazione
Indicatore fallimento
*In52  Off    OK
On     fallimento
Elenco File Utilizzati
ANMG201L  Anagrafica magazzino      (ACG)
CQLOTT1L  Lotti ricevuti al controllo qualità
MOMA201L  Movimenti di magazzino    (ACG)
MWMV200F  Movimentazione di massa   (ACG)
.
FLUSSO : 
* Registra i movimenti magazzino della dichiaraz. di collaudo * Verifica se il collaudo ha scartato qualche pezzo
C                     Z-ADDT§QSCA    SCARTI 153
*
C           U$QRIL    SUB  SCARTI    BUONA  153
C           U$QRIL    SUB  T§QLOT    DELTA  153
*
* T§QLOT  quantità dichiarata
* U$QRIL  quantità rilevata
* SCARTI  quantità scartata
* BUONA   quantità buona
* DELTA   delta quantità
MOVIMENTI EFFETTUABILI : 
1)  Q.tà Lotto è riportata da Collaudo a Magazzino
T$CCQ1 e T$CCQ2
2)  Q.tà scartata tolta dalla giacenza e posta in Mag.scarti (T$CSC1 T$CSC2)
3)  Q.tà DELTA è sottratta o aggiunta nella giacenza e messa eventualmente in magaz. errori documentali.
I campi della tabella CRB stabiliscono le causali di movimentazione
## CONTENUTO DEI CAMPI
 :  : FLD T$CSC1    Causale di scarto        1    CHAR 4
 :  : FLD T$MSC1    Magazzino di scarto      1    CHAR 2
 :  : FLD T$CSC2    Causale di scarto        2    CHAR 4
 :  : FLD T$MSC2    Magazzino di scarto      2    CHAR 2
 :  : FLD T$CDP1    Causale RIL > DICH       1    CHAR 4
 :  : FLD T$CDN1    Causale RIL < DICH       1    CHAR 4
 :  : FLD T$MDE1    Magazzino per delta qtà  1    CHAR 2
 :  : FLD T$CDP2    Causale RIL > DICH       2    CHAR 4
 :  : FLD T$CDN2    Causale RIL < DICH       2    CHAR 4
 :  : FLD T$MDE2    Magazzino per delta qta  2    CHAR 2
 :  : FLD T$CCQ1    Causale scarico CQ       1    CHAR 4
 :  : FLD T$MCQ1    Magazzino CQ             1    CHAR 2
 :  : FLD T$CCQ2    Causale scarico CQ       2    CHAR 4
 :  : FLD T$MCQ2    Magazzino CQ             2    CHAR 2
