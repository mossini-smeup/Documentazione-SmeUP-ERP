
**> Controllo esistenza coda B£QQ99 : 
 :  : IF FE( :  : DEC T(OJ) P(*JOBQ) K(B£QQ99) LI(*LIBL)) OP(=) F2(1) CM(       »_r_>>_1_ La coda è presente! Nessuna operazione richiesta)
 :  : IF FE( :  : DEC T(OJ) P(*JOBQ) K(B£QQ99) LI(*LIBL)) OP(=) F2(1) CM( :  : GOTO NNJOBQ99)
       »_r_>>_1_ Jobq B£QQ99 non presente!
 :  : INI   Vuoi creare la jobq B£QQ99?
 :  : CMD ?CRTJOBQ JOBQ(SMESYS/B£QQ99) TEXT('Coda esecuzione lavori B£QQ01')
 :  : CMD ?ADDJOBQE SBSD(QBATCH) JOBQ(SMESYS/B£QQ99) MAXACT(*NOMAX) SEQNBR(900)
 :  : FIN
 :  : TAG NNJOBQ99

**> Controllo esistenza coda B£JQ01 : 
 :  : IF FE( :  : DEC T(OJ) P(*JOBQ) K(B£JQ01) LI(*LIBL)) OP(=) F2(1) CM(       »_r_>>_1_ La coda è presente! Nessuna operazione richiesta)
 :  : IF FE( :  : DEC T(OJ) P(*JOBQ) K(B£JQ01) LI(*LIBL)) OP(=) F2(1) CM( :  : GOTO NNJOBQ01)
       »_r_>>_1_ Jobq B£JQ01 non presente!
 :  : INI   Vuoi creare la jobq B£JQ01?
 :  : CMD ?CRTJOBQ JOBQ(SMESYS/B£JQ01) TEXT('Coda seriale esecuzione lavori')
 :  : CMD ?ADDJOBQE SBSD(QBATCH) JOBQ(SMESYS/B£JQ01) MAXACT(1) SEQNBR(901)
 :  : FIN
 :  : TAG NNJOBQ01

