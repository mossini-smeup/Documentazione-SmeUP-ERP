 :  : HEA PRIV(001)

Architettura di Show.Up

Show.Up è diviso in tre parti :  componente Smeup di Joomla!, un web service e Sme.Up(fig. 1).

Joomla! è il noto CMS opensource scritto in php (ver. 2.5).
La documentazione di Joomla! è consultabile sul sito "www.joomla.org".
Il componente Sme.Up è una estensione di Joomla!.

Il web service è un modulo software (war) scritto in java.

COMPONENTE SMEUP DI JOOMLA

È una estensione di Joomla! di tipo componente (secondo la terminologia di Joomla!).
Utilizza le API messe a disposizione dal CMS.
Durante lo sviluppo si è tenuto conto dei pattern e delle convenzioni consigliate dal framework
applicativo messo a disposizione dal CMS.

Inoltre sono state inserite due librerie :  smea e smeup.
La prima delle due è stata ereditata da un precedente sviluppo (vedi sito di Banco Prova Armi).
La seconda che a tendere dovrà includere tutte le funzionalità della prima è stata sviluppata
specificatamente per Show.Up.
Le responsabilità di questa libreria sono : 
1) inviare le richieste (fun) al web service e parserizzare le risposte;
2) scrivere gli xml per il framework grafico javascript chiamato dhtmlx
3) risolvere le variabilie presenti nelle fun
4) interpretare gli eventi che arrivano dall'interfaccia utente e collegarli alle sezioni
grafiche e quindi ai rispettivi componenti grafici (albero, matrice form ecc.).

La libreria smea contiene i file javascript di dhtmlx e le funzionalità php di calcolo dei file javscript da
includere nelle pagine html.

WEB SERVICE
Il web service si occupa di comunicare con il gestionale Sme.Up tramite fun e di restituire a sui client
risposte in formato json o xml.
Il web service è di tipo REST.
Il paccheto war contiene al suo interno oltre ad alcune libreria (jar) dell'Apache Software Foundation
delle librerie sviluppate da Smea per precedenti progetti web : 
Servizi Loocup, Visualizzazione delle fun in excel, Agenda, web service di tipo SOAP per Agricar e altri.

In particolare ci sono : 

ConnectionPool.jar :  gestione delle connessioni verso smeup come pool di risorse
FUN2JavaConversion.jar :  funzionalità di conversione delle risposte XML di smeup in classi java
LoocupConnector2.jar :  implementazione delle connessione verso Sme.Up secondo le tipiche convezioni usate dai driver jdbc
SmeupConn.jar :  implementazione vera e propria a basso livello delle comunicazine con Sme.Up attraverso le code dati e una program call.
SmeupModel.jar :  classi di modello generiche come albero, matrice.

Utilizza inoltre la jersey per l'implementazione di REST.

Il pacchetto war si installa come una qualsiasi applicazione web che rispetta gli standard JEE 6.

Esempio di utilizzo : 

Chiamata : 

http://<serverName>/<contextName>/rest/openSmeup/xml?fun=F(EXB;B£SER_01;CON.PRO) 1(;;) 2(;;) INPUT()

Risposta : 

