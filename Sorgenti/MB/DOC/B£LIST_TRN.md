 :  : PRO Cod(LIS) Txt(Creazione Liste) STAT(00) RESP(ARRSTE)
 :  : ATT Cod(001) Txt(Operazioni sulle liste)
01. Apro la gestione liste collaboratori
02. Creo una lista vuota che chiamo "Esercizio 001 (Statica)"
03. Creo una lista dinamica  di tutti i collaboratori con sede Erbusco che chiamo "Esercizio 002 (Dinamica)"
04. Apro una ricerca sui collaboratori  (esempio LI;CNCOL;*), mediante colonne aggiuntive filtro tutti quelli del delivery
05. Mediante tasto destro sulla colonna genero il carrello
06. Ottengo la lista di Work personale
07. Sommo tale lista nella prima creata vuota
08. Ora unisco le due liste "Esercizio 001 e Esercizio 002"
09. Preparo una lista di tutti coloro che si chiamano "Luca" che chiamo "Esercizio 003 (Statica)"
10. Mediante operazioni tolgo dalla lista "Esercizio 001"   "Esercizio 003"
11. Entro in gestione della lista "Esercizio 001" e mediante Drag & Drop tolgo Almeno una persona

 :  : ATT Cod(ELE) Txt(Creazione Lista da Elenco di Codici)

01. Premo F04
02. Indico Tipo Oggetto LI, Parametro Oggetto - la classe oggetto per cui voglio creare una lista
03. Nel Codice  Oggetto invece indicare un codice un volta che vi ho posto il fuoco, premo tasto destro, gestione, aggiunta
04. Si aprirà la schermata per la selezione del tipo di lista, fra le varie voci selezionare "G - Da Carrello Generico"
05. Si aprirà la schermata per l'indicazione del nome da attribuire alla lista
06. Una volta confermato il nome, la lista verrà creata e verrà automaticamente aperta la schermata di gestione della stessa
07. Da questa schermata richiamando la sezione di destra ed indicando un codice di una lista esistente (*) avrò la possibilità di selezionare gli elementi della lista e selezionando fra di essa gli elementi che voglio riportare nella nuova lista e trascinandoli nella sezione di sinistra potrò alimentare la lista in creazione
08. Per cancellare o inserire un nuovo elemento è possibile dalla sezione di sinistra anche premere il tasto destro su un qualsiasi elemento della lista per cancellarlo o aggiungerlo.

 :  : ATT Cod(SQL) Txt(Creazione Lista da Where SQL)

01. Premo F04
02. Indico Tipo Oggetto LI, Parametro Oggetto - la classe oggetto per cui voglio creare una lista (è necessario che all'oggetto corrisponda un file di database, es. AR per gli articoli)
03. Nel Codice  Oggetto invece indicare un codice un volta che vi ho posto il fuoco, premo tasto destro, gestione, aggiunta
04. Si aprirà la schermata per la selezione del tipo di lista, fra le varie voci selezionare "001.WHR - Da Where SQL"
05. Si aprirà la schermata per l'indicazione del nome da attribuire alla lista
06. Una volta confermato il nome, la lista verrà creata e verrà automaticamente aperta la schermata di gestione della stessa
07. Da questa schermata avrò la possibilità di indicare una stringa SQL compatibile con il file corrispondente all'oggetto. (Es. se l'oggetto è l'articolo smeup che corrisponde al file BRARTI0F, posso mettere come contenuto E§TIAR='ART'

 :  : ATT Cod(ATT) Txt(Creazione Lista da Attributi)

01. Premo F04
02. Indico Tipo Oggetto LI, Parametro Oggetto - la classe oggetto per cui voglio creare una lista
03. Nel Codice  Oggetto invece indicare un codice un volta che vi ho posto il fuoco, premo tasto destro, gestione, aggiunta
04. Si aprirà la schermata per la selezione del tipo di lista, fra le varie voci selezionare "1 - Filtri su Attributi"
05. Si aprirà la schermata per l'indicazione del nome da attribuire alla lista
06. Una volta confermato il nome, la lista verrà creata e verrà automaticamente aperta la schermata di gestione della stessa
07. Da questa schermata avrò la possibilità di indicare sulla sinistra gli attributi che voglio determinare per costruire la lista e sulla destra i limiti dei valori dell'attributo indicato, attraverso i quali verranno determinati i codici appartenenti alla lista

 :  : ATT Cod(DIN) Txt(Lista Dinamiche)

La lista "*" identifica la lista di tutte le istanze di una certa classe oggetto. Ma se dopo l' "*" vengono indicate altre informazioni è possibile creare delle liste "dinamiche".

Lista di un codice

01. Premo F04
02. Indico Tipo Oggetto LI, Nel parametro CNCLI e nel codice *CodiceCliente
03. All'invio mi si aprirà la scheda di una lista che sarà composta solo da quel codice.

Lista di un elenco di codici

01. Premo F04
02. Indico Tipo Oggetto LI, Nel parametro CNCLI e nel codice *CodiceCliente1;CodiceCliente2
03. All'invio mi si aprirà la scheda di una lista che sarà composta solo dai due codici indicati.

Lista di codici aventi una parte di codice comune.

01. Premo F04
02. Indico Tipo Oggetto LI, Nel parametro TAB£AMO e nel codice *C5%
03. All'invio mi si aprirà la scheda di una lista che sarà composta dai moduli della lista che iniziano per C5.

Il carattere % può essere posto sia prima che dopo il codice o prima e dopo.



