ip = input("Enter IP address/subnet bits: ")
ip_class = ""
net_mask = ""
sub_ip = ""

# Check for valid input
if "/" not in ip or len(ip.split("/")) != 2:
    print("Invalid input!")
    exit(1)

# Split IP address and subnet bits
ip_addr = ip.split("/")[0]
sub_bits = ip.split("/")[1]

# Check for valid IP address
ip_octets = ip_addr.split(".")
if len(ip_octets) != 4:
    print("Invalid IP address!")
    exit(1)
for octet in ip_octets:
    if not octet.isnumeric() or int(octet) < 0 or int(octet) > 255:
        print("Invalid IP address!")
        exit(1)

# Check for valid subnet bits
if not sub_bits.isnumeric() or int(sub_bits) < 0 or int(sub_bits) > 32:
    print("Invalid subnet bits!")
    exit(1)

# Get IP address class
first_octet = int(ip_octets[0])
if 1 <= first_octet <= 126:
    ip_class = "Class A"
elif 128 <= first_octet <= 191:
    ip_class = "Class B"
elif 192 <= first_octet <= 223:
    ip_class = "Class C"
else:
    ip_class = "Invalid Class"

# Get network mask
if ip_class == "Class A":
    net_mask = "255.0.0.0"
elif ip_class == "Class B":
    net_mask = "255.255.0.0"
elif ip_class == "Class C":
    net_mask = "255.255.255.0"
else:
    net_mask = "Invalid Mask"

# Get subnet IP address
sub_ip_octets = []
for i in range(4):
    sub_ip_octets.append(str(int(ip_octets[i]) & int(net_mask.split(".")[i])))
sub_ip = ".".join(sub_ip_octets)

# Display results
print("IP Address:", ip_addr)
print("IP Address Class:", ip_class)
print("Network Mask:", net_mask)
print("Subnet IP Address:", sub_ip)