<?xml version="1.0" encoding="ISO-8859-1"?>
<UiSmeup Testo="  - "> <Service Titolo1="" Titolo2=" " Funzione="F(EXB;B£SER_01;CON.PRO) 1(;;) 2(;;) INPUT()" Servizio="B£SER_01" TSep="." DSep=","/>
<Griglia>
<Colonna Cod="CON000" Txt="Gruppo" Tip="" Lun="99" IO="O" Ogg="" Dpy="" Fill="" Aut=""/>
<Colonna Cod="CON001" Txt="Proprietà" Tip="" Lun="99" IO="O" Ogg="" Dpy="" Fill="" Aut=""/>
<Colonna Cod="CONTIP" Txt="Tipo" Tip="" Lun="20" IO="O" Ogg="OG" Dpy="" Fill="" Aut=""/>
<Colonna Cod="CONVAL" Txt="Valore" Tip="" Lun="99" IO="O" Ogg="[CONTIP]" Dpy="" Fill="" Aut=""/>
<Colonna Cod="CONDES" Txt="Descrizione" Tip="" Lun="99" IO="O" Ogg="[CONTIP]|[CONVAL]" Dpy="" Fill="" Aut=""/>
</Griglia>
<Righe>
<Riga Fld="Ambiente|Utente|UP|X1IMVI|Impresa virtuale"/>
<Riga Fld="Ambiente|Ingresso|IUX1IMVI|0100|X1IMVI    Impresa Virtuale"/>
<Riga Fld="Ambiente|Ambiente|TAB£B|X1IMVI|Smea S.r.l. - Impresa Virtuale"/>
<Riga Fld="Ambiente|Azienda|AZ|01|SMEA s.r.l"/>
<Riga Fld="Ambiente|Magazzino|TAMAG|1|Sede SMEA"/>
<Riga Fld="Ambiente|Esercizio|TAPER01||"/>
<Riga Fld="Ambiente|Data utente|D8*YYMD|20120223|Giovedì 23 Febbraio 2012 / Set 08"/>
<Riga Fld="Ambiente|Lingua|TAV§L||"/>
<Riga Fld="Sessione|Numero|  |584077|"/>
<Riga Fld="Sessione|Tipo lavoro|  |B|"/>
<Riga Fld="Server|Indirizzo IP|INIP|172.16.2.55|"/>
<Riga Fld="Sme.up|Rilascio|  |V3R2|"/>
<Riga Fld="Sme.up|Versione|  |22/02/12|"/>
<Riga Fld="Server|Nome|  |SRVAMM|"/>
<Riga Fld="Server|Tipo/Modello|  |9407M155633|"/>
<Riga Fld="Server|Numero di serie|  |65-08394|"/>
<Riga Fld="Server|Sistema operativo|  |V6R1M0|"/>
<Riga Fld="LOOC.up|Componenti JAVA|  ||"/>
<Riga Fld="LOOC.up|Componenti DELPHI|  ||"/>
<Riga Fld="LOOC.up|Emulatore|  ||"/>
<Riga Fld="LOOC.up|Versione JAVA|  ||"/>
<Riga Fld="LOOC.up|Versione SO Client|  ||"/>
</Righe>
</UiSmeup>

Oppure per avere la stessa risposta in formato JSON con una struttura dati "matriciale" : 

http://<serverName>/<contextName>/rest/openSmeup/table/json?fun=F(EXB;B%C2%A3SER_01;CON.PRO)%201(;;)%202(;;)%20INPUT()
Si noti la parte /table/json che ha sostituito /xml

