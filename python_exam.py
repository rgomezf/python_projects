import os
import traceback

folder_path = os.path.dirname(os.path.abspath(__file__))


def third_element(param_list):
    yield param_list[2:3]


def print_element(generated_object):
    for element in generated_object:
        print "The element in the generator object is: {}".format(element)


def get_device_id(usp_name):
    file_list = []
    result_list = []
    temp_list = []
    temp_obj = {}
    try:
        with open("{}/{}".format(folder_path, "source.txt"), "r") as source_file:
            lines = source_file.read().splitlines()
            for line in lines:
                if line.startswith('-'):
                    if temp_obj and temp_obj not in file_list:
                        file_list.append(temp_obj)
                        temp_obj = {}
                    continue
                temp_list = line.split("|")
                temp_obj[temp_list[0].strip()] = temp_list[1].strip()

        for x in file_list:
            if x['usp'] == usp_name:
                result_list.append(int(x['version_id']))

        return sorted(result_list)

    except BaseException:
        print traceback.format_exc()


def main():
    """
    Problem #1
    Write a function that returns a list containing every 3rd item in a given list.
    Implement this with a generator.
    """
    first_list = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
    second_list = ['p','r','o','g','r','a','m','i','z']
    third_list = [1, 3, 5, 7, 9, 11, 13]

    first_result = third_element(first_list)
    second_result = third_element(second_list)
    third_result = third_element(third_list)

    print_element(first_result)
    print_element(second_result)
    print_element(third_result)

    """
    Problem #2
    A file contains the following information. Write a function that reads the contents of the file. 
    The function gets the USP name and returns only the device IDs that match the USP name. 
    The return IDs must be sorted without duplication.    
    """
    assert get_device_id("USP-NAME-1") == [20065], "Would equal True"


if __name__ == '__main__':
    main()
