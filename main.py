import typer
import random
import string


app = typer.Typer()


lower_char = string.ascii_lowercase
upper_char = string.ascii_uppercase
speacial_char = string.punctuation
num = '0123456789'


@app.command()
def ultra_secure_pass(size):
    password = ''.join([random.choice(num +
        lower_char + upper_char + speacial_char)
        for n in range(int(size))])
    print(password)



@app.command()
def upper_char_pass(size):
    password = ''.join([random.choice(
        num + upper_char + speacial_char)
        for n in range(int(size))])
    print(password)



@app.command()
def lower_char_pass(size):
    password = ''.join([random.choice(
        num + lower_char + speacial_char)
        for n in range(int(size))])
    print(password)


if __name__ == "__main__":
    app()