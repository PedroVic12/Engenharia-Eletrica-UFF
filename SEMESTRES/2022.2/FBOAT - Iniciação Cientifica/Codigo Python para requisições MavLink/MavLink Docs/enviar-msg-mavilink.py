import struct
from pymavlink import mavutil

# Cria uma conexão MAVLink em modo escrita (comport)
master = mavutil.mavlink_connection('comport', baud=115200, source_system=255)

# Define a mensagem a ser enviada (por exemplo, HEARTBEAT)
msg = mavutil.mavlink.MAVLink_heartbeat_message(
    mavutil.mavlink.MAV_TYPE_GCS,
    mavutil.mavlink.MAV_AUTOPILOT_INVALID,
    0, 0, 0)

# Envia a mensagem
master.mav.send(msg)
