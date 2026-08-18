# Here, we import the random module to generate random IP addresses and numbers for our simulation.
import random

def generate_random_ip_address():
    return f"192.168.1.{random.randint(0,30)}"

def check_firewall_rules(ip_address, rules):
    for rule_ip, action in rules.items():
        if ip_address == rule_ip:
            return action
    return "allow"

def main():
    firewall_rules = {
        "192.168.1.1": "block",
        "192.168.1.5": "block",
        "192.168.1.7": "block",
        "192.168.1.14": "block",
        "192.168.1.17": "block",
        "192.168.1.19": "block",
    }

    for _ in range(12):
        ip_address = generate_random_ip_address()
        action = check_firewall_rules(ip_address, firewall_rules)
        random_number = random.randint(0, 9999)
        print(f"IP_Address: {ip_address}, Action: {action}, Random_Number: {random_number}")

if __name__ == "__main__":
    main()