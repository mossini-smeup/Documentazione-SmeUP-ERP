# Obiettivo
Attraverso questa /COPY vengono fissate tutta una serie di caratteristiche di una classe

# Funzioni

## DAT

Data una classe ritorna nella DS £K04DO una serie di caratteristiche della stessa : 

* £K04O_RD Ricerca x Decodifica :  indica che la classe è prevista la ricerca ordinata per descrizione
* £K04O_UL UsrLvl :  indica il livello minimo della classe USRLVL cui fa riferimento l'oggetto.
* £K04O_PE Parametro Esteso :  indica che per la classe è previsto un parametro di lunghezza superiore a 10 caratteri (es. oggetto CF)
* £K04O_KE Codice Esteso :  indica che per la classe le istanze possono presentare un codice oltre i 15 caratteri (es. J1PATHFILE)
* £K04O_CL Client :  indica che l'oggetto viene risolto dal client (es. J1PATHFILE)
* £K04O_IP Modalità Input Panel :  indica la modalità di risoluzione prevista per la classe nell'input panel (presenza o meno delle combo). Valori ammessi : 
B              Normale
C              Combo
E              Autocomplete
* £K04O_OD Presenza Decodifica :  al di là della presenza o meno della ricerca per decodifica indica se l'oggetto prevede o meno la ricerca (ci sono oggetti che non hanno una ricerca ordinata per decodifica, ma nondimeno hanno una decodifica, come ad esempio i V2)
* £K04O_RC Ricerca client :  indica che la ricerca per le istanze della classe è normalmente risolta dal client.
* £K04O_RE Ricerca emulazione :  indica che la ricerca per le istanze della classe è risolta attraverso un pgm di emulazione
* £K04O_GE Gestione :  indica se l'oggetto prevede azioni di gestione o meno (es. creazione, modifica, cancellazione, di cui oggetti come i V2 sono privi). Valori ammessi : 
               NO
1              SI
R              SI oggetto righe
* £K04O_NC No Schema T/CD* :  indica che per l'oggetto non è prevista lo schema per codice/descrizione (riguarda alcuni oggetti particolari, spesso virtuali)
* £K04O_CR Classe riferimento :  indica la classe di riferimento dell'oggetto (es. oggetto AZ, classe CNAZI)
* £K04O_OS Oggetto standard :  oggetti predefiniti (V2, V3, TAB£A e TAB£AMO)
* £K04O_NR Codice Numerico :  indica se l'oggetto è numerico oppure no (es. oggetto D8 è numerico)
* £K04O_FL Cartella a Menù :  indica se per l'oggetto c'è il richiamo alla cartella a menù (es. oggetto articolo ha cartella a menù)
* £K04O_PR Preview a Menù :  indica se per l'oggetto c'è il richiamo alla preview a menù
* £K04O_IM Immagine a Menù :  indica se per l'oggetto c'è il richiamo alla immagine a menù
* £K04O_CM Codice con minuscole :  indica se l'oggetto può avere dei caratteri minuscoli nel codice
* £K04O_II N° istanze indefinito :  indica se l'oggetto ha un numero di istanze indefinito o meno (es. L'oggetto D8 ha un numero di istanze indefinito)
* £K04O_MA Classe Master :  indica se l'oggetto ha una classe master
* £K04O_SL Scansione Istanze Lenta :  indica se l'oggetto potrebbe avere una scansione lenta degli elementi (es. l'oggetto MB)
* £K04O_PC Parametro indefinito :  indica se il parametro non è definito
* £K04O_VO Visualizzazione oggetto :  indica il tipo di visualizzazione che avrà l'oggetto e si divide in 8 casi : 
1) Descrizione (es. Oggetto CM)
2) Codice + Descrizione (es. Oggetto AR)
3) Int. Tipo + Codice (es. Oggetto OR)
4) Int. Tipo/Parametro + Codice (es. Oggetto DO)
5) Int. Tipo + Parametro + Codice (es. Oggetto FT)
6) Int. Tipo/Parametro + Codice + Descrizione (es. Oggetto TA)
7) Int. Tipo/Parametro + Descrizione (es. Oggetto CN)
0) Codice (la maggior parte degli oggetti)
* £K04O_GC Gestione client :  indica se l'oggetto prevede azioni di gestione dal client
* £K04O_NM Numerosità :  indica il tipo di numerosità che ci si aspetta dagli elementi dell'oggetto : 
1) Infinito (numeri e date)
2) Poche (es. Oggetto FL)
3) Medie (Es. Oggetto Q2)
4) Tante (es. Oggetto LI)
5) Indefinite (es. Oggetto **)
* £K04O_MS Modalità di Selezione :  Indica la modalità di selezione e visualizzazione degli elementi dell'oggetto.
* £K04O_LV Filtro Livello Massimo :  indica il livello massimo che può avere un record dell'oggetto
* £K04O_NE Num.elem.1a pagina :  indica il numero di elementi visibili nella prima pagina in caso di paginazione attiva.
Queste caratteristiche possono essere sovrascritte attraverso l'implementazione dell'exit B£K04G_U.

## COM - Funzione Combo
Data una classe ritorna nel campo £K04FO la funzione standard di risoluzione delle combo.
Il metodo identificata la corrisponde  modalità di combo prevista (per lo specifico si veda la documentazione del modulo B£EQRY)

## SCA.TPO - Scansione Classi Tipi Oggetto
Effettua una scansione di tutte le classi dei tipi oggetto e restituisce la lista.
## SCA.BAS - Scansione Classi Base
Effettua una scansione di solo le classi dei tipi oggetto base e restituisce la lista.
## SCA.MAS - Scansione Classi Master
Effettua una scansione di solo le classi dei tipi oggetto master e restituisce la lista.

# Exit
E' possibile implementare il pgm B£K04G_U, attraverso il quale poter sovrascrivere le caratteristiche previste dalla classe e/o aggiungere le caratteristiche delle classi create ad hoc, per l'installazione specifica.

