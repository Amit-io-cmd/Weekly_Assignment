List = [1, 4, 5, 6, 7, 4, 3, 2, 1]
new_list = []
for i in List:
    if i not in new_list:
        new_list.append(i)  


# write a program that counts how many times each word appears in a given list using the dictionary


# write a function that finds the maximum nuber in a list without using max()
nums=[12,14,5,6,78,9,87,45]
max_num=nums[0]
for num in nums[1:]:
    if num>max_num:
        max_num=num
print(max_num)
    

with open("C:/Users/SAMSUNG/Documents/satya.txt") as file:
     for line in file:
         if "error" in line.lower():
             print(line.strip())

# Given a list of words ,group them in a dictionary where the key is the first letter and the value is the list of word starting with that letter 
words=["apple","banana","apricot","blueberry","cherry"]
mydict={}
for word in words:
    x=word[0]
    if x not in mydict:
        mydict[x]=[]
    mydict[x].append(word)
print(mydict)
        