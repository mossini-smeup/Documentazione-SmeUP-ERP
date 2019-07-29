# Autorizzazioni
Esiste la possibilità di controllare l'autorizzazione di un OAV, sia in scansione slot, sia in ritorno del singolo attributo.
Questa modalità viene eseguita a richiesta, impostando un parametro nel richiamo della routine £OAV (£OAVI_CTRA).
In questo caso il valore dell'OAV viene lasciato vuoto, ed inoltre viene ritornato un flag di  "non autorizzazione" (£OAVO_NOAU) in modo da distinguere il caso di OAV con valore nullo (o zero) da quello di OAV non autorizzato.

Questa funzionalità è stata utilizzata nella presentazione delle colonne aggiuntive :  gli OAV a cui l'utente non è autorizzato non vengono presentati, e quindi non possono essere scelti.
Analogamente, nella presentazione degli OAV di un oggetto (INFO), vengono esclusi quelli non autorizzati.

## OAV numerici e autorizzazioni
In realtà, ad oggi, esiste una categoria di OAV almeno potenzialmente autorizzati :  i V/, (numerici).
Essi provengono dai numeri dell'oggetto, elaborati dalla routine £G37, che lancia i programmi specifici di ogni oggetto, in cui è previsto, ed in alcuni casi implementato, il controllo delle autorizzazioni.
Esiste nella £G37 il ritorno di una schiera di flag di campo non autorizzato.
Quindi, se il richiamo della £OAV richiede il controllo delle autorizzazioni, gli OAV V/ (ed i corrispondenti O/ storicizzati) tornano le autorizzazioni restituite dalla £G37.
Il risultato è che per questi oggetti, gli OAV V/ sono a tutti gli effetti sotto autorizzazione.

Gli OAV I/ e J/ che sono origine di OAV V/, sono stati sottoposti alla stessa autorizzazione.
Ad esempio, per l'oggetto DR, se l'utente non è abilitato ai prezzi, non può vedere sia gli OAV V/ sia gli I/ corrispondenti (come si potrà vedere in seguito).

## Classe di autorizzazione utilizzata
La classe di autorizzazione utilizzata dalla £G37 e quindi dagli OAV V/ e dai corrispondenti OAV I/ e J/ è la **RIS-**.
La funzione utilizzata è composta dal prefisso **VL_ seguito dal tipo e dal parametro oggetto (ad esempio VL_DRxxx).
E' stato inoltre aggiunto il codice RI06 alla B£S (AZ) per la gestione dell'autorizzazione dei numeri liberi.

# Autorizzazioni OAV oggetto E1
Ha lo scopo di autorizzare, in base a classi e funzioni già presenti e utilizzate :  - gli OAV I/ e J/ numerici dell'oggetto E1.

## Autorizzazioni
Le autorizzazioni si basano sulla classe 'RIS-', e sulla funzione 'VL_E1'

## Numeri G37 e OAV V/
Posizioni / Tipo / Posizione autorizzaz.
        1  Quantità um.interna    01
        2  Quantità um.esterna    01
        3  Costo standard         02
        4  Costo previsto         03
        5  Costo effettivo        03
        6  Importo standard       02
        7  Importo previsto       03
        8  Importo effettivo      03
        9  Entrate um.interna     01
       10  Uscite  um.interna     01
       11  Entrate um.esterna     01
       12  Uscite  um.esterna     01
       13  Valore entrate         02
       14  Valore uscite          02
 15 -  19  Numeri liberi          06


## OAV I/ e J/

Sono stati autorizzati con posizione 01 (quantità) i seguenti OAV
I/31   :  : DEC T(CS) P(F-GMMOVI0F) K(S§QTUM) I(·)
I/34   :  : DEC T(CS) P(F-GMMOVI0F) K(S§QTAQ) I(·)

Sono stati autorizzati con posizione 02 (costi/margini) i seguenti OAV
I/36   :  : DEC T(CS) P(F-GMMOVI0F) K(S§CSST) I(·)

