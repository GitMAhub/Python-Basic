def getFactorial(num) :
    if num == 0 or num == 1 :
        return 1
    else :
        return num*getFactorial(num-1)
   
def main():
    number = 5
    print(number,"! = ",getFactorial(number))
   
   
if __name__ == "__main__" :
    main()
