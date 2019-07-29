## Impostazione
_2_Impostazione struttura linee di ammortamento (tab. A5Cxx dove xx = cod. azienda)
 :  : DEC T(ST) P() K(A5C&AZ) I(_7_Linea di ammortamento  >>)

_2_Impostazione tabella di base applicazione cespiti (tab. A51)
 :  : DEC T(ST) P() K(A51) I(_7_Tabella base applicazione cespiti >>)

_2_Impostazione consolidamento delle linee (tab. B£4xx dove xx = cod. azienda)
 :  : DEC T(ST) P() K(B£4&AZ) I(_7_Consolidamento linee >>)

_2_Impostazione piani ammortamento delle linee
 :  : INI Gestione piani di ammortamento >>
 :  : CMD CALL A5PA01G
 :  : FIN

_2_Impostazione Causali
 :  : INI Gestione Causali >>
 :  : CMD CALL C5N000G PARM('OF' 'W D' 'AZ')
 :  : FIN

## Elaborazioni
 :  : INI Generazione movimenti automatici >>
 :  : CMD CALL A5GA01G
 :  : FIN

 :  : INI Stampa libro cespiti/Chiusura >>
 :  : CMD CALL A5ST03A
 :  : FIN

 :  : INI Riallineamento Fondo Ammortamento fiscale >>
 :  : CMD CALL A5UT12A
 :  : FIN

 :  : INI - Superammortamenti
- [Superammortamenti](Sorgenti/MB/DOC/A5CAMO_02)
 :  : FIN

 :  : INI - Iperammortamenti
- [Iperammortamento](Sorgenti/MB/DOC/A5CAMO_01)
 :  : FIN

## Interrogazioni
 :  : INI Scheda Cespiti >>
 :  : CMD CALL A5SK01G
 :  : FIN
 :  : INI Interrogazione/Stampa Movimenti >>
 :  : CMD CALL A5ST02A
 :  : FIN
 :  : INI Interrogazione/Stampa Cespiti>>
 :  : CMD CALL A5ST01A
 :  : FIN
 :  : INI Controllo differenze valori linee >>
 :  : CMD CALL A5ST04A
 :  : FIN
 :  : INI Controllo Plafond manutenzioni >>
 :  : CMD CALL A5UT11A
 :  : FIN
 :  : INI Stampa Prospetto Rivalutazioni >>
 :  : CMD CALL A5ST05A
 :  : FIN

## Documentazione tecnica
### Passi di calcolo

- Se il capitale supera il valore massimo ammortizzabile della categoria (impostato come valore da osservare), verrà scritto un movimento di ammortamento per la quota eccedente.
- Qualora il piano preveda un ammortamento per periodi e non per percentuali, verrà eseguito il relativo calcolo e si andrà al punto finale di calcolo indeducibilità.
- Se il piano è per dettaglio (cespite/linea/esercizio) verrà applicato senza altre considerazioni e si andrà al punto finale di calcolo indeducibilità.
- E' da prendere in considerazione il fatto che la % indeducibile può essere indicata solo sulla tabella della categoria, oppure sul piano del singolo cespite. Rimane come prerequisito in quest'ultimo caso che la causale indicata sul piano corrisponda alla causale prevista dalla linea.
- Se sulla linea è attiva la soglia dei cespiti minori, senza alcuna definizione di un piano a livello di cespite e se il cespite non è di una categoria immateriale, verrà scritto un movimento di ammortamento con la causale impostata sulla linea con % uguale a 100, che sostituisce integralmente quanto definito a livello di piano.
- Se nella linea è impostata la modalità di trattamento primo anno '1' con la relativa % di abbattimento e se il cespite non è di una categoria immateriale, la % di ammortamento viene ridotta di questo valore per l'ammortamento ordinario, finanziario, anticipato e accelerato.
- Se presente, viene eliminata la causale di ammortamento anticipato (e la relativa %), in modo da non tenerne conto nell'ammortamento, qualora sia stata superata la soglia di anni configurata sulla linea (tenendo conto anche del fatto che il cespite sia nuovo o usato).
- Come ultimo passo, se nella categoria è presente la % di ammortamento non deducibile (impostato come valore da tenere in considerazione), si nettificheranno i movimenti di ammortamento di tale percentuale e si aggiungerà un movimento di ammortamento non deducibile, per la somma delle quote tolte agli altri movimenti.


## Vendita e alienazione cespite :  movimenti collegati
Il campo RAVALO del movimento assume il significato di valore capitale in vendita/alienazione parziale (non solo vendita).
### Causali collegate

- _1_Vendite
Su ogni movimento di vendita si aggiunge un gruppo causali collegate di cui : 
1. Tipo movimento >VC :  Capitale venduto
2. Tipo movimento >VA :  Ammortamento venduto
3. Tipo movimento >VN :  Fondo venduto
4. Tipo movimento >PV :  Plusvalenza
5. Tipo movimento >MV :  Minusvalenza