Sono stati autorizzati con posizione 03 (prezzi/valori) i seguenti OAV
I/37   :  : DEC T(CS) P(F-GMMOVI0F) K(S§CSPR) I(·)
I/38   :  : DEC T(CS) P(F-GMMOVI0F) K(S§CSEF) I(·)

Sono stati autorizzati con posizione 06 (numeri liberi) i seguenti OAV
I/68   :  : DEC T(CS) P(F-GMMOVI0F) K(S§NUM1) I(·)
I/68   :  : DEC T(CS) P(F-GMMOVI0F) K(S§NUM2) I(·)
I/68   :  : DEC T(CS) P(F-GMMOVI0F) K(S§NUM3) I(·)
I/68   :  : DEC T(CS) P(F-GMMOVI0F) K(S§NUM4) I(·)
I/68   :  : DEC T(CS) P(F-GMMOVI0F) K(S§NUM5) I(·)


## Autorizzazioni su lista campi (5250)                               
La classe è sempre 'RIS-', la funzione è 'V5D-xxx', dove xxx è il campo S§TIDI (Tipo documento interno)  :  in questo modo è possibile autorizzare contestualmente documenti e movimenti.

Autorizzazioni con posizione 01 (quantità) ai seguenti campi
         :  : DEC T(CS) P(F-GMMOVI0F) K(S§QTUM) I(·)
         :  : DEC T(CS) P(F-GMMOVI0F) K(S§QTAQ) I(·)
_1_nuova  :  : DEC T(CS) P(F-GMMOVI0F) K(S§NCON) I(·)

Autorizzazioni con posizione 02 (costi/margini) ai seguenti campi
         :  : DEC T(CS) P(F-GMMOVI0F) K(S§CSST) I(·)

Autorizzazioni con posizione 03 (prezzi/valori) ai seguenti campi
_1_era 02 :  : DEC T(CS) P(F-GMMOVI0F) K(S§CSPR) I(·)
_1_era 02 :  : DEC T(CS) P(F-GMMOVI0F) K(S§CSEF) I(·)

Autorizzazioni con posizione 05 (enti) ai seguenti campi
         :  : DEC T(CS) P(F-GMMOVI0F) K(S§TIEN) I(·)
         :  : DEC T(CS) P(F-GMMOVI0F) K(S§COEN) I(·)
         :  : DEC T(CS) P(F-GMMOVI0F) K(S§TIES) I(·)
         :  : DEC T(CS) P(F-GMMOVI0F) K(S§COES) I(·)

Autorizzazioni con posizione 06 (numeri liberi) ai seguenti campi
_1_nuova  :  : DEC T(CS) P(F-GMMOVI0F) K(S§NUM1) I(·)
_1_nuova  :  : DEC T(CS) P(F-GMMOVI0F) K(S§NUM2) I(·)
_1_nuova  :  : DEC T(CS) P(F-GMMOVI0F) K(S§NUM3) I(·)
_1_nuova  :  : DEC T(CS) P(F-GMMOVI0F) K(S§NUM4) I(·)
_1_nuova  :  : DEC T(CS) P(F-GMMOVI0F) K(S§NUM5) I(·)


# Autorizzazioni OAV Oggetti DO e DR                                            
Lo scopo è quello di autorizzare, in base a classi e funzioni già presenti e utilizzate : 
- gli OAV I/ e J/ numerici dei documenti (testate e righe), e quelli riconducibili a
  numeri (agenti e tipi provvigioni, autorizzati conguintamente ai valori delle provvigioni).
- le funzioni di reperimento informazioni (£V5V,£V5Q,£V5F).

## Autorizzazioni                                                     
Le autorizzazioni si basano sulla classe 'RIS-', e su funzioni basate sul tipo documento(nel seguito indicato come xxx).

### G37 - DO
La funzione di autorizzazione è VL_DOxxx.

