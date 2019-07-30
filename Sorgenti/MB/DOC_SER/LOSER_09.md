 :  : HEA RESP(FP) STAT(10)
# Il servizio
## Obiettivo
 Obiettivo del servizio è fornire uno strumento flessibile e personalizzabile per la rappresentazione di statistiche.
La configurabilità delle schede è legata all'utilizzo di una struttura basata su script, che permette di specificare l'oggetto su cui effettuare operazioni statistiche, i valori numerici di interesse relativi all'oggetto ed eventuali attributi dell'oggetto, per raffinare ulteriormente la statistica.
A livello grafico quindi, le istanze dell'oggetto scelto sono visualizzate sull'asse X, mentre i valori numerici rappresentano le diverse serie, cioè
i valori Y corrispondenti a ciascuna istanza (non considerando  una possibile inversione degli assi effettuata a livello di componente grafico).
Ad esempio, effettuando statistiche sull'oggetto inventario (TAGMI) dell'applicazione GM, si ha che i diversi inventari vengono rappresentati sull'asse X mentre la quantità prevista, la quantità effettiva, la quantità dello scostamento, la percentuale dello scostamento, (cioè le dimensioni di analisi significative per l'inventario) sono le serie.

## Architettura
I componenti coinvolti sono : 
 * uno script specifico per applicazione/categoria di oggetti in cui vengono specificati le sezioni, gli spazi, le subsezioni, le chiavi, i valori numerici, gli attributi, il nome dei programmi specifici, i collegamenti tra chiavi-valori-attributi;
 * un programma specifico legato allo script, che si occupa del caricamento dei dati (chiavi, valori, spazi) da file in una stringa (DS), secondo un formato predefinito consistente con quanto definito nello script;
 * il servizio LOSER_09, che si occupa di rappresentare in matrice i dati che gli vengono mandati dal programma specifico, in base alle istruzioni contenute nello script;
 * la scheda delle statistiche LO_S09_01.
## Funzioni e metodi
### LIS
Metodi relativi alla visualizzazione in lista di elementi : 

 * **SCP** :  elenco di script - al momento è cablato nel servizio.
 * **SEZ** :  elenco delle sezioni contenute in uno script;
 * **SPA** :  elenco degli spazi della sezione;
 * **SUB** :  elenco delle subsezioni di una sezione;
 * **ATT** :  elenco delle caratteristiche degli attributi specificate nello script;
 * **NOM** :  restituisce un albero con il nome dello script in uso (metodo usato per caricare il codice dello script nella scheda LO_S09_01);
 * **TIM** :  restituisce una matrice contenente le prestazioni in base alle azioni eseguite sulla scheda;
 * **DET** :  restituisce informazioni di dettaglio - DA IMPLEMENTARE.

### PIA
Azioni che vengono eseguite sui piani.

 * **SCE** :  visualizza i filtri impostati nello script (le chiavi che hanno asse Z nelle subsezioni);
 * **PRE** :  restituisce i dati desiderati aggregati per codice oggetto.

### CAR
Azioni che visualizzano lo stato dei vari elementi coinvolti, da usare quindi principalmente per scopi di debug.

 * **KEY** :  restituisce una matrice contenente le informazioni relative alle chiavi ricavate dallo script;
 * **ATT** :  restituisce una matrice contenente le informazioni relative agli attributi delle chiavi ricavate dallo script;
 * **VAL** :  restituisce una matrice contenente le informazioni relative ai valori numerici ricavate dallo script;
 * **VA2** :  restituisce una matrice contenente i valori numerici e la stringa letta dal programma specifico;
 * **OGG** :  restituisce una matrice contenente i codici degli oggetti (eventualmente la decodifica) e la stringa letta dal programma specifico;
 * **COL** :  restituisce una matrice contenente le informazioni relative ai collegamenti tra chiavi-valori-attributi ricavate dallo script;
 * **GRA** :  restituisce una matrice che affianca i codici degli oggetti con i corrispondenti valori numerici.

# Gli script
## Posizione
Gli script si trovano nel file SCP_SET della libreria SMEDEV.
## Nome
**XX_S09_NN**, dove
 * **XX** è l'applicazione di appartenenza;
 * **S09** si riferisce al servizio responsabile della gestione delle statistiche (LOSER_09);
 * **NN** è un intero positivo progressivo.
Esempi di nomi sono
 * GM_S09_01;
 * X1_S09_01.
## Tag e attributi
Gli script hanno il compito di specificare tutte le informazioni necessarie per il corretto caricamento dei dati passati dal programma specifico al servizio e per definire quali informazioni visualizzare nella scheda.
### T.SEZ
Uno script è composto da una o più sezioni, che coincidono generalmente con il tipo/parametro dell'oggetto. Sono esempi di sezioni il periodo (PER), l'inventario (GMI), il collaboratore (COL), eccetera.
Gli attributi del tag sono : 

 * **Cod** :  un codice identificativo univoco di tre lettere;
 * **Txt** :  una descrizione testuale della sezione;
 * **Pgm** :  il nome del programma specifico.

