# break = Stop the loop completely.
# continue = Skip the current iteration and move to the next one.
for i in range(1, 11):
    if i == 5:
        break

    print(i)

#break with while loop

correct_password = "python123"

while True:
    password = input("Enter password: ")

    if password == correct_password:
        print("Access Granted")
        break

# continue example: skips even number

for i in range(1, 11):

    if i % 2 == 0:
        continue

    print(i)

# Secret Number Game

secret = 8
while True:
    number = int(input("guess the number: "))

    if number != secret:
        print("try again")

    else:
        print("congratulations!")

        break