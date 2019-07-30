 :  : HEA RESP(LS) STAT(10)
# OBIETTIVO
Gestire i menù nell'ambiente grafico.

# FUNZIONI E METODI
In input il parametro principale è costituito dall'oggetto 1, dal quale derivo il sorgente  del file SCP_MNU da prendere in considerazione. In input posso ricevere qualsiasi oggetto, e a seconda dell'oggetto verrà derivato il membro da leggere. Può anche essere passato direttamente l'oggetto MBSCP_MNU in questo in caso l'oggetto 1 identifica esattamente il membro.

I parametri V1/V2/V3/V4/V5 servono solo per passare delle variabili aggiuntive che possono poi essere utilizzate come variabili nello script del menù.

A seconda del tipo oggetto lo script viene determinato in modi differenti : 
- Con tipo Oggetto MB viene preso il codice del membro
- Con tipo Oggetto TAB£A viene preso il codice A_ + Codice oggetto
- Con tipo Oggetto TAB£AMO viene preso il codice M_ + Codice oggetto
- Con tipo Oggetto VD viene preso il codice V_ + Codice oggetto
- Con tutti gli altri ,( oppure se non esiste l'Oggetto A_+ Codice Oggetto ), viene preso il codice O_ + Tipo oggetto

Lo script dell'SCP_MNU ha dei tag simili a quelli della scheda : 
- G.SEZ -> definisce un titolo
- G.SUB -> definisce una funzione (deve essere per forza legata ad una sezione)
- I.SCH -> definisce una "sottoscheda" del menù. Ogni chiamata elabora una sola sottoscheda e può esistere la sottoscheda blank.
- DO/ENDDO  -> gestisce la scansione di una lista ( LOOP ) tramite i parametri passati in  :   Lis="" Par="" Flt=""
         es. :   Lis="LITAB£AMO" è la lista dei Moduli Applicazione
               Par="*All"
               Flt="C5"        Filtra solo i Moduli relativi all'Applicazione C5


 :  : PRO.SER Cod="MNU.TRE.1" Tit="Menù. Albero" Fun="F(TRE;LOA12;MNU.TRE) 1(;;-(O;;;)) P( VA(-(F;;**;SSC Sottoscheda)) VA(-(F;;**;SEZ Sezione)) VA(-(F;;**;SUB Subsezione)) VA(-(F;;**;V1 Variabile 1)) VA(-(F;;**;V2 Variabile 2)) VA(-(F;;**;V3 Variabile 3)) VA(-(F;;**;V4 Variabile 4)) VA(-(F;;**;V5 Variabile 5)))"

 :  : PRO.SER Cod="MNU.EXP.2" Tit="Menù. Esplosione" Fun="F(TRE;LOA12;MNU.EXP)" Ref="MNU.TRE.1"