Esempio
 :  : PAR F(04)
 :  : T.SEZ Cod="GMI" Txt="Statistiche Inventari" Pgm="GM_S09_01"


### T.SPA
Gli spazi rappresentano un elenco di istanze di oggetti dello stesso tipo/parametro.
Gli attributi del tag sono : 

 * **Mod** :  indica il modo di caricamento dei dati dal programma specifico : 
 ** **A** tramite G60 - NON IMPLEMENTATO;
 ** **B** dal programma specifico;
 ** **C** cablando direttamente i dati - NON IMPLEMENTATO.
 * **Ogg** :  tipo/parametro dell'oggetto.

Esempio
 :  : PAR F(04)
 :  : T.SPA Mod="B" Ogg="TAGMI"


### T.OGG
Gli oggetti sono i valori reali degli oggetti specificati nelle chiavi (le chiavi vengono descritte nel paragrafo successivo).
Ad esempio, effettuando statistiche nell'ambito degli inventari, una chiave è rappresentata dal magazzino :  gli oggetti della chiave sono quindi il magazzino A, il magazzino B, il magazzino C, cioè magazzini realmente esistenti.
Gli attributi del tag sono : 

 * **Mod**  :  indica il modo di caricamento dei dati dal programma specifico : 
 ** **A** tramite G60 - NON IMPLEMENTATO;
 ** **B** dal programma specifico;
 ** **C** cablando direttamente i dati - NON IMPLEMENTATO.
 * **Par**  :  l'istanza dell'oggetto. Riprendendo l'esempio, avrebbe il valore di "Magazzino A". Chiaramente, per ragioni di flessibilità, non deve essere direttamente implementata, dato che l'istanza dell'oggetto cambia continuamente. E' quindi opportuno utilizzare una variabile.
 ** **&SPA** :  "Par" viene inizializzato con l'istanza dello spazio correntemente selezionato.

Esempio
 :  : PAR F(04)
 :  : T.OGG Mod="B" Par="&SPA"

	
### T.KEY
Le chiavi indicano gli oggetti rilevanti per le statistiche dato lo spazio. Ad esempio, se lo spazio è un inventario, è interessante analizzare la sua composizione in termini di articolo, di magazzino, di area giacenza e di tipo giacenza.
Le chiavi sono quindi le dimensioni utilizzate per studiare lo spazio scelto.
Gli attributi del tag sono : 

 * **Ogg** :  tipo/parametro dell'oggetto della chiave;
 * **Pos** :  posizione iniziale all'interno della stringa (DS) passata dal programma specifico al servizio. E' importantissimo che questo valore coincida con quello specificato nel programma specifico, perchè mentre in quest'ultimo la posizione è cablata, il servizio legge la posizione iniziale dallo script :  se tali valori non coincidessero, il servizio estrarrebbe dati scorretti dalla stringa (DS).
 * **Lun** :  lunghezza dello spazio riservato alla chiave all'interno della stringa (DS) passata dal programma al servizio. Valgono le considerazioni effettuate per l'attributo precedente relative alla corrispondenza tra i valori;
 * **Txt** :  descrizione della chiave;
 * **Id** :  identificativo univoco progressivo della chiave - è importante che sia univoco;
 * **Con** :  modalità di rappresentazione in matrice : 
 ** **COD** :  viene visualizzato il codice;
 ** **DES** :  viene visualizzata la descrizione;
 ** **BOT** :  vengono visualizzati entrambi.

Esempio
 :  : PAR F(04)
 :  : T.KEY Ogg="TAMAG" Pos="01" Lun="03" Txt="Magazzino" Id="01"  Con="DES"


Nell'esempio presentato, nella stringa trasmessa dal programma specifico al servizio (composta da una serie di sottostringhe di lunghezza definita, indicata nel programma specifico stesso), in ogni sottostringa le posizioni da 01 a 03 sono riservate per il codice del magazzino.

### T.VAL
I valori numerici rappresentano le serie delle statistiche.
Gli attributi del tag sono : 

 * **Ogg** :  tipo/parametro dell'oggetto del valore - tipicamente "NR" (numero);
 * **Txt** :  descrizione del valore;
 * **Mod** :  indica il modo di caricamento dei dati dal programma specifico;
 * **Par** :  indica il nome del programma specifico;
 * **Pos** :  posizione iniziale del valore all'interno della stringa (DS) passata dal programma specifico al servizio. Vale quanto scritto per la chiave;
 * **Lun** :  lunghezza dello spazio riservato al valore all'interno della stringa (DS) passata dal programma al servizio. Vale quanto scritto per la chiave;
 * **Id** :  identificativo univoco progressivo della chiave - è importante che sia univoco;

Esempio
 :  : PAR F(04)
 :  : T.VAL Txt="Quantità prevista" Ogg="NR"  Mod="B"  Par="GM_S09_01" Pos="01" Lun="11"  Id="01"


