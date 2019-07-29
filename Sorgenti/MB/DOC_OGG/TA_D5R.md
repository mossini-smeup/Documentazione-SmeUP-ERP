# D5R - Riprese da sistemi conferenti
 :  : DEC T(ST) K(D5R)
## OBIETTIVO
Gestisce la modalità di ripresa di un dato (o serie di dati) in DELT_UP.
## CONTENUTO DEI CAMPI
 :  : FLD T$ELEM Codice
In funzione del sistema conferente, ad esempio per la contabilità generale è un conto o una sua parte. Può comunque essere un codice qualsiasi inserito dall'utente.
Il codice ** indica le azioni da eseguire nel caso in cui l'elemento inserito dal programma di ripresa, non esista nella tabella.
Oltre all'elemento specificato nei parametri di ripresa, vengono eseguiti anche tutti gli elementi del tipo xxxxxx.n, dove xxxxxx è l'elemento scelto dal programma di ripresa e n è un progressivo (ex. BOF.1, BOF.2, ecc.).
Questa possibilità è molto utile se vengono riempiti i successivi campi di contesto e tema (vedi dopo).
 :  : FLD T$DESC Descrizione
Descrizione libera
 :  : FLD T$D5RA S/S **Passi**
È il sottosettore della tabella D5E in cui sono codificate le azioni da eseguire.
Se viene lasciato in bianco, si indica a DELT_UP di non riprendere l'elemento (utile nei programmi di aggiustamento utente).
 :  : FLD T$D5RB **Prefisso passo**
È la radice di azioni da eseguire, codificate nel settore D5Exx, dove xx è specificato nel campo precedente.
_9_Esempio :  se viene specificato AZI0, verranno eseguite tutte le azioni che iniziano per AZI0 (AZI001,AZI010,ecc.).
 :  : FLD T$D5RC **Segno transazione**
È utilizzato per la ripresa di alcuni sistemi conferenti ed indica il segno della transazione con cui sono inserite le azioni. Il valori possibili sono : 
- >E = Entrata
- >U = Uscita
- >D= Dare
- >A= Avere
- >E e >U sono usati nella ripresa di magazzino ed indicano il segno del movimento primario (es. se inserisco E e scelgo una uscita la ripresa moltiplicherà per -1 quantità e valori).
- >D e >A sono tipicamente collegati alla contabilità generale.
 :  : FLD T$D5RD **Solo totali**
Utilizzato per la ripresa dalla contabilità generale. Al posto di elaborare le singole registrazioni contabili viene ritornato solo il totale per conto contabile.
_9_Esempio :  un indice può avere la necessità di conoscere il totale per conto nel periodo, per effettuare la sua ripartizione.
 :  : FLD T$D5RE **Contesto**
Si possono specificare un contesto ed un tema che sostituiranno quelli presenti negli elementi della tabella D5E, nel caso in cui in questi venga specificato ** (vedi help della tabella D5E).
Può essere utile nel caso in cui si vogliano eseguire le stesse azioni (elementi della tabella D5E) su contesti e/o temi diversi, senza voler replicare queste ultime.
 :  : FLD T$D5RF.T$D5RE Tema
