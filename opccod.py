import asyncio
import sys
sys.path.insert(0, "..")

from asyncua import ua, Server
from asyncua.common.node import Node
from asyncua.server.users import UserRole, User
users_db = {
    "admin":"admin"
}
class UserManager:
    def get_user(self, iserver, username=None, password=None, certificate=None):
         if username in users_db and password == users_db[username]:
             return User(role=UserRole.User)

async def main():
    server = Server(user_manager=UserManager())
    await server.init()
    server.set_endpoint("opc.tcp://0.0.0.0:4840/2749614/")
    # server.internal_server.InternalServer()
    uri = "http://ejemplo.org"
    idx = await server.register_namespace(uri)
    # Obtener el nodo raíz de Objects
    objects = server.nodes.objects
    # Crear un objeto en el servidor
    myobj = await objects.add_object(idx, "LaMejorFicha")
    # Crear una variable en el objeto
    myvar = await myobj.add_variable(idx, "Darly", "¿A que hora sales?")
    myvar1 = await myobj.add_variable(idx, "Edad", 56)
    myvar2 = await myobj.add_variable(idx, "Altura", 160.56)
    # Hacer que la variable sea editable
    await myvar.set_writable()
    await myvar1.set_writable()
    # Iniciar el servidor
    async with server:
        print("Servidor iniciado en opc.tcp://0.0.0.0:4840")
        while True:
            await asyncio.sleep(1)

if __name__ == "__main__":
    asyncio.run(main())