### T.ATT
Gli attributi si riferiscono alle subsezioni e permettono di effettuare statistiche su un sottoinsieme significativo dell'oggetto.
Ad esempio, se una subsezione è l'articolo, può essere interessante analizzare i dati relativi all'articolo in termini di classe materiale, cioè in termini di un OAV dell'oggetto principale.
Gli attributi del tag sono : 

 * **Ogg** :  tipo/parametro dell'oggetto dell'attributo;
 * **Cod** :  codice dell'OAV;
 * **Txt** :  descrizione dell'attributo;
 * **Id** :  identificativo univoco progressivo della chiave - è importante che sia univoco;
 * **Con** :  modalità di rappresentazione in matrice : 
 ** **COD** :  viene visualizzato il codice;
 ** **DES** :  viene visualizzata la descrizione;
 ** **BOT** :  vengono visualizzati entrambi.

Esempio
 :  : PAR F(04)
 :  : T.ATT Ogg="TACLS" Cod="I/10" Txt="Classe materiale"  Id="01"  Con="COD"


### T.COL
I collegamenti hanno il compito di correlare una chiave con i valori numerici e gli attributi da utilizzare per le statistiche.
Deve necessariamente esistere un'istruzione di tipo T.COL per ogni chiave.
Gli attributi del tag sono : 

 * **IdKey** :  chiave;
 * **IdVal** :  valori numerici associati alla chiave. Lo stesso valore numerico, se significativo, può essere associato a più chiave. L'associazione viene effettuata tramite l'attributo Id del valore. Se necessario inserire più di un valore numerico, le Id vanno separate da uno spazio bianco.
 * **IdAtt** :  attributi da associare alla chiave. Lo stesso attributo, se significativo, può essere associato a più chiavi. L'associazione viene effettuata tramite l'attributo Id dell'attributo. Se necessario inserire più di un attributo, le Id vanno separate da uno spazio bianco. L'attributo IdAtt è facoltativo.

Esempi
 :  : PAR F(04)
  :  : T.COL IdKey="04"  IdVal="01 02 03" IdAtt="01 02 03 04"
  :  : T.COL IdKey="02"  IdVal="01 03"


### T.SUB
Le subsezioni devono coincidere con le chiavi.
Gli attributi del tag sono : 

 * **Txt** :  descrizione della subsezione;
 * **Ogg** :  tipo/parametro dell'oggetto rappresentato dalla subsezione.

Esempio
 :  : PAR F(04)
 :  : T.SUB Txt="Articolo" Ogg="AR


### T.ASS
Gli assi sono riferiti alle subsezioni :  l'asse X indica la chiave da utilizzare come base della statistica e deve esistere obbligatoriamente ed essere unico. L'asse Z invece indica le chiavi da utilizzare come eventuale filtro sulle statistiche; è facoltativo e può essere multiplo.
Gli attributi del tag sono : 

 * **Ass** :  tipo dell'asse : 
 ** **X** :  obbligatorio e univoco, indica l'oggetto base della statistica.
 ** **Z** facoltativo e multiplo, indica i filtri.
 * **IdKey** :  chiave associata all'asse.

Esempio
 :  : PAR F(04)
 :  : T.SUB Txt="Articolo" Ogg="AR"
 :  : T.ASS Ass="X" IdKey="01"
 :  : T.ASS Ass="Z" IdKey="02"


# I programmi specifici
## Nome del programma
**XX_S09_NN**, dove

 * **XX** è l'applicazione di appartenenza;
 * **S09** si riferisce al servizio responsabile della gestione delle statistiche (LOSER_09);
 * **NN** è un intero positivo progressivo.
## Caratteristiche
Il programma specifico, da associare ad uno script, viene chiamato dal servizio LOSER_09 e restituisce una stringa (DS) adeguatamente formattata contenente i dati richiesti letti da file.
Il programma deve poter gestire correttamente il caso in cui i dati trasmessi superino i 30000 caratteri (limite della stringa) e le posizioni cablate devono corrispondere a quelle specificate nello script, visto che il servizio decodifica la stringa in base al contenuto dello script.
## Funzioni e metodi
# Esempi
Per visualizzare esempi di utilizzo delle statistiche, selezionare :  "My Loocup" -> "Esempi" -> "Capire Loocup" -> "Esempi applicativi" -> "Statistiche".
Sono disponibili esempi relativi a tre casistiche : 
 * Da zero :  indica la possibilità di costruire la scheda in base all'input dell'utente, che deve selezionare lo script, la sezione e lo spazio;
 * Da oggetti specifici :  script e sezione vengono specificati nella chiamata della funzione - l'utente deve quindi scegliere lo spazio di interesse da una lista che viene generata dal programma specifico relativo.
 * Da oggetto generico :  lo script viene specificato nella funzione e l'istanza dell'oggetto (lo spazio) viene scelta da una lista generata da un qualunque servizio.

# Sviluppi futuri

 * Migliorare il filtro sugli oggetti con 5250;
 * Ottimizzare le prestazioni (lettura su file, utilizzo della copy £TNU per trasformazioni stringa/numero e viceversa);
 * Caricamento di informazioni di dettaglio sulla singola istanza tramite popup;
 * riempimento delle date mancanti in base al periodo o in base ad impostazioni definite nello script;
 * G56;
 * Quando il componente grafico lo permette, inserire popup specifici per oggetto selezionato.

