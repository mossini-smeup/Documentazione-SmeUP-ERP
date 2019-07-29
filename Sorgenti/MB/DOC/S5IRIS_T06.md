
# Introduzione
Il processo di schedulazione ha come vincolo la l'obbligo di utlizzare in modo corretto la risorsa primaria (centro di lavoro oppure macchina), vale a dire di non occuparla con più di un impegno contemporaneamente (oppure di farlo in modo controlalto, in caso di batch o di multipostazioni).
Nella realtà, oltre alle risorse di questo tipo, che sono quelle su cui si esegue l'operazione, vi possono essere altre risorse da utilizzare, ad esempio attrezzi, persone, buffer, che denominiamo risorse secondarie "RS", e i cui impegni vengon o memorizzati nell'archivio
 :  : DEC T(OJ) P(*FILE) K(S5IRSE0F)
Il modo in cui viene controllata ogni risorsa secondaria è definito in tabella
 :  : DEC T(ST) K(BRK)
La suddivisione principale tra i tipi risorse secondarie è : 
* Risorse di segnalazione "RSS" :  il loro sovrautilizzo è segnalato ma permesso
* Risorse di vincolo "RSV" :  il loro sovrautilizzo non è permesso :  la schedulazione opera in modo tale da non violare il loro calendario di disponibilità (sia come orari di apertura, sia come numero di risorse presenti).
Mentre non vi è limite al numero di risorse di segnalazione, per ogni impegno risorse vi può essere solo un impegno secondario riferito ad una risorsa di vincolo. Se ve ne fosse più d'uno, i successivi, (secondo il logico S5IRSE0L) verrebbero trascurati (non declassati a risorse di segnalazione).

## Caratteristiche di una RS
Una RS è caratterizzata, in generale, dai seguenti campi della tabella BRK
 :  : DEC T(VO) P(T.BRK) K(T$BRKH)
 :  : DEC T(VO) P(T.BRK) K(T$BRKJ)
 :  : DEC T(VO) P(T.BRK) K(T$BRKL)
 :  : DEC T(VO) P(T.BRK) K(T$BRKK)
elemento del settore
 :  : DEC T(ST) K(BSC)

# Risorse secondarie di segnalazione
In questo caso, per ogni RSS,  viene segnalato se, almeno per un istante, si supera li vincolo di risorse disponibili.
Questa segnalazione può essere visualizzata anche sul singolo ordine o sul singolo impegno.
Va tenuto presente che tutti gli impegni che contribuiscono alla violazione delle RSS sono segnalati. Se, ad esempio, il numero di RSS è 4, e vi sono cinque impegni che la utlizzano, quattro dei quali ne occupano 1, mentre il rimanente ne occupa 2, per un totale di 6, non viene fatta nessuna considerazione particolare su quest'ultimo impegno.

# Risorse secondarie di vincolo
In queste risorse viene utilizzato anche il campo
 :  : DEC T(VO) P(T.BRK) K(T$BRKM)
Tecnicamente, se attivato nello script il conrtrollo RSV, e se ve ne sono di effettivamente presenti, viene eseguito, in varie modalità, il monitor RSV
 :  : DEC T(OJ) P(*PGM) K(S5SMES_76)
che, in base a quanto impostato nel campo di tabella precedentemente precedentemente esposto, decide quale versione lanciare del programma di effettivo controllo RSV, passandogli tutti i campi ricevuti (funzione, medodo, puntatori)
 :  : DEC T(OJ) P(*PGM) K(S5SMES_77)

La strategia, in questo caso, è la seguente.
Quando viene selezionato un impegno potenzialmente schedulabile '1' (con istante di inizio minore di quello attualmente scelto, o con istante uguale ma con CROR minore '2') viene determinato l'istante di disponibilità RSV maggiore  o uguale a '1' :  se per questo istante vale ancora la condizione '2', l'impegno sostituisce il precedente come impegno da schedulare. Quando sono stati analizzati tutti gli impegni pronti, si schedula l'impegno attualmente scelto.
Particolare cura va prestata nella stesura di programmi di "tiro" :  gli impegni tirati devono avere la stessa RSV del tirante. E' invece a cura dello standard di avanzare, dopo aver schedulato un impegno tirato, l'inizio della disponibilità della RSV.
Ancor maggior cura va prestata nella stesura di programmi di "spinta", non potendo implementare, in questo caso, a standard nessuna facilitazione, data l'eterogeneità delle situazioni.

E' applicata, se è il caso, la "preemption", vale a dire la strategia per cui, ad un certo istante, si interrompe l'esecuzione di un impegno, se viene meno il numero di RSV che necessita, per iniziare un altro impegno che richiede un numero
minore di risorse, compatibile con il nuovo valore.
Perchè questa situazione possa attivarsi, sono necessarie queste condizioni : 
* il profilo delle RSV deve essere variabile e comunque, in certi istanti, maggiore di uno. Se così non fosse, il profilo RSV sarebbe soltanto del tipo :  risorsa aperta / risorsa chiusa.
* gli impegni secondari hanno un numero diverso di RSV utilizzate. Se così non fosse, non si verificherebbe il caso di un impegno con numero RSV minore di un  altro, e quindi, nell'istante di calo della disponibilità, non ci sarebbe nessun impegno pronto a sostituirsi a quello non più eseguibile.
La preemption viene attivata soltanto in riduzione :  quando il profilo di RSV aumenta, non viene interrotto l'impegno con minor numero di risorse, per riprendere il precedente (con maggior numero) interrotto. In questo modo, a fronte di un possibile sottoutilizzo delle RSV, si riducono le interruzioni.





