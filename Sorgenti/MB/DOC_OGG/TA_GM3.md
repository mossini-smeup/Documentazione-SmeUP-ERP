# GM3 - Scenari di magazzino fiscale
## OBIETTIVO
Definizione degli ambienti di valorizzazione del magazzino fiscale
## CONTENUTO DEI CAMPI
Gli scenari possono essere utilizzati solo se, nella tabella GM1, è stato specificato nel campo 'Scenari in val.fisc. il valore '1' (SI), altrimenti viene assunto l'utilizzo dello scenario '**'.
In ambiente monoscenario vengono utilizzati i parametri di valorizzazione specificati nell'elemento '**' (scenario assunto). In mancanza dell'elemento '**' si considera che tutti i campi siano bianchi, quindi vengono utilizzati i paramentri assunti.
 :  : FLD T$ELEM __Scenario__
È un campo ad immissione libera. Definisce il codice dello scenario di valorizzazione che verrà richiesto prima dell'esecuzione di tutte le funzioni legati alle valorizzazione.
 :  : FLD T$GM3A __Oggetto intestatario__
È un attributo dell'articolo. Inserendo un valore in questo campo si definisce la gestione della valorizzazione fiscale per gruppo, dove il gruppo è l'attributo (ad esempio la classe fiscale o materiale).
**ATTENZIONE** :  utilizzando questa funzione non viene gestita il tipo area di storno (tipo 'S' specificato nella tabella GMR).
 :  : FLD T$GM3F __Raggrupp. sintetico?__
È un valore SI/NO :  è significativo in presenza dell'oggetto intestatario. Se impostato, viene memorizzato nell'archivio un elemento per oggetto di riferimento.
 :  : FLD T$GM3B __Sintesi 1__
È un attributo dell'oggetto intestatario. Definisce l'attributo sulla base del quale, durante la stampa della valorizzazione fiscale, verranno prodotti i totali 1 di sintesi. Non è significativo nel caso di valorizzazione per gruppo analitica (vedi nel seguito del documento per questa definizione).
 :  : FLD T$GM3C __Sintesi 2__
Come la Sintesi 1 per la produzione dei totali 2.
 :  : FLD T$GM3D __Gestione Oggetto di riferimento__
È un elemento V2 SI/NO. Se impostato, l'oggetto intestatario della valorizzazione dello scenario è l'articolo + l'oggetto di riferimento specificato nei campi seguenti.
Se questo campo è impostato e il campo tipo "Oggetto di riferimento" è lasciato a blanks, si assume di default 'CF' (configurazione).
 :  : FLD T$GM3L __Tipo ogg. di rifer.__
È un elemento della tabella *CNTT e specifica l'oggetto di riferimento da aggiungere all'articolo. Ha importanza se è impostato a '1' il campo precedente.
 :  : FLD T$GM3M __Param. Rifer.__
È il parametro dell'oggetto di riferimento.
 :  : FLD T$GM3E __Gruppo flag__
È un elemento della tabella B£Y. Se valorizzato, ai records di giacenza fiscale generati dal ricalcolo vengono assegnati i flags di questo elemento.
 :  : FLD T$GM3O __Suff.pgm.Aggiustam.__
E' il suffisso del programma di aggiustamento GMVA52_x ed è lanciato prima della scrittura del GMSIAN0F nel programma
standard GMVA52 (solo in quello).
E' utile, per esempio, per scrivere un tipo costo calcolato in modo particolare.

 :  : FLD T$GM3G __Scenario base__
È un elemento di questa stessa tabella GM3 :  se impostato, la valorizzazione fiscale assume i valori da quest'ultimo scenario, ad eccezione di quelli dell'ultimo esercizio, che sono assunti dallo scenario da elaborare. I due scenari devono avere tutti i campi uguali (ad eccezione dello scenario base).
_9_Esempio :  se si vuole eseguire una valorizzazione mensile, mantenendo le precedenti dell'anno, si può impostare lac seguente struttura : 

 :  : PAR F(04)
 Scenario mensile | Esercizio | Scenario base
              GEN |   2000-01 |   ANNO
              FEB |   2000-02 |   ANNO
              MAR |   2000-03 |   ANNO


