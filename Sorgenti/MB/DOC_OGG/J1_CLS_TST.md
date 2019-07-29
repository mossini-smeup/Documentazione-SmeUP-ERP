# Classi di test
Le classi di test (oggetti J1 CLS_TST) sono piccole classi Java che eseguono un compito specifico

## Intenti

**1- Isolamento**
Lo unit test è quella parte del ciclo di vita del software che consiste nel testare separatamente le "unità"  (algoritmi, moduli, struttura dati, ecc..) che lo compongono.
Il vero intento delle classi di unit test, però, non è tanto quello di verificare la correttezza di un'unità, ma quello di supportarne l'implementazione :  in parole povere, la classe di test non viene creata solo dopo che il modulo software è stato terminato, ma durante lo sviluppo, già dalle prime fasi, per testarne i "pezzetti" man mano che si creano.

**2- Sviluppo in Looc.up**
Solitamente le classi di test si creano in un ambiente asettico, ma In Looc.up lo sviluppo è particolarmente complicato per via dei tanti vincoli e delle tante dipendenze, e per lo stesso motivo è difficile creare piccoli programmi di test senza avere a disposizione la connessione, l'ambiente, le librerie, le dll, il sistema operativo, il server di rete, e chi più ne ha più ne metta. L'unica soluzione è quella di lavorare direttamente IN LOOC.UP. Queste classi di test girano in Looc.up, quindi ci permettono di risparmiare tempo e di sbagliare meno.

**3-Testabilità**
Una volta che lo sviluppo dell'unità è stabilizzato, la classe di test rimane utile per i test di regressione. Il renderli oggetti e il FUNizzarne la chiamata ci permette di creare dei flussi di test.

**4- Collaborazione**
Tutti quelli che lavorano su un modulo software, in uno qualunque degli strati, possono usare le classi di test

## Caratteristiche generali delle classi di test

**Piccole e isolate** :  devono essere tante e assolvere a compiti elementari (generare un file, controllare un xml, listare una directory, costruire una struttura dati in memoria, fare 1000 chiamate consecutive a un servizio, ecc..))
**Sempre disponibili** :  non devono essere legate all'utente, all'ambiente, all'as400, ma solo a Loocup.jar
**Input e output controllati**
**Sottoingegnerizzate**

## Utilizzo da Looc.up

### Scheda
1- Potete accedere alla scheda della classe di test usando la selezione oggetto (F4 -> J1 - CLS_TST - F4 (Elenco delle classi +di test registrate).)
Scelto l'oggetto, nella scheda c'è la documentazione di tutte le classi di test e un bottone per eseguire la classe scelta
La scheda è migliorabile secondo le nostre esigenze

### Servizio
Il servizio che esegue le classi di test è il JA_00_99 funzione TST.CLS. La fun riceve come parametro 1 l'oggetto CLS da lanciare. Al momento l'output del servizio è un messaggio. Anche qui, possiamo migliorare, aggiungere metodi al servizio, o arricchendo la sintassi della fun, ma senza cadere nella sovraingegnerizzazione

### Menù
Nel menù sviluppatore c'è un item che chiama la suddetta fun, passando nel codice dell'oggetto 1 il -, determinando quindi la richiesta di quale classe eseguire. La fun è : 

**F(INT;JA_00_99;CLS.TST) 1(J1;CLS_TST;-)**


## CREAZIONE (solo per sviluppatori Java)

### 1-Creare la classe
Una classe di test è una classe che implementa l'interfaccia **UnitTest**

 :  : PAR F(01) L(MON)
public interface UnitTest {
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;public void execute(UnitTestContext context, UnitTestResult result);
}


L'unico metodo da implementare è il metodo **execute()**, che viene chiamato dal servizio che esegue le classi.
Il metodo riceve due parametri : 
 **UnitTestContext** :  contiene le infomazioni di contesto in cui gira la classe, ad esempio la FUN che l'ha chiamata, la Mainguiframe, i parametri della classe (vedi paragrafo successivo)
 **UnitTestResult** :  è la struttura dati in cui vengono salvate le informazioni raccolte dal test, i suoi risultati, tra cui un output di messaggi, il risultato booleano, un xml generico che viene ritornato come output del servizio JA_00_99

Ad esempio, si potrebbe creare una classe
 :  : PAR F(01) L(MON)
public class TestaDomenica implements UnitTest {

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;public void execute(UnitTestContext context, UnitTestResult result) {

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; result.println(_r_"Inizio il test");
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Calendar oggi=Calendar.getInstance();
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; result.println(_r_"Oggi è " + oggi);

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; if (oggi.get(Calendar.DAY_OF_WEEK)!=Calendar.SUNDAY)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;result.setResult(false);
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;else
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;result.setResult(true);
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; >//creo un albero con la data di oggi
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; result.setXML(new UITreeXmlObject(new SmeupOpbect(_r_"D8",_r_"Y*MD",oggi)).toXml());
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;}
}

