## Costo Medio Annuale
Il Costo Medio Annuale (nel modello è codificato come >J11 o >J14) ed ha le seguenti caratteristiche : 
* Se fiscale (>J14) utilizzato anche per valorizzare la fascia LiFo dell'anno specifico, e >NON deve essere ponderato con le rimamenze dell'anno precedente.
* Se gestionale o fiscale, ma non per valorizzare una fascia LiFo (>J11), genericamente viene ponderato con le rimanenze (>Costo R11) dell'anno precedente
* Tipiche impostazioni di questo costo sono : 
** Tipo periodo >"A"= Anno tabella relativa _9_"D5O"
** Tipo risalita >"4" (Risalita Esercizio Precedente) nella tabella relativa al tipo costo (_9_TCO).
** Tipo costo di risalita >"R11" nella tabella relativa al tipo costo (_9_TCO), dove anche questo tipo costo è di tipo >"A"= Anno.
* La chiusura di magazzino deve essere >rigorosa solo a fine esercizio (31/12), in quanto essendo annuale le rimanenze (a quantità e valore) vengono consolidate con la fase di chiusura anno fiscale. Nei periodi intermedi le modifiche che possono intervenire sono : 
** Di quantità  :  se vengono modificati movimenti di magazzino, che concorrono al calcolo del costo medio, nei periodi precedentemente elaborati.
** Di valore esterno  :  se acquisti e/o lavorazioni esterne, sia totali che di Fase, nella fase di protocollazione fatture hanno subito una variazione di costo rispetto il costo previsto in fase di ordine.
** Di valore interno  :  >ovviamente nel caso vengano modificate aliquote di costo dei vari centri di costo.
* Il valore dell'articolo assumerà il costo medio dei movimenti che concorrono dall'inizio dell'anno più eventualmente le rimanenze alla fine dell'anno precedente.

## Costo Medio Year To Date
Il Costo Medio Year To Date, o costo progressivo dall'inizio dell'anno (nel modello definito come >J12 o >J15) ha le seguenti caratteristiche : 
* E' l'equivalente del precedente costo, che viene popolato, per tutti i periodi dell'esercizio, genericamente per scopi gestionali che tendono ad ottenere confronti di profittabilità (profitability) dell'articolo nei vari periodi, ottenendo scostamenti con il mese precedente così da assegnare al progressivo di quel periodo anche le modifiche dei mesi precedenti (se avvenute) consolidate dal punto di vista confronto statistico.
* Costo genericamente ponderato con le rimanenze (>Costo R11) relative all'anno precedente.
* Tipiche impostazioni di questo costo sono : 
** Tipo periodo >"P"= Anno/Mese tabella relativa _9_"D5O"
** Tipo risalita >"4" (Risalita Esercizio Precedente) nella tabella relativa al tipo costo (_9_TCO).
** Tipo costo di risalita >"R11" nella tabella relativa al tipo costo (_9_TCO), dove questo tipo costo è di tipo >"A"= Anno.
** Nel lancio di questo costo è necessario specificare il campo che determina che è un >"Costo progressivo".
* La chiusura di magazzino deve essere >rigorosa solo a fine esercizio (31/12), essendo conservato periodicamente il suo valore si discosta da quello precedente da quanto rilevato nel mese in analisi, più tutte le modifiche avvenute nei precedenti periodi che conferiscono per differenza nel periodo in analisi. Le modifiche che possono intervenire sono : 
** Di quantità  :  se vengono modificati movimenti di magazzino, che concorrono al calcolo del costo medio, nei periodi precedentemente elaborati.
** Di valore esterno  :  se acquisti e/o lavorazioni esterne, sia totali che di Fase, nella fase di protocollazione fatture hanno subito una variazione di costo rispetto il costo previsto in fase di ordine.
** Di valore interno  :  >ovviamente nel caso vengano modificate aliquote di costo dei vari centri di costo.
* Il valore dell'articolo assumerà il costo medio dei movimenti che concorrono dall'inizio dell'anno più eventualmente le rimanenze alla fine dell'anno precedente.

## Costo Medio Periodo
Il Costo di Periodo (nel modello definito come >J13 o >J16) ha le seguenti caratteristiche : 
* E' un costo periodico (genericamente mensile) dove la valorizzazione del costo, avendo come sua determinazione i soli versamenti del mese oltre alla giacenza del perioco (mese) precedente, può subire delle variazioni significative rispetto ad un costo di tipo annuale.
* Genericamente NON viene considerato un costo fiscale in quanto il periodo fiscale, dove, o applicare una fascia di costo (se voluta una gestione LiFo) o mediare con delle rimanenze, è l'anno economico.
* Costo genericamente deve essere ponderato con le rimanenze (>Costo R12) del periodo precedente (genericamente il mese)
* Tipiche impostazioni di questo costo sono : 
** Tipo periodo >"P"= Anno/Mese tabella relativa _9_"D5O"
** Tipo risalita >"5" (Risalita Periodo Precedente) nella tabella relativa al tipo costo (_9_TCO).
** Tipo costo di risalita >"R12" nella tabella relativa al tipo costo (_9_TCO), dove anche questo tipo costo è di tipo >"P"= Periodo (Mese)
** Nel lancio di questo costo >NON si deve specificare il campo che determina che è un >"Costo progressivo", come nel caso precedente in quanto è un costo puro di periodo.
* La chiusura di magazzino deve essere >rigorosa  a fine di ogni periodo  (mese) in quanto
** La determinazione della giacenza di fine periodo ed i movimenti del periodo, se errate, non verranno più riprese nella media del calcolo, in quanto consolidate nel tipo costo di rimanenza >"R12"  che, per periodo, non verrà più modificato anche se variate le quantità e/o i costi.
** La chiusura dovrà essere rigorosa >NON solo per quanto riguarda la gestione delle quantità ma anche per le valorizzazioni dei movimenti di acquisto e/o conto lavoro (con relativa fattura), in quanto se non presenti al momento del calcolo NON entreranno più nella determinazione del Costo Medio e di conseguenza del costo della rimananenza del suo periodo.
