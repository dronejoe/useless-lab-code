def get_data():
    with open("input-riceboard-bb43.txt", "r") as f:
        board_data = []
        for line in f:
            board_data.append([int(x) for x in line.split()])
        return board_data
    
    
def sum_board(array):
    total_rice = (array[0]**(array[1]**2) - 1) // (array[0] - 1) % array[2]
    return int(total_rice)


def output_data(data):
    with open("Output.txt", 'w') as f2:
        for i in data:
            f2.write("Case #{}: {}\n".format(i[0], i[1]))

            
def main():
    var = get_data()
    wasted_rice_cases = []
    for i in range(1, len(var)):
        print("dealing with {}".format(i))
        wasted_rice_cases.append([i, sum_board(var[i])])
    output_data(wasted_rice_cases)

if __name__ == '__main__':
    main()
