# OBIETTIVO

Dato un agente il programma, mostrandone i passaggi per la sua determinazione, esegue il calcolo relativo all'indennità meritocratica da liquidare in occasione della fine del rapporto.

# PREREQUISITI

Ai fini dell'applicazione di un corretto calcolo è necessario : 
* Inserire tramite F17 le variazioni degli indici ISTAT di ogni mese rispetto al mese precedente per gli anni che possono essere interessati dal calcolo. I valori imputati permangono, ma vanno aggiornati di mese in mese con l'avanzare del tempo.
* Aver gestito il piano contributi delle provvigioni per il calcolo del FIRR e dell'ISC

# NOTE SUL CALCOLO IN SMEUP

* Se sulla tabella AGE dell'agente non è indicata la data fine rapporto viene assunta la data odierna
* L'importo delle retribuzioni liquidate viene determinato leggendo il piano provvigioni (D5COSO Contesto TAAGE tema £PC) sommando le sole retribuzioni che risultano anche contabilizzate.
* Dagli stessi dati vengono calcolati il FIRR e l'ISC maturato
* Gli importi relativi al fatturato vengono invece reperiti dall'archivio delle provvigioni
* Il fatturato iniziale viene attualizzato fino alla data di fine rapporto

# NOTE SUL CALCOLO DELL' INDENNITA' MERITOCRATICA

Il calcolo si basa su quanto disposto nel documento di "Accordo Economico Collettivo" (AEC) del   16 Febbraio 2009, per la disciplina del rapporto di agenzia e rappresentanza commerciale del settore economico.

Per estrema sintesi, il calcolo viene così strutturato : 
* La base di calcolo è definita dall'importo previsto dall'art. 1751 del codice civile, che corrisponde alla media annuale delle retribuzioni degli ultimi 5 anni o del periodo di rapporto qualora questo sia inferiore
* A tale importo va applicata una percentuale determinata a sua volta dal n° di mesi di durata del rapporto e della percentuale di incremento del fatturato dovuto all'agente
* L'incremento del fatturato viene determinato confrontando un n° di trimestri dell'inizio del rapporto e dalla fine del rapporto variabile in base alla n° di anni di durata del rapporto, ed applicando inoltre nel confronto i coefficienti di rivalutazione ISTAT per i crediti di lavoro. Se la durata del rapporto è <= a 3 anni si confrontano i volumi, altrimenti la media annuale.
* L'importo così determinato non può comunque superare l'importo dato dalla differenza fra il valore del primo punto ed la somma di FIRR ed ISC maturati.

## TABELLA DI CALCOLO % INDENNITA' MERITOCRATICA
 :  : PAR L(TAB)
Durata Rapporto |% Incremento Fatturato|% Indennità
Fino a 12 Mesi  |Da  0 a   5           |-
Fino a 12 Mesi  |Da  5 a  30           |25
Fino a 12 Mesi  |Da 30 a  60           |30
Fino a 12 Mesi  |Da 60 a 150           |40
Fino a 12 Mesi  |Oltre   150           |100
Da 12 a 24 Mesi |Fino  a  30           |30
Da 12 a 24 Mesi |Da 30 a  60           |35
Da 12 a 24 Mesi |Da 60 a 150           |40
Da 12 a 24 Mesi |Oltre   150           |100
Da 24 a 36 Mesi |Fino  a  30           |35
Da 24 a 36 Mesi |Da 30 a  60           |40
Da 24 a 36 Mesi |Da 60 a 150           |45
Da 24 a 36 Mesi |Oltre   150           |100
Da 36 a 48 Mesi |Fino  a  30           |40
Da 36 a 48 Mesi |Da 30 a  60           |45
Da 36 a 48 Mesi |Da 60 a 150           |50
Da 36 a 48 Mesi |Oltre   150           |100
Da 48 a 60 Mesi |Fino  a  30           |45
Da 48 a 60 Mesi |Da 30 a  60           |50
Da 48 a 60 Mesi |Da 60 a 150           |55
Da 48 a 60 Mesi |Oltre   150           |100
Da 60 in Avanti |Fino  a  30           |50
Da 60 in Avanti |Da 30 a  60           |55
Da 60 in Avanti |Da 60 a 150           |60
Da 60 in Avanti |Oltre   150           |100


## TABELLA DI DETERMINAZIONE N° DI TRIMESTRI DA CONFRONTARE PER LA % DI INCREMENTO DEL FATTURATO
 :  : PAR L(TAB)
Durata Rapporto |N ° Trimestri
Fino a 3 Anni   |4
Da 4 a 6 Anni   |8
Da 7 a 9 Anni   |12
Da 10 a 12 Anni |16
Oltre 12 Anni   |20













