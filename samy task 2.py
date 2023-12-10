from ethereum.utils import check_checksum

def is_valid_ethereum_address(address):
    try:
        is_valid_checksum = check_checksum(address)
        return is_valid_checksum
    except ValueError:
        return False

def main():
    # Take Ethereum address as user input
    user_input_address = input("Enter an Ethereum address: ")

    # Remove any leading/trailing whitespaces from user input
    user_input_address = user_input_address.strip()

    # Check if the entered address is valid
    if is_valid_ethereum_address(user_input_address):
        print(f"The Ethereum address {user_input_address} is valid.")
    else:
        print(f"The Ethereum address {user_input_address} is not valid.")

if __name__ == "__main__":
    main()
