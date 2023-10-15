l = input("Enter the list: ")
c = 0
x = l.split()
for i in range(len(x)):
    if (x[i] == 'a' or x[i] == 'e' or x[i] == 'i' or x[i] == 'o' or x[i] == 'u' or x[i] == 'A' or x[i] == 'E' or x[i] == 'I' or x[i] == 'O' or x[i] == 'U'):
        print("Vowel found at", i + 1, "th position")
        c = 1
    if (c == 0):
        print("Item not found")
