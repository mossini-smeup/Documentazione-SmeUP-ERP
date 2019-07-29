# Documento in revisione
NOTA la versione precedente è la LOBASE_340
La documentazione del membro LOBASE_340 NON è aggiornata.

## Logica per la ricerca delle icone
La directory che contiene le icone di Loocup risiede sul filesystem e si chiama LOOCUP_ICO.
Con l'installazione di Loocup questa cartella viene creata all'interno della cartella di installazione di Loocup.

Quando viene chiesta l'icona di un oggetto Loocup utilizza il seguente meccanismo per reperire la posizone della cartella LOOCUP_ICO : 
1) se nel setup è definito l'elemento  Path con attributo uguale a ICO (XPATH=Setup/Program/BAS/Paths/Path[@Cod='ICO']) viene utilizzato l'attributo Value.
2) Se nel path indicato dall'attributo Value non c'è la cartella LOOCUP_ICO, viene ricercata nella cartella che contiene la cartella di installazione di loocup, la cartella LOOCUP_ICO/AMBIENTE.
3) Se non esiste la cartella al punto 2, si passa alla cartella di default.

Una volta identificata la posizone della cartella LOOCUP_ICO, come per la ricerca delle immagini, viene fatta una ricerca per risalita di tipo/parametro/codice all'interno della cartella LOOCUP_ICO, in modo da individuare il file fisico che contiene l'icona da usare.

