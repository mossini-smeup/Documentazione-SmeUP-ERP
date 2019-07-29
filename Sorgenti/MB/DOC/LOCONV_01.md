Le funzioni del convertitore sono sostanzialmente : 

## Trasformazione formati video in XML come da esempio seguente
I sorgenti dei formati video vengono letti e trasformati in un sorgente XML secondo una sintassi specifica : 

### Breve esempio di XML
>.   <Formato Cod="£UFMT1" Tip="RECORD" Sfl="" Srn="" Pox="" Poy="" Rows="24" Cols="080" Sfp="" Csr=""
.     <Modello>
.      <Controlli>
.       <Controllo Cod="IN1" Txt="**   ANAGRAFICA CESPITI   **">
.        <Condizioni>
.         <Condizione Se="" Allora="RI"/>
.        </Condizioni>
.       </Controllo>
.       <Controllo Cod="IN2" Txt="eamp;£G00DE"/>
.      </Controlli>
.      <Comandi>
.       <Comando Cod="F22" Txt="Informazioni Programma"/>
.       <Comando Cod="F02" Txt="Funzione"/>
.        <Condizioni>
.         <Condizione Se="(90)" Allora="RI"/>
.        </Condizioni>
.       </Comando>
.      </Comandi>
.     </Modello>
.       <Campi>
.        <Campo Cod="£RASDI" Txt="" Tip="Free" Lun="00015" Pos="01;002" IO="O" Ogg="" Edt="">
.         <Condizioni>
.          <Condizione Se="" Allora="HI"/>
.         </Condizioni>
.        </Campo>


## Sostituzione interfaccia video con comunicazione su code
Introduciamo la /COPY £UIA e le sue funzioni in sostituzione delle chiamate al video
Ogni scrittura o lettura del video viene sostituita da una lettura o scrittura sulla opportuna coda di dati.
La sostituzione viene fatta automaticamente da un programma specifico che : 
 * Crea un sorgente intermedio salvato nel file SRC
 * Crea se necessario un COPY per la DS del formato video salvata in £UI_DSP

### Breve esempio di sostituzione di RPG
>     C                   IF        £INZJT='I'
     C                   EXFMT     FMT3
     C                   ELSE
     C                   Eval      £UIAKS = '                    '
     C                   MOVEL(P)  'FMT3'        £UIAID
     C                   MOVEL(P)  'R'           £UIATF
     C                   MOVEL     £RASDI        £RASDI00
     C                   MOVEL     W$TPAR        W$TPAR00
     C                   MOVEL     W$ENIR        W$ENIR00
     C                   MOVEL     W$CASI        W$CASI00
     C                   MOVEL     W$DISE        W$DISE00
     C                   MOVEL     W$UNMS        W$UNMS00
     C                   MOVEL     W$GRDI        W$GRDI00
     C                   MOVEL     W$GRCI        W$GRCI00
     C                   MOVEL     W$NOMC        W$NOMC00
     C                   MOVEL     W$RCDV        W$RCDV00
     C                   MOVEL     W$CSVA        W$CSVA00
     C                   MOVEL     W$PESO        W$PESO00
     C                   MOVEL     W$CSVQ        W$CSVQ00
     C                   MOVEL     W$VOLU        W$VOLU00
     C                   MOVEL     W$LOTR        W$LOTR00
     C                   MOVEL     W$CLMA        W$CLMA00
     C                   MOVEL     W$CLVA        W$CLVA00
     C                   MOVEL     W$CLPR        W$CLPR00
     C                   MOVEL     W$CLCO        W$CLCO00
     C                   MOVEL     W$CLGE        W$CLGE00
     C                   MOVEL     W$CDLF        W$CDLF00
     C                   MOVEL     W$FL01        W$FL0100
     C                   MOVEL     W$CLFU        W$CLFU00
     C                   MOVEL     W$DEAR        W$DEAR00
     C                   MOVEL     W$DES2        W$DES200
     C                   MOVEL(P)  £UFMT3        £UIAD1
     C                   MOVEL(P)  'EXFMT'       £UIAOP
     C                   EXSR      £UIA
     C                   MOVEL(P)  £UIAD1        £UFMT3
     C                   MOVEL     £RASDI00      £RASDI
     C                   MOVEL     W$TPAR00      W$TPAR
     C                   MOVEL     W$ENIR00      W$ENIR
     C                   MOVEL     W$CASI00      W$CASI
     C                   MOVEL     W$DISE00      W$DISE
     C                   MOVEL     W$UNMS00      W$UNMS
     C                   MOVEL     W$GRDI00      W$GRDI
     C                   MOVEL     W$GRCI00      W$GRCI
     C                   MOVEL     W$NOMC00      W$NOMC
     C                   MOVEL     W$RCDV00      W$RCDV
     C                   MOVEL     W$CSVA00      W$CSVA
     C                   MOVEL     W$PESO00      W$PESO
     C                   MOVEL     W$CSVQ00      W$CSVQ
     C                   MOVEL     W$VOLU00      W$VOLU
     C                   MOVEL     W$LOTR00      W$LOTR
     C                   MOVEL     W$CLMA00      W$CLMA
     C                   MOVEL     W$CLVA00      W$CLVA
     C                   MOVEL     W$CLPR00      W$CLPR
     C                   MOVEL     W$CLCO00      W$CLCO
     C                   MOVEL     W$CLGE00      W$CLGE
     C                   MOVEL     W$CDLF00      W$CDLF
     C                   MOVEL     W$FL0100      W$FL01
     C                   MOVEL     W$CLFU00      W$CLFU
     C                   MOVEL     W$DEAR00      W$DEAR
     C                   MOVEL     W$DES200      W$DES2
     C                   ENDIF

