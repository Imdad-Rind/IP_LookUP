def ip_Class_Info(ip_address):
    split_ip = ip_address.split(".")
    ip = int(split_ip[0])

    if ip in range(0, 128):
        return "A"

    elif ip in range(128, 192):
        return "B"

    elif ip in range(192, 224):
        return "C"

    elif ip in range(224, 240):
        return "D"

    elif ip in range(240, 256):
        return "E"


def ip_host_and_net_info(ip_class, ip_address):

    split_ip = ip_address.split(".")
    ip_last_part = split_ip[3]

    if "/" in str(ip_last_part):
        ip_last_part = split_ip[3].split("/")
        cidr = int(ip_last_part[1])

        if ip_class == "A":

            a_default_net_bits = 8
            a_default_host_bits = 24

            new_net_bits = a_default_net_bits - cidr
            new_host_bits = a_default_host_bits + new_net_bits

            number_of_networks = 2 ** new_net_bits
            number_of_hosts = 2 ** new_host_bits
            usable_ip = number_of_hosts - 2

            class_a_net_n_host = {"networks": number_of_networks, "hosts": number_of_hosts, "usableIp": usable_ip}
            return class_a_net_n_host

        elif ip_class == "B":
            new_net_bits = cidr - 16
            b_default_host_bits = 16
            new_host_bits = b_default_host_bits - new_net_bits

            number_of_networks = 2 ** new_net_bits
            number_of_hosts = 2 ** new_host_bits
            usable_ip = number_of_hosts - 2

            class_a_net_n_host = {"networks": number_of_networks, "hosts": number_of_hosts, "usableIp": usable_ip}
            return class_a_net_n_host

        elif ip_class == "C":
            new_net_bits = cidr - 24
            b_default_host_bits = 8
            new_host_bits = b_default_host_bits - new_net_bits

            number_of_networks = 2 ** new_net_bits
            number_of_hosts = 2 ** new_host_bits
            usable_ip = number_of_hosts - 2

            class_a_net_n_host = {"networks": number_of_networks, "hosts": number_of_hosts, "usableIp": usable_ip}
            return class_a_net_n_host

        elif ip_class == "D":
            return None
        elif ip_class == "E":
            return None
    else:
        raise "CIDR is not provided"