- _1_Alienazioni
Su ogni movimento di alienazione si aggiunge un gruppo causali collegate di cui : 
1. Tipo movimento> LC :  Capitale alienato
2. Tipo movimento >LA :  Ammortamento alienato
3. Tipo movimento >LN :  fondo alienato
4. Tipo movimento >MV :  Minusvalenza


## Calcolo movimenti di VC, VA, LC, LA

- _1_Vendita totale
-- Il movimento manuale ha l'importo della vendita.
-- Movimento di Capitale venduto (>VC)= importo del valore aggiornato del cespite.
-- Movimento di Ammortamento venduto (>VA)= residuo da ammortizzare, se non a zero (se a zero vuol dire che si vende un cespite totalmente ammortizzato).
-- Movimento di Fondo venduto (>VN)= valore del fondo di ammortamento (che in questo modo va a zero).

- _1_Alienazione totale
-- Il movimento manuale non ha nessun importo.
-- Movimento di Capitale alienato (LC)= importo del valore aggiornato del cespite.
-- Movimento di Ammortamento alienato (LA)= importo pari al residuo da ammortizzare, se non a zero (se a zero vuol dire che si aliena un cespite totalmente ammortizzato).
-- Movimento di Fondo alienato (LN)= il valore del fondo di ammortamento (che in questo modo va a zero).

- _1_Vendita parziale
-- Il movimento manuale ha l'importo della vendita e il valore del capitale in vendita parziale.
-- Movimento di Capitale venduto (VC)= importo del valore del capitale in vendita parziale. Se è maggiore del valore aggiornato del cespite, si esce con un messaggio d'errore.
-- Movimento di Ammortamento venduto (VA)= importo pari al minore tra il residuo da ammortizzare e il capitale venduto, se non a zero. Se è uguale a zero si vende parzialmente un cespite totalmente ammortizzato.
-- Movimento di Fondo venduto (VN)= importo pari al fondo precedente moltiplicato per il rapporto tra la quota di capitale che si sta vendendo e il valore aggiornato del cespite.

- _1_Alienazione parziale
-- Il movimento manuale ha il valore del capitale in alienazione parziale.
-- Movimento di Capitale alienato (LC)= importo del valore del capitale in alienazione parziale.
Se è maggiore del valore aggiornato del cespite, si esce con un messaggio d'errore.
-- Movimento di Ammortamento alienato (LA)= importo pari al minore tra il residuo da ammortizzare e il capitale alienato, se non a zero (se è uguale a zero, si aliena parzialmente un cespite totalmente ammortizzato).
-- Movimento di Fondo alienato (LN)= importo pari al fondo precedente moltiplicato per il rapporto tra la quota di capitale che si sta alienando e il valore aggiornato del cespite.

- _1_Vendita frazionata
-- Il movimento manuale ha l'importo della vendita e il numero di elementi venduti.
-- Se il numero di elementi totali è zero, o il numero di elementi venduti è maggiore o uguale al totale, comparirà un messaggio d'errore.
-- Si determina il valore del capitale in vendita parziale, moltiplicando il valore aggiornato del cespite per il rapporto tra la quantità venduta e la quantità totale. A questo punto ci si riconduce alla vendita parziale.

- _1_Alienazione frazionata
-- Il movimento manuale ha il numero di elementi alienati.
-- Se il numero di elementi totali è zero, oppure se il numero di elementi alienati è maggiore o uguale al totale comparirà un messaggio d'errore.
-- Si determina il valore del capitale in alienazione parziale, moltiplicando il valore aggiornato del cespite per il rapporto tra la quantità alienata e la quantità totale. A questo punto ci si riconduce all'alienazione parziale.


## Calcolo plus/minusvalenza

- _1_Input
_2_V = Importo vendita (0 se alienazione)
_2_C = Valore aggiornato cespite (al lordo del movimento che si sta trattando)
_2_A = Ammortamento eseguito (totale)
_2_F = Fondo ammortamento = A - Quota non ammortizzabile - Ammortamento perso
_2_N = Residuo da ammortizzare usato in calcolo plus/minusvalenza = C - F

- _1_Output
_2_P = Plusvalenza = V - N se V > N
_2_M = Minusvalenza = N - V se N > V
Se alienazione, essendo V=0, è sempre una minusvalenza

In caso di vendita o alienazione parziale, si determina la frazione di capitale in vendita, conoscendo >Q (valore capitale per vendita o alienazione parziale) >N'= N x (Q / C).
In caso di vendita o alienazione frazionata, se si vendono / alienano >X elementi su >Y totali, si determina >N''= N x (X / Y), utilizzando rispettivamente >N' o >N'' in luogo di >N.

