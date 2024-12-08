from Crypto.PublicKey import RSA
from Crypto.Cipher import AES
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Random import get_random_bytes
import colorama
import random
import os

# Colour Objects, Used For Nicer Output
reset = colorama.Fore.RESET
red = colorama.Fore.RED
yellow = colorama.Fore.YELLOW
blue = colorama.Fore.BLUE
magenta = colorama.Fore.MAGENTA

# Aborts the program and says goodbye to the user in German
def ceasefire() -> None:
    # Tschüss is German for an informally goodbye
    print(f"{magenta}Aborting, Tschüss!{reset}")
    # Exits The Program
    exit()

# Overwrites a file with random bytes 10 times, destroying all data in the file
# The harpoon is a long-range, all weather cruise missle designed to destroy enemy surface ships/vessels
def harpoon(file: str) -> None:
    for cycle in range(10):
        # Opens file in read and write mode
        with open(file, "r+b") as f:
            # The extra 3000 bytes are meant to make it hard to recover the file
            amount_of_bytes_to_write = os.path.getsize(file) + 3000
            random_bytes = random.randbytes(5000)
            f.write(random_bytes)
            f.truncate()

# Encrypts a file with AES, encrypts the encryption key with RSA, than throws the now encrypted key away
def scramble_coms(file: str) -> None:
    # Generate an RSA key pair and cipher# NOTE: WORKS!!! - remove me after the destroyer is done
    rsa_keys = RSA.generate(4096)
    rsa_public_key = rsa_keys.publickey()
    rsa_cipher = PKCS1_OAEP.new(rsa_public_key)
    # Generate an AES key and Cipher
    aes_key = get_random_bytes(32)
    aes_cipher = AES.new(aes_key, AES.MODE_CTR)
    # Read the file data
    with open(file, "rb") as f:
        file_data = f.read()
        # Adds some junk data to the file data
        file_data += random.randbytes(15000)
        # Encryptes the file data
        file_data = aes_cipher.encrypt(file_data)
    # Encrypts the AES key with the RSA cipher to make it a little harder to recover, odd but its extra security just in case
    aes_key = rsa_cipher.encrypt(aes_key)
    # Overwrites the now encrypted AES key with random bytes (256-bits)
    aes_key = get_random_bytes(32)
    # Deletes the reference to the aes key
    del aes_key
    # Write the encrypted data to the file (open in write-bytes mode)
    with open(file, "wb") as f:
        f.write(file_data)

# Destroys (harpoons) and encryptes (scrambles coms) a file, than deletes it
def torpedo(file: str) -> None:
    try:
        # Encrypt the file
        scramble_coms(file)
        # Destory the file (overwrite the entire file 10 times with random data)
        harpoon(file)
        # Delete the file
        os.remove(file)
    except FileNotFoundError:
        print(f"{red}[!] Error: the following file was not found and must be destroyed{reset}: {yellow}{file}{reset}".title())
        print(f"{red}[!] The file may contain sensitive data!{reset}".title())
        try:
            file_path = input(f"{magenta}Please Specify The Exact Path To The File So It Can Be Destroyed [Ex: ./Hackesoup/Temp/{blue}{file}{reset}{magenta}]{reset}: ")
        except KeyboardInterrupt:
            print(f"{yellow}[!] Okay but just know the file will not be destroyed{reset}".title())
        except:
            print(f"{red}[!] Another error has occured, the file will not be destroyed!{reset}".title())
            print(f"{red}[!] Exiting{reset}".title())

    except:
        print(f"{red}[!] Error: Something went wrong during the file destruction process!{reset}".title())

# Pretty much the same as the original torpedo function, except the user is prompted for a file to destory
def specialized_torpedo():
    file = input("Please Specify a File To Destroy, Make Sure To Include The Full Path [ex: ./a/b/c.txt]: ")
    try:
        try:
            # Preforms a basic security check
            file_path_list = file.split("/")
            if ".Hackesoup" in file_path_list or "Hackesoup" in file_path_list:
                print(f"{red}[!] Warning: the file specified might be used by Hackesoup.{reset}".title())
                keep_firing = input("Are You Sure You Want To Continue? [y or n]:  ")
                if keep_firing.lower() != "y":
                    ceasefire()
            else:
                pass
        except:
            print(f"{red}[!] Error: Invalid Input!")
        # Encrypt the file
        scramble_coms(file)
        # Destory the file (overwrite the entire file 10 times with random data)
        harpoon(file)
        # Delete the file
        os.remove(file)
    except FileNotFoundError:
        print(f"{red}[!] Error: the file could not find the file under the specified path!{reset}", f"{yellow}File Path{reset}: {blue}{file}{reset}".title())
    except ValueError:
        print(f"{red}[!] Error: Invalid input!{reset}".title())
    except:
        print(f"{red}[!] Error: Something went wrong during the file destruction process!{reset}".title())