### G37 - DR
La funzione di autorizzazione è VL_DRxxx.

Posizioni / Tipo / Posizione autorizzaz.
  1 -  30  Quantità               01
 21 -  50  Valori in valute       03
 51 -  60  Valori a costo         02
       61  N.Contenitori          01
 62 -  66  N.liberi (1/5)         06
       67  Costo unitario         02
       71  Q.tà fatt.             01
 72 -  83  Prezzi/Importi/Imposte 03
 84 -  95  Provvigioni            04
101 - 112  Valori in valute       03
113 - 117  Valori a costo         02
118 - 126  Valori medi in valute  03
127 - 129  Costi medi             02
130 - 143  Delta                  02
144 - 145  Quantità residue       01
146 - 150  N.liberi (6/10)        06


## OAV I/ J/                                                          
La funzione di autorizzazione è la stessa, per uniformità, di quella utilizzata per autorizzare i numeri G37 (e quindi, implicitamente) gli OAV /N, quindi è 'VL-DOxxx' per le testate, e 'VL-DRxxx' per le righe.

### OAV DO

Sono stati autorizzati con posizione 01 (quantità) i seguenti OAV
I/49   :  : DEC T(CS) P(F-V5TDOC0F) K(T§PESN) I(·)
I/50   :  : DEC T(CS) P(F-V5TDOC0F) K(T§PESL) I(·)
I/51   :  : DEC T(CS) P(F-V5TDOC0F) K(T§NCOL) I(·)

Sono stati autorizzati con pa posizione 03 (prezzi/valori) i seguenti OAV
I/CZ   :  : DEC T(CS) P(F-V5TDOC0F) K(T§SCM1) I(·)
I/C0   :  : DEC T(CS) P(F-V5TDOC0F) K(T§SCM2) I(·)
I/C1   :  : DEC T(CS) P(F-V5TDOC0F) K(T§SCM3) I(·)
I/C2   :  : DEC T(CS) P(F-V5TDOC0F) K(T§SCM4) I(·)
I/C3   :  : DEC T(CS) P(F-V5TDOC0F) K(T§SCM5) I(·)

Sono stati autorizzati con posizione 04 (provvigioni) i seguenti OAV
I/61   :  : DEC T(CS) P(F-V5TDOC0F) K(T§AGE1) I(·)
I/62   :  : DEC T(CS) P(F-V5TDOC0F) K(T§AGE2) I(·)
I/66   :  : DEC T(CS) P(F-V5TDOC0F) K(T§PER1) I(·)
I/67   :  : DEC T(CS) P(F-V5TDOC0F) K(T§PER2) I(·)
I/AE   :  : DEC T(CS) P(F-V5TDOC0F) K(T§AGE3) I(·)
I/AF   :  : DEC T(CS) P(F-V5TDOC0F) K(T§AGE4) I(·)
I/AG   :  : DEC T(CS) P(F-V5TDOC0F) K(T§PER3) I(·)
I/AH   :  : DEC T(CS) P(F-V5TDOC0F) K(T§PER4) I(·)
I/CV   :  : DEC T(CS) P(F-V5TDOC0F) K(T§TPR1) I(·)
I/CW   :  : DEC T(CS) P(F-V5TDOC0F) K(T§TPR2) I(·)
I/CX   :  : DEC T(CS) P(F-V5TDOC0F) K(T§TPR3) I(·)
I/CY   :  : DEC T(CS) P(F-V5TDOC0F) K(T§TPR4) I(·)

