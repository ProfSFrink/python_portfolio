#Sorting Algorithms
#by Steven Partlow
#This was a project that was part of the 2022 Complete Python Bootcamp from Zero to Hero in Python Course on Udemy
#https://www.udemy.com/course/complete-python-bootcamp/

#I am currently taking an 'Advanced Software and Web Developer' diploma with Pitman Training in the UK. The second course on this diploma 'Overview of Software Development' covered 
#sorting algorithms, mainly three types an insertion sort, selection sort and a bubble sort. We did not have to code these but where walked through how they worked and what the 
#computer is doing at each step until the sort was completed. The three algorithms sorted an array of numbers [5,2,1,7,6] in ascending order. As I am also learning python on a 
#bootcamp on udemy, I thought it would be interesting to combine the two and try to code the algorithms in python.

def insertion_sort(nums):
    index = 0
    temp = 0

    print("Nums: {} Index: {} Temp: {}".format(nums,index,temp))
    
    for count in nums:
        print("Nums: {} Index: {} Temp: {}".format(nums,index,temp))
        
        for index in range(1,len(nums)):
            print("Nums: {} Index: {} Temp: {}".format(nums,index,temp))
            
            if nums[index-1] > nums[index]:
                temp = nums[index-1]
                nums[index-1] = nums[index]
                nums[index] = temp
                print("Nums: {} Index: {} Temp: {}".format(nums,index,temp))

def selection_sort(nums):
  n = len(nums)
  temp = 0  

  for count in range(n):
    minimum = count

    for index in range(count+1, n):
        if (nums[index] < nums[minimum]):
            minimum = index
            print("{} index: {} minimum: {} temp: {}".format(nums,index,minimum,temp))
    
    temp = nums[count]
    nums[count] = nums[minimum]
    nums[minimum] = temp
    print("{} count: {} minimum: {} temp: {}".format(nums,count,minimum,temp))
    
  return nums

def bubble_sort(nums):
    temp = 0

    print(nums)
    
    for counter in range(0,len(nums)):
        for index in range(0,len(nums)-1):
            if nums[index] > nums[index+1]:
                temp = nums[index+1]
                nums[index+1] = nums[index]
                nums[index] = temp
                print(nums)

if __name__ == "__main__":

    print("Sorting Algorithms")
    print("-----------------------------------")
    print("1. Run a insertion sort")
    print("2. Run a selection sort")
    print("3. Run a bubble sort")
    print("-----------------------------------")

    while True: 
        try:
            option = int(input("Select an option: ")) 
        except:
            print("You must enter either 1,2 or 3 please try again!") 
            continue
        else:
            if option == 1: 
                array = [5,2,1,7,6]
                insertion_sort(array)
                break   
            elif option == 2: 
                array = [5,2,1,7,6]
                selection_sort(array)
                break
            elif option == 3:
                array = [5,2,1,7,6]
                bubble_sort(array)
                break
            else:
                print("You must enter either 1,2 or 3 please try again!") 
                continue