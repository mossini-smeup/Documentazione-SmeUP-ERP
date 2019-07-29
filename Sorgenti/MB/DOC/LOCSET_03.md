# L'Utilizzo dei setup da parte dello sviluppatore
Vengono qui di seguito descritte le possibilità a disposizione dello sviluppatore per l'utilizzo dei setup.

# Le risalite
Prima di descrivere i punti in cui lo sviluppatore può fissare lo specifico setup da applicare ad una particolare funzione applicativa, vengono qui descritti i livelli di risalita attraverso cui vengono determinati i valori del setup. E' importante infatti notare che i valori dei setup non sono sempre indicati in modo esplicito.


- **Dal default del client**. Se non viene specificato nulla, il client recupera i suoi valori default ed applica quelli. Il valore di default è indicato nell'help del campo.


![LOCSET_02](http://localhost:3000/immagini/LOCSET_03/LOCSET_02.png)

- **Dalla configurazione del client**. Questo livello vale solo per i setup di excel (**SET.EXC**). Cliccando il tasto destro sull'icona verde, in alto nella finestra del client, è possibile gestire una configurazione di carattere generale del client. All'interno di questo c'è una voce "Esportazione", attraverso cui possono essere forzati dei default.


![LOCSET_03](http://localhost:3000/immagini/LOCSET_03/LOCSET_03.png)
![LOCSET_04](http://localhost:3000/immagini/LOCSET_03/LOCSET_04.png)
![LOCSET_05](http://localhost:3000/immagini/LOCSET_03/LOCSET_05.png)

- **Da setup della funzione**. Il setup della funzione può essere reperito in vari modi e a disposizione dell'utente possono anche essere disponibili più configurazioni del medesimo setup per la stessa funzione. In presenza di setup multipli il setup attivo è comunque sempre uno solo, quello selezionato in quel momento dall'utente. I setup di funzione possono essere definiti alternativamente : 
-- Da scheda (cioè da uno script SCP_SCH), se il corrispondente componente può essere emesso in una sezione di scheda (es. il setup di una matrice può essere indicato in questo modo, il setup di un report no).
-- Da servizio :  nel servizio che compone l'xml dei dati della funzione è possibile accodare anche l'xml del/dei setup che si vogliono applicare a tale funzione.
- **Dall'attributo Parent**. Fra gli attributi dei setup che vengono fissati in scheda o da servizio, è normalmente previsto un particolare campo chiamato "Parent" :  in questo attributo può essere specificato un oggetto **J3**, attraverso cui lo standard fornisce alcuni modelli pre-configurati di setup. Quando si usa questo campo (utilizzo che viene consigliato) tutti i valori indicati nel modello verranno ereditati dal setup specifico, con la possibilità in quest'ultimo di poterli comunque sovrascrivere. E' quindi possibile indicare un modello per riprenderne la configurazione e specificare poi in esplicito i soli campi che si ha interesse di indicare in modo specifico. I modelli sono catalogati nello script della scheda **SCP_SCH/J3_SET_STD**.


![LOCSET_06](http://localhost:3000/immagini/LOCSET_03/LOCSET_06.png)
![LOCSET_07](http://localhost:3000/immagini/LOCSET_03/LOCSET_07.png)

- **Da setup utente**. Va infine considerato che a disposizione dell'utente viene fornita la possibilità di manipolare i setup della funzione personalizzandoli interattivamente e creando quello che viene definito "setup utente". Quando questo avviene, ai setup forniti da scheda/servizio, si affiancano anche questi setup utente che sono selezionabili come setup da applicare alla funzione.


# Le risalite dei compenenti di output (FRM.REP/FRM.G53/SET.EXC)
Per i setup del componente REP, G53 ed EXC, in aggiunta a quanto esplicitato in precedenza esiste un'elaborazione di ricostruzione aggiuntiva. Reperito il setup di funzione viene infatti applicata una risalita a pettine, per ogni attributo di setup per i seguenti livelli : 

* Default del setup per **/**/** (cioè per qualsiasi utente, su qualsiasi contesto, su qualsiasi setup)
* Default del setup per gruppo utente/**/** (cioè per quel gruppo utente, su qualsiasi contesto, su qualsiasi setup)
* Default del setup per utente/**/** (cioè per quel gruppo utente, su qualsiasi contesto, su qualsiasi setup)
* Default del setup per **/contesto/** (cioè per qualsiasi utente, sul contesto, su qualsiasi setup)
* Default del setup per gruppo utente/contesto/** (cioè per quel gruppo utente, sul contesto, su qualsiasi setup)
* Default del setup per gruppo utente/contesto/setupname (cioè per quel gruppo utente, sul contesto, sul nome del setup di funzione)
* Default del setup per utente/contesto/** (cioè per quel gruppo utente, sul contesto, su qualsiasiasi setup)
* Default del setup per utente/contesto/setupname (cioè per quel gruppo utente, sul contesto, sul nome del setup di funzione)
* Eventuale Override da LDA (viene cercata nella G00 la memoria con codice OVS.codicesetup). Questa funzionalità è normalmente utilizzata solo nella struttura dei flussi.

Per la citata risalita a pettine si intende che vengono elaborati i livelli sopracitati e per ogni livello vengono trattenuti i soli valori riempiti. Es. Se a livello di **/**/** vengono definiti gli attributi a e b, mentre a livello di gruppo utente/**/** viene definito solo l'attributo b, alla fine il setup finale sarà composto dall'attributo a reperito dal livello **/**/** e dall'attributo b reperito dal livello gruppo utente/**/**.

Con i termini contesto/setupname, si intendono invece : 
* Contesto :  il Context della funzione. Questa informazione può essere fissata dal servizio attraverso il Setup Program nell'attributo "Context", oppure viene calcolata dal cliente nel seguente modo :  nomescheda/idsezione(o titolo sezione se per la sezione non è stato indicato un codice ID) tagliato a 15 caratteri massimo. Questa informazione può essere comunque reperita tutte le volte che si accede alla gestione dei setup di una particolare funzione.
* Setupname :  è il nome del setup della funzione, viene reperito dall'attributo "Name" del setup. Se tale attributo è assente dal setup viene assunto blank. Questo vale solo per i setup da programma.

I sopracitati setup possono essere gestiti/inseriti da due particolari punti : 
* Dalla scheda del modulo LOCSET, indicando manualmente le chiavi che vogliono essere inserite
* Dalla finestra di elaborazione della particolare esportazione, attraverso la voce gestione setup

![LOCSET_01](http://localhost:3000/immagini/LOCSET_03/LOCSET_01.png)
**NOTA BENE :  Eccezione per SET.EXC**

Per l'excel sussiste un'eccezione tale per cui il setup nativo dell'esportazione è di tipo GRA_EXC; mentre le risalite avvengono tramite il setup SET.EXC. Per questo nella gestione dei setup vengono riportate entrambe. Quando voglio riprendere al momento un particolare setup posso utilizzare il GRA_EXC, mentre se voglio impostare una risalita va utilizzato il SET.EXC.

![LOCSET_08](http://localhost:3000/immagini/LOCSET_03/LOCSET_08.png)


