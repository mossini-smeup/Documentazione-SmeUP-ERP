# Obiettivo
Definire l'accesso di un utente ad uno oggetto dagli ingressi principali, è un caso particolare di autorizzazioni per oggetto applicato ai modi di arrivare ad un oggetto.

Per ingressi master intendiamo : 
- Menù di Accesso (JATRE_01C/B£MENU)
- Menù Oggetto (LOA12)
- Popup dell'oggetto (JATRE_06C)
- Apertura diretta della scheda di un oggetto (JATRE_18C)
- Gestione oggetto (£G99)
- Surf/Fly oggetto (£G46)
- Risorse di un oggetto (£K09)

# Elementi Necessari
Per poter utilizzare le autorizzazioni Ingressi master occorre definire : 
- Tabella B£P :  classe di autorizzazione OGG.MAS
- V2AUTOG :  valori fissi su autorizzazioni
- Tabella B£SAZ :  defizione dei valori di autorizzazione ammessi (Elementi OG00, OG01, OG02, OG03, OG04, OG05) .
- Tabella B£2 :  flag per la nuova gestione azioni valorizzato con 1 (questo perché il controllo delle autorizzazioni di gestione è centralizzato nella £G99).

# Funzionamento
La classe di autorizzazione utilizzata è **OGG.MAS**, mentre la funzione indirizza all'oggetto tramite _Tipo;Parametro;Codice_ (corrispondente all'attributo G/21 dell'oggetto).
Questo tipo di autorizzazioni sfrutta delle risalite che vanno dalla più stringente alla più generale :  dove è presente un'autorizzazione sulla singola istanza prevarrà su quella della classe solo se è più restrittiva.
Es :  se non si è autorizzati a vedere i clienti, non è possibile abilitare un singolo codice cliente. Viceversa se si è autorizzati a vedere i clienti, è possibile disabilitare il singolo codice cliente.
Inoltre per la classe OGG.MAS su qualsiasi oggetto viene testata anche la classe USRLVL, confrontata con il livello operativo previsto per l'oggetto.
Se l'utente ha un livello operativo inferiore le autorizzazioni vengono forzate al minimo.

Per dettagli tecnici sul funzionamento si rimanda alla documentazione dell'api £AUO.
- [TST Copy autorizazioni](Sorgenti/MB/DOC_OGG/P_TSTAUO)

## Casi particolari
### Applicazioni e Moduli
In caso di autorizzazioni **ingresso master sui moduli**, ha precedenza l'autorizzazione associata all'applicazione a cui appartiene il modulo. Per cui, se autorizzo un'applicazione allora posso vedere tutti i moduli (a meno di autorizzazioni a livello di modulo). Viceversa, se disautorizzo un'applicazione nessun modulo della stessa sarà visibile, qualsiasi siano le autorizzazioni al modulo stesso.
### Schede diverse dalla scheda di oggetto
Su **scheda** è possibile specificare nel tag S.EXD.AUT il tipo di autorizzazione qualora l'oggetto master non sia nell'oggetto 1.
* Esempio S.EXD.AUT OgMasTp="CN" OgMasPa="CLI" OgMasCd="&OG.K1" dove OgMasTp è il Tipo Oggetto Master, OgMasPa è il Parametro Oggetto Master e OgMasCd è il Codice Oggetto Master.
* Inoltre è possibile specificare OgMasO1 che, se valorizzato ad 1, usa l'oggetto 1 ricevuto dalla scheda per controllare le autorizzazioni
### Tabelle
 **La gestione dati e la gestione allegati sono gestiti solo in caso di passaggio dalla £G99, per cui non sono usati negli elementi delle tabelle.