Sono stati autorizzati con posizione 06 (numeri liberi) i seguenti OAV
I/AS   :  : DEC T(CS) P(F-V5TDOC0F) K(T§NUM1) I(·)
I/AT   :  : DEC T(CS) P(F-V5TDOC0F) K(T§NUM2) I(·)
I/AU   :  : DEC T(CS) P(F-V5TDOC0F) K(T§NUM3) I(·)
I/AV   :  : DEC T(CS) P(F-V5TDOC0F) K(T§NUM4) I(·)
I/AW   :  : DEC T(CS) P(F-V5TDOC0F) K(T§NUM5) I(·)
I/BZ   :  : DEC T(CS) P(F-V5TDOC0F) K(T§NR06) I(·)
I/B0   :  : DEC T(CS) P(F-V5TDOC0F) K(T§NR07) I(·)
I/B1   :  : DEC T(CS) P(F-V5TDOC0F) K(T§NR08) I(·)
I/B2   :  : DEC T(CS) P(F-V5TDOC0F) K(T§NR09) I(·)
I/B3   :  : DEC T(CS) P(F-V5TDOC0F) K(T§NR10) I(·)

### OAV DR

Sono stati autorizzati con posizione 01 (quantità) i seguenti OAV
I/36   :  : DEC T(CS) P(F-V5RDOC0F) K(R§QT01) I(·)
I/37   :  : DEC T(CS) P(F-V5RDOC0F) K(R§QT02) I(·)
I/38   :  : DEC T(CS) P(F-V5RDOC0F) K(R§QT03) I(·)
I/39   :  : DEC T(CS) P(F-V5RDOC0F) K(R§QT04) I(·)
I/40   :  : DEC T(CS) P(F-V5RDOC0F) K(R§QT05) I(·)
I/41   :  : DEC T(CS) P(F-V5RDOC0F) K(R§UNMV) I(·)
I/42   :  : DEC T(CS) P(F-V5RDOC0F) K(R§FATC) I(·)
I/43   :  : DEC T(CS) P(F-V5RDOC0F) K(R§Q01V) I(·)
I/44   :  : DEC T(CS) P(F-V5RDOC0F) K(R§Q02V) I(·)
I/45   :  : DEC T(CS) P(F-V5RDOC0F) K(R§Q03V) I(·)
I/46   :  : DEC T(CS) P(F-V5RDOC0F) K(R§Q04V) I(·)
I/47   :  : DEC T(CS) P(F-V5RDOC0F) K(R§Q05V) I(·)
I/AE   :  : DEC T(CS) P(F-V5RDOC0F) K(R§NUCO) I(·)
J/002  :  : DEC T(OA) P(DR        ) K(J/002 ) I(·)
J/003  :  : DEC T(OA) P(DR        ) K(J/003 ) I(·)
J/004  :  : DEC T(OA) P(DR        ) K(J/004 ) I(·)
J/005  :  : DEC T(OA) P(DR        ) K(J/005 ) I(·)
J/O01  :  : DEC T(OA) P(DR        ) K(J/O01 ) I(·)
J/O02  :  : DEC T(OA) P(DR        ) K(J/O02 ) I(·)

Sono stati autorizzati con posizione 03 (prezzi/valori) i seguenti OAV
I/29   :  : DEC T(CS) P(F-V5RDOC0F) K(R§VAL1) I(·)
I/30   :  : DEC T(CS) P(F-V5RDOC0F) K(R§VAL2) I(·)
I/31   :  : DEC T(CS) P(F-V5RDOC0F) K(R§VAL3) I(·)
I/32   :  : DEC T(CS) P(F-V5RDOC0F) K(R§VAL4) I(·)
I/33   :  : DEC T(CS) P(F-V5RDOC0F) K(R§VAL5) I(·)
I/88   :  : DEC T(CS) P(F-V5RDOC0F) K(R§QRIV) I(·)
I/89   :  : DEC T(CS) P(F-V5RDOC0F) K(R§PEFF) I(·)
I/90   :  : DEC T(CS) P(F-V5RDOC0F) K(R§VALR) I(·)
I/91   :  : DEC T(CS) P(F-V5RDOC0F) K(R§CAMR) I(·)
I/92   :  : DEC T(CS) P(F-V5RDOC0F) K(R§PFRA) I(·)
I/EC   :  : DEC T(CS) P(F-V5RDOC0F) K(R§QEFF) I(·)
I/ED   :  : DEC T(CS) P(F-V5RDOC0F) K(R§QEFV) I(·)