![LOBASE_099](http://localhost:3000/immagini/LOBASE_07/LOBASE_099.png)

 T(**Assunti : **)
- Looc.up è installato nella directory LOOCUP, nell'esempio specifico C : /PROGRAMMI/LOOCUP.
- La directory di installazione LOOCUP contiene la directory LOOCUP_ICO che contiene le icone di default. Questa directory viene creata durante l'installazione iniziale di Loocup.



## Forzatura Path di Icone da Sme.Up
E' possibile forzare la directory base delle icone di LoocUp attraverso gli script di configurazione di Loocup (file SCP_SET).
La dichiarazione della variabile ICO, mediante il tag C.PAT, attributo Value consente di forzare la cartella delle icone.
Qui di seguito vediamo il frammento di script : 
C.SEZ Cod="Path"
C.PAT Cod="ICO" Txt="Icone" Type="TREE" Value="PERCORSO_IMG"
Il percorso può essere relativo o assoluto. Nel primo caso va concepito a partire dalla directory di installazione di LoocUp.

## Caratteri non consentiti nei path
Qualora gli identificativi dell'oggetto di cui si sta ricercando l'icona contengano caratteri non consentiti in un percorso di file system, tali caratteri andranno sostituiti con il carattere meno (-). Quindi l'icona dell'oggetto di tipo ** sarà contenuto nella cartella --. Gli oggetti di tipo OJ-*USRPRF avranno le loro icone nella cartella -USRPRF contenuta nella cartella OJ.


## Casi particolari
Se viene ricercata l'icona dell'oggetto TA, *CNTT; XX, ci si riconduce alla ricerca dell'icona dell'oggetto (XX; ; )
Se viene ricercata l'icona dell'oggetto (OG, OG, XX)  o dell'oggetto (OG,   ; XX) ci si riconduce alla ricerca dell'icona dell'oggetto (XX; ; )
Se viene ricercata l'icona dell'oggetto (OG, XX, YY) ci si riconduce alla ricerca dell'icona dell'oggetto (XX, YY, )


## Meccanismo di ricerca delle icone
Ogni oggetto, comando e azione può avere icone specifiche o generiche definite da tipo/parametro/codice di appartenenza.
Se l'icona dell'oggetto (tipo/parametro/codice) così definita non è presente sul filesystem interviene la logica di risalita, che permette la ricerca di icone più generiche come l'icona dell'istanza (tipo/parametro) o l'icona ancora più generica della classe (tipo).
Si andrà quindi a ricercare l'icona rispettando il seguente ordine : 

- LOOCUP_ICO/tipo/parametro/codice.PNG/GIF ( icona specifica)
- LOOCUP_ICO/tipo/parametro/default.PNG/GIF (icona generica)
- LOOCUP_ICO/tipo/codice.PNG/GIF (icona specifica)
- LOOCUP_ICO/tipo/default.PNG/GIF (icona generica)
- LOOCUP_ICO/default.PNG/GIF (icona generica)


**NOTA 1**  :  Il modulo grafico (SMETRAY) non visualizza l'icona di default generica. Il modulo base (LOOCUO.JAR) la utilizza. Questa è però costituita da un'immagine di 16x16 trasparente. E' stata operata questa scelta per uniformità grafica e per evitare interventi sul codice.

**NOTA 2** :  al codice viene trimmato, pertanto, eventuali spazi a sinistra vengono eliminati.


![LOBASE_098](http://localhost:3000/immagini/LOBASE_07/LOBASE_098.png)filesystem e nella scheda)

Nell'esempio in figura possiamo notare dove sono posizionate le icone nel filesystem (in alto) e la loro visualizzazione nel componente albero della scheda (in basso). In particolare notiamo l'icona specifica assegnata all'oggetto CN;CLI;001 (recuperata dal filesystem nel percorso LOOCUP_ICO\CN\CLI\001.gif, vedi etichetta (1) ) e l'icona generica dell'oggetto CN;CLI;005 (non trovata nel filesystem l'icona specifica nel percorso LOOCUP_ICO\CN\CLI\005.gif viene recuperata l'icona generica nel percorso LOOCUP_ICO\CN\CLI\default.gif, vedi etichetta (2) ).

## Schemi di ricerca delle icone
Di seguito vediamo gli schemi per identificare l'icona di un oggetto

![LOBASE_120](http://localhost:3000/immagini/LOBASE_07/LOBASE_120.png)
![LOBASE_121](http://localhost:3000/immagini/LOBASE_07/LOBASE_121.png)OG;XX;YYY - TA;*CNTT;XX)

![LOBASE_121](http://localhost:3000/immagini/LOBASE_07/LOBASE_121.png)
 :  : PAR F(03)
Nei casi particolari delle icone di programma (come per esempio l'icona di Microsoft Word, Microsoft Office ...) l'icona viene richiesta direttamente al sistema operativo e non è quindi inclusa in nessun percorso di Loocup.



## Tipi di icone -- TODO Validare
Le icone in Loocup possono rappresentare : 

- oggetti
- funzioni (verbo/azione)
- comandi


Le icone-oggetto sono catalogate nelle diverse classi note di Smeup (AR per gli articoli, CN per i contatti ...).
Le icone-funzione sono icone che rappresentano azioni generiche, che non sono associate ad un oggetto specifico. Ad esempio l'azione "taglia", l'azione "copia" generica.
Le icone-comando sono icone che rappresentano comandi, ovvero azioni riferite ad un oggetto specifico. Ad esempio l'icona "copia testo" dovrà essere diversa dall'icona "copia cliente" poichè è differente l'oggetto a cui è riferita l'azione, e differente quindi il comando. Queste icone sono catalogate con tipo **J1** e parametro **KEY**.


## Le icone nei componenti
In alcuni componenti di Loocup è possibile visualizzare icone specifiche e generiche dell'oggetto come descritto. Inoltre, in alternativa, su alcuni componenti è anche possibile visualizzare delle icone differenti da quelle standard, semplicemente definendo nell'attributo **i="..."** del nodo dell'xml a cui appartiene l'oggetto, l'azione o il comando un percorso specifico dal quale attingere l'icona.

### I bottoni
Nel componente bottone è possibile visualizzare icone oggetto in vari modi.
L'icona può dipendere esclusivamente dall'oggetto a cui fa riferimento il bottone :  in questo caso l'xml del componente bottone vengono assegnati gli attributi tipo, parametro e codice dai quali è possibile risalire all'icona visualizzata.
 :  : I.XML
          ...
          <Oggetto Nome="Bottone" Tipo="CN" Parametro="CLI" Codice="" Testo="Bottone" />
          ...
 :  : I.XML.END

In alternativa è possibile assegnare altre icone al componente assegnando all'attributo i='...' valori differenti. Le icone possono essere : 

- icone dirette (es.  :  con i="M1")
- riferite ad oggetti (es.  :  con i="CN;CLI;001")
- specificando il pathfile (es.  :  con Tipo="J1" Parametro="PATHFILE" e i="[*ICON_PATH]\Verde.gif")


 :  : I.XML
...
<Oggetto Tipo="" Parametro="" Codice="" Testo="" i="M1"  />
...
<Oggetto Tipo="" Parametro="" Codice="" Testo="" i="CN;CLI;001"  />
...
<Oggetto Tipo="J1" Parametro="PATHFILE" Codice="" Testo="" i="[*ICON_PATH]\Verde.gif"  />
...
 :  : I.XML.END

### L'albero
Nel componente albero è possibile visualizzare icone generiche, icone oggetto o icone specifiche valorizzando nel setup l'attributo **icone='...'** con i seguenti valori : 

- **icone="no"** per visualizzare le icone generiche dei nodi (la cartella per i nodi con figli, il punto per i nodi foglia senza figli)
- **icone="yes"** per visualizzare le icone oggetto che dipendono dal tipo, parametro e codice del nodo
- **icone="specific"** per visualizzare solo le icone specificate nell'attributo **i='...'** (vedi di seguito)


Nell'xml del componente albero vengono assegnati gli attributi tipo, parametro e codice dai quali è possibile risalire all'icona visualizzata.
 :  : I.XML
<Oggetto>
...
<Oggetto Tipo="CN" Parametro="CLI" Codice="001" Testo="Cliente" />
...
</Oggetto>
 :  : I.XML.END

![LOBASE_096](http://localhost:3000/immagini/LOBASE_07/LOBASE_096.png)
In alternativa è possibile assegnare altre icone al componente assegnando all'attributo i='...' valori differenti. Le icone possono essere : 

- icone dirette (es.  :  con i="M1")
- riferite ad oggetti (es.  :  con i="CN;CLI;001")
- specificando il pathfile (es.  :  con Tipo="J1" Parametro="PATHFILE" e i="[*ICON_PATH]\Verde.gif")


 :  : I.XML
<Oggetto>
...
<Oggetto Tipo="" Parametro="" Codice="" Testo="Cliente" i="M1" />
<Oggetto Tipo="" Parametro="" Codice="" Testo="Cliente" i="CN;CLI;001" />
<Oggetto Tipo="J1" Parametro="PATHFILE" Codice="" Testo="Cliente" i="[*ICON_PATH]\Verde.gif" />
...
</Oggetto>
 :  : I.XML.END

![LOBASE_097](http://localhost:3000/immagini/LOBASE_07/LOBASE_097.png)
### La matrice
Nel componente matrice è possibile visualizzare icone oggetto sull'intestazione o nella cella con i seguenti valori : 

- **iconeTesta="no"** per non visualizzare le icone oggetto nell'intestazione
- **iconeTesta="yes"** per visualizzare le icone oggetto nell'intestazione
- **icone="no"** per non visualizzare le icone oggetto nella cella
- **icone="yes"** per visualizzare le icone oggetto nella cella


Per visualizzare un'**icona sull'intestazione** della matrice è sufficiente assegnare all'attributo oggetto (ogg) della colonna l'oggetto a cui è riferita la colonna. Ad esempio per visualizzare nell'intestazione della colonna l'icona con tipo="CN" e parametro="CLI" è sufficiente scrivere nell'xml Ogg="CNCLI", come segue : 
 :  : I.XML
<Griglia>
...
<Colonna Cod="ID colonna" Txt="Descrizione colonna" Tip="" Lun="3" IO="O" Ogg="CNCLI" />
...
</Griglia>
 :  : I.XML.END

![LOBASE_100](http://localhost:3000/immagini/LOBASE_07/LOBASE_100.png)
Per visualizzare un'**icona nella cella** della matrice è sufficiente assegnare all'attributo oggetto (ogg) della colonna il codice della colonna che specifica l'icona tra parentesi quadre ed eventualmente il tipo e/o parametro comuni a tutte le celle della colonna.
Ad esempio per visualizzare nelle celle della seconda colonna le icone ;; CN;; CN;CLI; AR;; e AR;ART; è sufficiente scrivere nell'xml Ogg="[ID1]", e nelle celle della colonna con codice ID1 specificare gli oggetti per ogni singola riga come segue : 
 :  : I.XML
<Griglia>
<Colonna Cod="ID1" Txt="colonna1" Tip="" Lun="3" IO="O" Ogg="" />
<Colonna Cod="ID2" Txt="colonna2" Tip="" Lun="15" IO="O" Ogg="[ID1]" />
</Griglia>
<Righe>
...
<Riga Fld="|00001"/>
<Riga Fld="CN|00001"/>
<Riga Fld="CNCLI|00001"/>
<Riga Fld="AR|00001"/>
<Riga Fld="ARART|00001"/>
...
</Righe>
 :  : I.XML.END

![LOBASE_101](http://localhost:3000/immagini/LOBASE_07/LOBASE_101.png)eterogeneo)

Nel caso in cui le celle della colonna siano di uno stesso tipo, ad esempio CN;; CN;CLI; e CN;COL; , è sufficiente scrivere nell'xml Ogg="CN[ID1]", e nelle celle della colonna con codice ID1 specificare i parametri di ogni singola riga come segue : 
 :  : I.XML
<Griglia>
<Colonna Cod="ID1" Txt="colonna1" Tip="" Lun="3" IO="O" Ogg="" />
<Colonna Cod="ID2" Txt="colonna2" Tip="" Lun="15" IO="O" Ogg="CN[ID1]" />
</Griglia>
<Righe>
...
<Riga Fld="|00001"/>
<Riga Fld="CLI|00001"/>
<Riga Fld="COL|00001"/>
...
</Righe>
 :  : I.XML.END

![LOBASE_102](http://localhost:3000/immagini/LOBASE_07/LOBASE_102.png)omogeneo)

## Le icone dei componenti Java
I componenti Java, utilizzano delle icone che sono incluse nel file Loocup.jar.
La modifica delle icone è possibile solamente passando attraverso l'IDE Eclipse.

### Classificazione delle icone
I componenti java, utilizzano due tipi di icone :  quelle per i pulsanti/toolbar e quelle di altro tipo.

Passiamo ad analizzare componente per componente le icone utilizzate

