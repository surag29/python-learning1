def main():

    try:
        a =  int(input("enter the number :"))
        print(f"the numeber is {a}")
        return

    except Exception as e:
        print(e)

    else:
        print("the this will run if only try block runs")  #when inside method we use return right then this will not execute 

    finally:
        print("this will print always inside a method or anywhere ") #this will run irrespective of anything 
main()