Sono stati autorizzati con posizione 04 (provvigioni) i seguenti OAV
I/15   :  : DEC T(CS) P(F-V5RDOC0F) K(R§AGE1) I(·)
I/16   :  : DEC T(CS) P(F-V5RDOC0F) K(R§AGE2) I(·)
I/17   :  : DEC T(CS) P(F-V5RDOC0F) K(R§PER1) I(·)
I/18   :  : DEC T(CS) P(F-V5RDOC0F) K(R§PER2) I(·)
I/93   :  : DEC T(CS) P(F-V5RDOC0F) K(R§AGE3) I(·)
I/94   :  : DEC T(CS) P(F-V5RDOC0F) K(R§AGE4) I(·)
I/95   :  : DEC T(CS) P(F-V5RDOC0F) K(R§PER3) I(·)
I/96   :  : DEC T(CS) P(F-V5RDOC0F) K(R§PER4) I(·)
I/D5   :  : DEC T(CS) P(F-V5RDOC0F) K(R§TPR1) I(·)
I/D6   :  : DEC T(CS) P(F-V5RDOC0F) K(R§TPR2) I(·)
I/D7   :  : DEC T(CS) P(F-V5RDOC0F) K(R§TPR3) I(·)
I/D8   :  : DEC T(CS) P(F-V5RDOC0F) K(R§TPR4) I(·)

Sono stati autorizzati con posizione 06 (numeri liberi) i seguenti OAV
I/AW   :  : DEC T(CS) P(F-V5RDOC0F) K(R§NUM1) I(·)
I/AX   :  : DEC T(CS) P(F-V5RDOC0F) K(R§NUM2) I(·)
I/AY   :  : DEC T(CS) P(F-V5RDOC0F) K(R§NUM3) I(·)
I/AZ   :  : DEC T(CS) P(F-V5RDOC0F) K(R§NUM4) I(·)
I/A0   :  : DEC T(CS) P(F-V5RDOC0F) K(R§NUM5) I(·)
I/B4   :  : DEC T(CS) P(F-V5RDOC0F) K(R§NR06) I(·)
I/B5   :  : DEC T(CS) P(F-V5RDOC0F) K(R§NR07) I(·)
I/B6   :  : DEC T(CS) P(F-V5RDOC0F) K(R§NR08) I(·)
I/B7   :  : DEC T(CS) P(F-V5RDOC0F) K(R§NR09) I(·)
I/B8   :  : DEC T(CS) P(F-V5RDOC0F) K(R§NR10) I(·)
R/DO/NUM1  :  : DEC T(OA) P(DR        ) K(R/DO/NUM1) I(·)
R/DO/NUM2  :  : DEC T(OA) P(DR        ) K(R/DO/NUM2) I(·)
R/DO/NUM3  :  : DEC T(OA) P(DR        ) K(R/DO/NUM3) I(·)
R/DO/NUM4  :  : DEC T(OA) P(DR        ) K(R/DO/NUM4) I(·)
R/DO/NUM5  :  : DEC T(OA) P(DR        ) K(R/DO/NUM5) I(·)
R/DO/NR06  :  : DEC T(OA) P(DR        ) K(R/DO/NR06) I(·)
R/DO/NR07  :  : DEC T(OA) P(DR        ) K(R/DO/NR07) I(·)
R/DO/NR08  :  : DEC T(OA) P(DR        ) K(R/DO/NR08) I(·)
R/DO/NR09  :  : DEC T(OA) P(DR        ) K(R/DO/NR09) I(·)
R/DO/NR10  :  : DEC T(OA) P(DR        ) K(R/DO/NR10) I(·)


## Autorizzazioni su lista campi (5250)                               
La classe è sempre 'RIS-', la funzione per i DO e i DR è 'V5D-xxx'.

