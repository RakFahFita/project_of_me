C=25000
P=16000
V=10000
JN=500
print("voici notre menu")
print("crevette= 25000ar, poisson frite= 16000ar, viande sauté+legumes= 10000ar")
client=str(input("que voulais vous? : "))
if(client=="crevette"):
    prix=C
elif(client=="poisson frite"):
    prix=P
elif(client=="viande sauté avec legumes"):
    prix=V


J=str(input("voulez vous du jus : "))
if(J=="oui"):
    prix=prix+JN
else:
    prix=prix
print("votre addition est",prix,"Ar.")