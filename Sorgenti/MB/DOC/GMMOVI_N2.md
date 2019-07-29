# Regole costruzione causali magazzino
Si definisce come causale "**master**" di un movimento di magazzino quella riportata sul movimento stesso (GMMOVI). Le altre causali (secondarie) eventualmente collegate ad essa sono in GMMOAR.

Dove si fanno consultazioni a livello di GMMOVI è dalla causale master che si reperiscono le informazioni : 
 * Area del movimento, e quindi
 ** Gruppo area
 ** Area interna / esterna
 ** Area di proprietà / di terzi
 * Comportamento fiscale

Le causali secondarie dovranno avere o la stessa area o un'area con caratteristiche uguali e lo stesso comportamento fiscale (anche se quest'ultimo fatto non è rilevante :  serve solo per chiarezza).

## Tipo giacenza
Il tipo giacenza deve essere diverso per tutte le causali (master e secondarie) :  se l'area è la stessa non ha senso che il GMQUAN si aggiornato 2 volte dallo stesso movimento. Se invece le causali hanno diverse aree, nella scansione movimenti per tipo giacenza senza aver impostato l'area si correrebbe il rischio di avere due volte lo stesso movimento

## Lettura movimenti con ricostruzione giacenza
(quindi anche determinazione giacenza alla data)

|  Nam="Condizioni giacenza" R="1" |
| 
| .COL Txt="N." LunAut="1" |
| ---|----|
| 
| .COL Txt="Gruppo Aree" LunAut="1" |
| 
| .COL Txt="Area" LunAut="1" |
| 
| .COL Txt="Tipo Giacenza" LunAut="1" |
| 
| .COL Txt="Proprietà :  Terzi / Azienda" LunAut="1" |
| 
| .COL Txt="Localizzazione :  Interna / Esterna" LunAut="1" |
| 
| .COL Txt="Key 1/4" LunAut="1" |
| 
| .COL Txt="Note .............." LunAut="1" |
| 
| .COL Txt="Altre note ......" LunAut="1" |
|  1) | blank / non_blank | blank       | blank       | blank  / T / A | blank / I / E | NS                | Vedi Nota (1)| Vedi Nota (A) |
|  2) | NS                     | non_blank | blank       | NS                | NS              | NS                | Vedi Nota (1)| Vedi Nota (A) |
|  3) | blank / non_blank | blank       | non_blank | blank  / T / A | blank / I / E | blank / V / * | Vedi Nota (1)| Vedi Nota (B) |
|  4) | NS                     | non_blank | non_blank | NS               | NS              | blank / V / * | Vedi Nota (2)| Vedi Nota (B) |
| 

**Legenda**
__NS__; non significativo (e quindi non trattato il valore ricevuto :  non si fanno controlli di congruità)
__blank  / T / A__; blank = tutte le aree; T = di Terzi; A = dell'Azienda
__blank / I / E__;  blank = tutte le aree; I = Interne; E = Esterne
__blank / V / *__; ogni Key del tipo giacenza :  blank = blank; V = valore specifico; * = valore qualsiasi

**Note**
__Nota (1)__; legge GMMOVI, se Tipo Giacenza non_blank filtro su Key 1/4, se Area o Tipo Giacenza o Gruppo Aree o Proprietà o Localizzazione diversi da blank aggancia GMMOAR (se caso 3, quello del tipo giacenza altrimenti quello con progressivo 1)
__Nota (2)__; legge GMMOAR, aggancia GMMOVI e filtro Key 1/4
__Nota (A)__; per quanto riguarda GMQUAN, esclude i Tipi Giacenza secondari (legge la tabella)
__Nota (B)__; essendo il tipo giacneza fisso lo tratta indipendentemente dal flag secondario

## Selezione scansione
Le routines di lettura giacenza alla data e di scansione movimenti, per decidere quali movimenti trattare, analizzazno il contenuto di £GMDDS e decidono, in base ai campi impostati, in quale caso si trovano tra quelli esposti in tabella e si comportano di conseguenza :  decidono il modo di scansione.

Nella tabella Tipo giacenaa si imposta il campo "Tipo giacenza secondaria" (Valore SI/NO), se impostato i record di GMQUAN appartenenti a tipi giacenze così contrassegnati NON contribuiscono alla giacenza totale a meno che sia stato selezionato unicamente questo tipo giacenza (idem per GMMOAR).

Questa selezione viene fatta in : 
 * calcolo giacenza totale alla data
 * analisi disponibilità
 * interrogazione / stampa GMQUAN

Le causali secondarie dovranno movimentare tipi giacenza secondari (quelle MASTER -> NO), per cui in GMMOAR il progressivo 1 dovrà avere il flag T.Giac. secondaria = blank, i successivi progressivi dovranno avere il flag = '1' (un T.Gicenza non può essere per certe causali principale e per altre secondario).
