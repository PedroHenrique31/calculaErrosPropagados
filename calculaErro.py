margemErro=1 #V
Vin=271 #V
Vout=280 #V
def erroSomaSubtracao(erro1,erro2):
        erroTotal=0.0
        
        er1=erro1**2
        er2=erro2**2
        erroTotal=(er1+er2)**(1/2)
        return erroTotal

##  C=A/B (erC/C)=sqrt[(erA/A)²+(erB/B)²]       
def erroDiv(V1,V2,erro1,erro2):
        margemVin=(erro1/V1)**2
        margemVout=(erro2/V2)**2
        
        erroQuadratico=margemVin+margemVout
        C=V1/V2
        erroEstim=erroQuadratico**(1/2)
        erroTotal=C*erroEstim
        return erroTotal
##  C=A*B (erC/C)=sqrt[(erA/A)²+(erB/B)²]
def erroMultiplicacao(A,B,erroA,erroB):
        percentualErro1=(erroA/A)**2
        percentualErro2=(erroB/B)**2
        
        C=A*B
        erroQuadratico=percentualErro1+percentualErro2
        erroEstim=erroQuadratico**(1/2)
        erroTotal=C*erroEstim
        return erroTotal
print("O erro calculado da divisão é ",end="")
erro=erroDiv(Vin,Vout,margemErro,margemErro)
print(erro)
