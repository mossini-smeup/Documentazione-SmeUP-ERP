# OBIETTIVO
Permettere la manutenzione dell'archivio che definisce quali sono i giorni 'speciali', ossia i giorni che non hanno il normale orario lavorativo settimanale :  ferie, festività infrasettimanali, pre- o post-festivi. Per i giorni che definiamo 'non speciali' varranno le condizioni impostate per i giorni della settimana nella gestione risorse.
# DETTAGLIO FORMATI
# Formato guida

![B£DIR1_01](http://localhost:3000/immagini/MBDOC_OGG-P_B£DIR1/BXDIR1_01.png)
## Tipo risorsa gestita
Codice controllato sulla tabella TRG. Si veda la documentazione relativa per comprenderne il significato.

- [TRG - Tipo risorsa gestita](Sorgenti/MB/DOC_OGG/TA_TRG)

## Anno
Inserire l'anno da manutenere, se il campo è blank si passa alla lista degli anni già presenti.

# Formato immissione/variazione/annullamento

![B£DIR1_02](http://localhost:3000/immagini/MBDOC_OGG-P_B£DIR1/BXDIR1_02.png)
## Tabella mesi
Ogni riga rappresenta un mese ed ogni colonna un giorno.
Si devono indicare solo i giorni speciali, ossia che hanno un orario di lavoro diverso da quello solito settimanale, e lasciare in bianco tutti gli altri. Pertanto non occorre specificare nè sabati, nè domeniche.

I valori accettati sono : 

- 'F' = festivo con chiusura totale :  viene utilizzato per chiusura estiva, festività infrasettimanali, ecc. NB :  vale solo per i giorni in cui nessuno lavora in azienda.
- '1'-'5' = giorni con orario di lavoro particolare, come semifestivi, pre-festivi o post-festivi,che dipendono dalla risorsa. Ad es. un reparto può avere un orario ridotto, un altro avere orario normale. NB :   il codice indica quale dei 5 orari particolari della risorsa deve essere utilizzato (vedi archivio anagrafico risorse).


Sulla tabella mesi sono attive le funzioni di ricerca tabelle. La ricerca porta nella tabella OLG degli orari lavorativi per giorno per permettere di descrivere oltre agli orari il significato delle condizioni da 1 a 5. Tale codifica non è comunque indispensabile.

## Dettaglio
Immettendo un carattere qualsiasi in una riga della colonna 'Det', viene presentato un formato di dettaglio del mese scelto.
Questo formato riporta anche numero settimana dell'anno e giorno della settimana, e permette quindi una manutenzione più agevole e guidata.

# TABELLE COLLEGATE

- TRG  =    Tipo risorsa gestita
- OLG  =    Orari lavorativi

