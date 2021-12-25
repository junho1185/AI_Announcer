def get_airport_data(icao):

    data = []
    file = open('./data/airports.txt', 'r', encoding='utf-8')
    str = ''
    str = file.readlines()

    for line in str:
        line_data = line.split('\t')
        if(line_data[0] == icao):
            print('Airport Data Found Using ICAO code: ' + icao)
            file.close()
            return line_data

    return data
