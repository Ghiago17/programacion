class persona:   
    def __init__ (self, nombre, apellido,cedula ,correo ,telefono):
        
       self.nombre = nombre
       self.apellido = apellido
       self.correo = correo
       self.cedula = cedula
       self.telefono = telefono
       
    def obtenernombre(self):
        return F' Mi nombre es {self.nombre}'
    
    def obtenerapellido(self):
        return F'mi apellido es {self.apellido}'
        
    def obtenertelefono(self):
        return F'mi telefono es {self.telefono}'

    def obtenercorreo(self):
        return F' mi correo es {self.correo}'
       
    def obtenercedula(self):
        return F'mi cedula es{self.cedula}'
  
print("nombre:jay-z","telefono:3243829748","apellido:valencia","correo:jayzvalencia10.2@gmail.com","cedula:1042582171")
