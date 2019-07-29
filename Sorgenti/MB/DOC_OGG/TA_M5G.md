# M5G - Conferma automatica consigli MRP
## OBIETTIVI
Impostare i suggerimenti MRP che sono soggetti ad applicazione automatica (Cieca).
Nel caso di suggerimenti di riduzione e anticipo e/o ritardo, si puo' effetturare l'applicazione
parziale del suggerimento (Solo riduzione e anticipo o ritardo).

 : T02 Elemento della tabella M5G : 
la sintassi dell'elemento di tabella comprende sia lo scenario dell'MRP sia il plant su cui si deve applicare il selfie. La separazione tra i due codici è effettuata col carattere _ .
Ad esempio l'elemento **_001 significa Scenario = ** e Plant = 001.

## Impianto monoplant.
Si può inserire solo l'elemento scenario , in questo caso si applica a tutti i plant.
Se è vuoto o assente il selfie è disabilitato


## Impianto multiplant
L'elemento solo scenario è obbligatorio. Se assente il selfie è disabilitato.
L'elemento vuoto sta per "assente" non per "risale".

Esempio 1
Elemento solo scenario :  vuoto
Elemento scenario/plant assente :  no selfie
Elemento scenario/plant vuoto :  no selfie
Elemento scenario/plant pieno :  selfie con dati specifici

Esempio 2
Elemento solo scenario :  pieno
Elemento scenario/plant assente :  selfie con dati generali (di solo scenario)
Elemento scenario/plant vuoto :  no selfie
Elemento scenario/plant pieno :  selfie con dati specifici


## CONTENUTO DEI CAMPI
 :  : FLD T$M5G0 __  Eliminazione PR __
Il suggerimento di eliminazione viene applicato per la produzione
 :  : FLD T$M5G1 __ Eiminazione AQ   __
Il suggerimento di eliminazione viene applicato per gli acquisti
 :  : FLD T$M5G2 __ Eliminazione LV  __
Il suggerimento di eliminazione viene applicato per il conto lavoro
 :  : FLD T$M5G3 __ Eliminazione TR  __
Il suggerimento di eliminazione viene applicato per i trasferimenti
 :  : FLD T$M5G4 __ Solo riduzione PR__
Se presente solo il suggerimento di riduzione, viene applicato per la produzione
 :  : FLD T$M5G5 __ Solo riduzione AQ__
Se presente solo il suggerimento di riduzione, viene applicato per gli acquisti
 :  : FLD T$M5G6 __ Solo riduzione LV__
Se presente solo il suggerimento di riduzione, viene applicato per il conto lavoro
 :  : FLD T$M5G7 __ Solo riduzione TR__
Se presente solo il suggerimento di riduzione, viene applicato per i trasferimenti
 :  : FLD T$M5G8 __ Riduzione e ant PR__
Se presenti i suggerimenti di riduzione e anticipo, per la produzione vengono applicati entrambi
 :  : FLD T$M5G9 __ Riduzione e ant AQ__
Se presenti i suggerimenti di riduzione e anticipo, per gli acquisti vengono applicati entrambi
 :  : FLD T$M5GA __ Riduzione e ant LV__
Se presenti i suggerimenti di riduzione e anticipo, per il conto lavoro vengono applicati entrambi
 :  : FLD T$M5GB __ Riduzione e ant TR__
Se presenti i suggerimenti di riduzione e anticipo, per i trasferimenti vengono applicati entrambi
 :  : FLD T$M5GC __ Riduzione e rit PR__
Se presenti i suggerimenti di riduzione e ritardo, per la produzione vengono applicati entrambi
 :  : FLD T$M5GD __ Riduzione e rit AQ__
Se presenti i suggerimenti di riduzione e ritardo, per gli aquisto vengono applicati entrambi
 :  : FLD T$M5GE __ Riduzione e rit LV__
Se presenti i suggerimenti di riduzione e ritardo, per il conto lavoro vengono applicati entrambi
 :  : FLD T$M5GF __ Riduzione e rit TR__
Se presenti i suggerimenti di riduzione e ritardo, per i trasferimenti vengono applicati entrambi
 :  : FLD T$M5GG __ Solo anticipo PR  __
Se presente solo il suggerimento di anticipo, viene applicato per la produzione
 :  : FLD T$M5GH __ Solo anticipo AQ  __
Se presente solo il suggerimento di anticipo, viene applicato per gli acquisti
 :  : FLD T$M5GI __ Solo anticipo LV  __
Se presente solo il suggerimento di anticipo, viene applicato per il conto lavoro
 :  : FLD T$M5GJ __ Solo anticipo TR  __
Se presente solo il suggerimento di anticipo, viene applicato per i trasferimenti
 :  : FLD T$M5GK __ Solo ritardo  PR  __