L'oggetto **UnitTestResult**, dopo l'esecuzione, sarà preso in carico dal servizio, che, a seconda del metodo di chiamata, visualizzarà un messaggio con il risultato dei **"println()"**, oppure visualizzarà l'albero, oppure registrerà il risultato **True** o **False** in una matrice che raggolga tutti i test eseguiti

 :  : PAR F(03)
Le classi possono essere create in qualunque package. Crearle nel package **Smeup.smeui.uiunittest.tests** permette di mantenere ordine; crearle nello stesso package della classe da testare permette di referenziare anche metodi con visibilità "package" e non solo quelli "public",


### 2-Registrare la classe
Per permettere a Looc.up di reperire le classi di test, identificarle ed elencarle, si è pensato di registrarele in un file di properties incluso nel jar di Looc.up. Questo svincola le classi dall'ambiente e dall'as400 e velocizza la creazione.
Il file di properites è Smeup/smeui/uiunittest/testClasses.properties
Ecco una parte del contenuto

 :  : PAR F(01) L(MON)
-------------------------------
**BAS_GRD.CODE**=BAS_GRD
**BAS_GRD.CLASS**=Smeup.smeui.uidatastructure.uigridxml.UIGridXmlObjectAddictTest
**BAS_GRD.DESC**=Classe di test per le colonne aggiuntive in Java

**BAS_TMN.CODE**=BAS_TMN
**BAS_TMN.CLASS**=Smeup.smeui.uiunittest.tests.UnitTestManagerTest
**BAS_TMN.DESC**=Test del gestore delle classi di test
-------------------------------

Per ogni classe vengono definiti
- Codice :  codice dell'oggetto J1 CLS_TST
- Classe :   classe Java
- Descrizione  :  decodifica dell'oggetto
_Come si nota dall'esempio, il codice viente utilizzato per identificare il blocco di proprietà_

### 3-Definire il setup
Se (e solo se) si vuole creare una classe interattiva, che permetta all'utente di definire dei parametri di input, è possibile creare un configuratore.
Lo script di configurazione è
 :  : DEC T(MB) P(SCP_CFG) K(CLS_TST) D(MB/SCP_CFG/CLS_TST)
La sezione di parametri definiti per una classe è identificata dal tag che porta il codice della classe stessa.
_7_Quando la classe viene eseguita in modalità interattiva, se esiste una configurazione, questa viene invocata, e le risposte passate alla classe. 

_r_Quando invece la classe è eseguira in modalità batch, non viene richiamato nessun configuratore, e i parametri rimangono vuoti.

## Esempi (per tutti gli svilupppatori)
Nella scheda di ogni classe è possibile creare una sottoscheda di esempi, che non sono necessariamente legati all'esecuzione della classe di test, ma al suo contesto di lavoro.
Ad esempio, la gli esempi legati alla __classe di test del generatore di barcode__ sono delle sezioni che contengono tanti barcode e che permettono di creare nuovi barcode. Queste sezioni ma non usano direttamente la classe di test, besì generatore di barcode di qui la classe è un test. Se un barcode non viene visualizzato, si può lanciare la classe di test con quel determinato barcode, e isolare l'errore.


# Classi registrate

## BAS_GRD Classe di test per le colonne aggiuntive in Java
Questa classe esegue la classe di "esplosione" delle colonne aggiuntive di una matrice a partire da una fun o da un file XML matrice. L'output è in forma di messaggi.

## BAS_IMC Classe di test per la generazione di immagini calcolate
Questa classe testa la classe di generazione delle immagini "calcolate" (J1FUN, J4BRC, J1COL)

## BAS_TMN Test del gestore delle classi di test
Questa classe controlla il corretto funzionamento del gestore delle classi di test, che legge il file in cui sono registrate le classi di test

## BAS_VAR Test del risolutore di variabili
Questa classe testa la risoluzione delle variabili

## CUB_DS4 Classe di test per la generazione del DS4
Questa classe esegue il generatore del ds4 (file di databeacon) a partire da una fun o da un file XML matrice. L'output è in forma di messaggi.

## HIE_HIE Test della costruzione delle colonne aggiuntive
Questa classe richiama il gestore delle colonne aggiuntive e crea un albero

## IMD_TS1 Classe di test per la generazione del IMD
Questa classe testa la creazione delle immagini dimaniche (composite)

## SPC_XML Test della lettura dell'XML per modulo SPC
Questa classe, data una fun o un XML, richiama il modulo SPC e

## DBM_SEP Test dell'algoritmo di guess del sepatatore in un CSV
Dato un separatore atteso e un testo con separatore, controlla se il separatore trovato nel testo è uguale a quello attesto








