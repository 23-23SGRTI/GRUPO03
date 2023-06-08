from io import open
import time

def verifica_primo(n):
	c=0
	x=2
	if n>=2:
		while x<=n/2:
			if n%x==0:
				c=c+1
				x=x+1
			else:
				x=x+1
		if c==0:
			return True
		else:
			return False
	else:
		return False
def genera_primos(n):
	lp=[]
	x=2
	while n!=0:
		if verifica_primo(x)==True:
			lp.append(x)
			x=x+1
			n=n-1
		else:
			x=x+1
	return lp
def pyq():
	
	p=int(input("\tValor de (p)="))
	while verifica_primo(p)==False:
		print("\t(p) tiene que ser un numero primo !!!")
		p=int(input("\tValor de (p)="))
	q=int(input("\tValor de (q)="))
	while verifica_primo(q)==False or q==p:
		print("\t(q) tiene que ser un numero primo diferente de (p) !!!")
		q=int(input("\tValor de (q)="))
	lpq=[p,q]
	return lpq
	
def calculae(ø):
	e=2
	le=[]
	while e>1 and e<ø :
		if mcd(e,ø)==1:
			le.append(e)
			e=e+1
		else:
			e=e+1
	print("\nVALORES PARA (e)="+str(le))
	e=int(input("\n\tValor de (e)="))
	while mcd(e,ø)!=1:
		print("\n\tEliga un valor de la lista !!!")
		e=int(input("\n\tValor de (e)="))
	return e

def mcd(e,ø):
	m=ø%e
	while m!=0:
		ø=e
		e=m
		m=ø%e
	return e

def congruente(e,ø):
	k=1
	m=(1+(k)*(ø))%(e)
	while m!=0:
		k=k+1
		m=(1+(k)*(ø))%(e)
	d=int((1+(k)*(ø))/(e))
	return d

def cifrarmensaje(msj,key):
	msj=msj.upper()
	lm=msj.split(" ")
	cmc=""
	lmc=[]
	for i in lm:
		pal=cifrarpalabra(i,key)
		lmc.append(pal)
	for j in lmc:
		cmc=cmc+str(j)+" "
	return cmc

def cifrarpalabra(m,k):
	lpc=[]
	lp=[]
	n,e=k
	cpc=""
	for i in m:
		x=buscarpos(i)
		lp.append(x)
	for j in lp:
		c=(j**e)%n
		lpc.append(c)
	for k in lpc:
		cpc=cpc+str(k)+" "
	return cpc	
	

def buscarpos(x):
	alf="ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
	c=0
	for i in alf:
		if x==i:
			return c
		else:
			c=c+1	

def descifrarmensaje(msj,key):
	msj=msj.upper()
	lm=msj.split("  ")
	cmc=""
	lmc=[]
	for i in lm:
		pal=descifrarnumero(i,key)
		lmc.append(pal)
	for j in lmc:
		cmc=cmc+str(j)+" "
	return cmc

def descifrarnumero(m,k):
	lnc=[]
	ln=[]
	n,d=k
	cnc=""
	men=m.split(" ")
	for i in men:
		x=int(i)
		ln.append(x)
	for j in ln:
		m=(j**d)%n
		lnc.append(m)
	for k in lnc:
		l=buscarlet(k)
		cnc=cnc+str(l)
	return cnc

def buscarlet(x):
	alf="ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
	c=0
	for i in alf:
		if x==c:
			return i
		else:
			c=c+1	


print("\t\t\t\t//////////////// METODO DE CIFRADO (RSA) ///////////////////////")

print("\nELEGIMOS 2 VALORES DE NUMEROS PRIMOS DISTINTOS")
lista_primos=genera_primos(50)
p,q=pyq()

n=p*q

ø=(p-1)*(q-1)

e=calculae(ø)

d=congruente(e,ø)

print("\nLLAVE PUBLICA Y PRIVADA ")
key_public=[n,e]
key_private=[n,d]
print("\n\tLLAVE PUBLICA="+str(key_public)+"\n\tLLAVE PRIVADA="+str(key_private))



inicio = time.time()
cien_ci=open("100des.txt", "r")
cien=cien_ci.read()
print("\nAHORA PODEMOS DESCIFRAR MENSAJES DE 100 PALABRAS CON EL METODO (RSA)")
print("\n\tMensaje Cifrado : ")
mensaje_descifrado=descifrarmensaje(cien,key_private)
print("\tMensaje Descifrado : "+str(mensaje_descifrado))
fin = time.time()
tiempo=fin-inicio
print("EL TIEMPO QUE SE DEMORO EN DECIFRAR EL MENSAJE DE 100 PALABRAS FUE: " + str(tiempo) + " segundos")



#inicio = time.time()
#mil_ci=open("1000des.txt", "r")
#mil=mil_ci.read()
#print("\nAHORA PODEMOS DESCIFRAR MENSAJES DE 1000 PALABRAS CON EL METODO (RSA)")
#print("\n\tMensaje Cifrado : ")
#mensaje_descifrado=descifrarmensaje(mil,key_private)
#print("\tMensaje Descifrado : "+str(mensaje_descifrado))
#fin = time.time()
#tiempo=fin-inicio
#print("EL TIEMPO QUE SE DEMORO EN DECIFRAR EL MENSAJE DE 1000 PALABRAS FUE: " + str(tiempo) + " segundos")



#inicio = time.time()
#dmil_ci=open("10000des.txt", "r")
#dmil=dmil_ci.read()
#print("\nAHORA PODEMOS DESCIFRAR MENSAJES DE 10000 PALABRAS CON EL METODO (RSA)")
#print("\n\tMensaje Cifrado : ")
#mensaje_descifrado=descifrarmensaje(dmil,key_private)
#print("\tMensaje Descifrado : "+str(mensaje_descifrado))
#fin = time.time()
#tiempo=fin-inicio
#print("EL TIEMPO QUE SE DEMORO EN DECIFRAR EL MENSAJE DE 10000 PALABRAS FUE: " + str(tiempo) + " segundos")



#inicio = time.time()
#cmil_ci=open("100000des.txt", "r")
#cmil=cmil_ci.read()
#print("\nAHORA PODEMOS DESCIFRAR MENSAJES DE 100000 PALABRAS CON EL METODO (RSA)")
#print("\n\tMensaje Cifrado : ")
#mensaje_descifrado=descifrarmensaje(cmil,key_private)
#print("\tMensaje Descifrado : "+str(mensaje_descifrado))
#fin = time.time()
#tiempo=fin-inicio
#print("EL TIEMPO QUE SE DEMORO EN DECIFRAR EL MENSAJE DE 100000 PALABRAS FUE: " + str(tiempo) + " segundos")




#inicio = time.time()
#mill_ci=open("1000000des.txt", "r")
#mill=mill_ci.read()
#print("\nAHORA PODEMOS DESCIFRAR MENSAJES DE 1000000 PALABRAS CON EL METODO (RSA)")
#print("\n\tMensaje Cifrado : ")
#mensaje_descifrado=descifrarmensaje(mill,key_private)
#print("\tMensaje Descifrado : "+str(mensaje_descifrado))
#fin = time.time()
#tiempo=fin-inicio
#print("EL TIEMPO QUE SE DEMORO EN DECIFRAR EL MENSAJE DE 100000 PALABRAS FUE: " + str(tiempo) + " segundos")