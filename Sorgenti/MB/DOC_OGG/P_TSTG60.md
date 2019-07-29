# OBIETTIVO
Gestire la possibilità di selezionare elenchi di oggetti con diversi criteri di ricerca.  Restituire fino a 999 valori di un oggetto di un dato tipo parzializzando e ordinando sui valori della sua struttura

# PREREQUISITI
- Corretta compilazione della tabella B§O che in base al tipo/parametro oggetto fornisce dataBase, campi chiave, eventuale descrizione e defaults

- Creazione OAV per oggetto CS

D/COPY QILEGEN,£G60E
D/COPY QILEGEN,£G60I

C/COPY QILEGEN,£G60

# PARAMETRI

## PARAMETRI DI INPUT

- Programma utente :  _campo £G60PG_

- Funzione :  _campo £G60FU_  Indica quale operazione si vuole eseguire.
 :  : PAR
DAT       Dati dell'oggetto (TAB§O)
RIC       Ricerca elemento
RND       Caricamento casuale
CAR       Caricamento
CARVIS    Caricamento con visualizzazione Sql

_La funzione RND permette la creazione di una lista casuale di oggetti scelti tra il totale degli oggetti trovati. Quando
il metodo è *Blanks allora il numero di oggetti nella lista corrisponde al numero prescelto dall'utente, mentre quando si
utilizza il metodo MAX anche il numero di oggetti viene reperito in maniera casuale.


- Metodo :  _campo £G60ME_

Funzione RND : 
 * *Blanks   Caricamento casuale normale
 * MAX        Caricamento casuale fino ad un numero massimo

Funzione CAR e CARVIS : 
 *  *Blanks       Per codice / compreso / avanti
 *   _SG_RP     Per codice / compreso / indietro
 *   _SG_RD    Per codice / escluso  / avanti
 *   _SL_RP     Per codice / escluso  / indietro
 * DE_SL_RD  Per descr. / compresa / avanti
 * DE_SG_RP  Per descr. / compresa / indietro
 * DE_SG_RD  Per descr. / esclusa  / avanti
 * DE_SL_RP   Per descr. / esclusa  / indietro
 * DC_SL_RD  Desc.R.Cod / compresa / avanti
 * DC_SG_RP  Desc.R.Cod / compresa / indietro
 * DC_SG_RD  Desc.R.Cod / esclusa  / avanti
 * DC_SL_RP  Desc.R.Cod / esclusa  / indietro

- Tipo :  Tipo oggetto da selezionare _campo £G60T1_

- Parametro :  Par. oggetto da selezionare _campo £G60P1_

- Codice Iniziale :   Limite iniziale per key oggetto (.. da B§O) _campo £G60K1_

- Codice Finale :  Limite finale   per key oggetto (.. da B§O) _campo £G60K4_

- Numero Elementi :  Numero Oggetti da selezionare _campo £G60QT_

- Filtro :  _campo £60F_

La /copy £G60 riceve una schiera £60F che costituisce il filtro.
Gli elementi della schiera sono strutturati secondo la DS £G60DS : 
 * DS di appoggio sottodefinizione schiere di filtri
D £G60DS          DS
 * Tipo Filtro
D  £G60TF                 1      2
 * Codice Filtro
D  £G60CF                 3     17
 * Tipo Accesso
D  £G60TA                18     19
 * Valore di filtro
D  £G60VF                20     34

il campo £G60TF può contenere i valori 'CS', in questo caso la variabile £G60CF è il campo di un file, oppure 'OA' in questo caso la variabile £G60CF è un OAV dell'oggetto.

_Esempio : 
la sintassi dovrebbe essere la seguente : 
TpCampo          OpValore
CSA§ARTI         = AA

La £G60 accetta come operatore l'oggetto V2/OPC03 e non occorre inserire le virgolette in quanto lo fa automaticamente se il campo è alfanumerico

- Ordinamento :  Campi ordinamento _campo £60O_

## PARAMETRI DI OUTPUT

- Codici e descrizioni :  _campi £60C/£60D_
- Numero Elementi :  _campo £G60QT_
- File Messaggi :  _campo £G60FI_
- Indicatore errore :  _campo £G6035_
- Indicatore ricerca :  _campo £G6036_
- Messaggio di ritorno :  _campo £G60MS_

# ESEMPI DI CHIAMATA

EVAL      £G60PG= Programma_utente
EVAL      £G60FU='Funzione'
EVAL      £G60ME='Metodo'
EVAL      £G60T1= Tipo_oggetto_da_selezionare
EVAL      £G60P1= Par_oggetto_da_selezionare
EVAL      £G60K1= Limite_iniziale_key_oggetto
EVAL      £G60K4= Limite_finale_key_oggetto
EVAL      £G60QT= Numero_Oggetti_da_selezionare
EVAL      £60F  = Condizioni_selezione
EVAL      £60O  = Campi_ordinamento

EXSR      £G60

EVAL      Messaggio_ritorno         = £G60MS
EVAL      File_messaggi             = £G60FI
EVAL      Errore                    = £G6035
EVAL      Ricerca                   = £G6036
EVAL      Codice_Oggetti_Selezionati= £60C
EVAL      Descr_Oggetti_Selezionati = £60D



# NOTE
_1_
 * Se viene impostato un ordinamento(£60O) prevale sempre
sull'ordinamento di metodo(£G60ME)
 * Se viene impostato un ordinamento(£60O) £G60K1 viene utilizzato per
puntare la paginazione, deve essere quindi un codice esistene o *BLANKS
 * Per parzializzare un valore = *blanks utilizzare '-'

