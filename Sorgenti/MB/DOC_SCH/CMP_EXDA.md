 :  : TAG Id="DED_01" Txt="Drag & Drop da Albero"
### Drag & Drop da Albero
In presenza di un albero si può effettuare il drag & drop selezionando uno o più elementi
da una sezione di partenza (la seleziona multipla si effettua
tramite CTRL+clic sui singoli elementi), trascinandoli e rilasciandoli nella sezione di arrivo.
Nel setup della sezione di partenza è necessario specificare l'abilitazione al drag (Drag = 'Yes'
per il drag singolo e Drag='Multi' per il drag multiplo) e nel dinamismo occorre specificare
l'azione da eseguire al momento del drop.

Nell'esempio è possibile provare l'utilizzo del Drag & Drop da Albero : 
selezionando uno o più elementi dall'albero nella parte sinistra dello schermo, si possono
trascinare nella parte destra; al momento del rilascio gli elementi saranno accodati a quelli già
presenti nell'albero a destra, oppure andranno a crearlo nel caso non esista.
Gli elementi già presenti non verranno ripetuti.


 :  : TAG Id="DED_02" Txt="Drag & Drop da Matrice"
### Drag & Drop da Matrice
In presenza di una matrice si può effettuare il drag & drop selezionando uno o più elementi
da una sezione di partenza (la seleziona multipla si effettua tramite il CTRL+Clic sulle singole
RIGHE della matrice, non funziona se si selezionano le singole celle),
trascinandoli e rilasciandoli nella sezione di arrivo.
Nel setup della sezione di partenza è necessario specificare l'abilitazione al drag (Drag = 'Yes')
e nel dinamismo occorre specificare l'azione da eseguire al momento del drop.

Nell'esempio è possibile provare l'utilizzo del Drag & Drop da matrice : 
selezionando una o più righe dalla matrice nella parte sinistra dello schermo, si possono
trascinare nella parte destra; per selezionare più righe occorre cliccare sulla parte grigia alla
sinistra della matrice dove è presente la freccia che indica la riga evidenziata.
Al momento del rilascio gli elementi saranno accodati a quelli già presenti
nella matrice a destra, oppure andranno a crearla se non esiste.
Gli elementi già presenti non verranno ripetuti.


 :  : TAG Id="INC" Txt="I.INC.VAM"
### Include di variabili MDE
Nelle schede è possibile includere le variabili contenute in una memorizzazione estesa passandole
come parametri di input attraverso il seguente TAG
S.VAR.MDE Str="Struttura" Con="Contesto" Ute="Utente" Nam="Nome"
In questo modo tutte le variabili sono richiamabili attraverso la forma &IN.nome_variabile.

Nell'esempio, cliccando su una qualsiasi memorizzazione all'interno della matrice verranno
visualizzati nella parte inferiore dello schermo gli attributi valorizzati, a destra, e il contenuto
dei parametri passati dall'include, a sinistra.

 :  : TAG Id="VAM" Txt="S.VAR.MDE"
### Variabili MDE
Nelle schede è possibile includere le variabili contenute in una memorizzazione estesa passando
S.VAR.MDE Str="Struttura" Con="Contesto" Ute="Utente" Nam="Nome"
Le variabili sono disponibili sia singolarmente, che in un unica variabile, chiamata MDE_VAR,
che le contiene tutte.
In questo modo tutte le variabili sono richiamabili attraverso la forma [nome_variabile].

Nell'esempio, cliccando su una qualsiasi memorizzazione all'interno della matrice verranno
visualizzati nella parte inferiore dello schermo gli attributi valorizzati, a destra, e il contenuto
della variabile MDE_VAR, a sinistra.

 :  : TAG Id="VAS" Txt="I.INC.VAS"
### Include di variabili da servizio
Nelle schede è possibile includere le variabili restituite da un programma passando
I.INC.VAS Pgm(Programma) Fun(Funzione) Met(Metodo) Par(Parametro) Ent(Entry di servizio)
Le variabili sono disponibili sia singolarmente, che in un unica variabile, chiamata SER_VAR,
che le contiene tutte.
In questo modo tutte le variabili sono richiamabili attraverso la forma &IN.nome_variabile.

Nell'esempio, è possibile scegliere tra due esempi : 
* A :  Sono utilizzabili le variabili A=Pippo, B=Pluto, C=XXX e la variabile SER_VAR che è composta da entrambe.
* B :  Sono utilizzabili le variabili A=Topolino e B=Paperoga, e la variabile SER_VAR che è composta da entrambe.

Nella parte inferiore dello schermo è visibile il contenuto della variabile SER_VAR.


 :  : TAG Id="SER" Txt="S.VAR.SER"
### Variabili SER
Nelle schede è possibile includere le variabili restituite da un programma passando
S.VAR.SER Pgm="Programma" Fun="Funzione" Met="Metodo" Par="Parametro" Ent="Entry di servizio"
Le variabili sono disponibili sia singolarmente, che in un unica variabile, chiamata SER_VAR,
che le contiene tutte.
In questo modo tutte le variabili sono richiamabili attraverso la forma [nome_variabile].

Nell'esempio, è possibile scegliere tra due esempi : 
* A :  Sono utilizzabili le variabili A=Pippo, B=Pluto, C=XXX e la variabile SER_VAR che è composta da entrambe.
* B :  Sono utilizzabili le variabili A=Topolino e B=Paperoga, e la variabile SER_VAR che è composta da entrambe.

Nella parte inferiore dello schermo sono visibili tutte e 4 le possibili variabili.