# Impostazione
I valori possibili da impostare sono : 
## Visibilità
Permette di definire il tipo di accesso all'oggetto. Le possibili scelte, definite nell'elemento OG00 della tabella B£SAZ, sono : 
- 99. Autorizzato :  permette il libero accesso all'oggetto
- 96. Selezionabile :  al momento ha lo stesso significato di Autorizzato.
- 93. Visibile/Non selezionabile :  l'oggetto è visibile, ma non è consentito l'accesso (ad esempio vedo l'icona del modulo, ma non è cliccabile).
- 91. Non autorizzato :  l'oggetto non è accessibile e l'opzione non è nemmeno visibile.

## Gestione dati
Permette di definire gli accessi ai dati e impatta sulle azioni disponibili all'utente. Le possibili scelte, definite nell'elemento OG01 della tabella B£SAZ, sono : 
- 89. Gestione Dati :  è possibile gestire i dati dell'oggetto selezionato.
- 85. Visibilità Dati :  i dati dell'oggetto selezionato sono visibili, ma non modificabili.
- 81. Dati Nascosti :  i dati dell'oggetto selezionato sono nascosti.

## Gestione Allegati
Permette di definire gli accessi ai dati, influenza per esempio la nuova gestione. Le possibili scelte, definite nell'elemento OG02 della tabella B£SAZ, sono : 
- 79. Gestione Note, Parametri, ecc :  è possibile gestire gli allegati dell'oggetto selezionato.
- 75. Visibilità Note, Parametri ecc :  gli allegati dell'oggetto selezionato sono visibili, ma non modificabili.
- 71. Note, Parametri, ecc. nascosti :  gli allegati dell'oggetto selezionato sono nascosti.

## Immagine
Permette di definire gli accessi all'immagine di un oggetto. Le possibili scelte, definite nell'elemento OG03 della tabella B£SAZ, sono : 
- 69. Immagine accessibile
- 61. Immagine non accessibile

## Preview
Permette di definire gli accessi alla preview di un oggetto. Le possibili scelte, definite nell'elemento OG04 della tabella B£SAZ, sono : 
- 59. Preview accessibile
- 51. Preview non accessibile

## Cartella
Permette di definire gli accessi alla preview di un oggetto. Le possibili scelte, definite nell'elemento OG05 della tabella B£SAZ, sono : 
- 49. Cartella accessibile
- 41. Cartella non accessibile

_3_Per le Risorse di un oggetto (Immagine, Preview e Cartella) si rimanda al documento : 
- [Immagini , Folder e Preview di un oggetto](Sorgenti/MB/DOC/LOBASE_12)


# Esempi di funzionamentoi

## Esempio 1

**Obiettivo**
Bloccare l'accesso ad una Applicazione/Modulo per un singolo utente.

Passo 1 : 
Apriamo la scheda **Ingressi Master**, accessibile dal menù del modulo B£AUTO.
Per prima cosa bisogna verificare che esista un elemento nel file AUTOOG0F con classe OGG.MAS, tipo oggetto **,  come attributo il  G/21 e funzione **.
La funzione ** indica che la funzione da abbinare alla classe OGG.MAS sarà il valore restituito dall'OAV (quindi la tripletta _Tipo;Parametro;Codice_ dell'oggetto che si vuole autorizzare).
Per farlo clicchiamo sulla voce di menù **OGG.MAS in AUTOOG0F**.

![B£AUTO19](http://localhost:3000/immagini/B£AUTO_09/BXAUTO19.png)
Passo 2 : 
Creiamo l'autorizzazione alla classe OGG.MAS, per un utente e come funzione inseriamo un codice di applicazione/modulo. Per fare questo occorre  cliccare sulla voce **Gestione classe OGG.MAS e specificare classe, utente, Tipo;Parametro : Codice. Questo è l'equivalente in scheda dell'UP AUT.
A questo punto nella matrice di aggiornamento è possibile modificare o inserire nuove autorizzazioni.

![B£AUTO20](http://localhost:3000/immagini/B£AUTO_09/BXAUTO20.png)
Nel primo valore occorre inserire la scelta per la visibilità, nel secondo quella per la gestione dati e nella terza per la gestione degli allegati.
Per prova inseriamo rispettivamente i valori 93, 81 e 71 per il modulo C5BASE.
Il risultato è che l'icona del modulo C5BASE è visibile ma non cliccabile. Non è  possibile accedere ai moduli di tale applicazione.
Come si può vedere nell'immagine seguente : 

![B£AUTO21](http://localhost:3000/immagini/B£AUTO_09/BXAUTO21.png)
Se il valore di visibilità viene modificato in 91, neanche l'icona del modulo sarà visibile e tentando di accedere direttamente alla scheda del modulo compare il messaggio "Non Autorizzato".

# Esempio 2

**Obiettivo**
Bloccare l'accesso ad un cliente per un singolo utente.

Passo 1
Apriamo la scheda **Ingressi Master**, accessibile dal menù del modulo B£AUTO.
Per prima cosa bisogna verificare che esista un elemento nel file AUTOOG0F con classe OGG.MAS, tipo oggetto **,  come attributo il  G/21 e funzione **.
La funzione ** indica che la funzione da abbinare alla classe OGG.MAS sarà il valore restituito dall'OAV (quindi la tripletta _Tipo;Parametro;Codice_ dell'oggetto che si vuole autorizzare).
Per farlo clicchiamo sulla voce di menù **OGG.MAS in AUTOOG0F**.

![B£AUTO19](http://localhost:3000/immagini/B£AUTO_09/BXAUTO19.png)
Passo 2
Creiamo l'autorizzazione alla classe OGG.MAS, per un utente e come funzione inseriamo un codice cliente
Nel primo valore occorre inserire la scelta per la visibilità, nel secondo quella per la gestione dati e nella terza per la gestione degli allegati.
Per prova inseriamo rispettivamente i valori 93, 85 e 75.
Tentando di accedere alla scheda cliente il risultato è il seguente : 

![B£AUTO22](http://localhost:3000/immagini/B£AUTO_09/BXAUTO22.png)
Passo 3
Ora rendiamo la scheda non visibile mettendo il valore 91 nel primo campo

![B£AUTO14](http://localhost:3000/immagini/B£AUTO_09/BXAUTO14.png)
Riprendiamo l'autorizzazione vista precedentemente e modifichiamola. Cambiamo il valore della visibilità da 93 a 91
In questo caso se si tenta di accedere alla scheda compare il messaggio "Non Autorizzato".



