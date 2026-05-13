import socket

ip = input("IP adresi gir: ")
baslangic = int(input("Başlangıç portu: "))
bitis = int(input("Bitiş portu: "))
timeout = float(input("Timeout süresi: "))

print(f"\n{ip} taranıyor...\n")

acik_portlar = []

for port in range(baslangic, bitis + 1):

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    sock.settimeout(timeout)

    result = sock.connect_ex((ip, port))

    if result == 0:

        try:
            servis = socket.getservbyport(port)
        except:
            servis = "Bilinmiyor"

        print(f"𖤝𖤝 Port {port} AÇIK | Servis: {servis}")

        acik_portlar.append(port)

    sock.close()

print("\nTarama bitti!")

if len(acik_portlar) == 0:
    print("Açık port bulunamadı.")
else:
    print("Açık portlar:")

    for port in acik_portlar:
        print(port)