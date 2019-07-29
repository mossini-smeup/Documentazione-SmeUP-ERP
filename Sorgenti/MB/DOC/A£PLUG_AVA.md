# MODELLO
La libreria SMEMOD sarà la "cassaforte degli elementi" di tabelle (file TABELM0F) Conterrà inoltre i files (PF) fissati (es.CQPIAN0F) Avere cura di NON METTERE MAI IN LISTA LIBRERIE la SMEMOD

# TEAM MODELLO
 :  : PAR F(01) L(PUN)
- MAGNI
- MARAZZI
- MILANI
- ZANCHI



| 
| .COL Txt="App" |
| ---|----|
| 
| .COL Txt="Resp." LunAut="1" |
| A5 |   Ferrari P |
| A£ | |
| B£ |   Milani L. |
| BR |   Milani L. |
| C£ |   Milani L. |
| CQ |   Goffi G. |
| C5 |   Ferrari P. |
| D0 |   Marazzi A. |
| D5 | |
| D9 |   Togni A. |
| ED | |
| GA |   Archetti G. |
| GM | |
| IG | |
| JA |   Garatti R. |
| JM | |
| LO |   Arrighini S. |
| MM | |
| MP |   Magni R . |
| MT | |
| M5 |   Magni R. |
| PH |   Avaldi A. |
| P0 | |
| P5 |   Bonzanini F. |
| SF | |
| S5 | |
| V5 |   Marazzi A. |
| WE |   Dotti D. |
| 


## CONFIGURAZIONE MODELLO (tabelle specifiche per applicazione)
I responsabili di un'applicazione devono avere a disposizione il sistema informativo "MOD" (tab. B£B) o appartenere al gruppo utenti "ADM" (vedi B£UT55).
In tale ambiente di "lavoro" si opera, come libreria dati, in SMEUP_MOD che in pratica è l'azienda "modello". In esso sono contenuti tutti i file di Sme.up.
La compilazione delle tabelle DEVE fare riferimento alla funzione B£AM70 mediante comando _7_up fun (es. per tab.P5I)


|  Nam="Funzioni per Tabella" |
| Tipo oggetto |   ST  | |
| ---|----|----|
| Parametro| (blank) | |
| Settore Tabella   | P5I |       TIPO IMPEGNO MATERIALI |
| 


Selezionare poi l'azione :  "Funzione lista elementi"

Mediante questa funzione è possibile : 
 * modificare la tabella nell'ambiente di lavoro (SMEUP_MOD)
 * verificare (anche in drill-down) la congruenza del contenuto ("F17" + opzione "DD")
 * confrontare con SMEMOD gli elementi della tabella (F17)
 * parcheggiare in SMEMOD gli elementi della tabella (opzione "13")
Se nel compilare una tabella si incrocia una tabella di cui non si è responsabili sollecitare chi di dovere per continuare nel lavoro ...

# RESPONSABILI COMPILAZIONE TABELLE (PER IL MODELLO)

| 
| .COL Txt="Tab." |
| ---|----|
| 
| .COL Txt="Compilatore" |
| 
| .COL Txt="x applicazione" |
| 
| .COL Txt="x tabella" |
| 
| .COL Txt="Nota" LunAut="1" |
| B£A   |Milani L.   |        B£     |    -     | - |
| B£AMO |Milani L.   |        B£     |    -     | - |
| B£1   |Milani L.   |        B£     |    -     | - |
| B£2   |Milani L.   |        B£     |    -     | - |
| BRE   |Marazzi A.  |        -      |    V51   | CLI, FOR |
| ...   |Milani L.   |        -      |    B£2   | Azienda |
| BRZ   |Milani L.   |        -      |    BRE   | Azienda |
| '*CNAA' |Milani L.   |        B£     |    -     | - |
| '*CNAV' |Milani L.   |        B£     |    -     | - |
| '*CNGG' |Milani L.   |        B£     |    -     | - |
| '*CNOJ' |Milani L.   |        B£     |    -     | - |
| '*CNTT' |Milani L.   |        B£     |    -     | - |
| IVA   |Marazzi A.  |        -      |    V51   | 20 |
| LIN   |Milani L.   |        -      |    B£2   | quelle ISO |
| MAF   |Milani L.   |        -      |    B£2   | 1 |
| MAG   |Milani L.   |        -      |    B£2   | 1 |
| NSC   |Milani L.   |        B£     |    -     | B£C, B£E, B£S |
| NSI   |Milani L.   |        B£     |    -     | NOT |
| NSA   |Milani L.   |        B£     |    -     | NTSTRU0F |
| TRG   |Milani L.   |        -      |    -     | - |
| VAL   |Milani L.   |        -      |    B£2   | quelle ISO |
| 


# RESPONSABILI COMPILAZIONE FILES

| 
| .COL Txt="Tab." |
| ---|----|
| 
| .COL Txt="Compilatore" |
| 
| .COL Txt="x applicazione" |
| 
| .COL Txt="Manutenzione" |
| 
| .COL Txt="Nota" LunAut="1" |
| AUTOAP0F  | Milani L.   |       B£       |  B£UT11B    |tutte le autorizzazioni previste |
| B£SLOT0F  | Milani L.   |       B£       |  B£UT11B    |mediante B£OAV3 |
| BRENTI0F  | Milani L.   |       B£       |  B£UT11B    |solo ente "azienda" |
| CQPIAN0F  | Goffi G.    |       CQ       |     "       |con cpyf da CQPIAN0F di SMEMOD |
| IGFORM0F  | Goffi G.    |       CQ       |     "       |- |
| IGLEGA0F  | Goffi G.    |       CQ       |     "       |- |
| TABELA0F  | Buffoli S.  |       B£       |  B£MNU0     |schiera |
| TABELV0F  | Milani L.   |       B£       |  B£UT11B    |da TABELM0F |
| TABEL00F  | Milani L.   |       B£       |  B£UT11B    |- |
| TABDS00F  | Milani L.   |       B£       |     -       |in SMETAB (?) |
| TABDC00F  | Milani L.   |       B£       |     -       |in SMETAB (?) |
| 

