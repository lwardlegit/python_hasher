from Hash_maker import Hash_maker
hashmaker = Hash_maker("my_hash")


def main():
    hashmaker.random_string()
    print(f"random string:  {hashmaker.value}")
    hashmaker.hash_string()
    print(f"hash: {hashmaker.hash}")

main()