### G11 DO
Autorizzazioni con posizione 01 (quantità) ai seguenti campi
         :  : DEC T(CS) P(F-V5TDOC0F) K(T§PESN) I(·)
         :  : DEC T(CS) P(F-V5TDOC0F) K(T§PESL) I(·)
         :  : DEC T(CS) P(F-V5TDOC0F) K(T§NCOL) I(·)

Autorizzazioni con posizione 03 (prezzi/valori) ai seguenti campi
         :  : DEC T(CS) P(F-V5TDOC0F) K(T§SCM1) I(·)
         :  : DEC T(CS) P(F-V5TDOC0F) K(T§SCM2) I(·)
         :  : DEC T(CS) P(F-V5TDOC0F) K(T§SCM3) I(·)
         :  : DEC T(CS) P(F-V5TDOC0F) K(T§SCM4) I(·)
         :  : DEC T(CS) P(F-V5TDOC0F) K(T§SCM5) I(·)

Autorizzazioni con posizione 04 (provvigioni) ai seguenti campi
         :  : DEC T(CS) P(F-V5TDOC0F) K(T§AGE1) I(·)
         :  : DEC T(CS) P(F-V5TDOC0F) K(T§AGE2) I(·)
         :  : DEC T(CS) P(F-V5TDOC0F) K(T§AGE3) I(·)
         :  : DEC T(CS) P(F-V5TDOC0F) K(T§AGE4) I(·)
         :  : DEC T(CS) P(F-V5TDOC0F) K(T§PER1) I(·)
         :  : DEC T(CS) P(F-V5TDOC0F) K(T§PER2) I(·)
         :  : DEC T(CS) P(F-V5TDOC0F) K(T§PER3) I(·)
         :  : DEC T(CS) P(F-V5TDOC0F) K(T§PER4) I(·)
         :  : DEC T(CS) P(F-V5TDOC0F) K(T§TPR1) I(·)
         :  : DEC T(CS) P(F-V5TDOC0F) K(T§TPR2) I(·)
         :  : DEC T(CS) P(F-V5TDOC0F) K(T§TPR3) I(·)
         :  : DEC T(CS) P(F-V5TDOC0F) K(T§TPR4) I(·)

Autorizzazioni con posizione 05 (enti) ai seguenti campi
         :  : DEC T(CS) P(F-V5TDOC0F) K(T§TCCL) I(·)
         :  : DEC T(CS) P(F-V5TDOC0F) K(T§CDCL) I(·)
         :  : DEC T(CS) P(F-V5TDOC0F) K(T§TCDC) I(·)
         :  : DEC T(CS) P(F-V5TDOC0F) K(T§CDCC) I(·)
         :  : DEC T(CS) P(F-V5TDOC0F) K(T§TCDF) I(·)
         :  : DEC T(CS) P(F-V5TDOC0F) K(T§CODF) I(·)
         :  : DEC T(CS) P(F-V5TDOC0F) K(T§TCDS) I(·)
         :  : DEC T(CS) P(F-V5TDOC0F) K(T§CODS) I(·)
         :  : DEC T(CS) P(F-V5TDOC0F) K(T§VET1) I(·)
         :  : DEC T(CS) P(F-V5TDOC0F) K(T§RVE1) I(·)
         :  : DEC T(CS) P(F-V5TDOC0F) K(T§VET2) I(·)
         :  : DEC T(CS) P(F-V5TDOC0F) K(T§RVE2) I(·)
         :  : DEC T(CS) P(F-V5TDOC0F) K(T§VET3) I(·)

