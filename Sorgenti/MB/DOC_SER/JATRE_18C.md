 :  : HEA CLAS(B) STAT(10)
# OBIETTIVO
Questo servizio costruisce l'XML del layout (sezioni/subsezioni) delle schede di LOOC.up.
I dati contenuti nelle subsezioni delle schede sono generati da : 
- questo servizio mediante alcune istruzioni D della scheda (es. semafori, label, ...)
- altri servizi, mediante chiamate D.FUN.STD

## Oggetto scheda
Il servizio ricevendo l'oggetto, senza definizione della scheda da utilizzare, la deriva eseguendo i seguenti passaggi : 
- Tipo e parametro
- Se Tipo "TA"
-- Tipo e primi 3 caratteri del parametro
- Se Tipo "MB" e parametro inizia per "DOC_"
-- Tipo e primi 3 caratteri del parametro
- Se Tipo "MB" e parametro inizia per "SCP_"
-- Tipo e primi 3 caratteri del parametro
- Tipo
- Se tipo "AZ" assume "CNAZI"
- Se tipo "CL" assume "CNCLI"
- se tipo "CO" assume "TAC5B" e parametro
- se tipo "BA" assume "CNBAN"
- se tipo "TABAN" assume "CNBAN"
- Se tipo "CNAZI" assume "AZ"
- Se tipo "CNCLI" assume "CL"
- se tipo "TAC5B" assume "CO" e parametro
- se tipo "CNBAN" assume "BA"
- se tipo "CNBAN" assume "TABAN"
- assume "OGOG"

# FUNZIONI/METODI
## Scheda indicando il membro
Membro specifico con oggetto facoltativo
 :  : PRO.SER Fun="F(EXD;*SCO;) 1(-;-;-) 2(MB;SCP_SCH;-(O))". Cod="00001"
L'oggetto 4 indica la sottoscheda da utilizzare.
 :  : PRO.SER Fun="F(EXD;*SCO;) 1(-;-;-) 2(MB;SCP_SCH;-(O)) 4(;;-) 5(OJ;*LIB;-)". Cod="00002"
L'Oggetto 5 indica in quale libreria forzare la lettura della scheda.
 :  : PRO.SER Fun="F(EXD;*SCO;) 1(-;-;-) 2(MB;SCP_SCH;-(O)) 5(OJ;*LIB;-)". Cod="00003"

### Scheda a partire da un oggetto.
L'oggetto è obbligatorio. Da questo derivo la scheda risalendo al tipo e con default "OG".
 :  : PRO.SER Fun="F(EXD;*SCO;) 1(-(O);-(O);-(O))". Cod="00004"
Ad esempio : 
F(EXD;*SCO;) 1(AR;ART;A01)
Tenta di aprire nel primo file SCP_SCH prima "ARART", se manca cerca "AR", se manca cerca "OG".
L'oggetto 3 indica un suffisso (separato dal carattere _) delle scheda.
 :  : PRO.SER Fun="F(EXD;*SCO;) 1(-;-;-) 2(MB;SCP_SCH;-(O))". Cod="00005"
Ad esempio : 
F(EXD;*SCO;) 1(AR;ART;A01) 3(;;BAS)
Cerca in ordine l'oggetto "ARART_BAS" e "AR_BAS".

Il parametro viene utilizzato per passare altre informazioni alla scheda, in modalità a TAG, accessibili tramite le variabili statiche di scheda _&_PA.

Ad esempio, se una scheda viene chiamata con P(AR(A01) OVE(660533))
al suo interno potrà accedere alle informazioni con
_&_PA.AR (vale A01)
_&_PA.OVE (vale 660533)

Per ulteriori dettagli consultare
 :  : DEC T(MB) P(DOC) K(LOCEXD_06) I(_7_Variabili di scheda           >>)

 :  : PRO.SER Cod=".6" Tit="Generazione XML scheda. " Fun="F(EXD;JATRE_18C;) 1(;;-(F;;;Oggetto di rif.)) 2(MB;;-(F;;MB;Membro)) 3(;;-(F;;;Suffisso)) 4(;;-(F;;;Sottoscheda)) 5(OJ;*LIB;-(F;;OJ*LIB;Libreria))"

