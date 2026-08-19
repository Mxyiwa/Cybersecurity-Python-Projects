# Here, we import the random module to generate random IP addresses and numbers for our simulation.
import random

# The generate_random_ip_address function generates a 
# random IP address in the range of
def generate_random_ip_address():
    return f"192.168.1.{random.randint(0,30)}"

# The check_firewall_rules function checks if a given IP 
# address is present in the firewall rules.
def check_firewall_rules(ip_address, rules):
    for rule_ip, action in rules.items():
        if ip_address == rule_ip:
            return action
    return "allow"


# The main function serves as the entry point for the simulation. 
# It defines a set of firewall rules, generates random IP addresses, 
# checks them against the rules, and prints the results along with a random number.
def main():
    firewall_rules = {
        "192.168.1.1": "block",
        "192.168.1.5": "block",
        "192.168.1.7": "block",
        "192.168.1.14": "block",
        "192.168.1.17": "block",
        "192.168.1.19": "block",
    }


# We run the simulation for 12 iterations using a for loop, 
# generating a random IP address each time,
# checking it against the firewall rules, 
# and printing the result along with a random number.
    for _ in range(12):
        ip_address = generate_random_ip_address()
        action = check_firewall_rules(ip_address, firewall_rules)
        random_number = random.randint(0, 9999)
        print(f"IP_Address: {ip_address}, Action: {action}, Random_Number: {random_number}")



# This function is called the main function, 
# which serves as the entry point for the simulation. 
# It generates random IP addresses, checks them against predefined firewall rules, 
# and prints the results along with a random number.
if __name__ == "__main__":
    main()