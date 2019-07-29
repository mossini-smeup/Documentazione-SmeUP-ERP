# Obiettivi
Indicare la modalità standard di lavoro per costruire un modello di Smeup declinato
per uno specifico settore merceologico o distretto industriale.

# Modalità di Gestione e Configurazione Ambiente Modello
## Codifica Modello
Inserire in V2.MODAP il codice del modello xy
Attualmente
 xy Identificativo modello
01 Gomma
02 Metal
03 Sygest

## Libreria Dati
La libreria dati sarà SMEMOD£xx con xx=identificativo modello
Questa viene inizialmente copiata dalla SMEUP_FIL

## Libreria Sorgenti
La libreria SME_£xy per tutti i source/oggetti/script/ecc standard del modello
Questa libreria sarà gestita dal laboratorio (o meglio da UN SOLO RESPONSABILE del gruppo di lavoro responsabile del modello, es. FRANCO SALA per il METAL)
Le /copy std del modello le chiamiamo £Zya
I pgm che scriviamo e consideriamo std Zy. (es. Z20001, Z2BR01, )
Altrimenti saranno X1 se sono presonali del cliente

## Tabelle
Si tenderà ad avere delle applicazioni specifiche in tab b£a del tipo Zy (es. Z1 per Gomma e Z2
per Metal)
Le tabelle std del modello le chiamiamo Zya	(a=0..1,A..Z), dove Y è la sigla del modello.
I codici dei sottosettori (std del modello) di tabelle standard Sme.UP iniziano per Z.
Quando dal cliente creiamo tabelle o programmi personali, inizieranno sempre per X

## Ambiente Applicativo
Ambiente di sviluppo & demo del modello (MxySVI)
Ambiente del modello (Mxy)
	SMEMOD£xy	Libreria dati alla v4r1 (poi v5r1)
	SME_£xy	Libreria sorgenti e oggetti del modello £xy (es. SME_£01 per la GOMMA)
	SME*4.1	Librerie standard Sme.UP v4r1 (poi v5r1)

## Convenzione rilascio modello

Quando lavoriamo per preparare il modello, useremo uno (o più) ambienti di lavoro (es. UP_M02SVI)
Da questo il resp. del modello parte per CONSOLIDARE in SMEMOD£xy.
Si potrà ricostruire un ambiente di lavoro , partendo dal modello e facendo conversioni


## Conversioni (?)
	Sorgenti in SMECON/SG_SM  :  programmi std di conversione SIGLAM->SMEUP)

# Modelli Gestiti
## Gomma
 :  : DEC T(MB) P(DOC_PER) K(Z1)
## Metal
 :  : DEC T(MB) P(DOC_PER) K(Z2)
## Sygest
 :  : DEC T(MB) P(DOC_PER) K(Z3)










