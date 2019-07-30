# OBIETTIVO
Fornire informazioni relative alle Ritenute :  Anagrafica percipienti, Fatture, Pagamenti.
# FUNZIONI/METODI
## LISTE
### LIS.CON
Costruisce una matrice che riporta i record di tipo "CN" presenti sul file C5RITE0F (ovvero i percipienti). I contatti sono raggruppati per tipologia. In aggiunta a questi dati, mostra anche il valore impostato per il campo "Rapporto Fiscale" nella tabella BRX.
### LIS.FAT
Costruisce una matrice che riporta i record che hanno "E4" come oggetto origine (ovvero le fatture) e che hanno come riferimeto il contatto passato in oggetto 1 (in questo caso quello indicato nella riga su cui si è cliccato nella sezione "Soggetti"). I dati esposti sono gli stessi che si ottengono interrogando l'archivio delle ritenute.
### LIS.PAG
Costruisce una matrice che riporta i record che hanno "RR" come oggetto origine (ovvero i pagamenti) e che hanno come riferimeto la fattura passata in oggetto 1. I dati esposti sono gli stessi che si ottengono interrogando l'archivio delle ritenute.
### LIS.REG
Ritorna una matrice che riporta la lista delle registrazioni legate al conto passato in oggetto 1.
La funzione calcola anche il saldo al mese precedente, in modo che, sommato all'elenco delle registrazioni, si ottenga sempre la quadratura contabile per il mese scelto. Nei parametri è necessario indicare l'esercizio contabile e il periodo interessati.
## SALDO
### SAL.CON
Ritorna il saldo del mese corrente e degli 11 mesi precedenti. In oggetto 1 va passato il codice del conto contabile di cui si vuole il saldo, mentre nel parametro NPE va indicato il numero di periodi per il quale si vuole il calcolo.
## REGISTRAZIONI
### REG.AUT
Ritorna una matrice contenente la lista delle registrazioni automatiche relative all'ambito delle ritenute e dell'Enasacro, leggendo la TA C5U. In aggiunta riporta anche il codice tributo relativo all'elemento riportato.
## PERIODO
### PER.LIS
Ritorna un albero che riporta i periodi che vanno dal mese in corso a ritroso fino al primo anno caricato nella TA PER.
### PER.FAT
Ritorna una matrice che riporta i dati relativi alle fatture per il periodo indicato in oggetto 1. La struttura utilizzata per mostrare i dati è quella ottenbile dall'interrogazione archivi ritenute, salvo per il fatto che è stata aggiunta la colonna dell'Enasarco carico percipiente.
### PER.PAG
Ritorna una matrice che riporta i dati relativi alle fatture per il periodo indicato in oggetto 1. La struttura utilizzata per mostrare i dati è quella ottenbile dall'interrogazione archivi ritenute.
### PER.DIC
Ritorna una matrice che estrae dati relativi a fatture già interamente pagate alla data passata in oggetto 1 e a fatture anche non interamente pagate i cui pagamenti hanno data competenza compatibile con quella passata in oggetto 1. Tale funzione riproduce ciò che viene effettuato nella "Stampa Certificazioni" delle Ritenute.
### PER.FAP
Ritorna una matrice che estrae dati relativi a fatture ancora aperte alla data passata in oggetto 1.
Tale funzione riproduce ciò che viene effettuato nella "Stampa Documenti con Ritenuta d'Acconto " delle Ritenute, quando si seleziona 1= Stampa Documenti Non Saldati nel campo "Tipo Stampa".


 :  : PRO.SER Cod="LIS.CON.1" Tit="Liste. Contatti" Fun="F(EXB;C5SER_05;LIS.CON) 1(CN;;-(F;;CN;Contatto))"

 :  : PRO.SER Cod="LIS.FAT.2" Tit="Liste. Fatture" Fun="F(EXB;C5SER_05;LIS.FAT)" Ref="LIS.CON.1"

 :  : PRO.SER Cod="LIS.PAG.3" Tit="Liste. Pagamenti" Fun="F(EXB;C5SER_05;LIS.PAG) 2(E4;;-(O;;E4;Reg.contabile))"

 :  : PRO.SER Cod="LIS.REG.4" Tit="Liste. Registrazioni" Fun="F(EXB;C5SER_05;LIS.REG) 2(E4;;-(O;;E4;Reg.contabile)) P()"

 :  : PRO.SER Cod="SAL.CON.5" Tit="Saldo. Contabile" Fun="F(EXB;C5SER_05;SAL.CON) 3(CO;;-(O;;CO;Conto contabile)) P()"

 :  : PRO.SER Cod="REG.AUT.6" Tit="Registrazioni. Automatiche" Fun="F(EXB;C5SER_05;REG.AUT) 4(TA;;-(F;;TA;Tabella))"

 :  : PRO.SER Cod="PER.LIS.7" Tit="PERIODO. Lista" Fun="F(TRE;C5SER_05;PER.LIS)" Ref="REG.AUT.6"

 :  : PRO.SER Cod="PER.FAT.8" Tit="PERIODO. Fatture" Fun="F(EXB;C5SER_05;PER.FAT) 5(D8;;-(O;;D8;Data))"

 :  : PRO.SER Cod="PER.PAG.9" Tit="PERIODO. Pagamenti" Fun="F(EXB;C5SER_05;PER.PAG)" Ref="PER.FAT.8"

 :  : PRO.SER Cod="PER.DIC.10" Tit="PERIODO. Dichiarazioni" Fun="F(EXB;C5SER_05;PER.DIC)" Ref="PER.FAT.8"

 :  : PRO.SER Cod="PER.FAP.11" Tit="PERIODO. Fatture aperte" Fun="F(EXB;C5SER_05;PER.FAP)" Ref="PER.FAT.8"