Autorizzazioni con posizione 06 (numeri liberi) ai seguenti campi
_1_nuova  :  : DEC T(CS) P(F-V5TDOC0F) K(T§NUM1) I(·)
_1_nuova  :  : DEC T(CS) P(F-V5TDOC0F) K(T§NUM2) I(·)
_1_nuova  :  : DEC T(CS) P(F-V5TDOC0F) K(T§NUM3) I(·)
_1_nuova  :  : DEC T(CS) P(F-V5TDOC0F) K(T§NUM4) I(·)
_1_nuova  :  : DEC T(CS) P(F-V5TDOC0F) K(T§NUM5) I(·)
_1_nuova  :  : DEC T(CS) P(F-V5TDOC0F) K(T§NR06) I(·)
_1_nuova  :  : DEC T(CS) P(F-V5TDOC0F) K(T§NR07) I(·)
_1_nuova  :  : DEC T(CS) P(F-V5TDOC0F) K(T§NR08) I(·)
_1_nuova  :  : DEC T(CS) P(F-V5TDOC0F) K(T§NR09) I(·)
_1_nuova  :  : DEC T(CS) P(F-V5TDOC0F) K(T§NR10) I(·)

### G11 DR
Autorizzazioni con posizione 01 (quantità) ai seguenti campi
         :  : DEC T(CS) P(F-V5RDOC0F) K(R§QT01) I(·)
         :  : DEC T(CS) P(F-V5RDOC0F) K(R§QT02) I(·)
         :  : DEC T(CS) P(F-V5RDOC0F) K(R§QT03) I(·)
         :  : DEC T(CS) P(F-V5RDOC0F) K(R§QT04) I(·)
         :  : DEC T(CS) P(F-V5RDOC0F) K(R§QT05) I(·)
         :  : DEC T(CS) P(F-V5RDOC0F) K(R§Q01V) I(·)
         :  : DEC T(CS) P(F-V5RDOC0F) K(R§Q02V) I(·)
         :  : DEC T(CS) P(F-V5RDOC0F) K(R§Q03V) I(·)
         :  : DEC T(CS) P(F-V5RDOC0F) K(R§Q04V) I(·)
         :  : DEC T(CS) P(F-V5RDOC0F) K(R§Q05V) I(·)
_1_nuova  :  : DEC T(CS) P(F-V5RDOC0F) K(R§NUCO) I(·)

Autorizzazioni con posizione 03 (prezzi/valori) ai seguenti campi
         :  : DEC T(CS) P(F-V5RDOC0F) K(R§VAL1) I(·)
         :  : DEC T(CS) P(F-V5RDOC0F) K(R§VAL2) I(·)
         :  : DEC T(CS) P(F-V5RDOC0F) K(R§VAL3) I(·)
         :  : DEC T(CS) P(F-V5RDOC0F) K(R§VAL4) I(·)
         :  : DEC T(CS) P(F-V5RDOC0F) K(R§VAL5) I(·)
         :  : DEC T(CS) P(F-V5RDOC0F) K(R§VAL5) I(·)
         :  : DEC T(CS) P(F-V5RDOC0F) K(R§QRIV) I(·)
         :  : DEC T(CS) P(F-V5RDOC0F) K(R§PEFF) I(·)
         :  : DEC T(CS) P(F-V5RDOC0F) K(R§VALR) I(·)
         :  : DEC T(CS) P(F-V5RDOC0F) K(R§CAMR) I(·)
         :  : DEC T(CS) P(F-V5RDOC0F) K(R§PFRA) I(·)
         :  : DEC T(CS) P(F-V5RDOC0F) K(R§QEFF) I(·)
         :  : DEC T(CS) P(F-V5RDOC0F) K(R§QEFV) I(·)

