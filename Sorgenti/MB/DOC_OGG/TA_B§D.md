# B§D - TIPI ACCESSO A P.C.
 :  : DEC T(ST) K(B§D)
## CONTENUTO DEI CAMPI
 :  : FLD T$B§DG **Tipo percorso dati**
_7_(in sviluppo]
Utilizzato dalla routine**£PCT**, rappresenta il tipo percorso dei dati, quindi il file system dove verranno scritti i dati trasferiti mediante la £PCT.
Valori che può assumere :  dati trasferiti mediante la £PCT,
' ' - Valore assunto (per continuità con le vecchie versioni) :  la cartella indicata nei parametri della £PCT rappresenta una cartella condivisa, definita sotto il percorso**/QDls/**, con la limitazione della nomenclatura files tipo PC_DOS a otto caratteri + estensione a 3 caratteri (xxxxxxxx.yyy)
'1' - IFS :  la cartella indicata nei parametri della £PCT rappresenta una cartella memorizzata direttamente nell'IFS dell'AS400, ovvero nella root**/**; non ha particolari limitazioni delle nomenclature, salvo l'ampiezza dei campi di compilazione della £PCT e l'impossibilità di scrivere in /QSYS.LIB.
