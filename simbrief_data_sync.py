import requests
import xml.etree.ElementTree as elemTree
def get_simbrief_data(username):

    URL = 'https://www.simbrief.com/api/xml.fetcher.php?username='+username

    data = []
    response = requests.get(URL)
    xml_text = response.text
    status = response.status_code

    if status != 200:
        print('Internet Connection Error')
        return data

    tree = elemTree.fromstring(xml_text)

    print('Simbrief Data Synchronization Successful by Simbrief ID: ' + username)
    origin = tree.find('./origin')
    destination = tree.find('./destination')
    time = tree.find('./times')
    flight_number = tree.find('general')
    captain_crew = tree.find('./crew')

    data.append(origin.find('icao_code').text)                  #data[0] = origin Airport ICAO
    data.append(destination.find('icao_code').text)             #data[1] = destination Airport ICAO
    data.append(time.find('est_time_enroute').text)             #data[2] = estimated flight time (sec)
    data.append(flight_number.find('flight_number').text)       #data[3] = flight number
    data.append(captain_crew.find('cpt').text)                  #data[4] = captain name
    data.append(captain_crew.find('pu').text)                   #data[5] = crew manager name
    data.append(time.find('orig_timezone').text)                #data[6] = origin timezone
    data.append(time.find('dest_timezone').text)                #data[7] = destination timezone

    return data