Autorizzazioni con posizione 04 (provvigioni) ai seguenti campi
         :  : DEC T(CS) P(F-V5RDOC0F) K(R§AGE1) I(·)
         :  : DEC T(CS) P(F-V5RDOC0F) K(R§AGE2) I(·)
         :  : DEC T(CS) P(F-V5RDOC0F) K(R§AGE3) I(·)
         :  : DEC T(CS) P(F-V5RDOC0F) K(R§AGE4) I(·)
         :  : DEC T(CS) P(F-V5RDOC0F) K(R§PER1) I(·)
         :  : DEC T(CS) P(F-V5RDOC0F) K(R§PER2) I(·)
         :  : DEC T(CS) P(F-V5RDOC0F) K(R§PER3) I(·)
         :  : DEC T(CS) P(F-V5RDOC0F) K(R§PER4) I(·)
         :  : DEC T(CS) P(F-V5RDOC0F) K(R§TPR1) I(·)
         :  : DEC T(CS) P(F-V5RDOC0F) K(R§TPR2) I(·)
         :  : DEC T(CS) P(F-V5RDOC0F) K(R§TPR3) I(·)
         :  : DEC T(CS) P(F-V5RDOC0F) K(R§TPR4) I(·)

Autorizzazioni con posizione 05 (enti) ai seguenti campi
         :  : DEC T(CS) P(F-V5RDOC0F) K(R§RECO) I(·)

Autorizzazioni con posizione 06 (numeri liberi) ai seguenti campi
_1_nuova  :  : DEC T(CS) P(F-V5RDOC0F) K(R§NUM1) I(·)
_1_nuova  :  : DEC T(CS) P(F-V5RDOC0F) K(R§NUM2) I(·)
_1_nuova  :  : DEC T(CS) P(F-V5RDOC0F) K(R§NUM3) I(·)
_1_nuova  :  : DEC T(CS) P(F-V5RDOC0F) K(R§NUM4) I(·)
_1_nuova  :  : DEC T(CS) P(F-V5RDOC0F) K(R§NUM5) I(·)
_1_nuova  :  : DEC T(CS) P(F-V5RDOC0F) K(R§NR06) I(·)
_1_nuova  :  : DEC T(CS) P(F-V5RDOC0F) K(R§NR07) I(·)
_1_nuova  :  : DEC T(CS) P(F-V5RDOC0F) K(R§NR08) I(·)
_1_nuova  :  : DEC T(CS) P(F-V5RDOC0F) K(R§NR09) I(·)
_1_nuova  :  : DEC T(CS) P(F-V5RDOC0F) K(R§NR10) I(·)


## Funzioni
Le autorizzazioni sulle funzioni sono state rese omogenee, ed è stata resa esplicita la
richiesta del controllo autorizzazione, e conseguentemente la risposta

### Funzioni fatturazione £V5F
Questa routine controllava le autorizzazioni con la funzione V5xxx, e, in caso di visualizzazione, presentava il messaggio di utente non autorizzato.
Sono stati aggiunti tre campi alla /COPY, di controllo e ritorno autorizzazioni.
Se richiamata in controllo autorizzazioni, al primo richiamo viene tornato se l'utente non è autorizzato rispettivamente a importi/tasse/conti/scadenze/spese e alle provvigioni.
E' stata inoltre modificata l'associazione : 
In precedenza
Posizione 03  :  non autorizzato per importi, tasse, conti e scadenze
Posizione 04  :  non autorizzato per provvigioni e spese
E' diventata
Posizione 03  :  non autorizzato per importi, tasse, conti, scadenze e spese
Posizione 04  :  non autorizzato per provvigioni
NB :  questa funzione, se l'utente non è autorizzato, ritorna comunque i valori.
Nei richiami standard (focus), in questo caso è disattivato il passaggio alla presentazione dei valori.
Nei richiami personali, è cura dell'implementatore di decidere come procedere.

### Funzioni quantità e valori £V5Q e £V5Q
Per completare l'intervento, anche a queste due funzioni sono stati aggiunti due campi,
controllo autorizzazioni (input) e utente autorizzato (output).
L'associazione, che utilizza la funzione 'VL_DR_xxx' è : 
. Posizione 01 per la £V5Q (quantità)
. Posizione 03 per la £V5V (valori)
Per analogia alla £V5F, anche in questi casi i campi vengono sempre ritornati, anche in caso di utente non autorizzato.
Questa funzionalità è stata utilizzata, ad oggi, soltanto nel focus di riga.

