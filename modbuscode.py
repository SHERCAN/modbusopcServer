from pymodbus.server.sync import StartTcpServer
from pymodbus.device import ModbusDeviceIdentification
from pymodbus.datastore import ModbusSequentialDataBlock
from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext
# from twisted.internet import reactor

# Configurar los bloques de datos
store = ModbusSlaveContext(
    di=ModbusSequentialDataBlock(0, [17]*100),
    co=ModbusSequentialDataBlock(0, [17]*100),
    hr=ModbusSequentialDataBlock(0, [17]*100),
    ir=ModbusSequentialDataBlock(0, [17]*100))

context = ModbusServerContext(slaves=store, single=True)

# Definir la información de identificación del dispositivo
# identity = ModbusDeviceIdentification.create()

# Iniciar el servidor Modbus TCP
StartTcpServer(context, address=("0.0.0.0", 502))

print("Servidor Modbus TCP iniciado en localhost:5020")
# reactor.run()