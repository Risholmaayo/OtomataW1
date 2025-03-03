def is_binary(s):
    # Periksa setiap karakter dalam string
    for char in s:
        if char not in {'0', '1'}:
            return False
    return True

# Ambil input 
user_input = input("Input: ")

# Periksa input
if is_binary(user_input):
    print(f"'{user_input}' adalah bilangan biner.")
else:
    print(f"'{user_input}' bukan bilangan biner.")
