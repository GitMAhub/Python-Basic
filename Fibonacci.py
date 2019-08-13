def getFibAtPos(num) :
    if num == 0 :
        return 0
    elif num == 1 :
        return 1
    else :
        return getFibAtPos(num-1)+getFibAtPos(num-2)
   
def main():
    pos = 6
    print("At position",pos,"fibonacci is ",getFibAtPos(pos))
   
   
if __name__ == "__main__" :
    main()
