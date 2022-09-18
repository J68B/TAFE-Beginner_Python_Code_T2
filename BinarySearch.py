# API name: binarySearch
# Purpose: search for a given search word in an ordered list
# Input arguments: list of names and the search name
# Return value: True if search name is found in list, False otherwise
# Exceptions: null list, null search name, input of wrong type

# let names_list be a list of names in alphabetical order
# let search_name be a name to search in the list
def binarySearch(name_list, search_name):

    # initialize variables
    start = 0                # point to the start of list
    end = len(name_list) - 1 # point to the end of list
    mid = (start + end) // 2  # point to the middle of list

    # while search_name is not found in the middle of the list
    while start <= end:
        # if search_name is in the first half
        if search_name < name_list[mid]:
            # focus the search to the first half
            end = mid - 1
        # else
        else:
            # focus the search to the second half
            start = mid + 1
        # endif
    # endwhile 

    # if search_name was found in the list
    if start <= end:
        # search name found
        return True
    # else
    else:
        # search name not found
        return False
    # endif

# Run tests
if __name__ == "__main__":
    
    list_of_names = ["Andy", "Bandy", "Candy", "Dandy", "Handy", "Kandy", "Mandy", "Pandy", "Randy", "Sandy", "Tandy"]
    
    # Test case #1
    if binarySearch(list_of_names, "Andy"):
        print ("Test 1 passed")
    else:
        print ("Test 1 failed")
        
    # Test case #2
    if binarySearch(list_of_names, "Tandy"):
        print ("Test 2 passed")
    else:
        print ("Test 2 failed")
        
    # Test case #3
    if binarySearch(list_of_names, "Candy"):
        print ("Test 3 passed")
    else:
        print ("Test 3 failed")
        
    # Test case #4
    if binarySearch(list_of_names, "Pandy"):
        print ("Test 4 passed")
    else:
        print ("Test 4 failed")
        
    # Test case #5
    if not binarySearch(list_of_names, "Nanda"):
        print ("Test 1 passed")
    else:
        print ("Test 1 failed")
        
    # Test case #1
    if not binarySearch(list_of_names, "90432iu"):
        print ("Test 1 passed")
    else:
        print ("Test 1 failed")
        
    # Test case #1
    if binarySearch(list_of_names, 65845):
        print ("Test 1 passed")
    else:
        print ("Test 1 failed")
        
    # Test case #1
    if not binarySearch(list_of_names, "gfdxsvzds"):
        print ("Test 1 passed")
    else:
        print ("Test 1 failed")
        
    # Test case #1
    if not binarySearch(list_of_names, ""):
        print ("Test 1 passed")
    else:
        print ("Test 1 failed")