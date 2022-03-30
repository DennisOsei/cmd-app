from solution import *

expected_output1 = ['Hingis Martina Female 4/2/1979 Green',
                         'Kelly Sue Female 7/12/1959 Pink',
                         'Kournikova Anna Female 6/3/1975 Red',
                         'Seles Monica Female 12/2/1973 Black',
                         'Abercrombie Neil Male 2/13/1943 Tan',
                         'Bishop Timothy Male 4/23/1967 Yellow',
                         'Bonk Radek Male 6/3/1975 Green',
                         'Bouillon Francis Male 6/3/1975 Blue',
                         'Smith Steve Male 3/3/1985 Red']

expected_output2 = ['Abercrombie Neil Male 2/13/1943 Tan',
                         'Kelly Sue Female 7/12/1959 Pink',
                         'Bishop Timothy Male 4/23/1967 Yellow',
                         'Seles Monica Female 12/2/1973 Black',
                         'Bonk Radek Male 6/3/1975 Green',
                         'Bouillon Francis Male 6/3/1975 Blue',
                         'Kournikova Anna Female 6/3/1975 Red',
                         'Hingis Martina Female 4/2/1979 Green',
                         'Smith Steve Male 3/3/1985 Red']

expected_output3 = ['Smith Steve Male 3/3/1985 Red',
                         'Seles Monica Female 12/2/1973 Black',
                         'Kournikova Anna Female 6/3/1975 Red',
                         'Kelly Sue Female 7/12/1959 Pink',
                         'Hingis Martina Female 4/2/1979 Green',
                         'Bouillon Francis Male 6/3/1975 Blue',
                         'Bonk Radek Male 6/3/1975 Green',
                         'Bishop Timothy Male 4/23/1967 Yellow',
                         'Abercrombie Neil Male 2/13/1943 Tan']
# read text files
pipeFile = open('pipe.txt', 'r')
spaceFile = open('space.txt', 'r')
commaFile = open('comma.txt', 'r')
# create out put file

dataList = read_files(pipeFile, spaceFile, commaFile)
male, female = process_and_clean_data(dataList)
allData, total = sort_data(male, female)
actual_output1 = sorted_by_gender(allData)
actual_output2 = sorted_by_birth_date(total)
actual_output3 = sorted_by_last_name(total)

print("Expected Output 1:", expected_output1)
print("Actual Output 1:", actual_output1)
assert actual_output1 == expected_output1

print("\nExpected Output 2:", expected_output2)
print("Actual Output 2:", actual_output2)
assert actual_output2 == expected_output2

print("\nExpected Output 3:", expected_output3)
print("Actual Output 3:", actual_output3)
assert actual_output3 == expected_output3
