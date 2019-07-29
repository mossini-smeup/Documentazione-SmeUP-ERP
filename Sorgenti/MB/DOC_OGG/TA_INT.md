# INT - Parametri interrogazione standard
## CONTENUTO DEI CAMPI
 :  : FLD T$ELEM Elemento
Il codice dell'elemento ha la seguente struttura :  _7_gnxx dove "g"  rappresenta il gruppo di appartenenza; "n"  ha valore 0 se il campo è alfanumerico e 1 se numerico; "xx" è un progressivo da 01 a 99.

 :  : PAR F(01) L(TAB)
- Schema|Gruppo
- da 1 a 5|A
- da 6 a 0|B
- da A a E|C
- da F a J|D
- da K a O|E
- da P a T|F



Esistono anche gli elementi TE_s, dove "s" è lo schema che contiene la descrizione dello schema e l'eventuale programma di aggiustamento
da eseguire.
 :  : FLD T$DESC Descrizione
È la descrizione dell'elemento.
**Descrizioni speciali** : 
_7_xCxTxP :  ritorna la descrizione di un oggetto.
- x  può essere * per specificare un codice o & per utilizzare un codice presente in un altro elemento della tabella, appartenente allo stesso gruppo.
- C  codice oggetto o numero dell'elemento che contiene il codice.
- T  tipo oggetto o numero dell'elemento che contiene il tipo.
Se il tipo viene derivato da un altro campo (usando quindi la &), e questo campo restituisce un codice più lungo di 2 byte, questo campo viene interpretato come Tipo+ Parametro.

In alcuni archivi infatti abbiamo il tipo e il parametro insieme in un unico campo lungo 12.
_9_Esempio :   &08&34 prende il cod. scritto nell'elem.08 e lo decodifica con il tipo scritto nell'elem 34. Se l'elem 34 restituisce (ad es.) CNCLI allora  nella decodifica il parametro usato è CLI.
- P  parametro oggetto o numero dell'elemento che contiene il parametro (facoltativo).
Il numero dell'elemento deve avere a 2 cifre e si riferisce sempre all'elemento alfanumerico.
_9_Esempi :  &01*AR ritorna la descrizione dell'articolo presente nell'elemento g001 (g è il gruppo). &05*CN&03 ritorna la descrizione dell'ente con parametro contenuto nell'elemento g003 e codice in g005.

_7_xCxTxP >oav :  ritorna il valore dell'OAV.
- oav è il nome dell'OAV da applicare all'oggetto specificato.
_9_Esempi :  &01*AR >I/10 ritorna la classe materiale dell'articolo contenuto nell'elemento g001.

_7_xCxTxP >>oav :  ritorna il significato dell'OAV (£OAVSI).
_9_Esempi :  &01*AR >>I/10 ritorna la descrizione della classe materiale dell'articolo contenuto nell'elemento g001.
 :  : FLD T$ITE2 __Titolo 2. Intestazioni campo__
Sono le intestazioni che vengono visualizzate/stampate.
 :  : FLD T$NPGM __Pgm da lanciare__
È l'eventuale programma utente di aggiustamento schiere che va specificato nell'elemento TE_s, dove s è lo schema di stampa.
Un esempio è il B£GI25X_XX. Il pgm viene richiamato prima del riempimento delle schiere con elementi dinamici (cioè contenenti OAV o altro).
 :  : FLD T$ICHG __Gruppo Autorizzazioni__
Se impostato può essere autorizzato con Classe Autorizzazione RIS- e funzione uguale all'ambiente dello schema di interrogazione. Valori validi x autorizzazione 1 a 9.
 :  : FLD T$ITAM __Condizionamento__
Per i campi numerici se vengono impostati i valori +/- continguamente all'indicazione di un attributo, tale attributo verrà applicato solo se il n° è positivo o negativo.
