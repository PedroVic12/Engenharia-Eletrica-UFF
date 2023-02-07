import requests
from pymavlink import mavutil

# Cria uma conexão MAVLink em modo leitura (comport)
master = mavutil.mavlink_connection('comport', baud=115200, source_system=255)

# Espera por uma mensagem HEARTBEAT
msg = master.recv_match(type='HEARTBEAT', blocking=True)

# Extrai informações da mensagem HEARTBEAT
flight_mode = msg.custom_mode
battery_voltage = msg.voltage_battery

# Envia as informações para o servidor via requisição HTTP
data = {
    'flight_mode': flight_mode,
    'battery_voltage': battery_voltage
}
response = requests.post('http://example.com/data', data=data)
