# Nome programma
Nei programmi Sme.UP è possibile avere accesso a due diverse informazioni riguardanti il loro nome :  il nome oggetto e il nome sorgente.
* Il nome oggetto (£PDSNP) è il nome dell'oggetto *PGM vero e proprio.
* Il nome sorgente (£U13MB) è il nome del membro sorgente da cui è stato compilato.
Normalmente queste due informazioni coincidono, ma non succede ad esempio nelle repliche.
Il programma XX valorizza £PDSNP='XX' e £U13MB='XX'.
La sua replica XXA valorizza £PDSNP='XXA' e £U13MB='XX'.

Quando in un programma bisogna usare il "nome programma", bisogna sempre fare attenzione a quale dei due campi usare. Ad esempio nella costruzione del nome di una exit è più opportuno usare £U13MB.

## Nota sui campi "nome programma"
Questi sono i campi che abbiamo a disposizione "run-time" che contengono il nome del programma/sorgente : 
* £PDSNP :  nome programma
* £PDSNM :  nome modulo
* XXSDS :  nome membro sorgente da cui è stato compilato (info teoricamente presente in SDS ma non riportata in £PDS)
* £U13MB :  nome sorgente da cui ho compilato (aggiunto dal pre-compilatore)
* OAV J/005 dell'OJ*PGM

Vediamo i valori di questi vari campi in 4 oggetti *PGM : 
* RPG è un RPGLE
* RPGA è una replica di RPG creata per duplicazione
* RPG_R è una replica di RPG creata per ricompilazione
* SQLRPG è un SQLRPGLE
* SQLRPGA è una replica di SQLRPG creata per duplicazione
* SQLRPG_R è una replica di SQLRPG creata per ricompilazione


| 
| .COL Cod="COL001" Txt="*PGM" LunAut="1" |
| ---|----|
| 
| .COL Cod="COL002" Txt="£PDSNP" LunAut="1" |
| 
| .COL Cod="COL003" Txt="£PDSNM" LunAut="1" |
| 
| .COL Cod="COL004" Txt="XXSDS" LunAut="1" |
| 
| .COL Cod="COL005" Txt="£U13MB" LunAut="1" |
| 
| .COL Cod="COL006" Txt="OAV" LunAut="1" |
| RPG|RPG|_7_RPG|RPG|RPG|RPG |
| RPGA|RPGA|_7_RPG|RPG|RPG|RPG |
| RPG_R|RPG_R|_7_RPG_R|RPG|RPG|RPG |
| SQLRPG|SQLRPG|_7_SQLRPG|_7_SQLRPG|SQLRPG|SQLRPG |
| SQLRPGA|SQLRPGA|_7_SQLRPG|_7_SQLRPG|SQLRPG|SQLRPG |
| SQLRPG_R|SQLRPG_R|_7_SQLRPG_R|_7_SQLRPG_R|SQLRPG|SQLRPG |
| 


£PDSNM e XXSDS non andrebbero mai usati come "nome programma". Si comportano infatti in modo differente a seconda del "tipo" di programma. XXSDS non esiste a standard quindi non è un problema.

£PDSNM dovrebbe quindi essere usato solo nel caso remoto in cui serva effettivamente il nome modulo (informazione tecnica).

Quindi, come detto precedentemente, l'utilizzo "normale" dovrebbe quindi passare per £U13MB o OAV. O per £PDSNP in caso serva il nome effettivo dell'oggetto.
£U13MB può essere usato solo all'interno del programma stesso. Per avere l'informazione relativa ad un altro programma è necessario usare l'OAV.

# File sorgente di compilazione.
Il campo £U13MB contiene, come detto precedentemente, il nome membro effettivo da cui il programma è stato compilato.
il campo £U13FI invece contiene il nome del file source da cui il programma è stato originariamente compilato. Questo campo non conterrà mai il valore £UI_SRC ma sempre il valore originale.
Questo campo può essere usato solo all'interno del programma stesso. Per avere questa informazione ma relativa ad un altro programma, è necessario usare l'OAV J/003 dell'oggetto OJ*PGM.

## Nota sull'OAV J/003 dell'oggetto OJ*PGM
Molti programmi hanno come sorgente di compilazione "effettivo" il £UI_SRC.
L'OAV effettua un tentativo di correzione, ma non sempre riesce.
L'OAV recupera il nome file source tramite un API, se l'api restituisce £UI_SRC, allora va a leggere il sorgente in £UI_SRC ed estrae il sorgente effettivo.
Questo comporta almeno due problemi. Se la libreria da cui è stato originariamente compilato non esiste, non riesce a leggere il £UI_SRC.(Ad esempio se compilo da SMEDEV e ho installato SMEUP_DEV, l'API restituisce SMEDEV/£UI_SRC. Tale libreria non esiste e quindi non viene fatta la risalita). C'è un problema analogo in caso la SMEDEV esista ma non sia quella giusta. Ad esempio perché sul sistema sono installare più "versioni" di Sme.UP. Se ad esempio SMEDEV esiste ma io sto leggendo da SMEDEV2, dovrei andare a leggere in SMEDEV2.

## Nota su SDS
Nella SDS sono inserite anche le informazioni relative al file source da cui il programma è stato compilato (e la relativa libreria).
Ma in caso di SQLRPGLE i dati non sono significativi (contengono SEMPRE QTEMP/QSQLTEMP1).
Inoltre abbiamo il problema del £UI_SRC.
Quindi questi dati non vanno mai usati.


