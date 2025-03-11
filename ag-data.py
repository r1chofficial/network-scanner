import nmap

def scan_network(ip_range):
    
    nm = nmap.PortScanner()
    
    print(f"Taranıyor: {ip_range}...")
    
    
    nm.scan(hosts=ip_range, arguments='-sn -PE -PS')
    
    
    if not nm.all_hosts():
        print("Hiçbir cihaz bulunamadı. Lütfen IP aralığını ve ağ yapılandırmanızı kontrol edin.")
    else:
        print("Ağdaki cihazlar:")
        for host in nm.all_hosts():
            if 'mac' in nm[host]['addresses']:
                mac_address = nm[host]['addresses']['mac']
            else:
                mac_address = "Bilinmiyor"
            
            print(f"IP: {host}, MAC: {mac_address}, Durum: {nm[host].state()}")

if __name__ == "__main__":
    
    ip_range = "192.168.0.0/24"
    
    # Ağı tarama
    scan_network(ip_range)