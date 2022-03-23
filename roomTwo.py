from telnetlib import Telnet as T
from robot.api.deco import keyword

def attach(ue, cell):
    address = "na-robot.ddns.net"
    port = 8012
    data = "attach  ue={} cell={}".format(ue, cell)
    conn = T(address, port)
    conn.write(data.encode())
    response = conn.read_all().decode()
    print(response)
    # conn.close()
    return response

def detach(ue):
    address = "na-robot.ddns.net"
    port = 8012
    data = "detach  ue={}".format(ue)
    conn = T(address, port)
    conn.write(data.encode())
    response = conn.read_all().decode()
    print(response)
    conn.close()
    return response


def start_traffic(ue, mbps, bearer):
    address = "na-robot.ddns.net"
    port = 8012
    data = 'trf_data_start  ue={} mbps={} baerer={} '.format(ue, mbps, bearer)
    conn = T(address, port)
    conn.write(data.encode())
    response = conn.read_all().decode()
    print(response)
    conn.close()
    return response


def stop_traffic(ue, bearer):
    address = "na-robot.ddns.net"
    port = 8012
    data = 'trf_data_stop   ue={} baerer={} '.format(ue, bearer)
    conn = T(address, port)
    conn.write(data.encode())
    response = conn.read_all().decode()
    print(response)
    conn.close()
    return response

@keyword("POSITIVE_RESPONSE_COMPARATOR")
def compare_positive_response():
    conn = T("na-robot.ddns.net", 8012)
    conn.write("attach  ue=1 cell=1".encode())
    response = conn.read_all().decode()
    print(response)
    return response

@keyword("NEGATIVE_RESPONSE_COMPARATOR")
def compare_negative_response():
    conn = T("na-robot.ddns.net", 8012)
    conn.write("attach  ue=2 cell=5".encode())
    response = conn.read_all().decode()
    print(response)
    return response
