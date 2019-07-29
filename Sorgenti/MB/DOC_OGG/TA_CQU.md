# CQU - Modalità skip-lott
 :  : DEC T(ST) K(CQU)
## OBIETTIVO
Questa tabella ha due diversi utilizzi : 
- Determinazione del piano di campionamento : 
    Permette di definire la modalità di skip-lot per i lotti in accettazione materale
- Determinazione dell'applicabilità della fase di collaudo
    Permette di definire la frequanza con cui le singole fasi di un ciclo di collaudo devono essere applicate
## CONTENUTO DEI CAMPI
 :  : FLD T$MSKI **Metodo di skip**
Definisce il tipo di grandezza temporale che deve essere considerata
Il valore  S=Settimane è equivalente ad un periodo G=Giorni con moltiplicatore 7
           M=Mesi considera come data limite lo stesso giorno del (o dei) mesi precedenti
           A=Mesi considera come data limite lo stesso giorno dell' (o degli) anni precedenti
Il valore  1=Nella settimana considera il periodo che inizia il lunedi e termina la domenica della settimana
                             presa in esame
           2=Nel mese        considera il periodo che inizia il giorno 1 e termina il giorno 31 (o 28 o 29 o 30)
                             del mese della data presa in esame
           3=Nel bimestre    come il caso 2, solo che viene considerato il bimestre. I bimestri sono cosi suddivisi : 
                             Gennaio   - Febbraio
                             Marzo     - Aprile
                             Maggio    - Giugno
                             Luglio    - Agosto
                             Settembre - Ottobre
                             Novembre  - Dicembre
           4=Nel trimestre   come il caso 2, solo che viene considerato il trimestre. I trimestri sono cosi suddivisi : 
                             Gennaio   - Marzo
                             Aprile    - Giugno
                             Luglio    - Settembre
                             Ottobre   - Dicembre
           5=Nel quadrimestre come il caso 2, solo che viene considerato il quadrimestre. I quadrimestri sono suddivisi : 
                             Gennaio   - Aprile
                             Maggio    - Agosto
                             Settembre - Dicembre

           6=Nel semestre come il caso 2, solo che viene considerato il semestre. I semestri sono suddivisi : 
                             Gennaio   - Giugno
                             Luglio    - Dicembre

           7=Nell'anno come il caso 2, solo che viene considerato l'anno corrente

I valori 1=Nella settimana 2=Nel mese 3=Nell'anno, a differenza dei valori S=Settimane M=Mesi A=Anni
considerano i periodi all'interno del periodo. Ad esempio se utilizzo il valore S significa che viene
considerato un intervallo temporale di 7 giorni, mente il valore 1 considera il periodo che inizia il lunedi
e termina la domenica, quindi se effettuo un collaudo il sabato, ed il lunedi successivo questo collaudo
dovrà essere rieffettuato, in quanto la settimana è cambiata, anche se sono trascorsi solo 2 giorni.
Per i valori 1 2 3 4 5 6 e 7 NON verrà considerato il campo Moltiplicatore.

 :  : FLD T$FTMO **Moltiplicatore**
E' il moltiplicatore che deve essere applicato alla grandezza precedente : 
ad esempio se il campo Metodo di skip ha valore G Giorni e quasto campo ha valore 3
significa che deve essere considerato un tempo di 3 giorni.
Questo campo NON è significativo per i seguenti valori del campo Metodo di skip : 
1 Nella settimana
2 Nel mese
3 Nel bimestre
4 Nel trimestre
5 Nel quadrimestre
6 Nel semestre
7 Nell'anno
