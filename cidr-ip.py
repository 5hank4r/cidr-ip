import sys
import ipaddress

def generate_ips_from_subnet(subnet):
    try:
        # Create an IP network object
        network = ipaddress.ip_network(subnet.strip(), strict=False)
        
        # Generate and print all IP addresses in the network
        for ip in network:
            print(ip)
    
    except ValueError as e:
        # Handle invalid subnet format but do not print errors to stdout
        pass

if __name__ == "__main__":
    # Read from standard input (stdin)
    for line in sys.stdin:
        generate_ips_from_subnet(line)
