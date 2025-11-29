c=0
with open(r'C:\Users\ggashaw\Desktop\sample_file.txt','r') as file:
    data= file.read()
    lines =data.split()
    for word in lines:
        if not word.isnumeric():
            c+=1

print(c)