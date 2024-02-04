import socket


class Server ():
    
    def __init__(self, port = 3000):
        
        # dirección y un puerto
        self.host = socket.gethostname()
        self.port = port
        self.conn = self.connectionInit()
        
        
    def connectionInit (self):
        print (self.host)
    
        # creamos el socket para comunicarlo
        server_socket = socket.socket()
        
        # asociamos al socket la direccion y el puerto
        server_socket.bind((self.host,self.port))
        
        # número de clientes que puede atender mi servidor depende del número
        server_socket.listen(2)
        
        conn,self.address = server_socket.accept()
        return conn
    
    
    def run(self): 
        
        while True:
            
            #recibimos los datos de los clientes
            datos = self.conn.recv(1024).decode()
            
            print ("enviado desde cliente " + str(datos))
            
            datos = input (' Escribe al cliente -> ')
            
            self.conn.send(datos.encode())
            
        self.conn.close()
    
servidor = Server()
servidor.run()
    
        