
import csv
import os  #it is imported for deleting the data

def write_csv(filename):
    data = [
        {"name" : "Sahithi", "age" : 21},
        {"name": "Waseema", "age": 22}
    ]

    columnnames = ["name","age"]
    with open(filename, "w", newline="\n") as file:
        writer = csv.DictWriter(file, fieldnames=columnnames)
        writer.writeheader()
        writer.writerows(data)
    # print('CSV file written successfully')


def read_csv(filename):
    with open(filename, "r", newline="\n") as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(f"Name: {row['name']}, Age: {row['age']}")

def delete_csv(filename):
    if os.path.exists(filename):
        os.remove(filename)
        print(f"{filename} deleted successfully")
    else:
        print(f'{filename} does not exist')




#driver code
filename = "myfile.csv"
write_csv(filename)
print("Data read from csv file:")
read_csv(filename)
# delete_csv(filename)

