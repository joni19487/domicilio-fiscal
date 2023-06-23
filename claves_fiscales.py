import pandas as pd
def clave_fiscal(consulta):
    df = pd.read_csv("clave fiscal.csv", encoding="latin-1")   
    
   
    for row, datos in df.iterrows():
        for dato in datos:      
            cuit=dato[0:11]
            clave=dato[14:]
            if cuit==consulta:
               
               return clave
               
             
     
 

        
