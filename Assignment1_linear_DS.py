# Q1. Write a program to find all pairs of an integer array whose sum is equal to a given number?


arr=[]
size= int(input("Enter the size of the array: : "))
for i in range(size):
    num=int(input(f"Enter element {i+1}: "))
    arr.append(num)
num= int(input("Enter number for pairs: "))
def pairs(arr,num):
    pair=set()
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]+arr[j]==num:
                res=(min(arr[i],arr[j]),max(arr[i],arr[j]))
                pair.add(res)
    if not pair:
        print ("No Pairs found!",end=" ")
    else:
        return pair
print(pairs(arr,num))


# Q2. Write a program to reverse an array in place? In place means you cannot create a new array. You have to update the original array.


def reverse(arr):
    left, right = 0, len(arr) - 1  

    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr
arr=[]
size= int(input("Enter the size of array: "))
for i in range(size):
    num=int(input(f"Enter element {i+1} : "))
    arr.append(num)
print(reverse(arr))


# Q3. Write a program to check if two strings are a rotation of each other?


string1=input("Enter string 1 : ")
string2=input("Enter string 2 : ")
def  rotatestring(str1,str2):
    if len(str1)!=len(str2):
        return False
    temp=str1+str2
    if str1 in temp:
        return True
    else:
        return False
    
if rotatestring(string1,string2):
    print("Yes!")
else:
    print("No!")


# Q4. Write a program to print the first non-repeated character from a string?


def non_repeated(input_str):
    count = {}
    
    for ele in input_str:
        if ele in count:
            count[ele] += 1
        else:
            count[ele] = 1

    for ele in input_str:
        if count[ele] == 1:
            return ele

    return None

user_input = input("Enter a string: ")
print("First non-repeated character in the string is",non_repeated(user_input))


# Q5. Write a recursive function to check if a given string is a palindrome.


string= input("Enter string : ")
def palindrome(string):
    if len(string)==1:
        return True
    if string[0]==string[-1]:
        return palindrome(string[1:-1])
    else:
        return False
print(palindrome(string))


# Q6. Read about infix, prefix, and postfix expressions. Write a program to convert postfix to prefix expression.


def postfix_to_prefix(post):
    stack = []
    operators = set(['+', '-', '*', '/', '^'])

    for opr in post.split():
        if opr not in operators:
            stack.append(opr)
        else:
            var2 = stack.pop()
            var1 = stack.pop()
            pre = opr + var1 + var2
            stack.append(pre)

    return stack[0]

post = input("Enter a postfix expression separated by spaces: ")
pre = postfix_to_prefix(post)
print("Th Prefix expression is:", pre)


# Q7. Write a program to convert prefix expression to infix expression.

def prefix_to_infix(pre):
    stack = []
    operators = set(['+', '-', '*', '/', '^'])
    lst = pre.split()

    for opr in reversed(lst):
        if opr not in operators:
            stack.append(opr)
        else:
            var1 = stack.pop()
            var2 = stack.pop()
            infix = f'({var1} {opr} {var2})'
            stack.append(infix)

    return stack[0]

pre = input("Enter a prefix expression: ")
infix = prefix_to_infix(pre)
print("The infix expression is:", infix)

# Q8. Write a program to check if all the brackets are closed in a given code snippet.


def are_brackets_balanced(code):
    stack = []
    bracket_pairs = {')': '(', '}': '{', ']': '['}

    for char in code:
        if char in "({[":
            stack.append(char)
        elif char in ")}]":
            if not stack or stack[-1] != bracket_pairs[char]:
                return False
            stack.pop()

    return not stack

code = input("Enter a code snippet: ")
if are_brackets_balanced(code):
    print("Brackets are balanced.")
else:
    print("Brackets are not balanced.")


# Q9. Write a program to reverse a stack.

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)  

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None
      
    def peek(self):
        if not self.is_empty():
            return self.items[-1]  
        else:
            return None
    
    def get_stack(self):
        if not self.is_empty():
            return self.items
        else:
            return None
    
    def is_empty(self):
        return len(self.items) == 0
    
    def clearAll(self):
        self.items.clear()
        print("All Elements removed.")

stack=Stack()
newstack=Stack()
lenth=int(input('Enter no of items to Push : '))
for i in range(lenth):
    num=int(input(f"Enter {i+1}th number to append : "))
    stack.push(num)
print ('Original  Stack : ',stack.get_stack())
for i in range(lenth):
    stc=stack.get_stack()
    newstack.push(stc[lenth-(i+1)])
print ('New Stack : ',newstack.get_stack())


# Q10. Write a program to find the smallest number using a stack.

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)  

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None
      
    def peek(self):
        if not self.is_empty():
            return self.items[-1]  
        else:
            return None
    
    def get_stack(self):
        if not self.is_empty():
            return self.items
        else:
            return None
    
    def is_empty(self):
        return len(self.items) == 0
    
    def clearAll(self):
        self.items.clear()
        print("All Elements removed.")

stack=Stack()
lenth=int(input('Enter no of items to Push : '))
for i in range(lenth):
    num=int(input(f"Enter {i+1}th number to append : "))
    stack.push(num)
print ('Original  Stack : ',stack.get_stack())
print('Smallest number : ',min(stack.get_stack()))
