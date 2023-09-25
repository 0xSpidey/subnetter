import ipaddress, sys

def main():
    try:
        cidr = sys.argv[1]
        prefix = int(sys.argv[2])
        for subnet in ipaddress.ip_network(cidr).subnets(new_prefix=prefix):
            print(subnet)

    except IndexError:
        print("Error while parsing arguments.")
        print("Usage: python3 subnet.py <CIDR> <prefix>")
        sys.exit(1)
    except Exception as e:
        print(e)
        print("Ex: python3 subnet.py 1.1.0.0/16 24")
        sys.exit(1)

if __name__ == "__main__":
    main()
