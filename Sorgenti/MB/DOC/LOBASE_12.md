# Immagini, Folder e Preview di un oggetto

**NOTA si ricorda che gli esempi e la documentazione di dettaglio sugli script sono nei membri K09_PER e K09_STD, file SCP_SET

## Introduzione
Per ogni oggetto di smeup sono previste le cosiddette "risorse". Le risorse di un oggetto sono principalmente : 


- Immagine :  gestita tramite risalita, a partire dall'istanza, poi alla classe ed infine all'oggetto generico **, questo perchè è obbligatoria e non può non esistere. L'estensione consigliata ed impostata a standard per le immagini è .PNG
- Folder :  la carella dell'oggetto, dove è possibile trovare tutti i file relativi ad esso; questa può anche non esistere
- Preview :  è un file che rappresenta l'oggetto nella sua essenza,  una sorta di anteprima dell'oggetto. Ad esempio il pdf di un oggetto FT (fattura) o il link alla pagina web Youtube di un video. Per la maggior parte degli oggetti la preview corrisponde all'immagine


## Dove si trovano in Sme.UP
Le risorse sono visibili nella sezione _INFO_ dell'oggetto interessato. Ci si arriva dalla scheda dell'oggetto, oppure direttamente da tasto destro.

## Scheda di controllo e gestione
Dall'oggetto, da tasto destro, è possibile accedere alla scheda di **analisi/configurazione delle risorse**. Il percorso è :  **Properties /Controllo risorse oggetto**.
Attraverso questa scheda, in un unico punto di accesso è possibile impostare la struttura delle risorse.
Nel primo tab "Analisi Impostazione" è possibile controllare come e dove sono le risorse, si possono vedere : 

- Funzioni :  consente di rispondere alle domande _dov'è l'immagine, la cartella e la preview dell'oggetto** (la risposta è la **funzione per arrivarci**). _Questo permette, ad esempio, di mandare alla scheda di interfacciamento con un documentale.
- Oggetti :  identifica l'oggetto corrispondente alla risorsa
- Risalita Immagini :  mostra la risalita effettuata per l'immagine visualizzata

In tale analisi è possibile capire immediatamente con quale script è gestita la risorsa, se con lo standard o personalizzato, e quale sezione dello script viene utilizzata per reperire le informazioni sull'oggetto.

I tab successivi consentono di editare gli script di configurazione (K09_STD e K09_PER, rispettivamente lo standard e il personalizzato), mentre nell'ultimo è possibile testare, per ogni oggetto, il funzionamento.

![K09_001](http://localhost:3000/immagini/LOBASE_12/K09_001.png)
## Script di configurazione
Esistono due script di configurazione, un default e uno per le personalizzazioni, nel file> SCP_SET sono presenti il membro> K09_STD e >K09_PER.
Lo script delle personalizzazioni è già fornito come esempio, con tag asteriscati, e se impostati i richiami di oggetti già presenti nel default questi vengono sostituiti.
In quest'ultimo script sono presenti commenti per capirne meglio la gestione ed il funzionamento.

_r_IMPORTANTE :  Non è consentito modificare lo script K09_STD. Per personalizzare usare solo il K09_PER.

La logica che sta dietro agli script è la seguente : 
1- Ogni sezione dello script definisce quali sono Immagine, Preview e Folder dell'oggetto, rispondendo alle domande "Come ci arrivo?", "Qual'è l'oggetto", "Qual'è la risalita delle immagini"

2- Se, dato un oggetto, non viene trovata la sezione corrispondente, si risale alla classe e dalla classe al default.
Ad esempio, chiedendo CN CLI, se non esiste la sezione CNCLI si risale a CN, se non esiste CN si risale ad **

3- E' possibile definire delle condizioni di selezione per la sezione. Ad esempio, i CN il cui codice inizia per "A".


## Strato
Ogni oggetto è posizionato in uno "Strato" : 

- OGGETTI FORNITI DA SMEUP - Strato STD
- OGGETTI DI QUESTA INSTALLAZIONE - Strato 001
- OGGETTI DI GRUPPO AZIENDE - Strato 002
- OGGETTI DI AZIENDA - Strato 003


## Cartelle e strati
A seconda dello strato dell'oggetto, le sue risorse vengono posizionate in cartelle diverse.

In SCP_CLO vengono definite le variabili IMG.003, IMG.002, IMG.001, mentre IMG.STD è cablata. Queste conterranno le immagini dei quattro strati
In SCP_CLO vengono definite le variabili PRW.003, PRW.002, PRW.001. Queste conterranno le preview dei tre strati
In SCP_CLO vengono definite le variabili FLR.003, FLR.002, FLR.001. Queste conterranno le immagini dei tre strati


## Come associare un'immagine
Dalla sezione INFO dell'oggetto, andare nella sezione dedicata all'immagine.
Nella scheda che si presenta è possibile vedere se vi è già un'immagine associata all'istanza o altrimenti se vi è la risalita sulla classe e quindi sarà presente un'immagine generica.
Per la gestione cliccare il bottone "avanzate".

![K09_002](http://localhost:3000/immagini/LOBASE_12/K09_002.png)
Nella scheda di gestione vi è una piccola guida per l'associazione l'immagine; il passaggio più semplice e veloce è quello posto in primo piano, nella sezione "Da clipboard".
Facendo "copia" su un'immagine (presa dal pc, dal web, ecc...)  e successivamente aggiornando la sezione "Da clipboard", l'immagine copiata apparirà nel riquadro. Successivamente basterà trascinare l'immagine da sinistra verso destra perchè sia associata all'oggetto su cui stiamo lavorando, come conferma verrà mostrato un messaggio informativo.
In alternativa è possibile scegliere l'immagine da una cartella ed associarla sempre trascianandola.

![K09_003](http://localhost:3000/immagini/LOBASE_12/K09_003.png)
La cancellazione di un'immagine associata all'istanza (e quindi non un'immagine legata alla classe) è possibile sempre dalla scheda di gestione, passando nella sottoscheda di destra "Verifica percorsi".
Dalla sezione "percorso salvataggio nuova immagine", fare tasto destro sul percorso e passare alla scheda.
Nella scheda che viene aperta, nella parte di gestione dal menu di sinistra, è presente il comando "elimina". Alla prossima riapertura del client l'immagine non sarà più visibile sull'oggetto.

![K09_004](http://localhost:3000/immagini/LOBASE_12/K09_004.png)
## Richiamo di Immagini, folder e preview da popup/scheda oggetto

Per alcuni oggetti è stato deciso, al fine di evidenziare l'esistenza della possibilità, il fatto di avere già predisposta in maniera immediata, il richiamo della  corrispondente cartella (anche se non è predisposto alcun percorso). Sono stati definiti in questo modo gli oggetti più rilevanti (es. articolo o contatto).

Per tutti gli altri oggetti (ma anche per i sopracitati) la cartella è sempre raggiungibile dalla voce "Info", ci trovi un tab dedicato. Ma se si valuta di voler avere l'azione immediata come gli oggetti sopracitati, normalmente dovresti predisporre un'apposita B£J (appartenente al gruppo B£H), ma in questo caso visto che la funzione è "standard" è stata predisposta la possibilità di attivare tale richiamo attraverso la compilazione della tabella B§K£O (elemento = tipo oggetto o tipo oggetto + parametro) nei campi "Richiamo Immagine", "Richiamo Preview", "Richiamo Cartella".

