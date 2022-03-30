from datetime import datetime


def read_files(pipeFile, spaceFile, commaFile):
    # list to hold all data in all files
    dataList = []

    # appending data from pipe.txt to dataList by replacing | with ''
    for pd in pipeFile.readlines():
        data = pd.replace('|', '')
        dataList.append(data)

    # appending data from comma.txt to dataList by replacing , with ''
    for pd in commaFile.readlines():
        data = pd.replace(',', '')
        dataList.append(data)

    # appending data from pipe.txt to dataList
    for sd in spaceFile.readlines():
        dataList.append(sd)
    return dataList


def process_and_clean_data(dataList):
    splitData = []
    # cleaning unwanted data and filling missing information
    for data in dataList:
        d = data.split()
        if len(d) == 6:
            del (d[2])
        if d[2] == 'M':
            d[2] = 'Male'
        elif d[2] == 'F':
            d[2] = 'Female'
        splitData.append(d)
        # d.sort(key = lambda test_list: test_list[1])
    splitData.sort(key=lambda test_list: test_list[2])

    female = []
    male = []
    for row in splitData:
        # moving all colors to last
        if row[-1] not in ['Green', 'Pink', 'Red', 'Black', 'Tan', 'Yellow', 'Blue']:
            temp = row[-1]
            row[-1] = row[-2]
            row[-2] = temp
        # seperating female data and male data
        if 'Female' in row:
            female.append(row)
        else:
            male.append(row)
        date = row[-2].split('-')
        row[-2] = '/'.join(date)
    return male, female


def sort_data(male, female):
    female.sort(key=lambda test_list: test_list[0])
    male.sort(key=lambda test_list: test_list[0])
    total = female + male

    femaleStr = ' '
    maleStr = ' '
    allData = []
    for fm in female:
        jn = femaleStr.join(fm)
        allData.append(jn)

    for m in male:
        jn = maleStr.join(m)
        allData.append(jn)
    return allData, total


def sorted_by_gender(allData):
    return allData


def sorted_by_birth_date(total):
    lst2 = []
    # Output 2 - sorted by birth date, ascending then by last name ascending #
    tmp_dataList = total
    tmp_dataList.sort(key=lambda tmp_dataList: (datetime.strptime(tmp_dataList[-2], '%m/%d/%Y'), tmp_dataList[0]))
    for i in tmp_dataList:
        lst2.append(' '.join(i))
    return lst2


def sorted_by_last_name(total):
    lst3 = []
    tmp_dataList = total
    tmp_dataList.sort(key=lambda tmp_dataList: tmp_dataList[0])
    tmp_dataList = reversed(tmp_dataList)
    for i in tmp_dataList:
        lst3.append(' '.join(i))
    return lst3


def print_output(lst1, lst2, lst3):
    print('Output 1:')
    for data in lst1:
        print(data)

    print('\nOutput 2:')
    for data in lst2:
        print(data)

    print('\nOutput 3:')
    for data in lst3:
        print(data)


def main():
    pipeFile = open('pipe.txt', 'r')
    spaceFile = open('space.txt', 'r')
    commaFile = open('comma.txt', 'r')
    # create out put file
    # outputFile = open('output.txt', 'w+')

    dataList = read_files(pipeFile, spaceFile, commaFile)
    male, female = process_and_clean_data(dataList)
    allData, total = sort_data(male, female)
    lst1 = sorted_by_gender(allData)
    lst2 = sorted_by_birth_date(total)
    lst3 = sorted_by_last_name(total)
    print_output(lst1, lst2, lst3)


if __name__ == '__main__':
    main()
