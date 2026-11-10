from faker import Faker
import csv
output = open('my.csv', mode = 'w')
fake = Faker()
header = ['id','name','email']
mywriter = csv.writer(output)
mywriter.writerow(header)
for i in range(100):
    mywriter.writerow([i, fake.name(), fake.email()])
output.close()    