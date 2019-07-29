# GMY - Metodi valorizzaz. inventari
## CONTENUTO DEI CAMPI
 :  : FLD T$ELEM Elemento
È il codice dell'elemento.
Deve essere costruito secondo delle regole ben precise che permettano, così, una risalita nella determinazione del costo : 
AREA/TIPO/OAV
AREA/TIPO
AREA
**
"AREA" è l'area giacenza che sta leggendo.
"TIPO" è il tipo giacenza che sta leggendo.
"OAV" è l'oav dell'articolo che sta leggendo, l'attributo si trova nella tabella GMW.
"**" è l'elemento ultimo di risalita.
_9_Esempio : 
Si sta analizzando il record delle giacenze/Foto con le seguenti caratteristiche : 
Area giacenza GM;
Tipo giacenza AR;
Attributo articolo classe materiale con valore A.
Verrà eseguita la seguente risalita : 
Elemento :  GMARA
GMAR
GM
**
Il primo trovato sarà il metodo utilizzato nella valorizzazione.
 :  : FLD T$DESC Descrizione
È la descrizione dell'elemento.
 :  : FLD T$GMYA __Metodo Valorizzazione/Programma__
Contiene il metodo di valorizzazione (suffisso del programma GMFO_xxx).
Attivando la ricerca, si possono selezionare dei programmi standard già previsti da SMEUP. Attualmente è previsto il PGM con suffisso 01.
 :  : FLD T$GMYB __Parametri del metodo__
Contiene una serie di parametri definibili dal programma di controllo della tabella, che permettono modalità diverse di valorizzazione per lo stesso metodo.
Per 01 (*BASE) sono stati implementati i seguenti campi : 
_B_Posizioni 1 - 3  :  Forzatura tipo costo.
Se presente, è il tipo costo utilizzato nella valorizzazione, indipendentemente, da quello eventualmente scelto in precedenza.
_B_Posizione 4   :  Escludere.
Non viene eseguita la valorizzazione, pur essendo stata precedentemente richiesta.
_B_Posizione 5  :  Variare il valore.
Permette di Incrementare o Decrementare (impostando 'I' oppure 'D' ) in percentuale un valore definito nel campo successivo.
_B_Posizioni 6 - 10  :  Percenuale di variazione (es :  per 12,5 % si imposta 1250).
Valore di incremento o decremento in percentuale
