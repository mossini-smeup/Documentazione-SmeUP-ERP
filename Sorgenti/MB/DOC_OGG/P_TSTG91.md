# OBIETTIVI

Questa /COPY permette di andare ad ottimizzare e semplificare l'utilizzo di variabili all'interno di stringhe
di elaborazione.

Per la definizione del concetto di variabile  si rimanda alla documentazione dell'oggetto V3_EVA : 
- [Variabili (Lato SERVER)](Sorgenti/MB/DOC_OGG/V3_EVA)

# IL CONTESTO

E' un concetto importante da chiarire :  le variabili saranno sempre intestate ad un contesto (se non indicato
esplicitamente verrà attribuito tramite una numerazione automatica). Tramite questa struttura sarà possibile gestire
contemporanamente più insiemi di variabili interdipendenti (es. gestione contemporanea di differenti tipologie
di script).

## Attribuzione del contesto

Può essere : 
 * Indicato esplicitamente in £G91CO.
 * Associato ad un oggetto (tipo-parametro-codice in £G91TP-£G91PA-£G91CO). Attenzione a pulire sempre £G91CO in questo caso (potrebbe essere valorizzato da chiamate precedenti e causare un'attribuzione errata!).
 * Attribuito automaticamente.

# FUNZIONI/METODI

## CON - Contesti

### . NUT - Elimina contesti non utilizzati da 1 ora
 Permette di recuperare spazio eliminando i contesti e le variabili non utilizzate da più di un'ora.

### . SCO.INI - Scansione con posizionamento iniziale
 Inizializza la scansione dei contesti, con il ritorno del primo.

### . SCO.NXT - Scansione prossima
 Fatta in successione al metodo SCA.INI permette di proseguire la scansione dei contesti.

### . SCA.INI - Scansione con posizionamento iniziale
 Inizializza la scansione degli attributi attivi in un certo contesto, con il ritorno del primo di essi.

### . SCA.NXT - Scansione prossima
 Fatta in successione al metodo SCA.INI permette di proseguire la scansione degli attributi attive.

### . RIC     - Ricerca contesto
 Dato un attributo o una serie di attributi ritorna il contesto che soddisfa la ricerca. Se dovessero essere
 trovati più contesti la ricerca fallisce.

## VAR - Variabili

### .     - Decodifica/Ricerca
 Permette di decodificare e ricercare i nomi delle variabili disponibili

### . AGG - Aggiungi
 Valorizzando i relativi campi è possibile aggiungere, a livello di contesto, la definizione di una nuova
 variabile. I campi di valorizzzare in questo caso sono : 
 - £G91NV :  Nome variabile
 - £G91OV :  Tipo Oggetto di riferimento della variabile
 - £G91TV :  Valore della variabile
 - £G91DV :  Descrizione delle variabile
 - £G91AV :  Alias della variabile

### . G00 - Aggiunta variabile lunga (G00)
 Tramite questo metodo è possibile aggiungere variabili lunghe fino a 30000 caratteri.
 Essendo più lunghe del campo previsto per le altre variabili (£G91TV) è possibile impostarle inserendo il valore nel campo £G91SI.
 Non è necessario definirla come _&_G00.nomevariabile, pertanto la variabile pippo, non  cominciando per _&_G00, viene comunque automaticamente tradotta in _&_G00.pippo.
Non sono variabili di contesto, pertanto se si necessita di eventuali aggregazioni logiche si consiglia attribuire l'aggregazione ai nomi delle variabili, per esempio _&_G00.contesto.variabile1, _&_G00.contesto.variabile2 ecc..
Non è possibile utilizzarla negli altri metodi della funzione VAR, pertanto è possibile utilizzarla solo come traduzioni di stringa con output nel campo £G91SO, ma per esempio non è disponibile la lettura del suo contenuto tramite la funzione.metodo VAR.LET.
Le variabili lunghe sono utilizzabili anche nelle funzioni CND, con il limite di 256 caratteri, il resto del contenuto della variabile lunga nella memoria della gestione delle condizioni ciene ignorato.
La gestione di queste variabili avviene tramite la G00, pertanto i relativi dati sono memorizzati temporaneamente nel B£MEDE0F, cancellati poi alla chiusura del lavoro.

### . MUL - Aggiunta multipla
 Tramite questo metodo è possibile aggiungere più variabili con un unica chiamata. Per ottenere ciò la
 definizione delle variabili dovrà essere passata tramite la variabile £G91SI, con la seguente sintassi : 
 (Nome variabile(Tipo Oggetto;Valore : Descrizione|Alias))

### . UIB - Aggiunta in Formato UIB
 Tramite questo metodo è possibile valorizzare le variabili standard derivabili dai campi della DS £UIBDS
 (_&_OG.T1/P1/K1, _&_OG.FU ecc.). In questo caso il valore di tali variabili verrà passato tramite la valorizzazione
 della £UIBDS stessa.

Sulla base di esse sarò inoltre possibile sfruttare le variabili _&_O.
NB :  le variabili _&_Ox. si riferiscono sempre solo all'oggetto 1 ed anno la particolarità di ritornare "Assente" se il valore dell'oav è nullo. Tramite le variabili _&_Oxn è invece possibile sfruttare tutti i 6 codici disponibili. Per quest'ultime inoltre non è prevista la sopracitata risalita sul valore nullo.

### . RIM - Rimuovi
 Elimina la definizione di una variabile a livello di contesto.

### . LET - Leggi
 Dato il nome leggere il contenuto della variabile passata.

### . CHK - Verifica
 Permette di controllare l'esistenza di un nome di variabile (campo £G91NV)

### . SCP - Aggiunta da Script
 Permette di aggiungere la definizione di una variabile in funzione di quanto riportato
 nel campo £G91SI, secondo la seguente struttura
 - Tip    :  Tipo Oggetto di riferimento della variabile
 - Des    :  Descrizione delle variabile
 - Ali    :  Alias della variabile
 - Name   :  Nome variabile
 - Val    :  Valore della variabile
 - Pgm    :  Funzione di calcolo della variabile da passare in questo formato F(Componente;Servizio;Funzione) P(Parametri)

### . SCA.INI - Scansione con posizionamento iniziale
 Inizializza la scansione delle variabili attive in un certo contesto, con il ritorno della prima di esse (Non sono ritornate quelle del contesto di default).
Per avere l'elenco presente nel contesto di default bisogna eseguire la scansione sul contesto *DFT.

### . SCA.NXT - Scansione prossima
 Fatta in successione al metodo SCA.INI permette di proseguire la scansione delle variabili attive.

### . RST - Reset e Crea Contesto
 Annulla il contesto ricevuto e contemporaneamente ne crea uno nuovo

### . CRE - Crea Contesto
 Crea un nuovo contesto

### . ELI - Elimina un Contesto
 Elimina un dato contesto

### . VIS - Visualizza Contesto
 Visualizza tutte le variabili di un dato contesto

## Funzione ERR - Errori

Per errori si intendono tutte quelle incongruenze che possono determinarsi nella trascodifica delle variabili
(es. non viene trovato il contenuto della variabile)

### . INI - Pulisci
 Pulisce tutti gli errori caricati in memoria

### . SCA.INI - Scansione con posizionamento iniziale
 Inizializza la scansione degli errori attivi, con il ritorno del primo di essi.

### . SCA.NXT - Scansione prossima
 Fatta in successione al metodo SCA.INI permette di proseguire la scansione degli errori.

## . RST - Reset e Crea Contesto
 Annulla tutti contesto creati fino a quel momento e contemporaneamente ne crea uno nuovo

## Funzione STR - Stringa

### . TRA - Traduci
 Data una stringa con contenente delle variabili, ne attua la sostituzione all'interno della
 stringa con i relativi valori.
 In presenza di variabili non traducibili ritorna l'indicatore di errore acceso.

### . VER - Verifica
 Il funzionamento è identico a quello del metodo TRA con la differenza che non viene tornata la
 stringa di risultato (in sostanza verifico solo che la stringa sia correttamente traducibile)

## Funzione CND - Condizione

Tramite questa funzione è possibile verificare ed applicare formule di condizione contenenti delle variabili.
Sono previsti sia i normali operatori di confronto che alcuni operatori logici (riportati di seguito).
E' inoltre possibile tramite l'utilizzo delle () impostare delle condizioni complesse.
Il risultato della condizione viene ritornato nella variabile £G91RS.

 Operatori previsti : 
- Confronto
-- Uguale           :  =
-- Minore           :  <
-- Maggiore         :  >
-- Minore Uguale    :  <=
-- Maggiore Uguale  :  >=
-- Diverso          :  <>
-- Scansione        :  >>
- Logici
-- AND
-- OR
-- IMP
-- NOT
-- XOR
- Assegnazione
-- ==
### Condizione di *BLANKS
La condizione di *BLANKS è indicata con lo spazio vuoto
Per esempio se voglio indicare _&_CO.MYVAR<>*BLANKS si deve scrivere
 :  : PAR F(04)
 £G91FU = CND
 £G91ME = TRA
 £G91SI = _&_CO.MYVAR<>

oppure utilizzare il doppio apice, l'apice singolo non è supportato
 :  : PAR F(04)
 £G91FU = CND
 £G91ME = TRA
 £G91SI = "_&_CO.MYVAR"<>""

Stringa contenente spazi, utilizzare il delimitatore di stringa " (Doppio apice)
 :  : PAR F(04)
 £G91FU = CND
 £G91ME = TRA
 £G91SI = "IO SONO"<>

 :  : PAR F(04)
 £G91FU = CND
 £G91ME = TRA
 £G91SI = "IO SONO"<>""

 :  : PAR F(04)
 £G91FU = CND
 £G91ME = TRA
 £G91SI = "IO SONO"<>"TU SEI"

Il delimitatore serve solo a indicare l'inizio e la fine della stringa è quindi facoltativo
quando la stringa non contiene spazi.
 :  : PAR F(04)
 £G91FU = CND
 £G91ME = TRA
 £G91SI = "IO SONO"<>""

se la condizione è verificata ottengo : 
 :  : PAR F(04)
 £G91SO = 1

altrimenti : 
 :  : PAR F(04)
 £G91SO = 0


### . TRA - Traduci
 Verifica la condizione e ritorna la stringa della condizione con le variabili tradotte.

### . VER - Verifica
 Verifica la correzione sintattica della condizone

### . WRI - Scrivi
 Viene eseguito un set'n play interattivo che aiuta a scrivere la condizione

## Il formato delle Date

"_&_D8." + "Formato Data Speciale senza &" ( + ".Y" = Anno/Mese/Giorno  )
                                             ".y" = AnnoMeseGiorno
                                             ".d" = GiornoMeseAnno
                                             "  " = Giorno/Mese/Anno

## Il formato delle variabili _&_KI

"_&_KI." + "Oggetto" + "." + "Istanza" + "%" + "Attributo" + "%" + "Attributo"

La variabile di istanza non necessita una sua dichiarazione ma è implicitamente dichiarata.
L'oggetto e l'istanza dello stesso sono obbligatori mentre la catena di attributi è facoltativa

##  Il formato delle variabili _&_KU

"_&_KU." + "Codice Upp" + "%" + "Campo Configurazione"

La variabile di istanza non necessita una sua dichiarazione ma è implicitamente dichiarata.

