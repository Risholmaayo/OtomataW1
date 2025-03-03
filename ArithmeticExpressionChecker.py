def is_arithmetic_expression(expression):
    try:
        # Evaluasi ekspresi
        eval(expression)
        return True
    except:
        # Jika error, ekspresi tidak valid
        return False

# Ambil input 
user_input = input("Input : ")

# Periksa input
if is_arithmetic_expression(user_input):
    print(f"'{user_input}' adalah ekspresi aritmetika.")
else:
    print(f"'{user_input}' bukan ekspresi aritmetika.")