Se presente solo il suggerimento di ritardo, viene applicato per la produzione
 :  : FLD T$M5GL __ Solo ritardo  AQ  __
Se presente solo il suggerimento di ritardo, viene applicato per gli acquisti
 :  : FLD T$M5GM __ Solo ritardo  LV  __
Se presente solo il suggerimento di ritardo, viene applicato per il conto lavoro
 :  : FLD T$M5GN __ Solo ritardo  TR  __
Se presente solo il suggerimento di ritardo, viene applicato per i trasferimenti
 :  : FLD T$M5GO __ Pianificati PR    __
Vengono rilasciati i suggerimenti di pianificazione di produzione
 :  : FLD T$M5GP __ Data limite PR    __
E' la data suggerimento fino a cui vengono rilasciati i suggerimenti di pianificazione produzione
 :  : FLD T$M5GQ __ Pianificati AQ    __
Vengono rilasciati i suggerimenti di pianificazione acquisti
 :  : FLD T$M5GR __ Data limite AQ    __
E' la data suggerimento fino a cui vengono rilasciati i suggerimenti di pianificazione acquisti
 :  : FLD T$M5GS __ Pianificati LV    __
Vengono rilasciati i suggerimenti di pianificazione di conto lavoro
 :  : FLD T$M5GT __ Data limite LV    __
E' la data suggerimento fino a cui vengono rilasciati i suggerimenti di pianificazione conto lavoro
 :  : FLD T$M5GU __ Pianificati TR    __
Vengono rilasciati i suggerimenti di pianificazione di trasferimenti
 :  : FLD T$M5GV __ Data limite TR    __
E' la data suggerimento fino a cui vengono rilasciati i suggerimenti di pianificazione trasferimenti


 :  : FLD T$M5GW __Suffisso exit filtro__
Se impostato, è il suffisso x del programma M5M5R0R_x, che viene lanciato all'atto dell'applicazione
del suggerimento per escludere il consiglio dall'applicazione automatica.
NB :  questa exit permette di escludere sia consigli di modifica sia di emissione di nuovi ordini.
 :  : FLD T1M5G1 __No Riduzione        __
Se presenti i suggerimenti di riduzione e anticipo, per la produzione viene applicato solo
l'anticipo.
 :  : FLD T1M5G2 __No Riduzione        __
Se presenti i suggerimenti di riduzione e anticipo, per gli acquisti viene applicato solo
l'anticipo.
 :  : FLD T1M5G3 __No Riduzione        __
Se presenti i suggerimenti di riduzione e anticipo, per il conto lavoro viene applicato solo
l'anticipo.
 :  : FLD T1M5G4 __No Riduzione        __
Se presenti i suggerimenti di riduzione e anticipo, per i trasferimenti viene applicato solo
l'anticipo.
 :  : FLD T1M5G5 __No Anticipo         __
Se presenti i suggerimenti di riduzione e anticipo, per la produzione viene applicata solo
la riduzione
 :  : FLD T1M5G6 __No Anticipo         __
Se presenti i suggerimenti di riduzione e anticipo, per gli acquisti viene applicata solo
la riduzione
 :  : FLD T1M5G7 __No Anticipo         __
Se presenti i suggerimenti di riduzione e anticipo, per il conto lavoro viene applicata solo
la riduzione
 :  : FLD T1M5G8 __No Anticipo         __
Se presenti i suggerimenti di riduzione e anticipo, per i trasfermenti viene applicata solo
la riduzione
 :  : FLD T1M5GA __No Riduzione        __
Se presenti i suggerimenti di riduzione e ritardo, per la produzione viene applicato solo
l'anticipo
 :  : FLD T1M5GB __No Riduzione        __
Se presenti i suggerimenti di riduzione e ritardo, per gli acquisti viene applicato solo
l'anticipo
 :  : FLD T1M5GC __No Riduzione        __
Se presenti i suggerimenti di riduzione e ritardo, per il conto lavoro viene applicato solo
l'anticipo
 :  : FLD T1M5GD __No Riduzione        __
Se presenti i suggerimenti di riduzione e ritardo, per i trasferimenti viene applicato solo
l'anticipo
 :  : FLD T1M5GE __No Ritardo          __
Se presenti i suggerimenti di riduzione e ritardo, per la produzione viene applicata solo
la riduzione
 :  : FLD T1M5GF __No Ritardo          __
Se presenti i suggerimenti di riduzione e ritardo, per gli acquisti viene applicata solo
la riduzione
 :  : FLD T1M5GG __No Ritardo          __
Se presenti i suggerimenti di riduzione e ritardo, per il conto lavoro viene applicata solo
la riduzione
 :  : FLD T1M5GH __No Ritardo          __
Se presenti i suggerimenti di riduzione e ritardo, per i trasferimenti viene applicata solo
la riduzione
