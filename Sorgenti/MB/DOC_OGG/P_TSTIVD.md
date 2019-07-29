# API DI INTERFACCIA SUL DATABASE DI SMEUP.
Estende API £G60, permettendo di ottenere informazioni quali tracciati record, campi chiave, criteri di selezione di oggetti SmeUp, siano essi files di DB2-OS400 che oggetti
applicativi.

#


## Classi gestite.
F  File Fisico
O  Oggetto
P  Parametro
T  Tabella
V  Vista Virtuale
0  Piano/Vista MPS
.  Valori D5
_ Fonti LOA15

## Funzionalità.
Funzione.Metodo
- ver.Esi
Verifica l'esistenza dell'oggetto passato come "codice", e nel caso di errore, segnala. Fornisce file/libreria/tracciato in cui sono contenute le istanze dell'oggetto.
Fornisce stringa "where" di sintassi SQL atta ad identificare solo le istanze della classe in oggetto.

- sca.Pos/sca.Let
Estende la ver.Esi fornendo anche i metodi di posizionamento(POS) e lettura(LET) di tutti gli oggetti.

- fmt.Lin
Estende la ver.Esi fornendo anche i metodi di traduzione letterale della clausola SQL di "where".
Es :  (X >= Y --> X è maggiore o uguale ad Y)

- fmt.Lin_H
Estende la ver.Esi fornendo anche i metodi di traduzione letterale della clausola SQL di "where" aggiungendo però, rispetto all'analoga fmt.Lin, dei tag di attributi di
visualizzazione xml.
Es :  (X >= Y --> _7_X è maggiore o >uguale ad Y)

- dft.Rit
Estende la ver.Esi fornendo anche i metodi di traduzione letterale della clausola SQL di where aggiungendo però, anche una stringa select che rappresenta le
relazioni utilizzate nel motore SQL per restituire un recordset di istanze della classe in oggetto.

### Esempio 1, contatti : 
Data la classe contatti(CN) di SmeUp, si veda il comportamento della relativa vista _OCN : 

_7_Input
-----
Funzione    DFT        Default
Metodo      RIT        Ritorno Campi/Valori Assunti
Tipo        O            Oggetto
Codice      _OCN

>Output
------
Descrizione Contatto
File        BRENTI0F
Libreria    XGES_DAT
Tracciato   F-BRENTI0F
Codice  ID  E§CRAG
Descr.  ID  E§RAGS
Assunto ID  E§TRAG
Where       E§TRAG ='CLI' AND E§SCEN='01' AND E§DINV<=20120427 AND E§DFNV>=20120427

Select      00004E§TRAG    E§SCEN    E§DINV    E§DFNV
                 EQEQGELE            CLI
                                                                                       01

                                     20120427
                                                                                       20120427

Si noti come la select fornisca indicazioni sui campi di selezione e le relazioni che li interessano
nella fattispecie : 
E§TRAG ha relazione di EQual con 'CLI',
E§SCEN ha relazione di EQual con '01',
E§DINV di GreaterEqual con 20120427,
E§DFNV di LowerEqual con 20120427.

### Esempio 2, tabella : 
_7_Input
-----
Funzione               Verifica
Metodo                 Esistenza
Tipo
Codice      _TB£CAR

>Output
------
Descrizione DOMANDE COSTRUZIONE ARTICOLO
File        TABEL00F
Libreria    XGES_DAT_A
Tracciato   T.B£C
Codice  ID  TTELEM
Descr.  ID  TTDESC
Assunto ID
Where       TTSETT='B£CAR'
Select
TTANNU AS "TTANNU", TTSETT AS "TTSETT", TTELEM AS "TTELEM", TTDESC AS "TTDESC", SUBSTR(T
) AS "T$B£CM", SUBSTR(TTLIBE, 11, 30) AS "T$B£CP", SUBSTR(TTLIBE, 41, 3) AS "T$OR,1", SU
44, 2) AS "T$LU,1", SUBSTR(TTLIBE, 46, 3) AS "T$DE,1", SUBSTR(TTLIBE, 49, 3) AS "T$OR,2
LIBE, 52, 2) AS "T$LU,2", SUBSTR(TTLIBE, 54, 3) AS "T$DE,2", SUBSTR(TTLIBE, 57, 3) AS "T
TR(TTLIBE, 60, 2) AS "T$LU,3", SUBSTR(TTLIBE, 62, 3) AS "T$DE,3", SUBSTR(TTLIBE, 65, 3)
SUBSTR(TTLIBE, 68, 2) AS "T$LU,4", SUBSTR(TTLIBE, 70, 3) AS "T$DE,4", SUBSTR(TTLIBE, 73
R,5", SUBSTR(TTLIBE, 76, 2) AS "T$LU,5", SUBSTR(TTLIBE, 78, 3) AS "T$DE,5", SUBSTR(TTLIB

Si noti come la select fornisca in questo caso, indicazioni sui campi di selezione, effettuando oltretutto, dato il contesto tabellare, un parsing del campo TTLIBE
scomposto come indicato nella DataStructure relativa (in QILEGEN)
