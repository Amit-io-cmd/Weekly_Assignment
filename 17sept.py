# problem-2 Word Frequency Filter
from collections import Counter
with open('story.txt') as s:
    r=s.read()
    list=r.split()
mylist=[]
for i in list:
    if ',' in i:
        mylist.append(i.strip(',').lower())
    elif ';' in i:
        mylist.append(i.strip(';').lower())
    elif '-' in i:
        mylist.append(i.strip('-').lower())
    elif '.' in i:
        mylist.append(i.strip('.').lower())
    else:
        mylist.append(i.lower())
u=int(input("Enter the Word Frequency: "))
word_count=Counter(mylist)
for w in word_count.keys():
    if word_count[w]>u:
        print(w+':',word_count[w])

# problem -3 Library Borrow Checker
lib_books={'The Conch Bearer':10,'The Alchmist':15,'Last Flight':11,'my wings':2,'mission 2024':20}
print("Welcome to the Library!")
b=input("Enter the name of the Book: ")
for i in lib_books.keys():
    if i==b and lib_books[i]==0:
        print('Out of stock')
        break
    elif i==b:
        print('Issued')
        lib_books[i]-=1
        break
    elif b not in lib_books.keys():
        print('Not Found')
        break
with open('library.txt','w') as l:
    l.write(str(lib_books.items()))

# Problem 4: Unique Numbers & Statistics
num=input("Enter the numbers saprated by Space: ")
nums=num.split()
my_set=set(nums)
count=0
Sum=0
for i in my_set:
    count+=1
    Sum= Sum+int(i)
avg=Sum/count
print(count)
print(Sum)
print(avg)
print(max(my_set))
print(min(my_set))

# Problem 5: Student Attendance Manager
master_list= ['101', '102', '103', '104', '105', '106','107','108','109','110']
with open("attendance.txt", "r") as f:
    present_list= [line.strip() for line in f if line.strip()]
present = []
absent = []
for roll in master_list:
    if roll in present_list:
        present.append(roll)
    else:
        absent.append(roll)
print("Present Students:")
for roll in present:
    print(roll)
print("Absent Students:")
for roll in absent:
    print(roll)
with open("absent.txt", "w") as file:
    for roll in absent:
        file.write(roll + '\n')

# Problem 1: Top-Scoring Students by Subject using csv (comma-separated values) file
import csv
names=[]
subj=[]
marks=[]
my_dict={}
with open('marks.csv') as f:
    r=csv.DictReader(f)
    for i in r:
        names.append(i['name'])
        subj.append(i['subject'])
        marks.append(i['marks'])
my_dict['name']=names
my_dict['subject']=subj
my_dict['marks']=marks
subject_groups={}
for name,subject,mark in zip(names,subj,marks):
    mark=int(marks)
    if subject not in subject_groups:
        subject_groups[subject]=[]
    subject_groups[subject].append((name,mark))
print(subject_groups)
for k in subject_groups.keys():
    student_list = subject_groups[k]
    max_mark = max(student_list, key=lambda x: x[1])[1]
    top_scorers = [name for name, mark in student_list if mark == max_mark]
    print(k,top_scorers,max_mark)