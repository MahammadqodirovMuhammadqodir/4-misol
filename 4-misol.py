def besh_hiylasi(raqam):
    
    raqam_satr = str(raqam)  
    uzunlik = len(raqam_satr)  
    
    natija = "".join([str(int(r) * (5 ** uzunlik)) for r in raqam_satr]) 
    return int(natija)

print(besh_hiylasi(123))  
print(besh_hiylasi(4321)) 
print(besh_hiylasi(5))    
