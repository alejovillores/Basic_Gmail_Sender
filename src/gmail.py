# Libreria de trabajo 
import smtplib


#Constantes
RUTA = 'mensaje.txt'
PUERTO = 587
GMAIL= 'smtp.gmail.com'
mensaje =  "TU MENSAJE "

def registrarse():

    usuario = input("Ingrese el mail de usuario: ")
    password = input("Ingrese la contraseña: ")

    return usuario,password


def enviarMail():
    
    #creamos un servidor server
    server = smtplib.SMTP(GMAIL, PUERTO)
 
    server.starttls()
    usuario,password = registrarse()
    # Login Credentials for sending the mail
    server.login(usuario, password)
    destino  = input("Ingrese el mail de destino: ")


    try:
        server.sendmail(usuario, destino,mensaje)   
        print("Se envio exitosamente email a  %s:" % (destino))

    except :
        print("No se ha podido enviar correctamente el mail")
    
    server.quit()

enviarMail()

