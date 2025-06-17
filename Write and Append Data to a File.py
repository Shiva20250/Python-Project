
data = input("Enter text to write to the file: ")

with open("output.txt", "w") as file:
    file.write(data + "\n")

print("Data successfully written to output.txt.")


additional_data = input("Enter additional text to append: ")

with open("output.txt", "a") as file:
    file.write(additional_data + "\n")

print("Data successfully appended.")


print("Final Content of output.txt:")

with open("output.txt", "r") as file:
    for line in file:
        print(line.strip())

