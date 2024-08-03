from opcua import ua, Server
import datetime
import time

if __name__ == "__main__":
    server = Server()
    server.set_endpoint("opc.tcp://127.0.0.1:4840/freeopcua/server/")
    server.set_server_name("Lo mejor soy yo")
    server.set_security_policy([ua.SecurityPolicyType.NoSecurity])
    uri = "http://sena.opcua.yefar"
    idx = server.register_namespace(uri)
    objects = server.get_objects_node()
    myobj = objects.add_object(idx, "MyObject")
    myobj1 = objects.add_object(idx, "Cositas")
    myvar = myobj.add_variable(idx, "MyVariable", 0)
    myvar1 = myobj.add_variable(idx, "Consola", 5)
    cumple= myobj1.add_variable(idx,"Cumpleañera",26.1)
    cumple.set_writable()
    myvar.set_writable()
    server.start()
    print("Servidor OPC UA iniciado en opc.tcp://0.0.0.0:4840/freeopcua/server/")

    try:
        while True:
            # Simular una actualización de la variable
            new_value = datetime.datetime.now()
            # print(f"Actualizando valor a: {new_value}")
            #myvar.set_value(new_value)
            time.sleep(1)
    except KeyboardInterrupt:
        print("Servidor detenido por el usuario.")
    finally:
        # Detener el servidor antes de salir
        server.stop()
        print("Servidor OPC UA detenido.")