Lo scenario ANNO contiene gli esercizi annuali : 
... 1996, 1997, 1998, 1999
La valorizzazione dello scenario GEN assume i seguenti esercizi/scenari : 
ANNO/1996, 1997, 1998, 1999   GEN/2000-01
Quella di FEB invece : 
ANNO/1996, 1997, 1998, 1999   FEB/2000-02
Negli anni successivi, non è necessario aggiungere nuovi scenari, ma solo nuovi esercizi.
_9_Esempio :  nel 2001 lo scenario GEN conterrà gli esercizi 2000-01 e 2001-01 quando si elaborerà l'esercizio 2001-01, quello 2000-01 non
verrà considerato (gli esercizi precedenti l'ultimo sono assunti dallo scenario base ANNO, che conterrà l'esercizio, 2000).
 :  : FLD T$GM3H __Suffisso programma filtro articoli__
Normalmente un articolo assume la sua caratterizzazione fiscale dal flag di trattamento presente nella sua classe fiscale (BRF) :  non memorizzato se esso vale '2', memorizzato, ma escludibile dalla valorizzazione in fase di stampa, se esso vale '1'.
Se si vuole avere una gestione personale, sganciata dalla classe fiscale, si può scrivere un programma di filtro che, ricevendo il codice dell'articolo, ritorna il flag di trattamento fiscale.
Esso si dovrà chiamare GMVA00_x, dove x è questo suffisso.
 :  : FLD T$GM3N __Suffisso programma filtro Aree__
Normalmente un'area assume la sua caratterizzazione fiscale dal campo trattamento LIFO presente nella tabella GMR.
Se si vuole avere una gestione personale, si può scrivere un programma di filtro che, ricevendo il codice dell'area e dell'articolo, ritorna il flag di trattamento fiscale. Esso si dovrà chiamare GMVA01_X, dove X è questo suffisso.
**NOTE GENERALI**
Sono possibili questi tre tipi di valorizzazione : 
Per articolo (oggetto intestatario in bianco).
Per gruppo analitica (oggetto intestatario valorizzato e raggruppamento senza dettaglio in bianco).
Per gruppo sintetica (oggetto intestatario e raggruppamento senza dettaglio valorizzati).
I tre oggetti dell'archivio fiscale assumono, nei tre casi, il seguente significato : 
 :  : PAR F(04)
**Per articolo** : 
Articolo  :      Articolo.
Sintesi 1 :      OAV dell'articolo (in sintesi 1).
Sintesi 2 :      OAV dell'articolo (in sintesi 2).
**Per gruppo analitica** : 
Articolo  :      Articolo.
Sintesi 1 :      Gruppo :  OAV dell'articolo (in oggetto di ragguppamento).
Sintesi 2 :      OAV del gruppo (in sintesi 2).
**Per gruppo sintetica** : 
Articolo  :      Gruppo :  OAV dell'articolo (in oggetto di ragguppamento).
Sintesi 1 :      OAV del gruppo (in sintesi 1).
Sintesi 2 :      OAV del gruppo (in sintesi 2).

In ogni scenario è presente uno solo dei tre tipi di valorizzazione. Se si vuole avere una valorizzazione 'mista' per articolo e gruppo analitico o per articolo e gruppo sintetico (la coesistenza tra gruppo analitico e sintetico non è significativa) una soluzione può essere la seguente :  si costruisce un OAV utente dell'articolo che è l'articolo stesso, per gli articoli che vanno da soli, e il gruppo per quelli che vanno raggruppati. Si imposta questo OAV come codice di raggruppamento (sia analitico sia sintetico).  Per la decodifica e la ricerca, si può costruire questo oggetto come UFO, con il vincolo che non ci sia nessuna omonimia tra i codici dell'articolo e quelli del gruppo.
 :  : FLD T$GM3P __Arrotonda Importo Campo Schema__
Se impostato negli schemi (tabella INTFI) il campo importo viene arrotondato ai decimali previsti dalla valuta di conto impostata nella tabella B£2.

