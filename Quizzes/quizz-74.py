def build_packet_pkg(mac_rx:str, ip_rx:str, mac_tx:str, ip_tx:str, payload:str) -> str: # max data packet is 4 characters
    output = []
    # for i in range len(data) steps of 4
    for i in range(0, len(payload), 4):
        packet_data = ""
        for j in range(4):
            if i + j < len(payload):
                packet_data += payload[i + j]
            else:
                pass
        output.append(f"{mac_rx}|{ip_rx}|{mac_tx}|{ip_tx}|{packet_data}")
    return output

print(build_packet_pkg("00:00:00:00:00:00", "192.168.0.0", "00:00:00:00:00:01", "192.168.0.1", "hello world"))
            
                