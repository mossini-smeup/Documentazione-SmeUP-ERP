## Collegamento Co.ge -> Cespiti

La determinazione della categoria da presentare nel momento in cui viene applicato un movimento di acquisto a partire dal movimento contabile avviene attraverso la lettura dei parametri £A6. All'interno di questi parametri è possibile associare ad ogni conto contabile la relativa categoria cespiti. Questo fa sì che, applicando un movimento contabile d'acquisto, il sistema determini in modo automatico la categoria del cespite da creare e impedisca la creazione su altre categorie. Nel caso in cui a uno stesso conto contabile siano associate più categorie cespiti il sistema proporrà la creazione del cespite sulla prima delle categorie e accetterrà la sua variazione solo nel caso in cui la nuova categoria inserita sia inclusa all'interno dei parametri impostati sul conto stesso.


## Collegamento Cespiti -> Co.ge

I conti con cui vengono contabilizzati i movimenti registrati sui cespiti vengono determinati secondo questa risalita : 
1- Lettura conti su anagrafica cespite :  se non compilati passa al punto 2
2- Lettura conti da parametri £A5 per categoria :  se non compilati passa al punto 3
3- Lettura conti da tabella A5A :  se non compilati passa al punto 4
4- Lettura conti da parametri £A5 generici

Per facilitare l'impostazione e l'analisi di questi conti, all'interno del modulo Operazioni Contabili (A5OPCO) sono disponibili tre interrogazioni : 

 * Conti per categoria :  permette di analizzare i conti impostati sulla tabella A5A

![A5OPCO_005](http://localhost:3000/immagini/A5OPCO_03/A5OPCO_005.png)
 * Impostazione Conti /Causali Generiche :  permette di analizzare le causali/conti definiti a livello generale. In questo gruppo potrebbero, ad esempio, rientrare i conti elle plus/minusvalenze così come le causali utilizzate nella rilevazione degli ammortamenti.

![A5OPCO_001](http://localhost:3000/immagini/A5OPCO_03/A5OPCO_001.png)
 * Impostazione Conti /Causali per Categoria :  permette di analizzare le causali/conti specificati a livello di categoria

![A5OPCO_002](http://localhost:3000/immagini/A5OPCO_03/A5OPCO_002.png)
 * Impostazione Conti /Causali per Cespite :  permette di analizzare le causali/conti specificati a livello di singolo cespite.
![A5OPCO_003](http://localhost:3000/immagini/A5OPCO_03/A5OPCO_003.png)
Per ulteriori dettagli sulle tre schede si rimanda alla relativa documentazione.

## Suggerimenti di configurazione

In fase di attivazione dei collegamenti A5 - C5 si consiglia di procedere in questo modo : 


- Nel caso in cui esistano conti o causali contabili generali (quindi che non variano al variare della categoria o del cespite) è possibile impostarli all'interno della scheda di impostazione conti/causali generiche presente all'interno del modulo delle operazioni contabili (A5OPCO). Questa funzionalità è generalmente sfruttata per l'impostazione dei conti di imputazione di plusvalenze/minusvalenze oppure per configurare il conto di contropartita utilizzato nella contabilizzazione delle vendite o ancora per definire le causali contabili utilizzate per la contabilizzazione dei diversi movimenti

![A5OPCO_001](http://localhost:3000/immagini/A5OPCO_03/A5OPCO_001.png)
- Impostazione conti a livello di categoria. All'interno della tabella delle categorie fiscali (settore A5A) è possibile definire i conti di ammortamento, fondo ammortamento e capitale specifici per categoria.

![A5OPCO_005](http://localhost:3000/immagini/A5OPCO_03/A5OPCO_005.png)
- Impostazione conti a livello di cespite. Sull'anagrafica del cespite è possibile definire i conti di ammortamento, fondo ammortamento e capitale specifici per il singolo cespite. Si sottolinea che questi conti vanno compilati solo nel caso in cui siano diversi da quelli definiti a livello di categoria.

![A5OPCO_006](http://localhost:3000/immagini/A5OPCO_03/A5OPCO_006.png)
- Impostazione conti specifici per particolari movimenti. Nel caso in cui ci sia la necessità di configurare conti specifici su particolari causali di movimentazione (es. conti per ammortamenti indeducibili o conti per ammortamenti anticipati, ecc.) impostarli attraverso la scheda Causali/Conti per categoria o Causali/Conti per cespite.




## Contabilizzazione vendite

Per gestire in modo automatico le rilevazioni contabili relative alle vendite/alienazioni si consiglia di procedere in questo modo : 
* All'interno della registrazione contabile della vendita utilizzare come contropartita del cliente un conto transitorio
* Impostare a livello generale : 
** Come conto dare del capitale venduto il conto transitorio
** Come conto avere del fondo venduto il conto transitorio
** Come conto dare delle plusvalenze il conto transitorio
** Come conto avere delle plusvalenze il conto relativo alle plusvalenze
** Come conto avere delle minusvalenze il conto transitorio
** Come conto dare delle minusvalenze il conto relativo alle minusvalenze
* Impostare sulle categorie/cespiti i relativi conti di costo storico (capitale) e fondo.

Terminata la configurazione sarà possibile eseguire la contabilizzazione automatica della vendita del cespite che porterà a zero il saldo del conto transitorio e rileverà i relativi valori di costo storico, fondo e plus/minusvalenza utilizzando la funzione _Contabilizzazione Vendite disponibile all'interno del modulo Cespiti :  operazioni contabili.


