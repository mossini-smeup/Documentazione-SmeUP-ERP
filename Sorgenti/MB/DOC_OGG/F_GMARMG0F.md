## Contenuto
Informazioni relative a Plant/Articolo.

## Codice Oggetto (in TA/*CNTT)

## Chiave primaria
Vedi tabella C£F.

## Ulteriore chiave primaria
N.A.

## Altri condizionamenti facoltativi in ricerca
N.A.

## Tabella guida

## Autorizzazioni
La classe di autorizzazione è B£GRI2.
La funzione di autorizzazione è ART_MAG.

## Note strutturate (Tabella NSC)

## Parametri (Tabella C£E)
La categoria è definita in tabella C£F, a standard £P3.
I parametri £P3 sono importanti perchè da essi derivano gli OAV logistici : 
 * J/L01          Tipo ordine assunto
 * J/L02          % Scarto previsto
 * J/L03          Contenitore standard
 * J/L04          Qtà per contenitore


## Flussi (Tabella B£H)

## Costruzione automatica campi (tabella B£C)

## Presenza monitor - visualizzatore
N.A.

## Programmi di controllo

## /COPY
Interfaccia Dati magazzino/articolo (£GMA) : 
 :  : DEC T(MB) P(QILEGEN) K(£GMA)

## Gruppi flag

## Workflow e popup
N.A.

## Note particolari

## CONTENUTO DEI CAMPI

 :  : FLD M§TIGE **Tecnica di gestione**
Da esso viene ricavato l'oav AR e AM  J/M01 Tecnica di gestione articolo.

 :  : FLD M§LOCN **Codice Ubicazione**
Da esso viene ricavato l'oav AR e AM  J/M02 Ubicazione assunta.

 :  : FLD M§SMIN **Scorta minima**
Da esso viene ricavato l'oav AR e AM  J/M03 Scorta Minima visibile anche come fonte esistente di tipo SC.

 :  : FLD M§PTRI **Punto di riodino**
Da esso viene ricavato l'oav AR e AM  J/M04 Punto di riordino visibile anche come fonte esistente di tipo PR.

 :  : FLD M§LTEC **Lotto economico**
Da esso viene ricavato l'oav AR e AM  J/M05 Lotto Economico.

 :  : FLD M§COST **Consumo Stimato**
da esso viene ricavato l'oav AR e AM  J/M09 Consumo Stimato.
