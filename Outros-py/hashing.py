import hashlib
import time

text = "um texto aqui"
# message = hashlib.sha256(text.encode('utf-8')).hexdigest()
print(f"SHA-256  {hashlib.sha256(text.encode('utf-8')).hexdigest()} ")
print(f"SHA-512  {hashlib.sha512(text.encode('utf-8')).hexdigest()} ")

list = list(range(1, 10))
hashed_list=[]
hashed_dict={}

for item in list: 
    hashed_dict[item] = hashlib.sha256(str(item).encode('utf-8')).hexdigest()
    print(f"Item dicionário ->  {hashed_dict}")
    hashed_list.append(hashlib.sha256(str(item).encode('utf-8')).hexdigest())
    time.sleep(1)

'''print(f'Lista  -> {hashed_list}')
print(f'Dicionario  -> {hashed_dict}')'''
