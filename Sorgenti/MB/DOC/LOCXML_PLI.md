<?xml version="1.0" encoding="UTF-8"?>
<PLIST>
<UiSmeup>
<Attributi>
<Testo Contenuto="Alfanumerico" Scopo="Contenuto del titolo visualizzato in rosso nella barra oggetti" Obbligatorio="SI"/>
</Attributi>
</UiSmeup>
<Configurazione>
<Attributi>
<Default Contenuto="1" Scopo="" Obbligatorio="SI"/>
<Type Contenuto="1" Scopo="" Obbligatorio="SI"/>
</Attributi>
</Configurazione>
<Modulo>
<Attributi>
<Tipo Contenuto="Alfanumerico" Scopo="TIPO per chiave identificativa del modulo" Obbligatorio="SI"/>
<Parametro Contenuto="Alfanumerico" Scopo="PARAMETRO per chiave identificativa del modulo" Obbligatorio="SI"/>
<Codice Contenuto="COL | CUB | DOC | EMU | EXA | EXB | EXC | EXD | EXR | EXS | FRM | G30 | GRI | GRP | MAIN | OPN | TRE" Scopo="CODICE per chiave identificativa del modulo" Obbligatorio="SI"/>
<Testo Contenuto="Alfanumerico" Scopo="Testo descrittivo del modulo identificato da TIPO-PARAMETRO-CODICE" Obbligatorio="SI"/>
</Attributi>
</Modulo>
<Utente>
<Attributi>
<Tipo Contenuto="Alfanumerico (OJ)" Scopo="TIPO per chiave identificativa Utente" Obbligatorio="SI"/>
<Parametro Contenuto="Alfanumerico (*USRPRF)" Scopo="PARAMETRO per chiave identificativa Utente" Obbligatorio="SI"/>
<Codice Contenuto="Alfanumerico" Scopo="CODICE per chiave identificativa Utente" Obbligatorio="SI"/>
<Testo Contenuto="Alfanumerico" Scopo="Testo descrittivo" Obbligatorio="SI"/>
</Attributi>
</Utente>
<Funzione>
<Attributi>
<Tipo Contenuto="Alfanumerico (TA)" Scopo="TIPO per chiave identificativa Funzione" Obbligatorio="SI"/>
<Parametro Contenuto="Alfanumerico (JAT)" Scopo="PARAMETRO per chiave identificativa Funzione" Obbligatorio="SI"/>
<Codice Contenuto="Alfanumerico" Scopo="CODICE per chiave identificativa Funzione" Obbligatorio="SI"/>
<Testo Contenuto="Alfanumerico" Scopo="Testo descrittivo" Obbligatorio="SI"/>
</Attributi>
</Funzione>
<CfgKey3>
<Attributi>
<Tipo Contenuto="Alfanumerico (**)" Scopo="TIPO per chiave identificativa CfgKey3" Obbligatorio="SI"/>
<Parametro Contenuto="Alfanumerico" Scopo="PARAMETRO per chiave identificativa CfgKey3" Obbligatorio="SI"/>
<Codice Contenuto="Alfanumerico (STANDARD)" Scopo="CODICE per chiave identificativa CfgKey3" Obbligatorio="SI"/>
<Testo Contenuto="Alfanumerico" Scopo="Testo descrittivo" Obbligatorio="SI"/>
</Attributi>
</CfgKey3>
<Sez>
<Attributi/>
</Sez>
<Styles>
<Attributi/>
</Styles>
<Style>
<Name Contenuto="Alfanumerico" Scopo="Nome associato allo stile" Obbligatorio="SI"/>
<Desc Contenuto="Alfanumerico" Scopo="Descrizione associata allo stile" Obbligatorio="SI"/>
<FontName Contenuto="Alfabetico" Scopo="Nome del font utilizzato" Obbligatorio="SI"/>
<FontColor Contenuto="Alfanumerico" Scopo="Colore associato al carattere" Obbligatorio="NO"/>
<BackColor Contenuto="Alfanumerico" Scopo="Colore associato allo sfondo" Obbligatorio="NO"/>
<FontItalic Contenuto="Yes | No" Scopo="Indica se il carattere è corsivo" Obbligatorio="NO"/>
<FontSize Contenuto="Numerico" Scopo="Dimensione del carattere" Obbligatorio="NO"/>
<FontULine Contenuto="Yes | No" Scopo="Indica se il carattere deve essere sottolineato" Obbligatorio="NO"/>
<FontBold Contenuto="Yes | No" Scopo="Indica se il carattere deve essere in grassetto" Obbligatorio="NO"/>
</Style>
<Service>
<Attributi>
<Titolo1 Contenuto="Alfanumerico" Scopo="Titolo visualizzato in rosso nella barra oggetti" Obbligatorio="SI"/>
<Titolo2 Contenuto="Alfanumerico" Scopo="Titolo visualizzato in nero nella barra oggetti" Obbligatorio="SI"/>
<Funzione Contenuto="F (funzione;componente;metodo) 1(;;) 2(;;) 3(;;) 4(;;) 5(;;) 6(;;) P()" Scopo="Contiene la funzione che ha generato l'Xml" Obbligatorio="SI"/>
<Servizio Contenuto="Alfanumerico" Scopo="Contiene il nome del servizio che ha generato l'Xml" Obbligatorio="SI"/>
</Attributi>
</Service>
<Header>
<Attributi/>
</Header>
<Livello>
<Attributi>
<Caratteristiche Contenuto="1carattere alfanumerico seguito da 2 cifre" Scopo="Indica il pannello di destinazione dell'albero e il layout che deve esservi applicato"/>
</Attributi>
</Livello>
<Setup>
<Attributi/>
</Setup>
<Program>
<Attributi/>
</Program>
<BAS>
<Attributi/>
</BAS>
<GNT>
<Attributi>
<Open Contenuto="true | false" Scopo="Setta le caratteristiche della finestra di Gantt" Obbligatorio="NO"/>
<Title Contenuto="true | false" Scopo="Setta le caratteristiche della finestra di Gantt" Obbligatorio="NO"/>
<ResizeOnStart Contenuto="true | false" Scopo="Setta le caratteristiche della finestra di Gantt" Obbligatorio="NO"/>
<MoveOnStart Contenuto="true | false" Scopo="Setta le caratteristiche della finestra di Gantt" Obbligatorio="NO"/>
</Attributi>
</GNT>
<SCH__Program>
<Attributi>
<Cod Contenuto="DEF | P01 | P02 | P03 | P04 | P05 | P06 | P99 |" Scopo="Codice reativo allo schema che si sta utilizzando per la ricerca. P/xx -  Schemi del barratore. S/xx - Schemi dello script. I/xx -  Schemi da £G25" Obbligatorio="SI"/>
<Txt Contenuto="Alfabetico" Scopo="Descrizione associata al codice dello schema che si sta utilizzando per la ricerca" Obbligatorio="SI"/>
</Attributi>
</SCH__Program>
<ORD>
<Attributi>
<Cod Contenuto="Alfanumerico" Scopo="Codice relativo all'ordinamento che si sta utilizzando per la ricerca" Obbligatorio="SI"/>
<Txt Contenuto="Alfabetico" Scopo="Descrizione relativa al codice dell'ordinamento che si sta utilizzando per la ricerca" Obbligatorio="SI"/>
</Attributi>
</ORD>
<ORDLIST>
<Attributi/>
</ORDLIST>
<SCHLIST>
<Attributi/>
</SCHLIST>
<EXU>
<Attributi/>
</EXU>
<Authorizations>
<Attributi/>
</Authorizations>
<Authorization>
<Attributi>
<Class Contenuto="Elemento della tabella BliraP" Scopo="Identificare l'oggetto di autorizzazione" Obbligatorio="SI"/>
<AUA Contenuto="Componente grafico(LO.XXX)/Utente/Oggetto di autorizzazione Es :  LO.BAS/SF/MNU.BAR" Scopo="Identificare l'autorizzazione tramite la classe, l'utente e l'oggetto di auth" Obbligatorio="SI"/>
<Value Contenuto="Numerico" Scopo="Livello di importanza che definisce quanto sia riservata la funzione all'interno della categoria" Obbligatorio="SI"/>
</Attributi>
</Authorization>
<EDT>
<Attributi>
<Tipo Contenuto="HTML | TXT | RUL | RPG | FIX" Scopo="Tipologia del testo trattato all'interno dell'editor"/>
<NoMod Contenuto="1" Scopo="Indica che il tipo di documento è fissato"/>
<Lung Contenuto="Numerico" Scopo=""/>
<Control Contenuto="Alfanumerico" Scopo="Nel caso di testo controllato indica l'associazione con il configuratore (è il codice in MB-SCP_CFG)"/>
</Attributi>
</EDT>
<QRY>
<Attributi>
<Cod Contenuto="KEY | DEC | FIL" Scopo=""/>
<Txt Contenuto="" Scopo=""/>
</Attributi>
</QRY>
<TEXT>
<Attributi/>
</TEXT>
<QRYLIST>
<Attributi/>
</QRYLIST>
<UISezG30>
<Attributi/>
</UISezG30>
<Oggetto>
<Attributi>
<Nome Contenuto="Alfanumerico" Scopo="Nome relativo all'oggetto" Obbligatorio="NO"/>
<Tipo Contenuto="Alfanumerico" Scopo="TIPO relativo all'oggetto per la chiave identificativa T;P;K" Obbligatorio="SI"/>
<Parametro Contenuto="Alfanumerico" Scopo="PARAMETRO relativo all'oggetto per la chiave identificativa T;P;K" Obbligatorio="SI"/>
<Codice Contenuto="Alfanumerico" Scopo="CODICE relativo all'oggetto per la chiave identificativa T;P;K" Obbligatorio="SI"/>
<Testo Contenuto="Alfanumerico" Scopo="Testo visualizzato nell'albero in associazione all'oggetto" Obbligatorio="SI"/>
<Exec Contenuto="Alfanumerico" Scopo="Chiamata alla funzione di Looc.up associata alla selezione dell'oggetto" Obbligatorio="NO"/>
<AuthLevel Contenuto="xy" Scopo="x e y sono le due cifre che indicano rispettivamente la categoria e il livello di importanza dell'oggetto di autorizzazione. Insieme costituiscono il codice di protezione" Obbligatorio="NO"/>
<AuthValue Contenuto="z" Scopo="z è una cifra che indica il livello di importanza per l'oggetto di autorizzazione" Obbligatorio="NO"/>
<i Contenuto="Alfanumerico" Scopo=" Specifica un'icona diversa da quella standard da associare al bottone in LOOC.up; tale icona deve essere contenuta nella sottodirectory LOOCUP_ICO di LOOC.up" Obbligatorio="NO"/>
<POS Contenuto="Alfanumerico" Scopo="" Obbligatorio="NO"/>
<PIN Contenuto="Alfanumerico" Scopo="" Obbligatorio="NO"/>
<PDE Contenuto="Alfanumerico" Scopo="" Obbligatorio="NO"/>
</Attributi>
</Oggetto>
<Pres>
<Attributi>
<FormType Contenuto="TREE/TAB/ONE-SEC" Scopo="Definisce la forma di presentazione - ONE_SEC :  mostro una sola sezione. Se nel questionario ne sono presenti più di una viene mostrata solo la prima. - TREE :  Il questionario mostra sulla sinistra l'albero delle sezioni e sulla destra la prima sezione visibile. - TAB :  mostro le sezioni come un elenco di tab. Non vengono eseguite regole."/>
<AddAuxSection Contenuto="1/blank" Scopo="Specifico se aggiungere la sezione con i dati ausiliari (data creazione, data modifica, utente creazione utente modifica questionario, descrizione)"/>
</Attributi>
</Pres>
<Resp>
<Attributi>
<InputType Contenuto="RIS/FIX/SEC" Scopo=""/>
<OutputType Contenuto="RIS/FIX/SEC" Scopo=""/>
</Attributi>
</Resp>
<Rules>
<Attributi>
<Execution Contenuto="SECTION/QUESTION/blank" Scopo="SECTION :  le regole vengono eseguite al cambio di sezione QUESTION :  le regole vengono eseguite alla modifica di una risposta di una domanda blank :  le regole non vengono eseguite"/>
<Compile Contenuto="1/blank" Scopo=""/>
</Attributi>
</Rules>
<Proprieta>
<Attributi>
<TACFSF Contenuto="" Scopo=""/>
<TACFSG Contenuto="" Scopo=""/>
<TACFSH Contenuto="" Scopo=""/>
<TACFSA Contenuto="" Scopo=""/>
<TACFSB Contenuto="" Scopo=""/>
<TACFSC Contenuto="" Scopo=""/>
<TACFSD Contenuto="" Scopo=""/>
<TACFDL Contenuto="" Scopo=""/>
<TACFDA Contenuto="" Scopo=""/>
<TACFDB Contenuto="" Scopo=""/>
<TACFDM Contenuto="" Scopo=""/>
<TACFDC Contenuto="" Scopo=""/>
<TACFDN Contenuto="" Scopo=""/>
<TACFDO Contenuto="" Scopo=""/>
<TACFDF Contenuto="" Scopo=""/>
<TACFDG Contenuto="" Scopo=""/>
<TACFDE Contenuto="" Scopo=""/>
<TACFDI Contenuto="" Scopo=""/>
<TACFDH Contenuto="" Scopo=""/>
<TACFQA Contenuto="" Scopo=""/>
<TACFQB Contenuto="" Scopo=""/>
<TACFQF Contenuto="" Scopo=""/>
<TACFQG Contenuto="" Scopo=""/>
<TACFQH Contenuto="" Scopo=""/>
<TACFQI Contenuto="" Scopo=""/>
<TACFQL Contenuto="" Scopo=""/>
</Attributi>
</Proprieta>
<Regole>
<Attributi/>
</Regole>
<PRE>
<Attributi>
<CDATA Contenuto="Alfanumerico" Scopo="Può contenere testo generico di qualsiasi tipo"/>
</Attributi>
</PRE>
<Griglia>
<Attributi/>
</Griglia>
<Colonna>
<Attributi>
<Cod Contenuto="Alfanumerico" Scopo="Codice identificativo del campo della tabella" Obbligatorio="SI"/>
<Txt Contenuto="Alfanumerico" Scopo="Testo visualizzato in testa in corrispondenza della colonna" Obbligatorio="SI"/>
<Tip Contenuto="Alfanumerico" Scopo="Tipo dell'oggetto contenuto nel campo della matrice" Obbligatorio="SI"/>
<Lun Contenuto="Numerico" Scopo="Determina la lunghezza del campo della matrice" Obbligatorio="SI"/>
<IO Contenuto="I | O | H" Scopo="Determina se il campo è di Input, Output o Hidden" Obbligatorio="SI"/>
<Ogg Contenuto="Alfanumerico" Scopo="" Obbligatorio="SI"/>
<Dpy Contenuto="Alfanumerico" Scopo="Emissione dell'icona" Obbligatorio="SI"/>
<Fill Contenuto="Alfanumerico" Scopo="Per grafico ASSE/SERIE" Obbligatorio="SI"/>
</Attributi>
</Colonna>
<LisOgg>
<Attributi/>
</LisOgg>
<Campi>
<Attributi/>
</Campi>
<Campo>
<Attributi>
<Cod Contenuto="" Scopo=""/>
<Tip Contenuto="Free | Label | Message | Oggetto" Scopo=""/>
<Lun Contenuto="" Scopo=""/>
<Pos Contenuto="" Scopo=""/>
<IO Contenuto="" Scopo=""/>
<Txt Contenuto="" Scopo=""/>
<Ogg Contenuto="" Scopo=""/>
</Attributi>
</Campo>
<Comandi>
<Attributi/>
</Comandi>
<Comando>
<Attributi>
<Cod Contenuto="" Scopo=""/>
<Txt Contenuto="" Scopo=""/>
</Attributi>
</Comando>
<Condizioni>
<Attributi/>
</Condizioni>
<Condizione>
<Attributi>
<Se Contenuto="" Scopo=""/>
<Allora Contenuto="" Scopo=""/>
</Attributi>
</Condizione>
<Controlli>
<Attributi/>
</Controlli>
<Controllo>
<Attributi>
<Cod Contenuto="" Scopo=""/>
<Txt Contenuto="" Scopo=""/>
</Attributi>
</Controllo>
<Righe>
<Attributi/>
</Righe>
<Riga>
<Attributi>
<Fld Contenuto="Alfanumerico più il simbolo ' | '  di separazione" Scopo="Contiene tutti i campi della tabella per ogni riga separati dal simbolo ' | .'  ES(matrice con 3 colonne)  :  Fld='campo1 | campo2 | campo3' "/>
</Attributi>
</Riga>
<Riga__FRM>
<Attributi>
<Dat Contenuto="" Scopo="" Obbligatorio=""/>
<CDATA Contenuto="" Scopo="" Obbligatorio=""/>
</Attributi>
</Riga__FRM>
<Riga__SCRIPT>
<Attributi>
<CDATA Contenuto="" Scopo="" Obbligatorio=""/>
</Attributi>
</Riga__SCRIPT>
<Script>
<Attributi/>
</Script>
<LisVal>
<Attributi/>
</LisVal>
<Val>
<Attributi>
<Dat Contenuto="" Scopo="" Obbligatorio=""/>
<CDATA Contenuto="" Scopo="" Obbligatorio=""/>
</Attributi>
</Val>
<UIPopup>
<Attributi/>
</UIPopup>
<Video>
<Attributi>
<Versione Contenuto="" Scopo=""/>
<Livello Contenuto="" Scopo=""/>
<Programma Contenuto="" Scopo=""/>
<File Contenuto="" Scopo=""/>
<Libr Contenuto="" Scopo=""/>
<Creato Contenuto="" Scopo=""/>
</Attributi>
</Video>
<UIDoc>
<Attributi/>
</UIDoc>
<Links>
<Attributi/>
</Links>
<Link>
<Attributi>
<URL Contenuto="Indica il percorso (relativo) per l'identificazione del documento/risorsa da visualizzare"/>
</Attributi>
</Link>
<Formato>
<Attributi>
<Modello Contenuto="" Scopo=""/>
<Setup Contenuto="" Scopo=""/>
</Attributi>
</Formato>
<Risposte>
<Attributi/>
</Risposte>
<Risposta>
<Attributi>
<Dom Contenuto="" Scopo="Codice dellla domanda"/>
<Sig Contenuto="" Scopo=""/>
<Ris Contenuto="" Scopo="Codice della risposta"/>
<Dec Contenuto="" Scopo="Decodifica della risposta"/>
<Cfg Contenuto="" Scopo="Riporta le risposte delle domande configurate :  la risposta della domanda principale è nell'attributo Ris, le altre in questo. Il campo è formattato a larghezza fissa."/>
<Flg Contenuto="" Scopo="In posizione 1 riporta la forzatura della domanda, in posizione 3 riporta la forzatura della post regola"/>
</Attributi>
</Risposta>
<DATI>
<Attributi>
<CDATA Contenuto="" Scopo=""/>
</Attributi>
</DATI>
<Key>
<Attributi/>
</Key>
<K1>
<Attributi>
<Tipo Contenuto="Alfanumerico" Scopo="TIPO identificativo della chiave"/>
<Parametro Contenuto="Alfanumerico" Scopo="PARAMETRO identificativo della chiave"/>
<Codice Contenuto="Alfanumerico" Scopo="CODICE identificativo della chiave"/>
<Testo Contenuto="Alfanumerico" Scopo="Testo descrittivo"/>
<Obb Contenuto="Alfanumerico" Scopo=""/>
<Mod Contenuto="Alfanumerico" Scopo=""/>
</Attributi>
</K1>
<K2>
<Attributi>
<Tipo Contenuto="Alfanumerico" Scopo="TIPO identificativo della chiave"/>
<Parametro Contenuto="Alfanumerico" Scopo="PARAMETRO identificativo della chiave"/>
<Codice Contenuto="Alfanumerico" Scopo="CODICE identificativo della chiave"/>
<Testo Contenuto="Alfanumerico" Scopo="Testo descrittivo"/>
<Obb Contenuto="Alfanumerico" Scopo=""/>
</Attributi>
</K2>
<Buttons>
<Attributi/>
</Buttons>
<Button>
<Attributi>
<Name Contenuto="Alfanumerico" Scopo="Nome associato al bottone"/>
<Status Contenuto="0 | 1" Scopo="Identifica lo stato del bottone --   > 1= attivo, 0= disattivo"/>
</Attributi>
</Button>
<OpzioneOggetti>
<Attributi>
<FU Contenuto="" Scopo="" Obbligatorio="SI"/>
<T1 Contenuto="Alfanumerico" Scopo="TIPO oggetto 1" Obbligatorio="SI"/>
<P1 Contenuto="Alfanumerico" Scopo="PARAMETRO oggetto 1" Obbligatorio="SI"/>
<K1 Contenuto="Alfanumerico" Scopo="CODICE oggetto 1" Obbligatorio="SI"/>
<S1 Contenuto="Alfanumerico" Scopo="DESCRIZIONE oggetto 1" Obbligatorio="SI"/>
<T2 Contenuto="Alfanumerico" Scopo="TIPO oggetto 2" Obbligatorio="SI"/>
<P2 Contenuto="Alfanumerico" Scopo="PARAMETRO oggetto 2" Obbligatorio="SI"/>
<K2 Contenuto="Alfanumerico" Scopo="CODICE oggetto 2" Obbligatorio="SI"/>
<S2 Contenuto="Alfanumerico" Scopo="DESCRIZIONE oggetto 2" Obbligatorio="SI"/>
<T3 Contenuto="Alfanumerico" Scopo="TIPO oggetto 3" Obbligatorio="SI"/>
<P3 Contenuto="Alfanumerico" Scopo="PARAMETRO oggetto 3" Obbligatorio="SI"/>
<K3 Contenuto="Alfanumerico" Scopo="CODICE oggetto 3" Obbligatorio="SI"/>
<S3 Contenuto="Alfanumerico" Scopo="DESCRIZIONE oggetto 3" Obbligatorio="SI"/>
<T4 Contenuto="Alfanumerico" Scopo="TIPO oggetto 4" Obbligatorio="NO"/>
<P4 Contenuto="Alfanumerico" Scopo="PARAMETRO oggetto 4" Obbligatorio="NO"/>
<K4 Contenuto="Alfanumerico" Scopo="CODICE oggetto 4" Obbligatorio="NO"/>
<S4 Contenuto="Alfanumerico" Scopo="DESCRIZIONE oggetto 4" Obbligatorio="NO"/>
</Attributi>
</OpzioneOggetti>
<Setup__Scheda>
<Attributi>
<ReadOnly Contenuto="Yes  |  No" Scopo="Indica se il testo è in sola lettura o modificabile" Obbligatorio="YES"/>
<Load Contenuto="I | D" Scopo="Indica se il contenuto viene caricato in modo immediato o differito" Obbligatorio="NO"/>
<Icone Contenuto="Yes  |  No" Scopo="Indica se associare ad ogni oggetto la relativa icona nel caso di alberi" Obbligatorio="NO"/>
<ShowTotal Contenuto="Yes | No" Scopo="" Obbligatorio=""/>
<ShowGroup Contenuto="Yes | No" Scopo="" Obbligatorio=""/>
<ShowFilter Contenuto="Yes | No" Scopo="" Obbligatorio=""/>
<SelFirst Contenuto="Yes | No" Scopo="Indica se il primo elemento dell'albero deve essere selezionato all'apertura" Obbligatorio="NO"/>
<Typ Contenuto="VBAR | LINE" Scopo="" Obbligatorio=""/>
<DynExpand Contenuto="Yes | No" Scopo="Indica se permettere l'espansione dinamica degli elementi dell'albero su selezione" Obbligatorio="NO"/>
<Recursive Contenuto="Yes | No" Scopo="Indica se permettere l'espansione ricorsiva degli elementi dell'albero su selezione" Obbligatorio="NO"/>
<MaxDepth Contenuto="Numerico" Scopo="Indica la masima profondità di espansione alla quale può giungere l'albero" Obbligatorio="NO"/>
<NodeText Contenuto="Text" Scopo="" Obbligatorio="NO"/>
</Attributi>
</Setup__Scheda>
<Layout>
<Attributi>
<Scheda Contenuto="Alfanumerico più il simbolo ' ; ' di separazione" Scopo="Chiave della scheda visualizzata (TIPO;PARAMETRO;CODICE)" Obbligatorio="SI"/>
<Lib Contenuto="Alfanumerico più il simbolo ' ; ' di separazione" Scopo="Libreria di ubicazione della scheda" Obbligatorio="SI"/>
</Attributi>
</Layout>
<Sez__inLayout>
<Attributi>
<Name Contenuto="Alfanumerico Sx dove x può essere lettera|numero" Scopo="Associa un nome alla sottoscheda in base al suo posizionamento. Il nome è sempre del tipo Sx dove x=A,B,C... o x=1,2,3... in base alla posizione relatica della scheda (Si rimanda alla costruzione della scheda dove AA e AB indicano, per esempio, 2 schede affiancate) " Obbligatorio="SI"/>
<Left Contenuto="Numerico più il simbolo ' % ' " Scopo="Definire la dimensione relativa della sottoscheda all'interno della scheda partendo da sinistra" Obbligatorio="NO"/>
<Top Contenuto="Numerico più il simbolo ' % ' " Scopo="Definire la dimensione relativa della sottoscheda all'interno della scheda partendo dall'alto"/>
<Right Contenuto="Numerico più il simbolo ' % ' " Scopo="Definire la dimensione relativa della sottoscheda all'interno della scheda partendo da destra"/>
</Attributi>
</Sez__inLayout>
<Sez__Definizione>
<Attributi>
<Name Contenuto="Alfanumerico Sx dove x può essere lettera|numero" Scopo="Associa un nome alla sottoscheda in base al suo posizionamento. Il nome è sempre del tipo Sx dove x=A,B,C... o x=1,2,3... in base alla posizione relatica della scheda (Si rimanda alla costruzione della scheda dove AA e AB indicano, per esempio, 2 schede affiancate) " Obbligatorio="SI"/>
</Attributi>
</Sez__Definizione>
<Sub>
<Attributi>
<Tit Contenuto="" Scopo=""/>
</Attributi>
</Sub>
<SCH>
<Attributi/>
</SCH>
<Setup__SCH>
<Attributi>
<Load Contenuto="D | I" Scopo="Indica se il contenuto deve essere caricato immediatamente o in modo differito" Obbligatorio="NO"/>
</Attributi>
</Setup__SCH>
<Targets>
<Attributi/>
</Targets>
<Target>
<Attributi>
<When Contenuto="Change | Click| DblClick | Expand | Return | ChangeRow | ChangeCol" Scopo="Indica l'azione sull'oggetto che induce la dinamicità"/>
<Where Contenuto="Alfanumerico" Scopo="Indica il nome della sezione sulla quale viene indotta la dinamicità"/>
<Title Contenuto="Alfanumerico" Scopo="Indica il nuovo titolo da associare alla sezione sulla quale viene indotta la dinamicità"/>
<Load Contenuto="D | I" Scopo="Indica se il caricamento dei dati nella sezione sulla quale viene indotta dinamicità avviene in modo immediato(I) o differito(D)"/>
<Sch.Var Contenuto="XXX(yy)" Scopo="Indica le variabili di scheda assegnate nel momento in cui viene eseguita l'azione espressa nell'attributo 'When'. Es. :  Sch.Var=XXX(yy) dove XXX è il nome della variabile e yy il valore assegnato"/>
</Attributi>
</Target>
<HTM>
<Attributi>
<Load Contenuto="D | I" Scopo="Indica se il contenuto deve essere caricato immediatamente o in modo differito" Obbligatorio="NO"/>
<ShowBar Contenuto="" Scopo="" Obbligatorio=""/>
<Browsing Contenuto="" Scopo="" Obbligatorio=""/>
<Zoom Contenuto="" Scopo="" Obbligatorio=""/>
<ZoomStart Contenuto="" Scopo="" Obbligatorio=""/>
<_Type Contenuto="" Scopo="" Obbligatorio=""/>
</Attributi>
</HTM>
<UiDoc_HTM>
<Attributi/>
</UiDoc_HTM>
<IMG>
<Attributi/>
</IMG>
<Setup__IMG>
<Attributi/>
</Setup__IMG>
<MAT>
<Attributi/>
</MAT>
<Setup__MAT>
<Attributi>
<Icone Contenuto="" Scopo="" Obbligatorio=""/>
<IconeTesta Contenuto="" Scopo="" Obbligatorio=""/>
<ToExcel Contenuto="" Scopo="" Obbligatorio=""/>
<AutoFit Contenuto="" Scopo="" Obbligatorio=""/>
<Load Contenuto="" Scopo="" Obbligatorio=""/>
<_Type Contenuto="" Scopo="" Obbligatorio=""/>
</Attributi>
</Setup__MAT>
<TRE>
<Attributi/>
</TRE>
<Base__TRE>
<Attributi/>
</Base__TRE>
<Setup__TRE>
<Attributi>
<Load Contenuto="" Scopo="" Obbligatorio=""/>
<Icone Contenuto="" Scopo="" Obbligatorio=""/>
<SelFirst Contenuto="" Scopo="" Obbligatorio=""/>
<DynExpand Contenuto="" Scopo="" Obbligatorio=""/>
<Recursive Contenuto="" Scopo="" Obbligatorio=""/>
<MaxDepth Contenuto="" Scopo="" Obbligatorio=""/>
<NodeText Contenuto="" Scopo="" Obbligatorio=""/>
<_Type Contenuto="" Scopo="" Obbligatorio=""/>
</Attributi>
</Setup__TRE>
<DYN>
<Attributi/>
</DYN>
<Setup__DYN>
<Attributi>
<ShowGroup Contenuto="" Scopo="" Obbligatorio=""/>
<DftGroup Contenuto="" Scopo="" Obbligatorio=""/>
<DftSort Contenuto="" Scopo="" Obbligatorio=""/>
<AlignTotal Contenuto="" Scopo="" Obbligatorio=""/>
<ShowTotal Contenuto="" Scopo="" Obbligatorio=""/>
<Expanded Contenuto="" Scopo="" Obbligatorio=""/>
<_Type Contenuto="" Scopo="" Obbligatorio=""/>
</Attributi>
</Setup__DYN>
<TRA>
<Attributi/>
</TRA>
<Setup__TRA>
<Attributi/>
</Setup__TRA>
<CHA>
<Attributi/>
</CHA>
<UiSmeup__CHA>
<Attributi/>
</UiSmeup__CHA>
<Setup__CHA>
<Attributi>
<Typ Contenuto="" Scopo="" Obbligatorio=""/>
<Asp Contenuto="" Scopo="" Obbligatorio=""/>
<_Type Contenuto="" Scopo="" Obbligatorio=""/>
</Attributi>
</Setup__CHA>
<BTN>
<Attributi/>
</BTN>
<UiSmeup__BTN>
<Attributi/>
</UiSmeup__BTN>
<Setup__BTN>
<Attributi>
<ShowText Contenuto="" Scopo="" Obbligatorio=""/>
<ShowIcon Contenuto="" Scopo="" Obbligatorio=""/>
<FillSpace Contenuto="" Scopo="" Obbligatorio=""/>
<Horiz Contenuto="" Scopo="" Obbligatorio=""/>
<Align Contenuto="" Scopo="" Obbligatorio=""/>
<_Type Contenuto="" Scopo="" Obbligatorio=""/>
</Attributi>
</Setup__BTN>
<SUB>
<Attributi/>
</SUB>
<Setup__SUB>
<Attributi/>
</Setup__SUB>
<LAB>
<Attributi/>
</LAB>
<Setup__LAB>
<Attributi>
<Load Contenuto="" Scopo="" Obbligatorio=""/>
<FontName Contenuto="" Scopo="" Obbligatorio=""/>
<FontColor Contenuto="" Scopo="" Obbligatorio=""/>
<BackColor Contenuto="" Scopo="" Obbligatorio=""/>
<FontSize Contenuto="" Scopo="" Obbligatorio=""/>
<Align Contenuto="" Scopo="" Obbligatorio=""/>
<_Type Contenuto="" Scopo="" Obbligatorio=""/>
</Attributi>
</Setup__LAB>
<PDF>
<Attributi/>
</PDF>
<UiDoc_PDF>
<Attributi/>
</UiDoc_PDF>
<GAU>
<Attributi/>
</GAU>
<Elemento>
<Attributi>
<Soglia1 Contenuto="Numerico" Scopo="Indica il valore iniziale della scala di valori rappresentabile" Obbligatorio="SI"/>
<Soglia2 Contenuto="Numerico" Scopo="Indica il valore finale della scala di valori rappresentabile" Obbligatorio="SI"/>
<Valore Contenuto="Numerico" Scopo="Indica il valore attuale che l'indicatore deve segnalare all'interno della scala di valori utilizzata" Obbligatorio="SI"/>
</Attributi>
</Elemento>
<Setup__GAU>
<Attributi>
<FontColor Contenuto="" Scopo="" Obbligatorio=""/>
<FontSize Contenuto="" Scopo="" Obbligatorio=""/>
<Text Contenuto="" Scopo="" Obbligatorio=""/>
<Inv Contenuto="" Scopo="" Obbligatorio=""/>
<Extend Contenuto="" Scopo="" Obbligatorio=""/>
<_Type Contenuto="" Scopo="" Obbligatorio=""/>
</Attributi>
</Setup__GAU>
<SEM>
<Attributi/>
</SEM>
<Elemento>
<Attributi>
<Soglia1 Contenuto="Numerico" Scopo="Indica il valore iniziale della scala di valori rappresentabile" Obbligatorio="SI"/>
<Soglia2 Contenuto="Numerico" Scopo="Indica il valore finale della scala di valori rappresentabile" Obbligatorio="SI"/>
<Valore Contenuto="Numerico" Scopo="Indica il valore attuale che l'indicatore deve segnalare all'interno della scala di valori utilizzata" Obbligatorio="SI"/>
</Attributi>
</Elemento>
<Setup__SEM>
<Attributi>
<FontColor Contenuto="" Scopo="" Obbligatorio=""/>
<FontSize Contenuto="" Scopo="" Obbligatorio=""/>
<Text Contenuto="" Scopo="" Obbligatorio=""/>
<Inv Contenuto="" Scopo="" Obbligatorio=""/>
<Extend Contenuto="" Scopo="" Obbligatorio=""/>
<_Type Contenuto="" Scopo="" Obbligatorio=""/>
</Attributi>
</Setup__SEM>
<IML>
<Attributi/>
</IML>
<Setup__IML>
<Attributi/>
</Setup__IML>
<Actions>
<Attributi/>
</Actions>
<Actions__EXU>
<Attributi>
<Insert Contenuto="Yes | No (default NO)" Scopo="Indica se si dispone del privilegio di inserimento sulla matrice" Obbligatorio="NO"/>
<Update Contenuto="Yes | No (default NO)" Scopo="Indica se si dispone del privilegio di aggiornamento sulla matrice" Obbligatorio="NO"/>
<Delete Contenuto="Yes | No (default NO)" Scopo="Indica se si dispone del privilegio di cancellazione sulla matrice" Obbligatorio="NO"/>
</Attributi>
</Actions__EXU>
<Fields>
<Attributi/>
</Fields>
<Field>
<Attributi>
<Name Contenuto="Alfanumerico (max 10 caratteri)" Scopo="Indica il campo della tabella al quale si riferisce il campo della matrice" Obbligatorio="SI"/>
<UseAs Contenuto="Key | potenzialmente qualsiasi codice di 3 caratteri" Scopo="Indica che il campo associato è utilizzato come chiave di indicizzazione" Obbligatorio="NO"/>
<IO Contenuto="I | O | H | B" Scopo="Indica se il campo è di Input(I), Output(O), Entrambi(B) o Nascosto(H)" Obbligatorio="SI (altrimenti inutile)"/>
<DefaultValue Contenuto="Alfanumerico" Scopo="Indica il valore di default nel momento dell'inserimento" Obbligatorio="NO"/>
<Fmt Contenuto="LC" Scopo="Indica se il contenuto deve essere espresso in LowerCase" Obbligatorio="NO"/>
</Attributi>
</Field>
<Action>
<Attributi>
<Type Contenuto="" Scopo=""/>
</Attributi>
</Action>
<Contenuto>
<Attributi>
<CDATA Contenuto="Alfanumerico" Scopo="Contenuto libero"/>
</Attributi>
</Contenuto>
<Messaggi>
<Attributi/>
</Messaggi>
<Messaggio>
<Attributi>
<Testo Contenuto="Alfanumerico" Scopo="Testo descrittivo del messaggio di errore"/>
<Livello Contenuto="Numerico" Scopo="Caratterizzare il livello di importanza dell'errore"/>
</Attributi>
</Messaggio>
<Esito>
<Caratteristiche/>
</Esito>
<Base>
<Attributi/>
</Base>
<LOCBAS>
<ComponenteGrafico>
<Provenienza XMLPresoDa="Apertura Menu iniziale/Apertura Popup"/>
</ComponenteGrafico>
</LOCBAS>
<LOCCUB>
<ComponenteGrafico>
<Provenienza XMLPresoDa="Cubo"/>
</ComponenteGrafico>
</LOCCUB>
<LOCCHT>
<ComponenteGrafico>
<Provenienza XMLPresoDa="Chart"/>
</ComponenteGrafico>
</LOCCHT>
<LOCGRP>
<ComponenteGrafico>
<Provenienza XMLPresoDa="Grafo"/>
</ComponenteGrafico>
</LOCGRP>
<LOCEDT>
<ComponenteGrafico>
<Provenienza XMLPresoDa="Apertura Editor"/>
</ComponenteGrafico>
</LOCEDT>
<LOCEMU>
<ComponenteGrafico>
<Provenienza XMLPresoDa="Emulatore"/>
</ComponenteGrafico>
</LOCEMU>
<LOCEXA>
<ComponenteGrafico>
<Provenienza XMLPresoDa="Grafico"/>
</ComponenteGrafico>
</LOCEXA>
<LOCEXB>
<ComponenteGrafico>
<Provenienza XMLPresoDa="Matrice (temporaneo)"/>
</ComponenteGrafico>
</LOCEXB>
<LOCEXD>
<ComponenteGrafico>
<Provenienza XMLPresoDa="Scheda oggetto"/>
</ComponenteGrafico>
</LOCEXD>
<LOCEXR>
<ComponenteGrafico>
<Provenienza XMLPresoDa="Modello dinamico"/>
</ComponenteGrafico>
</LOCEXR>
<LOCEXU>
<ComponenteGrafico>
<Provenienza XMLPresoDa="Updater matrice"/>
</ComponenteGrafico>
</LOCEXU>
<LOCFND>
<ComponenteGrafico>
<Provenienza XMLPresoDa="Ricerche per oggetto"/>
</ComponenteGrafico>
</LOCFND>
<LOCFRM>
<ComponenteGrafico>
<Provenienza XMLPresoDa="Form/PDF"/>
</ComponenteGrafico>
</LOCFRM>
<LOCGNT>
<ComponenteGrafico>
<Provenienza XMLPresoDa="Gantt"/>
</ComponenteGrafico>
</LOCGNT>
<LOCGND>
<ComponenteGrafico>
<Provenienza XMLPresoDa="Gantt/Distinta"/>
</ComponenteGrafico>
</LOCGND>
<LOCG30>
<ComponenteGrafico>
<Provenienza XMLPresoDa="Questionario"/>
</ComponenteGrafico>
</LOCG30>
<LOCHTM>
<ComponenteGrafico>
<Provenienza XMLPresoDa="Componente HTML"/>
</ComponenteGrafico>
</LOCHTM>
<LOCMAP>
<ComponenteGrafico>
<Provenienza XMLPresoDa="Componente Mappa"/>
</ComponenteGrafico>
</LOCMAP>
<LOCOPN>
<ComponenteGrafico>
<Provenienza XMLPresoDa="Componente Open"/>
</ComponenteGrafico>
</LOCOPN>
<LOCQRY>
<ComponenteGrafico>
<Provenienza XMLPresoDa="Ricerche per oggetto"/>
</ComponenteGrafico>
</LOCQRY>
<LOCSTR>
<ComponenteGrafico>
<Provenienza XMLPresoDa="Stella"/>
</ComponenteGrafico>
</LOCSTR>
<LOCSYS>
<ComponenteGrafico>
<Provenienza XMLPresoDa="Operazioni di sistema AS/400"/>
</ComponenteGrafico>
</LOCSYS>
<LOCTRE>
<ComponenteGrafico>
<Provenienza XMLPresoDa="Albero"/>
</ComponenteGrafico>
</LOCTRE>
</PLIST>
