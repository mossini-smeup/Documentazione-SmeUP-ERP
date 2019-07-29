# Definizione
La tabella è contenuta in archivi tabelle, TABEL0P, TABEL0I, ecc..., a loro volta suddivisi in settori.
Ogni settore è costituito da una definizione e da eventuali sottosettori, ognuno dei quali offre un numero libero di elementi.
Il sottosettore di una tabella è un sottogruppo della stessa (es. :  ogni sottosettore rappresenta un capitolo particolare della tabella, dedicato a particolari gestioni) e gli elementi in esso hanno la medesima struttura del settore di appartenenza.
La definizione delle tabelle si realizza attraverso il programma di gestione delle tabelle> B£DT10 (UP DEF), che consente di definire interattivamente il settore e i sottosettori presenti.

## Settore
Per ogni Settore si definiscono : 

- **Codice del Settore** (3 caratteri), ossia il codice della tabella;

- **Descrizione della tabella**;

- **Programma di Ricerca** (si indica qualora si voglia attivare una particolare ricerca sui campi legati alle tabelle. Viene attivato quando nel campo di ricerca si immette il prefisso /, mentre i caratteri a seguire possono essere utilizzati dall'utente come condizionamento);

- **Condizionamento ricerca** (si possono inserire dei parametri di condizionamento utilizzati dal programma di ricerca, se inserito);

- **Funzione per autorizzazioni** (la tabella può essere sottoposta ad autorizzazioni a livello di settore, sottosettore e singolo elemento);

- **Cartella per Help** :  definisce un nome di sottocartella interna alla cartella smehlp dove la tabella viene descritta;

- **Applicazione Specifica** (permette di indicare la sigla specifica dell'applicazione cui la tabella appartiene);

- **Archivio di Appartenenza** (identifica l'archivio tabelle a cui appartiene il settore inteso come insieme dei suoi elementi);

- **Programma di Controllo** (previsto per le tabelle particolarmente complesse caratterizzate da una gestione con un programma specifico). Tale programma deve esistere al momento della codifica del settore (es. :  per la tabella OLG di gestione degli orari di lavoro ci deve essere un programma che controlli che la somma degli intervalli di lavoro sia inferiore a 24 h);

- **Tabella a elemento Fisso** (le tabelle particolari devono avere un solo elemento, per ottenere il quale è necessario inserire * in questo campo, indicante il relativo codice identificativo **;

- **Gestione subsettore** :  permette di impostare in sede di definizione tabella se questa sarà una tabella forzatamente con sottosettori oppure forzatamente senza oppure a discrezione utente;

- **Oggetto in subsettore** (può essere libero, o il codice azienda o il codice nazione);

- **Risalita al subsettore** (definisce le modalità di risalita quando il sottosettore richiesto è assente).

![B£_TAB_03](http://localhost:3000/immagini/B£TABE_02/BX_TAB_03.png)
### Dettagli sul significato di alcuni campi
**Gestione subsettore**
Questo campo, come detto precedentemente, consente di impostare eventuali risalite sul sottosettore.
Questi i valori possibili : 

_1_ (Assume il bianco)
Qualunque settore venga indicato viene ignorato e viene usato il sottosettore blank.

_2_ (Al bianco se manca o deviazione)
Se viene indicato un sottosettore inesistente, viene usato quello blank o quello di devizione (se impostato)
Se viene indicato un sottosettore esistebnte, viene usato quello.
Se viene indicato il sottosettore blank, viene usato quello deviato (se impostato)

_3_ (Risale oggetto, se passo bianco)
Se viene indicato un sottosettore, viene usato quello (indipendentemente dall'esistenza del sottosettore e dell'aventuale impostazione dell'oggetto del sottosettore)
Se viene indicato sottosettore blank, viene usato l'oggetto impostato (campo "Oggetto in subsettore") se esiste

_4_ (Assume oggetto, se manca bianco)
Se viene indicato sottosettore blank, viene usato l'oggetto impostato (se impostato e se esiste)
Se viene indicato un sottosettore inesistente, viene usato l'oggetto impostato (se impostato e se esiste)
Se viene indicato un sottosettore esistente, viene usato quello.

_blank _(Non risale )
Non viene effettuata nessuna risalita

## Campi (Tracciato del Settore)
Per definire i campi della tabella si devono impostare per ogni campo : 

- **Nome** (per definizione il nome campo viene codificato con> T$tabx**, dove >tab** è il codice della tabella e >x è un progressivo alfanumerico dei campi della tabella. Una volta definito, il campo può essere ricercato nel dizionario dei campi con il carattere di richiesta dettaglio "!", "?");

- **Intestazione** (descrizione del campo);

- **Tipo e Parametro** (per definire se il campo può essere  uno degli oggetti Sme.up);

- **Lunghezza - Decimali** (caratteristiche del campo);

- **Obbligatorio - Non Controllare** (per indicare se il campo è obbligatorio o se non deve essere eseguito il controllo di validità quando è riferito ad un oggetto);

- **Annullare** (si usa in caso di manutenzione di una tabella successivamente al suo utilizzo, qualora si voglia eliminare  un campo dalla gestione).
In questi casi, poiché la tabella è in uso, non è possibile ridefinire il tracciato record e, anche annullando un campo, è necessario tenere fisse le posizioni di tutti gli altri.


![B£_TAB_04](http://localhost:3000/immagini/B£TABE_02/BX_TAB_04.png)
## Sottosettori
La struttura (tracciato) è quella del settore di appartenenza e sono richieste soltanto la definizione del Codice del Sottosettore (2 caratteri) e la Descrizione, che permettono di identificare il sottosettore univocamente.


![B£_TAB_05](http://localhost:3000/immagini/B£TABE_02/BX_TAB_05.png)
## Note Strutturate (vedi Documento Note Strutturate)

- **Definizione Settore** (nel contenitore >B£S** vengono inserite le note relative al settore);
- **Campo** (nel contenitore >B£C** vengono inserite le note relative al campo);
- **Elemento** (nel contenitore >B£E** vengono inserite le note relative all'elemento).


# Impostazioni (assegnazione dei settori)
## Creazione /COPY
Dopo la creazione della tabella, deve essere definito il codice RPG (mediante l'opzione 14) per permettere la mappatura del tracciato ai programmi.
L'utente deve indicare la libreria, il file e il nome della /copy della tabella da richiamare all'interno dei programmi.


![B£_TAB_06](http://localhost:3000/immagini/B£TABE_02/BX_TAB_06.png)
## Gestione dei Campi di un Settore
 **1) Ricerca nel Dizionario dei Campi**
È attivabile una ricerca alfabetica, digitando il carattere "!","?" nel nome del campo.

**2) Tipologia**
Indica la natura del campo e viene ricercata nella tabella >*cn/tt.
Ad un campo può essere associato qualsiasi oggetto :  un fornitore, un cliente, una tabella, un numero, un oggetto dell'as/400, ecc...
Si noti che il tipo di campo è  : 

- **Numerico**, quando è indicato con NR oppure se implicitamente previsto dal tipo stesso;
- **Oggetto**, quando è indicato con OJ (il tipo oggetto deve essere indicato nel campo 3 dei vincoli/limiti);
- **Elemento del DataBase**, se il campo è /C;
- **/V**, quando individua intestazioni esplicative della videata del pgm di gestione elementi tabelle. La sequenza di tali campi deve essere maggiore o uguale a 9000;
- **V1** o **V2**, quando si tratta di campi particolari, aventi valori fissi, standard o di Sme.up (es. :  partita IVA, codice fiscale, ecc...).

**3) Azioni sulla riga del Campo**


| 
| .COL Txt="C" Lun="020" A="L" |
| ---|----|
| 
| .COL Txt="Azione" LunAut="1" A="L" |
|  X | Esplode la riga in dettaglio |
|  B | Azzera tutte le posizioni a video dei campi partendo dal campo su cui è digitata sino al successivo con scelta F escluso |
|  C | Identifica, durante la funzione di posizionamento automatico, la riga di riferimento l'incolonnamento. |
|  F | Cessa l'azione delle scelte funzionali B e C |
| 

**4) Filler**
Indica quanti caratteri liberi devono separare l'ultima posizione dell'ultimo campo di cui è stata calcolata la posizione sul database dalla prima posizione del campo attuale.

**5) Valori/limiti**
È permesso indicare i valori o i limiti assumibili dai campi (per descrivere i parametri necessari ad individuare un oggetto o un membro di un file).
Le funzioni concesse sono : 

- >V            (il pgm gestione tabelle controllerà che il valore del campo, se inserito, corrisponda a uno dei quattro valori ammessi);
- >L    (il pgm gestione tabelle controllerà che il valore del campo, se inserito, sia compreso tra un limite inferiore e il corrispondente superiore);
- >OJ    (il terzo campo indica il tipo di oggetto e il quarto definisce la libreria in cui esso si deve trovare);
- >MB    (il terzo campo indica il file fisico nel quale il membro deve essere contenuto e il quarto la libreria in cui tale oggetto si deve trovare).

**6)  Prova schermo (F9)**
Dalla videata globale o da quella di dettaglio è possibile richiedere la presente funzione. Sono elaborati in ordine di sequenza tutti i campi che abbiano indicate le posizioni video per l'intestazione o per il campo o per la decodifica.
Sono esclusi i campi : 

- tipo /C
- nome T$ELEM

**7)  Costruzione formato video (F6)**
Il tasto funzionale F6 consente di attribuire valori automatici in lunghezza e posizione video ai campi che presentano le seguenti caratteristiche : 

- non sono campi di tipo "/C"
- non sono campi di tipo "/V"
- non hanno il nome T$ELEM


## Suggerimenti

- **/Copy**
Nel caso si personalizzi una tabella da un cliente, la /Copy deve essere creata con il prefisso "£TAB" nel file QRPGGEN della libreria di personalizzazione PER-XX.
- **Campi**
Mettendo !AR verrà effettuata una ricerca nel dizionario dei campi e verranno visualizzati solamente quei campi che hanno un nome che inizia per AR. Quindi nel dizionario si trovano le informazioni sul campo, a che settore appartiene, la sua tipologia, ecc..
- **Filler**
Se si cancella un campo lungo 13 per evitare problemi nei programmi dove è usata la tabella, inserisco il valore 13 nel filler del campo successivo in modo che le posizioni dei campi nel database rimangano invariate.


## Gestione degli elementi

-> Posizionamento/Scansione :  facendo un roll up/down si visualizzano gli elementi della tabella in ordine ascendente/discendente. Il posizionamento è effettuato sul primo elemento della tabella superiore/inferiore al codice elemento immesso a seconda che il roll sia up o down.

- >Controlli specifici :  previsti per tabelle particolarmente complesse che necessitano di una gestione con un programma specifico. Tale programma viene selezionato al momento della definizione del settore.

# Deviazione Tabelle
Questa modalità permette a Sme_up di leggere nativamente tabelle appartenenti ad altri gestionali come se fossero tabelle proprie (es. Sme_up può leggere la tabella Valute di PROJ come se fosse la propria tabella >VAL)
Per deviare una tabella su un'altra si deve impostare, nella definizione della tabella da deviare, "**" come applicazione specifica.


![B£_TAB_07](http://localhost:3000/immagini/B£TABE_02/BX_TAB_07.png)
L'elemento della tabella "B£I" (con nome tabella da deviare) stabilisce la modalità della deviazione (tabella su cui devia, ambiente applicativo a cui appartiene la tabella) : 


![B£_TAB_08](http://localhost:3000/immagini/B£TABE_02/BX_TAB_08.png)
# Archivi
## Archivi di definizione dei settori
Gli archivi di definizione possono stare in una libreria comune a diversi sistemi informativi poiché è normale che lo stesso settore non abbia due definizioni diverse sulla stessa macchina.
Abbiamo in particolare : 

- >TABDS = Descrizione settori

- >TABDC = Dettagli campi


## Archivi tabelle
Possono esistere più archivi contenenti le tabelle. Essi devono tutti iniziare con "TABEL" ed essere seguiti da un carattere specifico, che sarà sufficiente ad individuare completamente l'archivio interessato.
Abbiamo in particolare : 

- >TABEL P (tabelle generali di Impostazione);
- >TABEL V (tabelle valori fissi di Sme.up);
- >TABEL 0 (tabelle base).


# Autorizzazioni
Le autorizzazioni delle tabelle possono essere gestite in due modi  : 
**1.** Autorizzazione alla Gestione, con la classe RITSM

**2.** Autorizzazione all'Utilizzo, con la classe STATI

## Autorizzazione alla Gestione
Le autorizzazioni per la gestione delle tabelle necessitano di altre due specifiche che sono : 
**1.** la "funzione di autorizzazione", che viene definita nella testata;

**2.** l'utente.

La funzione di autorizzazione può assumere significati diversi in base alla protezione a livello di : 

**1) Gruppo di Settori**
Si attribuisce una unica funzione (libera) a tutti i settori che si vogliono raggruppare. L'autorizzazione viene gestita considerando il nome assegnato alla funzione stessa per identificarne il gruppo di appartenenza.
Si assume come funzione il nome stesso del settore. In mancanza di indicazioni diverse il sistema assume questo come livello.

**3) Sottosettore**
Si attribuisce come il nome del settore seguito da due asterischi. Ciò indica al programma di rilevare la funzione di autorizzazione dai subsettori. Normalmente tutti i subsettori sono protetti dalla stessa funzione.

**4) Elemento**
Si attribuisce come funzione il nome del settore seguito dal segno >-. Tale azione può essereeseguita a livello di settore e di subsettore. Il sistema assumerà come funzione il valore precedentemente immesso seguito dall'elemento> xxx-yyyyyy.

Esempio

- Tutti gli utenti possono eseguire sulle tabelle tutte le azioni, ad esclusione della cancellazione
- Le tabelle V5A, V5B e V5C sono raggruppate come VENDITE e modificabili solo dall'utente UTE003
- L'utente UTE016 può cancellare ciò che vuole
- Per la tabella >CRN solo l'utente UTE023 può eseguire l'inserimento
- Il sottosettore "CRNGA" può essere solo visualizzato
- L'elemento "FAT" della tabella >CRNVE può essere modificato solo da UTE020
- La tabella >CLS non può essere gestita da nessuno

![B£_TAB_09](http://localhost:3000/immagini/B£TABE_02/BX_TAB_09.png)>Tabella A - Modalità di definizione delle tabelle

![B£_TAB_10](http://localhost:3000/immagini/B£TABE_02/BX_TAB_10.png)>Tabella B - Autorizzazioni

## Autorizzazioni all'Utilizzo
### Condizionamento sulla Ricerca
Quando nel campo programma di condizionamento è indicato il nome di un programma specifico, si condiziona la modalità operativa presentare all'utente il formato della ricerca.
Per il programma standard, cioè quando il campo precedente è blank, le eventuali caratteristiche di autorizzazione all'utilizzo degli elementi sono indicate nella tabella stessa.

A tal fine, il valore da inserire dovrà avere la  struttura >XX-nnn, dove >XX indica la funzione della classe di protezione "STATI" e >nnn è la posizione iniziale del campo utilizzato come indicazione di stato dell'elemento della tabella.
In questo modo un elemento non autorizzato è, a tutti gli effetti, un elemento mancante (ad eccezione dei programmi dove, per le valutazioni di prestazioni, viene letto direttamente il record dal file).
Questo caso particolare nasce con lo scopo di aumentare la flessibilità di Sme.up nelle autorizzazioni (es. :  autorizzare un gruppo di utenti a particolari azioni diverse da quelle generalmente assegnate). Il meccanismo permette di definire un livello di priorità da [1..99] per discriminare l'utente generico da quello appartenente al gruppo personalizzato, in modo che, se avrà un livello di priorità maggiore allo standard, gli verranno assegnate autorizzazioni diverse.

Esempio
La tabella >GAR contiene un campo controllato dalla tabella B£WRA (tale campo inizia nella posizione 72) e, per attivare le autorizzazioni, è necessario : 

-  inserire il valore RA-072 sulla definizione della tabella;
- definire le autorizzazioni per la classe STATI e per la funzione RA, per tutti gli utenti o per uno specifico;
- indicare il riferimento alle Autorizzazioni

Per maggiori informazioni sulle Autorizzazioni, consultare le funzioni di base al relativo paragrafo.

# Azioni di massa
Per azioni di massa si intendono tutte le variazioni applicabili in blocco, senza dover modificareil singolo elemento. Questa è una tipica funzionalità di Sme.up che permette, con una sola operazione, di modificare un numero illimitato di settori, sottosettori, elementi e data base.

## Copia / Aggiunta / Aggiornamento
Le funzioni di servizio permettono di lavorare sulle definizioni e/o sul contenuto dei singoli settori per : 

- Spostare gli elementi di tabella
-- da un file ad un altro file
-- da una libreria all'altra
-- da un settore ad un altro
- Spostare le definizioni tabelle da una libreria ad un'altra
- Creare un nuovo file
- Condizionare e Parzializzare in molteplici modi le azioni richieste, quindi richiedere la fasatura completa (allineamento) di tutti i settori compresi nei limiti
- Limitare l'azione alle sole definizioni, agli elementi di tabella oppure ad entrambi.

La scelta 5 permette di creare un nuovo file tabelle con tutte le sue vie di accesso.
Alcuni esempi di azioni possibili sono : 

- Copiare la definizione completa di un settore XXX in un nuovo settore YYY;
- copiare tutti gli elementi di un settore da un sistema informativo ad un altro;
- cancellare tutti gli elementi di un settore;
- fasare due ambienti aggiungendo al secondo solo gli elementi nuovi inseriti nel primo.


![B£_TAB_11](http://localhost:3000/immagini/B£TABE_02/BX_TAB_11.png)
# Funzioni
## Tabelle di una applicazione
È possibile avere un elenco di tutte le tabelle presenti a livello di Applicazione o Applicazione/Modulo e per ogni tabella si possono ricercare gli elementi, aggiungerne di nuovi, interrogare la struttura, consultare la documentazione.

# /COPY  Tabelle SME.up

| 
| .COL Txt="Copy" A="L" |
| ---|----|
| 
| .COL Txt="Azione" LunAut="1" A="L" |
| >£LETSM| Aggancia il record di un elemenuto di una tabella SME.up. |
| >£RITSM| Esegue il controllo e/o la validità/decodifica dell'elemenuto di una tabella SME.up, e su richiesta anche la ricerca alfabetica. |
| >£RITES| Esegue il controllo e/o la validità/decodifica dell'elemenuto di una tabella SME.up, e su richiesta anche la ricerca alfabetica. |
| >£RITSS| Esegue la ricerca alfabetica e/o il controllo validità/decodifica settori/sottosettori SME.up. |
| >£RITCA| Esegue la ricerca dei campi totale o di un settore. |
| 

