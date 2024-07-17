import random
# Exercise 1
positive_count: int = 0;
negative_count: int = 0;
zero_count: int = 0;
divided_by_seven: int = 0;
last_positive_num: int = None;
last_negative_num: int = None;
for i in range(1, 11):
    number: int = int(input("Please enter a number: "));
    if number == -9999:
        break
    if number < -1000 or number > 1000:
        continue
    if number > 0:
        positive_count += 1;
        if positive_count != 0:
            last_positive_num = number;
    elif number < 0:
        negative_count += 1;
        if negative_count != 0:
            last_negative_num = number;
    else:
        zero_count += 1;
    if number % 7 == 0:
        divided_by_seven += 1;
else:
    print(f"The sum of positive numbers is: {positive_count}");
    print(f"The sum of negative numbers is: {negative_count}");
    print(f"The sum of zero numbers is: {zero_count}");
    print(f"The sum of numbers divided by seven is: {divided_by_seven}");
    print(f"The last positive number you enter is: {last_positive_num}");
    print(f"The last negative number you enter is: {last_negative_num}");

# Exercise 2
count_guess_attempts: int = 0;
play_again: str = "yes";
while play_again.lower() == "yes":
    rnd: int = random.randint(1, 100);
    while True:
        user_number: int = int(input("Please guess a number: "));
        count_guess_attempts += 1;
        if user_number > rnd:
            print("your number is too big");
        elif user_number < rnd:
            print("your number is too small");
        else:
            print("BINGO");
            print(f"The number of guessing attempts in the game is {count_guess_attempts}");
            play_again = input("Would you like to play again: ");
            break

# Exercise 3/1
number: int = int(input("Please enter a number: "));
for i in range(1, number + 1):
    for j in range(1, i + 1):
        print(j, end=" ");
    print();

for i in range(1, number):
    for j in range(1, number - i + 1):
        print(j, end=" ");
    print();

# Exercise 3/2
stars: int = int(input("Please enter a number of stars: "));
while stars % 2 == 0:
    stars: int = int(input("Please enter an odd number of stars: "));
height = (stars + 1) // 2;
for i in range(1, height + 1):
    print(" " * (height - i) + "*" * (2 * i - 1));

# Exercise 4
movies: list[str] = ["Pulp Fiction", "Fight Club", "The Green Mile"];
movies.append("The Terminator");
movies.insert(0, "The Pianist");
print(len(movies));

numbers: list[int] = [];
for i in range(1, 11):
    rnd_int: int = random.randint(1, 100);
    numbers.append(rnd_int);
print(numbers);

boolean: list[bool] = [];
for i in range(1, 11):
    rnd_bool: bool = random.choice([True, False]);
    boolean.append(rnd_bool);
print(boolean);

# Bonus Questions
random_word: str = "";
word_length: int = random.randint(5, 20);
for i in range(1, word_length):
    rnd_char: str = random.choice('abc');
    random_word += rnd_char;
print(random_word);

words: list[str] = [];
word_list: int = random.randint(10, 20);
for i in range(1, word_list):
    word_length: int = random.randint(5, 20);
    random_word: str = "";
    for j in range(1, word_length):
        rnd_char: str = random.choice('abc');
        random_word += rnd_char;
    words.append(random_word);
print(words);

