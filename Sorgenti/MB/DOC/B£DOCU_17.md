# Documentare un modulo

Documentare un modulo significa creare dei documenti (membri di documentazione) che vengano riconosciuti da Smeup come appartenenti ad un modulo.
Questo viene fatto creando gli opportuni membri di documentazione, le figure da includere nei membri stessi, gli sfondi ed i loghi da utilizzare per la stampa in pdf.
Smeup aiuta a creare e gestire questi artefatti nella _7_azione di menù Esplora, Base_up, Documentazione.

# Documenti

Abbiamo questi tipi di documento :  **applicativo**, **operativo**, di **sviluppo**, di**FAQ**, di**Glossario**, di**presentazioni**.
Ognuna di queste tipologie è referenziata secondo le rispettive regole di classificazione della scheda richiamata alla sopracitata azione (Esplora, Base_up, Documentazione) presente nella  scheda di ogni modulo.

Se questi membri esistono, vengono visualizzati nella scheda di documentazione (azione di menù "D"). La loro gestione completa invece si rimanda alla già citata gestione presente sotto Esplora.

 :  : PAR F(03)
Questi membri possono essere documenti contenente testo o un indici contenenti link ad altri documenti.


Ad esempio, supponiamo di voler documentare il modulo **B£BASE**.
**DOC/B£BASE** - Indice della documentazione applicativa :  rimanda a **DOC/B£BASE_01**, **DOC/B£BASE_02 , che contengono testo.
**DOC_OPE/B£BASE** - Documentazione operativa. Contiente testo.
**DOC_SVI/B£BASE** - Documentazione di sviluppo. Non esiste e non vogliamo crearlo.

# Figure

Le figure da includere nei documenti (tag **FIG**) devono essere archiviate nella cartella opportuna, che dipende dalla **variabile SME.IMG**  : 

**{SME.IMG}\TAB£A\<applicazione>\<modulo>**

ad esempio **{SME.IMG}\TAB£A\B£\B£BASE**

E' buona norma che il nome della figura abbia come prefisso il nome modulo (ad esempio B£BASE_001.jpg). Questo migliora la ricerca e l'indicizzazione.

 :  : PAR F(03)
La scheda dell'immagine contiene la funzione "Associa ad un documento", che permette di copiare l'immagine nell'apposita cartella semplicemente indicando il modulo a cui assegnala.


 :  : PAR F(03)
La _7_sezione Set'n'Play della scheda di documentazione di un modulo rimanda alla cartella corretta per tutte le figure del modulo.


# Sfondi e loghi
Gli sfondi ed i loghi vengono utilizzati per nella produzione dei PDF. Il processo è automatico e, per i moduli standard, non richiede alcun intervento da parte del documentatore.
Per vedere quali sfondi e loghi verranno utilizzati è sufficiente accedere alla scheda della classe VOCOD_SEL e consultarne le immagini.

# Moduli X1

Nella documentazione di moduli personalizzati, non standard, le regole di produzione sono le stesse.
Le uniche particolarità da tenere presente sono : 

- I file DOC, DOC_OPE e DOC_SVI devono essere nella **libreria LIBPER di personalizzazione** .

- Come per ogni installazione di Smeup, la variabile **SME.IMG deve essere personalizzata** per puntare ad un percorso raggiungibile che conterrà le figure standard distribuite.
- Anche le figure dei moduli X verrano archiviate tramite la variabile **PER.IMG** la quale deve essere personalizzata per puntare ad un percorso raggiungibile che conterrà le figure personali e gestita com la stessa struttura dei moduli standard.

**{SME.IMG}\TAB£A\<applicazione x>\<modulo x>**
**{PER.IMG}\TAB£A\<applicazione x>\<modulo x>**

- Le **immagini degli oggetti VOCOD_SEL** (sfondi e loghi) seguono le regole di risalita delle immagini di qualunque oggetto, quindi, se si vogliono utilizzare sfondi o loghi differenti da quelli standard, è necessario riassegnare le immagini agli oggetti, seguendo le consuete regole di personalizzazione delle immagini.
 :  : PAR F(03)
Non sostituire mai i loghi e gli sfondi standard perchè potrebbero essere ripristinati automaticamente dagli aggiornamenti!


Quindi, se l'installazione di Smeup è correttamente configurata per l'ambiente di lavoro, non dovrebbe essere necessario comportarsi diversamenta da come ci si comporta per documentare un modulo standard.

 :  : PAR F(03)
La _7_sezione Set'n'Play della scheda di documentazione di un modulo permette di testare l'ambiente in cui verranno creati i documenti.