{
  "r"  :  [ {
    "v"  :  [ ";;Ambiente", ";;Utente", "OG;;UP", "UP;;X1IMVI", "UP;|X1IMVI;Impresa virtuale" ]
  }, {
    "v"  :  [ ";;Ambiente", ";;Ingresso", "OG;;IUX1IMVI", "IU;X1IMVI;0100", "IU;X1IMVI|0100;X1IMVI    Impresa Virtuale" ]
  }, {
    "v"  :  [ ";;Ambiente", ";;Ambiente", "OG;;TAB£B", "TA;B£B;X1IMVI", "TA;B£B|X1IMVI;Smea S.r.l. - Impresa Virtuale" ]
  }, {
    "v"  :  [ ";;Ambiente", ";;Azienda", "OG;;AZ", "AZ;;01", "AZ;|01;SMEA s.r.l" ]
  }, {
    "v"  :  [ ";;Ambiente", ";;Magazzino", "OG;;TAMAG", "TA;MAG;1", "TA;MAG|1;Sede SMEA" ]
  }, {
    "v"  :  [ ";;Ambiente", ";;Esercizio", "OG;;TAPER01", "TA;PER01;", "TA;PER01|;" ]
  }, {
    "v"  :  [ ";;Ambiente", ";;Data utente", "OG;;D8*YYMD", "D8;*YYMD;20120223", "D8;*YYMD|20120223;Giovedì 23 Febbraio 2012 / Set 08" ]
  }, {
    "v"  :  [ ";;Ambiente", ";;Lingua", "OG;;TAV§L", "TA;V§L;", "TA;V§L|;" ]
  }, {
    "v"  :  [ ";;Sessione", ";;Numero", "OG;;  ", "  ;;584077", "  ;|584077;" ]
  }, {
    "v"  :  [ ";;Sessione", ";;Tipo lavoro", "OG;;  ", "  ;;B", "  ;|B;" ]
  }, {
    "v"  :  [ ";;Server", ";;Indirizzo IP", "OG;;INIP", "IN;IP;172.16.2.55", "IN;IP|172.16.2.55;" ]
  }, {
    "v"  :  [ ";;Sme.up", ";;Rilascio", "OG;;  ", "  ;;V3R2", "  ;|V3R2;" ]
  }, {
    "v"  :  [ ";;Sme.up", ";;Versione", "OG;;  ", "  ;;22/02/12", "  ;|22/02/12;" ]
  }, {
    "v"  :  [ ";;Server", ";;Nome", "OG;;  ", "  ;;SRVAMM", "  ;|SRVAMM;" ]
  }, {
    "v"  :  [ ";;Server", ";;Tipo/Modello", "OG;;  ", "  ;;9407M155633", "  ;|9407M155633;" ]
  }, {
    "v"  :  [ ";;Server", ";;Numero di serie", "OG;;  ", "  ;;65-08394", "  ;|65-08394;" ]
  }, {
    "v"  :  [ ";;Server", ";;Sistema operativo", "OG;;  ", "  ;;V6R1M0", "  ;|V6R1M0;" ]
  }, {
    "v"  :  [ ";;LOOC.up", ";;Componenti JAVA", "OG;;  ", "  ;;", "  ;|;" ]
  }, {
    "v"  :  [ ";;LOOC.up", ";;Componenti DELPHI", "OG;;  ", "  ;;", "  ;|;" ]
  }, {
    "v"  :  [ ";;LOOC.up", ";;Emulatore", "OG;;  ", "  ;;", "  ;|;" ]
  }, {
    "v"  :  [ ";;LOOC.up", ";;Versione JAVA", "OG;;  ", "  ;;", "  ;|;" ]
  }, {
    "v"  :  [ ";;LOOC.up", ";;Versione SO Client", "OG;;  ", "  ;;", "  ;|;" ]
  } ],
  "c"  :  [ {
    "aut"  :  "",
    "code"  :  "CON000",
    "dpy"  :  "",
    "fill"  :  "",
    "IO"  :  "O",
    "ogg"  :  "",
    "text"  :  "Gruppo",
    "tip"  :  ""
  }, {
    "aut"  :  "",
    "code"  :  "CON001",
    "dpy"  :  "",
    "fill"  :  "",
    "IO"  :  "O",
    "ogg"  :  "",
    "text"  :  "Proprietà",
    "tip"  :  ""
  }, {
    "aut"  :  "",
    "code"  :  "CONTIP",
    "dpy"  :  "",
    "fill"  :  "",
    "IO"  :  "O",
    "ogg"  :  "OG",
    "text"  :  "Tipo",
    "tip"  :  ""
  }, {
    "aut"  :  "",
    "code"  :  "CONVAL",
    "dpy"  :  "",
    "fill"  :  "",
    "IO"  :  "O",
    "ogg"  :  "[CONTIP]",
    "text"  :  "Valore",
    "tip"  :  ""
  }, {
    "aut"  :  "",
    "code"  :  "CONDES",
    "dpy"  :  "",
    "fill"  :  "",
    "IO"  :  "O",
    "ogg"  :  "[CONTIP]|[CONVAL]",
    "text"  :  "Descrizione",
    "tip"  :  ""
  } ]
}











