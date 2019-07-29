## Deviazione ad altro ambiente
>Se l'origine è DV (deviazione ad altro ambiente)
Parametro 1 : 
-    Pos.1/10  Gruppo fonti dell'altro ambiente. Se non impostato viene assunto il
.              gruppo fonti con  cui è stato richiamato escludendo, in modo
.              automatico, le fonti di deviazione. La deviazione può quindi
.              avvenire su 'n' ambienti in parallelo, ma non in serie. Attualmente
.              è possibile vedere fino a 5 ambienti contemporaneamente.
Parametro 2 : 
-    Pos.1/10  Libreria dei dati applicativi dell'altro ambiente (obbligatorio).
NB :  tutti gli oggetti che non siano puri dati applicativi sono assunti
dall'ambiente master : 
- gruppi fonti;
- definizioni fonti;
- tabelle (in particolare le definizioni delle fonti);
- programmi di aggiustamento.
Questa fonte è stata classificata come futura per convenzione, ma ritornerà sia
fonti presenti sia fonti future.
Inoltre è ininfluente quale valore si imposti sull'azione fonte (che è un dato
obbligatorio), e sui rimanenti parametri della fonte (classe fonte JMRP, descrizione
ridotta, ecc...). Tutti questi valori saranno assunti dalla fonte reale che viene
ritornata. Tra i parametri di ritorno di ogni elemento verrà impostata la libreria
dell'ambiente da cui deriva (per le altre fonti  viene lasciato in bianco). Questo
campo è a disposizione dello schema per essere riportato nella costruzione della
riga variabile (per interrogazioni e stampe).

In presenza di multiplant o di monoplant con codice diverso nei due ambienti non è
possibile una gestione libera dei plant di scansione, ma deve essere guidata da una
opportuna parametrizzazione.
Diamo le seguenti definizioni : 
>Ambiente originale : è quello in cui si esegue l'analisi disponibilità
>Ambiente deviato :  è quello da cui si estraggono le informazioni.
Va innanzitutto notato che il gruppo fonti presente nella fonte deviata
(parametro 1) è un campo dell'ambiente originale (come tutte le sue tabelle) e
quindi non è possibile inserirvi plant presenti soltanto nell'ambiente deviato.

Per ovviare a ciò, si deve impostare il
Parametro 3 : 
-    Pos.1/1   Strategia di corrispondenza
-    Pos.2/6   Parametro strategia
Come prima cosa, va ricordato che la scansione dell'ambiente deviato viene richiamata
per ogni plant Px del gruppo fonti originale.

Sono implementate
- >Strategia ' 'Corrispondenza esatta
Se non è stato impostato un gruppo fonti specifico, si esegue l'analisi
disponibilità nell'ambiente deviato con il solo plant Px.

Se è stato impostato un gruppo fonti (e quindi un gruppo plant) si esegue l'analisi
disponibilità nell'ambiente deviato (per il solo planr Px) solo se il plant Px è
presente in questo gruppo plant.
In questa strategia il parametro strategia è ininfluente.

- >Strategia '1'Corrispondenza parametrica
Il parametro strategia viene sottostringato in YZZZZ.
Viene eseguita l'exit M5M5D51_Y passando il parametro ZZZZ. Se questo programma è
assente, ci si riconduce alla strategia ' '.
L'exit ritorna due schiere di plant (di 50 elementi ciascuna) relativi all'ambiente
deviato ed a quello originale.
Ad esempo, supponiamo di ricevere le seguenti schiere di plant, rispettivamente
dell'ambiente deviato e di quello originale
V1 - O1
V2 - O1
V3 - O2
V4 - O3
V5 - O3
Nella scansione disponibilità dell'ambiente deviato non viene utilizzata la schiera
plant presente nel gruppo fonti eventualmente impostato come parametro 1 di questa
tabella.
Viene invece costruito un gruppo plant dinamico, nel seguente modo.
Quando viene ricevuto un plant di scansione Ox, si considerano tutti i plant Px che
hanno come corrispondenza, nella schiera, Ox.
Ad esempio : 
Se si riceve O1, si scandiscono i plant V1 e V2
Se si riceve O2, si scandisce il plant V3
Se si riceve O3, si scandiscono i plant V4 e V5
Se si riceve O4, non si scandisce nessun plant

Il plant della fonte è il plant origine Ox. Il plant Vx viene ritornato in un campo
apposito del colloquio.

Per questa strategia è stata realizzata l'exit standard M5M5D51_1, che riempie le
schiere plant nel seguente modo.
E' stato creato un nuovo settore di tabella M5D che contiene due schiere plant
(deviazione ed origine) ciascuna di 15 elementi.
Il paramentro della strategia è un elemento di questa tabella, quindi, se si ha
fino ad un massimo di 15 plant, non è necessario realizzare exit specifiche.

>Nota tecnicaRobustezza scansione
La tabella M5D risiede (come tutte le altre) nell'ambiente origine, quindi la schiera
plant origine è oggettizzata come TA/MAG, mentre la schiera plant deviata è di campi
liberi.
In generale, non è garantita la congruenza delle schiere ricevute.
Vengono eseguiti i seguenti controlli di robustezza (nel programma che elabora la
fonte di deviazione).
Sono trattate le le posizioni riempite in entrambe le schiere.
Se un plant Vx è ripetuto, viene trattata solo la prima occorrenza.
Se un plant Ox è inesistente, non verranno considerati i plant Vx legati ad esso,
in quanto Ox non verrà mai ricevuto.
Se un plant Vx è inesistente, nella scansione disponibilità non verrà ritornata
nessuna fonte.

