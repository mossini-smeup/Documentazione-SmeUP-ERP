# Costo  "Base"

## Logiche di Calcolo

Il calcolo >"BASE" permette di generare un costo calcolato assumendo : 
 * Elementi di >Distinta Base e aggregandogli un >costo di Materiale, piuttosto che di semilavorato
 * Elementi di >Ciclo di lavoro e moltiplicandolo per le >aliquote assegnate alle risorse a cui appartengono quelle fasi di ciclo

>Elementi di Distinta Base possono essere : 
 * La distinta >standard dell'oggetto articolo
 * La distinta >effettiva di un oggetto, quale un articolo, un ordine, una riga di documento di conto lavoro, un lotto o una commessa; con possibilità di derivare la distinta di un qualsiasi oggetto da quella di un oggetto di livello più alto, oppure, nel caso di documento passivo, derivare la distinta della bolla di entrata da quella dell'ordine di acquisto che ha contribuito a generarlo.
 * La distinta  >consuntiva di un oggetto, generata nel valutare i movimenti di prelievo a magazzino (  _9_GMMOVI ) assegnati a quello specifico oggetto.

>Elementi di Ciclo di lavoro possono essere : 
 * Il ciclo >standard dell'oggetto articolo
 * Il Ciclo >effettivo di un oggetto, quale un articolo, un ordine,  un lotto o una commessa; con possibilità di derivarlo per un qualsiasi oggetto da quello di un oggetto di livello più alto.
 * Il Ciclo  >consuntivo di un oggetto, generato dal riepilogo delle attività produttive rilevate (  _9_P5ATTI ) per quello specifico oggetto.

>Elementi di Costo del Materiale e/o Semilavorato che possono essere assunti : 
 * Costi legati all'ultimo documento di entrata (bolla) di quel materiale
 * Costi legati all'ultimo ordine di acquisto di quel materiale
 * Costi medi del materiale e/o del semilavorato
 * Costi di listino del materiale e/o del semilavorato
 * Costi manuali legati al materiale e/o semilavorato

>Aliquote assegnate alle risorse che possono essere : 
 * Attribuite al Centro di Costo assegnato alla risorsa presente sulla fase
 * Attribuite alla Risorsa impostata sulla fase del ciclo
 * Attribuite alla Risorsa impostata sulla fase del ciclo e se non trovata l'aliquota, risalita fino al Centro di Costo assegnato a quella risorsa

## Lancio Calcolo costo Base Multicontesto
 :  : INI Esecuzione Calcolo costo Base Multicontesto >>
 :  : CMD CALL D0CO01B
 :  : FIN


## Autorizzazioni
_7_Documentazione in fase di sviluppo

## Impostazioni

Le impostazioni del calcolo costi si dividono in varie sezioni

![D0CCMC_21A](http://localhost:3000/immagini/D0CCMC_13O/D0CCMC_21A.png)
### Impostazioni di Estrazione
Le impostazioni di estrazione sono specifiche per tipo contesto

### Impostazioni di Estrazione - Contesto AR (Articolo)
![D0CCMC_21B](http://localhost:3000/immagini/D0CCMC_13O/D0CCMC_21B.png) * Ricalcolo LowLevelCode Si/No. Il LowLevelCode serve per ricalcolare i componenti base (di acquisto) prima degli altri così da calcolare gli articoli in sequenza discendente rispetto all'ordinamento di utilizzo nella distinta base presente nel parametro relativo della tabella >TCO specifica di quel tipo costo.

### Impostazioni di Estrazione - Contesto DR (Documento)
![D0CCMC_21C](http://localhost:3000/immagini/D0CCMC_13O/D0CCMC_21C.png)
_7_Documentazione in fase di sviluppo

### Impostazioni di Estrazione - Contesto OR (Ordine Prodiuzione)
![D0CCMC_21D](http://localhost:3000/immagini/D0CCMC_13O/D0CCMC_21D.png)
_7_Documentazione in fase di sviluppo


### Impostazioni di Calcolo
_7_Documentazione in fase di sviluppo

### Impostazioni di Completamento
_7_Documentazione in fase di sviluppo

### Impostazioni di Documentazione ed Errori
_7_Documentazione in fase di sviluppo

### Impostazioni di Memorizzazione
_7_Documentazione in fase di sviluppo


## Controllo dei risultati
_7_Documentazione in fase di sviluppo

