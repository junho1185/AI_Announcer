# -*- coding: utf-8 -*-
import datetime
import pytz

def kor_make_script(airline, flight_hour, flight_minute, simbrief_data, origin_airport_data, destination_airport_data, captain_name):

    origin_country = origin_airport_data[2]
    origin_city = origin_airport_data[3]
    destination_country = destination_airport_data[2]
    destination_city = destination_airport_data[3]
    destination_airport = destination_airport_data[4]

    flight_number = simbrief_data[3]
    cabin_name = simbrief_data[5]

    kor_script = []
    boarding_script = ''
    before_gate_close_script = ''
    before_takeoff_script = ''
    seat_belt_and_security_script = ''
    approach_script = ''
    before_landing_script = ''
    after_landing_script = ''

    captain_name = captain_name.lower()
    cabin_name = cabin_name.lower()

    print('Korean Script Info: ')
    print('\t- AirLine Code : ', airline)
    print('\t- Departure : ' + origin_country)
    print('\t- Arrival : ' + destination_airport)
    print('\t- Flight Hour : ' + str(flight_hour))
    print('\t- Flight Minute : ' + str(flight_minute))

    if airline == 1:        #Korean Air
        if origin_country != destination_country:
            boarding_script = '승객 여러분, 안녕하십니까? 스카이팀 회원사인 저희 대한항공은 여러분의 탑승을 진심으로 환영합니다. 우리 비행기는 ' + origin_country + ' ' + origin_city + '에서 ' + destination_country + ' ' + destination_city + '까지 가는 대한항공 ' + flight_number + '편입니다.'
        else:
            boarding_script = '승객 여러분, 안녕하십니까? 스카이팀 회원사인 저희 대한항공은 여러분의 탑승을 진심으로 환영합니다. 우리 비행기는 ' + origin_city + '에서 ' + destination_city + '까지 가는 대한항공 ' + flight_number + '편입니다.'
        boarding_script = boarding_script + '저희 승무원들은 여러분께서 안전하고 편안하게  여행하실 수 있도록 정성을 다하겠습니다. 노트북 등 큰 전자기기는 좌석 하단 또는 기내 선반에 보관해 주시기 바랍니다. 비행 중 여러분의 안전을 담당하는 안전요원인 승무원의 지시에 협조해주시기 바라며, 계속해서 잠시 화면을 주목해주시기 바랍니다. '
        before_gate_close_script = '승객 여러분, ' + destination_city + '까지 가는 대한항공 ' + flight_number + '편 곧 출발하겠습니다.'
        before_gate_close_script = before_gate_close_script + '기내에서 승무원의 업무를 방해하는 행위, 전자담배를 포함한 흡연, 전자기기 사용 기준 위반은 항공보안법에 따라 금지돼있습니다. 또한 애플 맥북 프로 15인치 노트북은 비행 안전을 위해 기내에서 사용이 불가하오니 전원을 꺼주시고 충전을 하지 마시기 바랍니다. 감사합니다. '
        before_takeoff_script = '승객 여러분, 우리 비행기는 이제 이륙하겠습니다. 여러분의 안전을 위해 좌석 벨트를 매셨는지 다시 한번 확인해주시기 바랍니다.'
        seat_belt_and_security_script = '승객 여러분, 방금 좌석 벨트 표시등이 꺼졌습니다. 그러나 비행기가 갑자기 흔들리는 경우에 대비해 자리에서는 항상 좌석벨트를 매시기 바랍니다. 좌석벨트 표시등이 켜질 경우 안전을 위해 서비스가 제한될 수 있음을 알려드립니다. 휴대전화 또는 보조배터리는 압착될 경우 화재의 위험이 있습니다. 좌석 등받이를 움직이기 전 전자기기가 좌석 틈새로 빠지지 않았는지 확인하시기 바랍니다. 또한 전자담배를 포함한 기내에서의 흡연은 항공 보안법에 따라 엄격히 금지돼있음을 알려드립니다. 감사합니다. '
        approach_script = '안내 말씀 드리겠습니다. 곧 ' + destination_airport + '에 도착하겠습니다. 착륙 준비를 위해 꺼내 놓은 짐, 노트북 등 큰 전자 기기는 앞 좌석 아래나 선반 속에 다시 보관해 주시고, 창문 덮개는 열어두시기 바랍니다. 잠시 후 헤드폰과 잡지를 걷겠으니 협조해 주시기 바랍니다. 또한 영상물을 시청하고 계시는 분은 계속 헤드폰을 사용하실 수 있으며, 사용하신 후 내리시기 전 앞 좌석 주머니 속에 넣어 주시기 바랍니다. 아울러 기내 면세품 예약 주문서 작성을 마치신 승객께서는 저희 승무원에게 전달해 주시기 바랍니다. 감사합니다. '
        before_landing_script = '승객 여러분, 우리 비행기는 곧 착륙하겠습니다. 좌석 벨트를 매주십시오. 그리고 창문 덮개는 열어주시기 바랍니다. 감사합니다.'
        after_landing_script = '승객 여러분, 우리 비행기는 ' + destination_airport +'에 도착했습니다. 비행기가 완전히 멈춘 후 좌석벨트 표시등이 꺼질 때까지 자리에서 기다려 주시고 선반을 여실 때에는 안에 있는 물건이 떨어질 수 있으니 조심해주십시오. 오늘도 스카이팀 회원사인 저희 대한항공을 이용해주셔서 대단히 감사합니다. 저희 승무원들은 앞으로도 안전하고 편안하게 여행하실 수 있도록 정성을 다하겠습니다. 감사합니다. '

    elif airline == 2:  #Asiana Airlines

        if flight_hour >= 1:
            boarding_script = '승객 여러분, 안녕하십니까? 스타얼라이언스 아시아나항공 ' + flight_number + '편의 탑승을 환영합니다. ' + destination_airport + '까지의 비행시간은 ' + str(flight_hour) + '시간 ' + str(flight_minute) + '분이 걸릴 것으로 예상하며, ' + destination_city + '까지 아름다운 비행에 아시아나항공이 함께하겠습니다. 아울러 기내에서 전자담배를 포함한 흡연, 승무원의 업무방해, 전자기기 사용 기준 위반은 항공보안법 저촉사항임을 안내드립니다. 감사합니다. '
        else:
            boarding_script = '승객 여러분, 안녕하십니까? 스타얼라이언스 아시아나항공 ' + flight_number + '편의 탑승을 환영합니다. ' + destination_airport + '까지의 비행시간은 ' + str(flight_minute) + '분이 걸릴 것으로 예상하며, ' + destination_city + '까지 아름다운 비행에 아시아나항공이 함께하겠습니다. 아울러 기내에서 전자담배를 포함한 흡연, 승무원의 업무방해, 전자기기 사용 기준 위반은 항공보안법 저촉사항임을 안내드립니다. 감사합니다. '

        before_gate_close_script = '승객 여러분, 곧 출발하겠습니다. 자리에 앉아 좌석벨트를 매주시기 바랍니다. 감사합니다. '
        before_takeoff_script = '승객 여러분, 곧 이륙하겠습니다. 좌석벨트를 매셨는지 다시 한번 확인해주시기 바랍니다. 감사합니다. '
        seat_belt_and_security_script = '승객 여러분, 안전을 위해 자리에서는 항상 좌석벨트를 착용하시고, 화장실 내 향수, 스프레이 사용으로 화재경보기가 작동할 수 있으니 사용을 삼가시기 바랍니다. 식사 제공 후 면세품을 판매하겠습니다. 구입을 원하시면 주문서를 써주시고, 예약 주문하신 분은 승무원에게 말씀해주십시오. 면세품 관련 자세한 내용은 안내 책자를 참고하시기 바랍니다. 감사합니다. '
        approach_script = '승객 여러분, 우리 비행기는 ' + destination_airport + '에 접근하고 있습니다. 안전벨트를 매주시고 등받이와 테이블은 제자리로 해주십시오. 창문 덮개는 열어주시고, 꺼내놓으신 짐은 앞 좌석 밑이나 선반 속에 다시 넣어주시기 바랍니다. 감사합니다. '
        before_landing_script = '승객 여러분, 잠시 후 ' + destination_airport + '에 도착하겠습니다. 좌석벨트를 매주시고 창문 커튼은 열어주십시오. 좌석 등받이와 테이블, 발밭침, 그리고 꺼내주신 짐은 제자리로 해주시기 바랍니다. 감사합니다. '
        after_landing_script = '승객 여러분, ' + destination_airport + '에 도착했습니다. 좌석벨트를 착용하시고 비행기가 멈춘 후 선반을 여실 때에는 물건이 떨어지지 않게 주의해 주십시오. 오늘 스타얼라이언스 아시아나항공을 이용해 주신 승객여러분께 진심으로 감사드리며 늘 여러분과 함께하겠습니다. 안녕히 가십시오. '

    elif airline == 3:  #JinAir

        boarding_script = 'Fly better fly, 진에어에 탑승하신 승객 여러분, 안녕하세요? 저희 지니들은 여러분의 탑승을 진심으로 환영합니다. 이 비행기는 '
        if origin_country != destination_country:
            boarding_script = boarding_script + origin_country + ' ' + origin_city + '에서 ' + destination_country + ' ' + destination_city + '까지 가능 진에어 ' + flight_number + '편입니다. 목적지인 ' + destination_airport + '까지 예정된 비행시간은 이륙 후 '
        else:
            boarding_script = boarding_script + destination_city + '까지 가능 진에어 ' + flight_number + '편입니다. 목적지인 ' + destination_airport + '까지 예정된 비행시간은 이륙 후 '
        if flight_hour >= 1:
            boarding_script = boarding_script + str(flight_hour) + '시간 ' + str(flight_minute) + '분 입니다. '
        else:
            boarding_script = boarding_script + str(flight_minute) + '분 입니다. '

        before_gate_close_script = '출발을 위해 좌석벨트를 매주시고, 등받이와 테이블을 제자리로 해주세요. 또한 휴대용 전자기기를 비행기 모드로 변경해주시고, 비행 중 좌석 간 이동은 삼가시기 바랍니다. 안전하고 편안한 여행을 위한 우리 모두의 약속, 꼭 지켜주세요. 고맙습니다. 기본이 좋아요, 여행은 진에어. '
        before_takeoff_script = '승객 여러분, 우리 비행기는 이제 이륙하겠습니다. 여러분의 안전을 위해 좌석벨트를 매셨는지 다시 한 번 확인해주시기 바랍니다. '
        seat_belt_and_security_script = '계속해서 안내 말씀 드리겠습니다. 승객 여러분의 안전을 위해, 마스크를 반드시 올바르게 착용해주시고, 마스크를 폐기하실 경우 좌석 앞 주머니에 있는 위생 봉투에 넣어 승무원에게 전달해주시기 바랍니다. 아울러 기내에서는 대화 및 불필요한 기내 이동은 자제해주시고, 발열, 기침 등의 의심증상이 있으신 경우 승무원에게 말씀해주시기 바랍니다. 고맙습니다. '
        approach_script = '승객 여러분, 우리 비행기는 ' + destination_airport + '에 접근하고 있습니다. 안전벨트를 매주시고 등받이와 테이블은 제자리로 해주십시오. 창문 덮개는 열어주시고, 꺼내놓으신 짐은 앞 좌석 밑이나 선반 속에 다시 넣어주시기 바랍니다. 감사합니다.'
        before_landing_script = '승객 여러분, 우리 비행기는 곧 착륙하겠습니다. 좌석 등받이와 테이블을 제자리로 해주시고, 좌석벨트를 매주세요. 그리고 착륙 중 창문 덮개는 열어 두시기 바랍니다. '
        after_landing_script = '승객 여러분, 우리 비행기는 ' + destination_airport + '에 도착했습니다. 여러분의 안전을 위해 비행기가 완전히 멈춘 후 좌석벨트 표시등이 꺼질 때까지 자리에서 기다려 주시기 바랍니다. 도착 후 선반을 여실 때는 안에 있는 물건이 떨어질 수 있으니 조심해주세요. 내리실 때는 여러분의 소중한 물건, 그리고 진에어와의 추억 모두 잊지 말고 꼭 챙겨주세요. 국내 최다 노선에 운항중인 저희 진에어는, 앞으로도 여러분의 즐거운 여행길에 함께하겠습니다. 감사합니다. 안녕히 가십시오. 기본이 좋아요, 여행은 진에어. '

    elif airline == 4:  #AirBusan
        if flight_hour >= 1:
            boarding_script = '승객 여러분, 사랑합니다. ' + origin_country + ' ' + origin_city + '에서 ' + destination_airport + '까지 가는 에어부산 ' + flight_number + '편이며, 비행 시간은 이륙 후 ' + str(flight_hour) + '시간 ' + str(flight_minute) + '분 입니다.  지금부터 모든 전자기기는 비행 모드로 바꿔 주시거나 전원을 꺼 주시기 바랍니다. 기내에서는 전자담배를 포함한 흡연, 폭언 및 폭행 등 업무 방해 행위가 엄격히 금지돼 있으니 기내 안전요원인 승무원의 안내에 협조해 주십시오. 또한 코로나19 확산 방지를 위해 기침 또는 재채기를 할 때는 옷 소매로 입과 코를 가려 기침 매너를 준수해주십시오. Fly Smart, 에어부산 프렌즈와 함께 편안한 시간 보내시기 바랍니다. 감사합니다. '
        else:
            boarding_script = '승객 여러분, 사랑합니다. ' + destination_airport + '까지 가는 에어부산 ' + flight_number + '편이며, 비행 시간은 이륙 후 ' + str(flight_minute) + '분 입니다.  지금부터 모든 전자기기는 비행 모드로 바꿔 주시거나 전원을 꺼 주시기 바랍니다. 기내에서는 전자담배를 포함한 흡연, 폭언 및 폭행 등 업무 방해 행위가 엄격히 금지돼 있으니 기내 안전요원인 승무원의 안내에 협조해 주십시오. 또한 코로나19 확산 방지를 위해 기침 또는 재채기를 할 때는 옷 소매로 입과 코를 가려 기침 매너를 준수해주십시오. Fly Smart, 에어부산 프렌즈와 함께 편안한 시간 보내시기 바랍니다. 감사합니다. '

        before_gate_close_script = '승객 여러분, 항공 보안을 위한 탑승권 확인에 협조해주셔서 감사합니다. 에어부산 ' + flight_number + '편 곧 출발하겠습니다. 안전벨트를 매주시기 바랍니다. 감사합니다. '
        before_takeoff_script = '승객 여러분, 곧 이륙하겠습니다. 안전벨트를 매셨는지 다시 한번 확인해주시기 바랍니다. 감사합니다. '
        seat_belt_and_security_script = '계속해서 안내 말씀 드리겠습니다. 코로나19 감염 예방 관리를 위해 기내에서는 반드시 마스크로 입과 코를 완전히 가려 착용해 주시고, 취식을 자제해 주십시오. 또한 자리 이동은 불가하오니 배정받은 좌석에 앉아주시기 바랍니다. 승객 여러분의 안전을 위해 협조해 주십시오. 감사합니다. '
        approach_script = '승객 여러분, 우리 비행기는 ' + destination_airport + '에 접근하고 있습니다. 안전벨트를 매주시고 등받이와 테이블은 제자리로 해주십시오. 창문 덮개는 열어주시고, 꺼내놓으신 짐은 앞 좌석 밑이나 선반 속에 다시 넣어주시기 바랍니다. 감사합니다. '
        before_landing_script = '승객 여러분, 곧 착륙하겠습니다. 안전벨트를 매셨는지 다시 한번 확인해주시기 바랍니다. 감사합니다. '
        after_landing_script = '승객 여러분, ' + destination_airport + '에 도착했습니다. 에어부산 프렌즈와 함께 기분 좋고 편안한 시간 보내셨습니까? 에어부산을 이용해주신 승객 여러분께 진심으로 감사드리며, 언제나 설레는 마음으로 여러분을 모시겠습니다. 감사합니다. 안녕히 가십시오. '

    elif airline == 5:  #AirSeoul

        if origin_country != destination_country:
            boarding_script = '에어서울 가족 여러분, 탑승을 환영합니다. ' + destination_country + ' ' + destination_airport + '까지 가는 에어서울 ' + flight_number + '편의 비행 시간은 '
        else:
            boarding_script = '에어서울 가족 여러분, 탑승을 환영합니다. ' + destination_airport + '까지 가는 에어서울 ' + flight_number + '편의 비행 시간은 '

        if flight_hour >= 1:
            boarding_script = boarding_script + str(flight_hour) + '시간 ' + str(flight_minute) + '분이 걸릴 것으로 예상하며, ' + captain_name + ' 기장과 ' + cabin_name + ' 캐빈 매니저를 비롯한 승무원들과 함께 행복한 여행을 시작하겠습니다. 저희 에어서울은 젋은 비행기, 최대 3인치 더 넓은 좌석 간격으로 보다 쾌적하게 여러분을 모시겠습니다. 기내에서는 안전을 담당하고 있는 안전요원인 승무원의 지시에 따라주시기 바라며, 흡연, 승무원의 업무 방해, 전자기기 사용기준 위반은 항공보안법에 저촉됨을 알려드립니다. 잠시 후 기내 안전에 대해 안내드리겠습니다. 승무원을 주목해주시기 바랍니다. 감사합니다. '
        else:
            boarding_script = boarding_script + str(flight_minute) + '분이 걸릴 것으로 예상하며, ' + captain_name + ' 기장과 ' + cabin_name + ' 캐빈 매니저를 비롯한 승무원들과 함께 행복한 여행을 시작하겠습니다. 저희 에어서울은 젋은 비행기, 최대 3인치 더 넓은 좌석 간격으로 보다 쾌적하게 여러분을 모시겠습니다. 기내에서는 안전을 담당하고 있는 안전요원인 승무원의 지시에 따라주시기 바라며, 흡연, 승무원의 업무 방해, 전자기기 사용기준 위반은 항공보안법에 저촉됨을 알려드립니다. 잠시 후 기내 안전에 대해 안내드리겠습니다. 승무원을 주목해주시기 바랍니다. 감사합니다. '

        before_gate_close_script = '승객 여러분, 탑승권 확인에 도움을 주셔서 감사합니다. 곧 출발하겠으니 자리에 앉아 좌석벨트를 매주시기 바랍니다. 감사합니다. '
        before_takeoff_script = '승객 여러분, 기다려 주셔서 감사합니다. 에어서울 비행기 곧 이륙하겠습니다. 좌석벨트를 매셨는지 다시 한번 확인해주시기 바랍니다. '
        seat_belt_and_security_script = '승객 여러분, 방금 좌석 벨트 표시등이 꺼졌습니다. 그러나 비행기가 갑자기 흔들리는 경우에 대비해 자리에서는 항상 좌석벨트를 매시기 바랍니다. 좌석벨트 표시등이 켜질 경우 안전을 위해 서비스가 제한될 수 있음을 알려드립니다. 휴대전화 또는 보조배터리는 압착될 경우 화재의 위험이 있습니다. 좌석 등받이를 움직이기 전 전자기기가 좌석 틈새로 빠지지 않았는지 확인하시기 바랍니다. 또한 전자담배를 포함한 기내에서의 흡연은 항공 보안법에 따라 엄격히 금지돼있음을 알려드립니다. 감사합니다. '
        approach_script = '승객 여러분, 잠시 후 ' + destination_airport + '에 도착하겠습니다. 좌석벨트를 매주시고, 좌석 등받이와 테이블은 제자리로 해주시기 바랍니다. 창문 커튼은 열어주시고, 짐은 선반이나 앞 좌석 밑에 넣어주십시오. 감사합니다. '
        before_landing_script = '에어서울 가족 여러분, 에어서울 비행기 곧 착륙하겠습니다. 좌석벨트를 매셨는지 다시 한번 확인해주시기 바랍니다. 감사합니다. '
        after_landing_script = '에어서울 가족 여러분, ' + destination_airport + '에 도착했습니다. 여러분의 안전을 위해 좌석벨트를 계속 매고 계시고, 비행기가 완전히 멈춘 후 선반을 여실 때에는 물건이 떨어지지 않게 주의해주시기 바랍니다. 오늘 에어서울을 탑승해주신 여러분께 감사드리며, 다음 여행에 다시 만나뵙게 되기를 바랍니다. 아울러 에어서울 홈페이지를 방문하시면 무료 또는 특가 항공권 구매 혜택을 누리실 수 있습니다. 승객 여러분의 많은 이용 바랍니다. 안녕히 가십시오. '

    elif airline == 6: #T'way Air

        if origin_country != destination_country:
            boarding_script = '티웨이 가족 여러분, 이 비행기는 ' + destination_country + ' ' + destination_airport + '까지 가는 티웨이항공 ' + flight_number + '편이며, 예정된 비행시간은 이륙 후 '
        else:
            boarding_script = '티웨이 가족 여러분, 이 비행기는 ' + destination_airport + '까지 가는 티웨이항공 ' + flight_number + '편이며, 예정된 비행시간은 이륙 후 '

        if flight_hour >= 1:
            boarding_script = boarding_script + str(flight_hour) + '시간 ' + str(flight_minute) + '분 입니다. 좌석벨트를 매주시고 등받이와 팔걸이, 창문덮개 그리고 테이블을 제자리로 해주십시오. 모든 휴대용 전자기기의 와이파이를 포함한 무선 통신 기능을 해제하시고, 비행기 모드로 변경해주시기 바랍니다. 또한, 코로나19 감염 예방관리 지침에 따라 기내에서는 항시 마스크를 착용해주시고, 반드시 지정된 좌석에 앉아 주시기 바랍니다. 마스크를 착용하지 않을 경우 국토교통부의 지시에 따라 탑승이 제한될 수 있습니다. '
        else:
            boarding_script = boarding_script + str(flight_minute) + '분 입니다. 좌석벨트를 매주시고 등받이와 팔걸이, 창문덮개 그리고 테이블을 제자리로 해주십시오. 모든 휴대용 전자기기의 와이파이를 포함한 무선 통신 기능을 해제하시고, 비행기 모드로 변경해주시기 바랍니다. 또한, 코로나19 감염 예방관리 지침에 따라 기내에서는 항시 마스크를 착용해주시고, 반드시 지정된 좌석에 앉아 주시기 바랍니다. 마스크를 착용하지 않을 경우 국토교통부의 지시에 따라 탑승이 제한될 수 있습니다. '

        boarding_script = boarding_script + '오늘 ' + captain_name +' 기장을 비롯한 저희 승무원들은 여러분을 ' + destination_city + '까지 정성껏 모시겠습니다. 산업안전보건법에 따라 고객 응대 근로자를 위한 보호 조치가 시행되었습니다. 승무원을 향한 폭언 및 무리한 요구 등은 삼가주시기 바랍니다. 따뜻한 말 한마디와 배려로 편안한 여행이 되도록 티웨이 가족 여러분의 많은 협조 부탁드립니다. '
        before_gate_close_script = '티웨이항공 ' + flight_number + '편, 출입문 닫겠습니다. 지상직원은 하기해 주십시오. 휴대용 전자기기는 비행기 모드로 변경해주시고, 리튬베터리가 내장된 스마트 가방의 전원은 꺼주시기 바랍니다. 아울러, 맥북 프로 15인치 제품은 배터리 안전 문제로 기내에서의 사용을 금지하고 있습니다. '
        before_takeoff_script = '티웨이 가족 여러분, 곧 이륙하겠습니다. 좌석벨트를 매셨는지 확인해주시기 바랍니다.'
        seat_belt_and_security_script = '티웨이 가족 여러분, 좌석벨트 표시등이 꺼졌습니다. 기류 변화에 대비해 자리에서는 항상 좌석벨트를 매주시기 바랍니다. 선반을 여실 때는 물건이 떨어지지 않도록 주의해 주십시오. 또한, 리튬베터리 화재 예방을 위해 소지하신 전자기기나 보조 배터리의 발열, 또는 부풀어 오르는 증상이 발생했을 경우 즉시 승무원에게 알려주시기 바랍니다. '
        approach_script = '티웨이 가족 여러분, 잠시 후 ' + destination_airport + '에 도착하겠습니다. 또한, 착륙에 필요한 안전 업무 수행을 위해 기내 판매를 종료하겠습니다.구매를 하지 못하신 분께서는 양해해주시기 바랍니다. 꺼내 놓으신 짐들은 떨어지지 않도록 선반 속과 앞 좌석 밑에 보관해주십시오. 좌석벨트를 매주시고 등받이와 팔걸이, 창문 덮개, 그리고 테이블을 제자리로 해주시기 바랍니다. 모든 휴대용 전자기기의 와이파이를 포함한 무선 통신 기능을 해제하시고, 비행기 모드로 변경해주십시오. '
        before_landing_script = '티웨이 가족 여러분, 저희 비행기는 착륙을 위해 바퀴를 내렸습니다. 가족 여러분의 안전을 위해 좌석벨트를 매주시고, 화장실 사용은 삼가주시기 바랍니다. 고맙습니다. '
        after_landing_script = '티웨이 가족 여러분, 우리 비행기는 ' + destination_airport + '에 도착했습니다. 비행기가 완전히 멈춘 후 좌석벨트 표시등이 꺼질 때까지 자리에 앉아 계시기 바랍니다. 선반을 여실 때에는 물건이 떨어지지 않도록 주의해주시고, 잊으신 짐들이 없는지 다시 한 번 살펴주십시오. 행복을 나누는 항공사 티웨이와 함께해주신 가족여러분, 앞으로도 더욱 정성껏 모시겠습니다. 안녕히 가십시오.'

    elif airline == 7:  #AeroK

        if origin_country != destination_country:
            boarding_script = '새로운 여정의 시작, 에어로케이의 탑승을 진심으로 환영합니다. 우리 비행기는 ' + destination_country + ' ' + destination_airport + '까지 가는 에어로케이 ' + flight_number + '편입니다. ' + destination_city + '까지의 비행시간은 이륙 후 '
        else:
            boarding_script = '새로운 여정의 시작, 에어로케이의 탑승을 진심으로 환영합니다. 우리 비행기는 ' + destination_airport + '까지 가는 에어로케이 ' + flight_number + '편입니다. ' + destination_city + '까지의 비행시간은 이륙 후 '

        if flight_hour >= 1:
            boarding_script = boarding_script + str(flight_hour) + '시간 ' + str(flight_minute) + '분이며, '
        else:
            boarding_script = boarding_script + str(flight_minute) + '분이며, '

        boarding_script = boarding_script + captain_name + ' 기장과 ' + cabin_name + ' 객실 사무장을 비롯한 모든 승무원들이 오늘 여러분의 안전하고 즐거운 비행을 담당하겠습니다. 기내 안전요원인 승무원의 지시에 협조해주세요. 항법 장비에 영향을 주는 전자기기의 전원을 꺼주시고, 모바일 기기는 비행모드로 사용해주세요. 전자 담배를 포함한 흡연이나 폭언, 폭행, 성적 수치심 유발행위 등 승무원의 업무를 방해하는 행위가 엄격히 금지돼있으니 유의하세요. 잠시 후 승무원들이 승객 안전 브리핑을 직접 시연하겠습니다. 지금부터 에어로케이와 함께 행복한 여정이 시작됩니다. 고맙습니다. '
        before_gate_close_script = '승객 여러분, 곧 출발하겠습니다. 자리에 앉아 좌석벨트를 매주시기 바랍니다. 감사합니다. '
        before_takeoff_script = '승객 여러분, 곧 이륙하겠습니다. 좌석벨트를 매셨는지 다시 한 번 확인해주세요. '
        seat_belt_and_security_script = '승객 여러분, 방금 좌석 벨트 표시등이 꺼졌습니다. 그러나 비행기가 갑자기 흔들리는 경우에 대비해 자리에서는 항상 좌석벨트를 매시기 바랍니다. 좌석벨트 표시등이 켜질 경우 안전을 위해 서비스가 제한될 수 있음을 알려드립니다. 휴대전화 또는 보조배터리는 압착될 경우 화재의 위험이 있습니다. 좌석 등받이를 움직이기 전 전자기기가 좌석 틈새로 빠지지 않았는지 확인하시기 바랍니다. 또한 전자담배를 포함한 기내에서의 흡연은 항공 보안법에 따라 엄격히 금지돼있음을 알려드립니다. 감사합니다. '
        approach_script = '승객 여러분, 우리 비행기는 착륙을 위해 하강을 시작했습니다. 지금부터 승무원의 안전 업무에 협조해주세요. 좌석벨트를 매주시고 좌석 등받이와 테이블을 제자리로 해주세요. 창문 덮개는 열어주시고, 스마트폰 등의 전자기기는 비행기가 착륙 후 활주로를 벗어날 때까지 비행모드로 계속 유지해주세요.노트북을 포함해 비행 중 꺼내놓은 소지품은 앞 좌석 밑이나 선반 속에 다시 넣어주세요. 고맙습니다. '
        before_landing_script = '승객 여러분, 곧 착륙하겠습니다. 좌석벨트를 매셨는지 다시 한 번 확인해주세요. '
        after_landing_script = '승객 여러분, 우리 비행기는 ' + destination_airport + '에 도착했습니다. 안전을 위해 좌석벨트 표시등이 꺼질 때까지 벨트를 계속 매주세요. 주기장에 도착한 후 선반을 열 때는 안에 있는 물건이 떨어지지 않도록 주의하세요. 오늘 에어로케이를 이용해주신 승객 여러분, 저희와 함께한 시간이 즐겁고 행복하셨기를 바라며, 다음 여행길에도 반가운 모습으로 다시 뵙기를 바랍니다. 고맙습니다. '

    elif airline == 8:  #AirPremia

        if origin_country != destination_country:
            boarding_script = '승객 여러분, 탑승을 진심으로 환영합니다. 이 비행기는 ' + origin_country + ' ' + origin_city + '에서 ' + destination_country + ' ' + destination_airport + '까지 가는 에어프레미아 ' + flight_number + '편입니다. 오늘 예정된 비행 시간은 이륙 후 '
        else:
            boarding_script = '승객 여러분, 탑승을 진심으로 환영합니다. 이 비행기는 ' + origin_city + '에서 ' + destination_airport + '까지 가는 에어프레미아 ' + flight_number + '편입니다. 오늘 예정된 비행 시간은 이륙 후 '

        if flight_hour >= 1:
            boarding_script = boarding_script + str(flight_hour) + '시간 ' + str(flight_minute) +'분입니다. '
        else:
            boarding_script = boarding_script + str(flight_minute) + '분입니다. '

        boarding_script = boarding_script + captain_name + ' 기장을 비롯한 저희 승무원들은 여러분을 정성껏 모시겠습니다. 출발을 위해 좌석벨트를 매주시고, 등받이와 테이블을 제자리로 해주십시오. 모든 휴대용 전자기기는 전원을 끄거나 비행기 모드로 변경해주시기 바랍니다. 또한, 좌석 앞 주머니 속에 보관할 수 없는 큰 전자기기는 좌석 하단, 또는 기내 선반에 보관해 주십시오. 비행 중 여러분의 안전을 담당하는 안전요원인 승무원의 지시에 협조해주시기 바라며, 계속해서 기내 안전에 관해 안내해드리겠습니다. 잠시 화면을 주목해주시기 바랍니다. '
        before_gate_close_script = '승객 여러분, 우리 비행기 곧 출입문 닫습니다. 지상 직원이 계시면 하기해주시기 바랍니다. 고맙습니다. '
        before_takeoff_script = '승객 여러분, 우리 비행기는 곧 이륙하겠습니다. 좌석벨트를 매셨는지 확인해주시기 바랍니다. 고맙습니다. '
        seat_belt_and_security_script = '승객 여러분, 방금 좌석벨트 표시등이 꺼졌습니다. 그러나 기류 변화로 비행기가 갑자기 흔들릴 수 있으니 자리에서는 항상 좌석벨트를 매주시기 바랍니다. 선반을 여실 때에는 안에 있는 물건이 떨어지지 않도록 주의해주십시오. 또한 전자담배를 포함한 기내에서의 흡연은 항공보안법에 따라 엄격히 금지되어 있음을 알려드립니다. 비행 중 도움이 필요한 승객께서는 언제든지 저희 승무원을 불러주십시오. 고맙습니다. '
        approach_script = '승객 여러분, 우리 비행기는 잠시 후 ' + destination_airport + '에 도착하겠습니다. 꺼내놓은 짐 또는 큰 전자기기는 앞 좌석 아래나 선반 속에 다시 보관해 주시기 바랍니다. 고맙습니다. '
        before_landing_script = '승객 여러분, 우리 비행기는 곧 착륙하겠습니다. 좌석벨트를 매주시고 등받이와 테이블을 제자리로 해주십시오. 모든 휴대용 전자기기는 전원을 끄거나 비행기 모드로 변경해주시기 바랍니다. 고맙습니다. '
        after_landing_script = '승객 여러분, 우리 비행기는 ' + destination_airport + '에 도착했습니다. 여러분의 안전을 위해, 비행기가 완전히 멈춘 후 좌석벨트 표시등이 꺼질 때까지 자리에 앉아 기다려주시기 바랍니다. 선반을 여실 때는 안에 있는 물건이 떨어질 수 있으니 주의해주시고, 내리실 때는 잊으신 물건이 없는지 다시 한번 확인해주십시오. 코로나19 감염 예방을 위해 승무원의 안내에 따라 내려주시기 바랍니다. 내리시는 순서가 될 때까지 잠시만 자리에서 기다려주십시오. 오늘도 저희 에어프레미아와 함께해주셔서 대단히 감사합니다. 저희 승무원들은 승객 여러분께서 항상 안전하고 편안하게 여행하실 수 있도록 최선을 다하겠습니다. 고맙습니다. 안녕히 가십시오. '

    elif airline == 9:  #FlyGangwon

        if origin_country != destination_country:
            boarding_script = '승객 여러분, 안녕하십니까? 플라이강원에 탑승하신 것을 진심으로 환영합니다. 이 비행기는 ' + origin_country + ' ' + origin_city + '에서 ' + destination_country + ' ' + destination_airport + '까지 가는 플라이강원 ' + flight_number + '편입니다. 목적지인 ' + destination_airport + '까지 예정된 비행시간은 이륙 후 '
        else:
            boarding_script = '승객 여러분, 안녕하십니까? 플라이강원에 탑승하신 것을 진심으로 환영합니다. 이 비행기는 ' + origin_city + '에서 ' + destination_airport + '까지 가는 플라이강원 ' + flight_number + '편입니다. 목적지인 ' + destination_airport + '까지 예정된 비행시간은 이륙 후 '

        if flight_hour >= 1:
            boarding_script = boarding_script + str(flight_hour) + '시간 ' + str(flight_minute) + '분입니다. 오늘 '
        else:
            boarding_script = boarding_script + str(flight_minute) + '분입니다. 오늘 '

        boarding_script = boarding_script + captain_name + ' 기장을 비롯한 저희 승무원들은 여러분을 정성껏 모시겠습니다. 출발을 위해 휴대전화는 비행모드로 전환해주시고, 노트북 등 큰 전자기기는 좌석 하단, 또는 기내 선반에 보관해주시기 바랍니다. 휴대전화 또는 보조배터리는 압착될 경우 화재의 위험이 있으니 좌석 틈새로 빠지지 않았는지 다시 한번 확인하시기 바랍니다. 비행 중 여러분의 안전을 담당하는 승무원의 지시에 협조해주시기 바라며, 계속해서 잠시 승무원을 주목해주시기 바랍니다. '
        before_gate_close_script = '승객 여러분, ' + destination_city + '까지 가는 플라이강원 ' + flight_number + '편, 곧 출입문 닫겠습니다. 감사합니다. '
        before_takeoff_script = '승객 여러분, 우리 비행기는 곧 이륙하겠습니다. 좌석벨트를 매셨는지 다시 한번 확인해주시기 바랍니다. '
        seat_belt_and_security_script = '승객 여러분, 방금 좌석벨트 표시등이 꺼졌습니다만, 비행기가 갑자기 흔들리는 경우에 대비해 자리에서는 항상 좌석벨트를 매주시기 바랍니다. 휴대전화 또는 보조배터리는 압착될 경우 화재의 위험이 있습니다. 좌석 등받이를 움직이기 전, 전자기기가 좌석 틈새로 빠지지 않았는지 확인하시기 바랍니다. 또한 전자기기를 포함한 기내에서의 흡연은 항공 보안법에 따라 엄격히 금지되어 있음을 알려드립니다. 여러분의 안전한 여행을 위해, 비행 중 음식물 섭취는 가급적 삼가주시고, 화장실을 사용하시는 승객께서는 반드시 손 소독제를 사용해주시기 바랍니다. 사용하신 마스크를 기내에서 교체하시는 경우, 좌석 앞주머니 속에 있는 위생 봉투를 이용하시고 항공기 뒤쪽에 있는 쓰레기통에 폐기해주시기 바랍니다. 또한 발열 등의 의심 증상이 있는 승객께서는 반드시 마스크를 착용하신 상태에서 도움을 요청해주시기 바랍니다. 여러분의 협조에 감사드립니다. '
        approach_script = '승객 여러분, 우리 비행기는 잠시 후에 ' + destination_airport + '에 도착하겠습니다. 좌석벨트를 매주시고 등받이와 테이블을 제자리로 해주십시오. 또한 창문 덮개는 열어주시고, 꺼내놓으신 짐들은 좌석 밑이나 선반 속에 보관해주시기 바랍니다. 감사합니다. '
        before_landing_script = '승객 여러분, 우리 비행기는 곧 착륙하겠습니다. 좌석벨트를 매셨는지 다시 한번 확인해주시기 바랍니다. '
        after_landing_script = '승객 여러분, 우리 비행기는 ' + destination_airport + '에 도착했습니다. 비행기가 완전히 멈춘 후 좌석벨트 표시등이 꺼질 때까지 자리에서 기다려주시고, 선반을 여실 때는 안에 있는 물건이 떨어질 수 있으니 조심해주십시오. 오늘도 플라이강원을 이용해주셔서 대단히 감사합니다. 저희 승무원들은 앞으로도 안전하고 편안한 여행을 위해 최선을 다하겠습니다. 감사합니다. '

    before_landing_script_2 = '승무원, 착석하십시오. '
    kor_script.append(boarding_script)
    kor_script.append(before_gate_close_script)
    kor_script.append(before_takeoff_script)
    kor_script.append(seat_belt_and_security_script)
    kor_script.append(approach_script)
    kor_script.append(before_landing_script)
    kor_script.append(after_landing_script)
    kor_script.append(before_landing_script_2)      # End of Korean Script Generation

    print('Korean Script Generated Successfully')
    print('length of Korean script : ', len(kor_script))

    return kor_script


def eng_make_script(airline, flight_hour, flight_minute, simbrief_data, origin_airport_data, destination_airport_data, captain_name):

    en_script = []
    boarding_script = ''
    before_gate_close_script = ''
    before_takeoff_script = ''
    seat_belt_and_security_script = ''
    approach_script = ''
    before_landing_script = ''
    after_landing_script = ''

    now = datetime.datetime.now(pytz.timezone('UTC')).hour
    now = now + int(simbrief_data[6])

    origin_country = origin_airport_data[5]
    destination_country = destination_airport_data[5]
    destination_city = destination_airport_data[6]
    destination_airport = destination_airport_data[7].strip()
    flight_number = simbrief_data[3]
    captain_name = simbrief_data[4].lower()
    cabin_name = simbrief_data[5].lower()

    print('English Script Info: ')
    print('\t- AirLine Code : ', airline)
    print('\t- Departure : ' + origin_country)
    print('\t- Arrival : ' + destination_airport)
    print('\t- Flight Hour : ' + str(flight_hour))
    print('\t- Flight Minute : ' + str(flight_minute))

    if (now % 24) < 12:
        boarding_script = 'Good morning, '
    elif (now % 24) <= 18:
        boarding_script = 'Good afternoon, '
    else:
        boarding_script = 'Good evening, '

    if airline == 1:        # KoreanAir

        if origin_country != destination_country:
            boarding_script = boarding_script + 'ladies and gentlemen. We would like to welcome you onboard Korean Air, a member of SkyTeam. This is flight ' + flight_number + ' bound for ' + destination_city + ', ' + destination_country + ". "
        else:
            boarding_script = boarding_script + 'ladies and gentlemen. We would like to welcome you onboard Korean Air, a member of SkyTeam. This is flight ' + flight_number + ' bound for ' + destination_city + ". "

        boarding_script = boarding_script + 'During the flight, our cabin crew will be happy to assist you in any way we can. Larger devices such as laptops must be stowed in the overhead bins or under the seat in front of you. Please cooperate with cabin crew who act as safety officers during the flight. Also, we ask that you direct your attention to the video screens for important safety information. '
        before_gate_close_script = 'Ladies and gentlemen, this is Korean Air flight ' + flight_number + ' bound for ' + destination_city + '. We will be departing shortly. Aviation security laws prohibit smoking, disturbing crew members and using non-approved electronic devices during the flight. Additionally, it is prohibited to turn on or charge your 15-inch Apple MacBook Pro laptop during the flight. Thank you for your cooperation. '
        before_takeoff_script = 'Ladies and gentlemen, we are now ready for take-off. Please make sure that your seatbelt is securely fastened.'
        seat_belt_and_security_script = 'Ladies and gentlemen, the captain has turned off seat belt sign but we recommend that you keep your seat fastened at all times. Once the seatbelt is on, we would like to inform you that service may be stopped for safety reasons. Please make sure electronic devices such as cellphones and portable chargers are stored safely as they can be damaged or become a potential biohazard when compressed. You are also reminded that smoking and the of electronic cigarettes are against the law. Thank you. '
        approach_script = 'Ladies and gentlemen, We are approaching ' + destination_airport + '. Please put your carry-on items in the overhead bins or under the seat in front you and open your window shades. Also, we will collect the headphones and magazines. If you are still using your headphones, you may continue to do so. Please leave your headphones in your seat pocket before you leave the aircraft. Thank you. '
        before_landing_script = 'Ladies and gentlemen, we will be landing shortly. Please fasten your seatbelt and open your window shades. Thank you. '
        after_landing_script = 'Ladies and gentlemen, we have landed at ' + destination_airport + '. Please remain seated until the captain turns off the seat belt sign. Please be careful when opening the overhead bins as the conternts may fall out. Thank you for choosing Korean Air, a member of SkyTeam and we hope to see you again soon. '

    if airline == 2:        # Asiana Air

        boarding_script = boarding_script + 'Ladies and gentlemen, Welcome to Asiana Airlines flight ' + flight_number + ', bound for ' + destination_airport + '. Our flight time will be '
        if flight_hour < 1:
            boarding_script = boarding_script
        elif flight_hour == 1:
            boarding_script = boarding_script + '1 hour '
        else:
            boarding_script = boarding_script + str(flight_hour) + 'hours '

        if flight_minute == 0:
            boarding_script = boarding_script + '. '
        elif flight_minute == 1:
            boarding_script = boarding_script + '1 minute. '
        else:
            boarding_script = boarding_script + str(flight_minute) + 'minutes. '

        boarding_script = boarding_script + 'In accordance with aviation security laws, smoking, violation of electronic devices regulations, or interference with captain or cabin crew duties is not permitted. Thank you for flying with Asiana Airlines, a member of Star Alliance. We hope you enjoy the flight. '
        before_gate_close_script = 'Ladies and gentlemen, We will be departing soon. Please be seated and fastened seatbelt. '
        before_takeoff_script = 'Ladies and gentlemen, we will take-off soon. Please checked that your seatbelt fastened. Thank you. '
        seat_belt_and_security_script = 'Ladies and gentlemen, please fasten your seatbelt while you are seated. Also the use of perfume or hair spray within the lavatory may cause the smoke alarm to sound. We will begin duty free service after meal service. If you would like order duty free items, please fill out the order form. If you ordered duty free items preflight, please let us know. For more information please refer to the in-flight shopping magazine. Thank you. '
        approach_script = 'Ladies and gentlemen, We are approaching ' + destination_airport + '. Please put your carry-on items in the overhead bins or under the seat in front you and open your window shades. Also, we will collect the headphones and magazines. If you are still using your headphones, you may continue to do so. Please leave your headphones in your seat pocket before you leave the aircraft. Thank you. '
        before_landing_script = 'Ladies and gentlemen, we will soon be landing at ' + destination_airport + '. To prepare for landing please fasten your seatbelt, return your seat back, leg rest, tray table, upright and open your window shades. Please put your items in back seat pocket, in your overhead bins, or under the seat. Thank you. '
        after_landing_script = 'Ladies and gentlemen, welcome to ' + destination_airport + '. Please remain seated until the seatbelt sign is off. When opening the overhead bins, be careful of bags that may fall out. Thank you for flying Asiana Airlines, a member of Star Alliance. We hope to see you again soon. '


    if airline == 3:        #Jin Air

        boarding_script = boarding_script + 'ladies and gentlemen, We would like to welcome you on board, Jin Air. This is flight ' + flight_number + ' bound for ' + destination_airport + '. Our flight time today will be '
        if flight_hour < 1:
            boarding_script = boarding_script
        elif flight_hour == 1:
            boarding_script = boarding_script + '1 hour '
        else:
            boarding_script = boarding_script + str(flight_hour) + 'hours '

        if flight_minute == 0:
            boarding_script = boarding_script + '. '
        elif flight_minute == 1:
            boarding_script = boarding_script + '1 minute. '
        else:
            boarding_script = boarding_script + str(flight_minute) + 'minutes. '

        boarding_script = boarding_script + 'To prepare for departure, please fasten your seatbelt, and return your seat and tray table to the upright position.Also, please set your electronic devices in airplane mode. Thank you. '
        before_gate_close_script = 'Ladies and gentlemen, We will be departing soon. Please be seated and fastened seatbelt. '
        before_takeoff_script = 'Ladies and gentlemen, we are now ready for take-off. Please make sure that your seatbelt is securely fastened. '
        seat_belt_and_security_script = 'Ladies and gentlemen, for your safety, please wear a mask. In case of discarding a used mask, you must put it in a sanitary bag in your seat pocket and pass it to our cabin crew. Also, please refrain from talking and unnecessary movement in the cabin. If you have symptoms such as fever or cough, please contact our cabin crew. Thank you. '
        approach_script = 'Ladies and gentlemen, We are approaching ' + destination_airport + '. Please put your carry-on items in the overhead bins or under the seat in front you and open your window shades. Also, we will collect the headphones and magazines. If you are still using your headphones, you may continue to do so. Please leave your headphones in your seat pocket before you leave the aircraft. Thank you. '
        before_landing_script = 'Ladies and gentlemen, we will be landing shortly. Please fasten your seatbelt, return your seat and tray table to the upright position, and open your window shade. '
        after_landing_script = 'Ladies and gentlemen, we have landed at ' + destination_airport + '. For your safety, please remain seated until the captain turns off the seatbelt sign. Thank you for flying with Jin Air. We hope to see you again soon. '


    if airline == 4:        #Air Busan
        boarding_script = boarding_script + 'ladies and gentlemen. Welcome to Air Busan flight ' + flight_number + ' bound for ' + destination_airport + '. Our flight time will be '
        if flight_hour < 1:
            boarding_script = boarding_script
        elif flight_hour == 1:
            boarding_script = boarding_script + '1 hour '
        else:
            boarding_script = boarding_script + str(flight_hour) + 'hours '

        if flight_minute == 0:
            boarding_script = boarding_script + '. '
        elif flight_minute == 1:
            boarding_script = boarding_script + '1 minute. '
        else:
            boarding_script = boarding_script + str(flight_minute) + 'minutes. '
        boarding_script = boarding_script + 'Please switch your electronic devices in flight mode. Aviation laws prohibit smoking and violence in the cabin. Also, to prevent the spread of Covid-19, please cover your nose and mouth with your sleeve when coughing or sneezing. We hope you enjoy the flight. Thank you. '
        before_gate_close_script = 'Ladies and gentlemen, please be seated and fasten your seatbelt. Thank you. '
        before_takeoff_script = 'Ladies and gentlemen, we will be taking off shortly. Please make sure your seatbelt is securely fastened. Thank you. '
        seat_belt_and_security_script = 'Ladies and gentlemen, for your safety, please wear a mask. In case of discarding a used mask, you must put it in a sanitary bag in your seat pocket and pass it to our cabin crew. Also, please refrain from talking and unnecessary movement in the cabin. If you have symptoms such as fever or cough, please contact our cabin crew. Thank you. '
        approach_script = 'Ladies and gentlemen, we are approaching ' + destination_airport + '. Please fasten your seatbelt, open the window shade, and return your seat back and tray table to the upright position. Thank you. '
        before_landing_script = 'Ladies and gentlemen, we will be landing shortly. Please check your seatbelt is securely fastened. Thank you. '
        after_landing_script = 'Ladies and gentlemen, we havve landed at ' + destination_airport + '. We wish you had a pleasant flight with us today. Thank you for flying Air Busan, and we hope to see you again soon. '

    if airline == 5:        #Air Seoul
        boarding_script = boarding_script + 'Ladies and gentlemen, Welcome to Air Seoul flight ' + flight_number + ' bound for ' + destination_airport + '. The captain is ' + captain_name + ', and the cabin manager is ' + cabin_name + '. Our flight time will be '
        if flight_hour < 1:
            boarding_script = boarding_script
        elif flight_hour == 1:
            boarding_script = boarding_script + '1 hour '
        else:
            boarding_script = boarding_script + str(flight_hour) + 'hours '

        if flight_minute == 0:
            boarding_script = boarding_script + '. '
        elif flight_minute == 1:
            boarding_script = boarding_script + '1 minute. '
        else:
            boarding_script = boarding_script + str(flight_minute) + 'minutes. '
        boarding_script = boarding_script + 'In accordance with aviation security law, we remind you that smoking, violation of electronic device regulation, or interference with captain or cabin duty is not permitted in any time. During the flight, please follow the instruction of the cabin crew. We will show safety demonstration. Please pay attention to cabin crew. Thank you. '
        before_gate_close_script = 'Ladies and gentlemen, we will depart soon. Please remain seated and fasten your seatbelt. Thank you for your cooperation. '
        before_takeoff_script = 'Thank you for waiting, ladies and gentlemen. We will take off soon. Please fasten your seatbelt. '
        seat_belt_and_security_script = 'Ladies and gentlemen, the captain has turned off seat belt sign but we recommend that you keep your seat fastened at all times. Once the seatbelt is on, we would like to inform you that service may be stopped for safety reasons. Please make sure electronic devices such as cellphones and portable chargers are stored safely as they can be damaged or become a potential biohazard when compressed. You are also reminded that smoking and the of electronic cigarettes are against the law. Thank you. '
        approach_script = 'Ladies and gentlemen, we will soon land at ' + destination_airport + '. Please remain seated and fasten your seatbelt. Return your seat back and tray table upright and open the window shade. Please stow bags in the overhead bin or under the seat. Thank you. '
        before_landing_script = 'Ladies and gentlemen, we will land soon. Please check that your seatbelt is fastened. Thank you. '
        after_landing_script = 'Ladies and gentlemen, welcome to ' + destination_airport + '. Please remain seated until the seatbelt sign is off. When opening the overhead bin, be careful of bags that may fall out. Thank you for flying with Air Seoul. We hope to see you again soon. '

    if airline == 6:        # T'way
        boarding_script = boarding_script + 'T wayers. This is T way air flight ' + flight_number + ' bound for ' + destination_airport + '. Our flight time today will be '
        if flight_hour < 1:
            boarding_script = boarding_script
        elif flight_hour == 1:
            boarding_script = boarding_script + '1 hour '
        else:
            boarding_script = boarding_script + str(flight_hour) + 'hours '

        if flight_minute == 0:
            boarding_script = boarding_script + 'after take-off. '
        elif flight_minute == 1:
            boarding_script = boarding_script + '1 minute after take-off. '
        else:
            boarding_script = boarding_script + str(flight_minute) + 'minutes after take-off. '
        boarding_script = boarding_script + 'Please return your seat back, arm rest, and tray table to the upright position and open the window shade. Please fasten your seatbelt and change your electronic devices to airplane mode and wireless connection including WIFI function. Due to Corona virus, please wear a mask in the cabin. Thank you. '
        before_gate_close_script = 'Door closing. All ground staffs, please deplane. Please change your electronic devices to airplane mode. Also, smart bag with lithium battery must be turned off. Thank you. '
        before_takeoff_script = 'Dear T wayers, we will be taking off soon. Please make sure that your seatbelt is fastened. '
        seat_belt_and_security_script = 'Dear T wayers, the seatbelt sign is off. We recommend you keep your seatbelt fastened while seated. When opening the overhead bin, be careful as the contents may fall out. Also, if your lithium battery is swelling or generating heat, please contact our cabin crew immediately. Thank you. '
        approach_script = 'Dear T wayers, we are approaching ' + destination_airport + '. We will now close the in-flight sales to prepare for landing. Please put your carry on items in the overhead bins or under the seat in front of you. Return your seat back, arm rest, and tray table to the upright position and open the window shade. Please fasten your seatbelt and change your electronic devices to airplane mode and wireless connection including WIFI function. Thank you. '
        before_landing_script = 'Dear T wayers, we will be landing soon. Please make sure that your seatbelt is fastened. Thank you. '
        after_landing_script = 'Dear T wayers, we have landed at ' + destination_airport + '. Please remain seated until the seatbelt sign is turned off. When opening the overhead bin, be careful as the contents may fall out. Please remember to take all your belongings. Thank you for joining us today, and we hope to see you again soon. Happy T way, it\'s yours. '

    if airline == 7:        #AeroK
        boarding_script = boarding_script + 'everyone, Welcome aboard, AeroK flight ' + flight_number + ' bound for ' + destination_airport + '. The captain of this flight is ' + captain_name + ', and your duty purser ' + cabin_name + '. Our flight time will be '
        if flight_hour < 1:
            boarding_script = boarding_script
        elif flight_hour == 1:
            boarding_script = boarding_script + '1 hour '
        else:
            boarding_script = boarding_script + str(flight_hour) + 'hours '

        if flight_minute == 0:
            boarding_script = boarding_script + 'after take-off. '
        elif flight_minute == 1:
            boarding_script = boarding_script + '1 minute after take-off. '
        else:
            boarding_script = boarding_script + str(flight_minute) + 'minutes after take-off. '

        boarding_script = boarding_script + 'In accordance with aviation security law, any violations including smoking, verbal abuse and sexual humiliation are strictly prohibited. At this time, please make sure that your mobile devices are on air flight mode. On behalf of your entire crew, it is our pleasure to have you onboard. Enjoy your journey with AeroK. Thank you. '
        before_gate_close_script = 'Door closing. All ground staffs, please deplane. Please change your electronic devices to airplane mode. Also, smart bag with lithium battery must be turned off. Thank you. '
        before_takeoff_script = 'We will be taking off shortly. Please make sure that your seatbelt is securely fastened. Thank you. '
        seat_belt_and_security_script = 'Ladies and gentlemen, the captain has turned off seat belt sign but we recommend that you keep your seat fastened at all times. Once the seatbelt is on, we would like to inform you that service may be stopped for safety reasons. Please make sure electronic devices such as cellphones and portable chargers are stored safely as they can be damaged or become a potential biohazard when compressed. You are also reminded that smoking and the of electronic cigarettes are against the law. Thank you. '
        approach_script = 'We have begun our descend to land. Please make sure that your seatbelt are fastened. Put your seat back and tray tables to the upright position. Open your window shades, and make sure your mobile devices and other devices and on air flight mode. For your safety, stow your laptops and other belongings under the seat in front of you or in the overhead bin. Thank you. '
        before_landing_script = 'We will be landing shortly. Please make sure that your seatbelt is securely fastened. Thank you. '
        after_landing_script = 'Dear passengers, We have landed at ' + destination_airport + '. For your safety, please remain seated with your seatbelt fastened until the seatbelt sign is off. Please be careful when opening the overhead bins since the items may have shifted during the flight. Once again, we thank you for flying with AeroK today. And we hope to see you again soon. Thank you.'

    if airline == 8:        #Air Premia
        boarding_script = boarding_script + 'ladies and gentlemen. We would like to welcome you on board, Air Premia flight ' + flight_number + ' bound for ' + destination_airport + '. Our flight time today will be '
        if flight_hour < 1:
            boarding_script = boarding_script
        elif flight_hour == 1:
            boarding_script = boarding_script + '1 hour '
        else:
            boarding_script = boarding_script + str(flight_hour) + 'hours '

        if flight_minute == 0:
            boarding_script = boarding_script + 'after take-off. '
        elif flight_minute == 1:
            boarding_script = boarding_script + '1 minute after take-off. '
        else:
            boarding_script = boarding_script + str(flight_minute) + 'minutes after take-off. '
        boarding_script = boarding_script + 'All crew members with captain ' + captain_name + ' are pleased to serve you to your destination. To prepare for departure, please fasten your seatbelt, and return your seat and tray table to the upright position. We also ask you change all your electronic devices to the airplane mode. Large electronic devices must be stowed under the seat or in the overhead bins during take-off and landing. Please cooperate with cabin crew who acts as safety officers during the flight. We ask you to direct your attention to the video screen for safety information. '
        before_gate_close_script = 'Ladies and gentlemen, we are about to close the door. Ground staff, please get off the aircraft now. Thank you. '
        before_takeoff_script = 'Ladies and gentlemen, we will be taking off soon. Please make sure that your seatbelt is fastened. Thank you. '
        seat_belt_and_security_script = 'Ladies and gentlemen, the captain has turned off the seatbelt sign. We recommend you keep your seatbelt fastened whenever you are seated. When opening the overhead bins, please be careful as the contents may fall out. Smoking and the use of electronic cigarettes are not possible anywhere on board. If you need any assistance, please ask our cabin crew. Thank you. '
        approach_script = 'Ladies and gentlemen, we are now approaching ' + destination_airport + '. Please stow your carry-on items including large electronic devices in the overhead bins or under the seat in front of you. Thank you. '
        before_landing_script = 'Ladies and gentlemen, we will be landing shortly. Please fasten your seatbelt, and return your seat and tray table to the upright position. Also, please change your electronic devices to the airplane mode at this time. Thank you. '
        after_landing_script = 'Ladies and gentlemen, we have landed at ' + destination_airport + '. For your safety, please remain seated until the seatbelt sign has been turned off. Be careful when opening the overhead bins, as the contents may fall out. Please check you have personal belongings with you when you leave the aircraft. To prevent the spread of covid-19, please stay in your seat until your turn has come. Thank you for choosing Air Premia, and we hope to see you again soon. '

    if airline == 9:        # Fly Gangwon
        boarding_script = boarding_script + ' ladies and gentlemen. Captain ' + captain_name + ' and the entire crew would like to welcome you onboard Fly Gangwon flight ' + flight_number + ' bound for ' + destination_airport + '. Our flight time today will be '
        if flight_hour < 1:
            boarding_script = boarding_script
        elif flight_hour == 1:
            boarding_script = boarding_script + '1 hour '
        else:
            boarding_script = boarding_script + str(flight_hour) + 'hours '

        if flight_minute == 0:
            boarding_script = boarding_script + 'after take-off. '
        elif flight_minute == 1:
            boarding_script = boarding_script + '1 minute after take-off. '
        else:
            boarding_script = boarding_script + str(flight_minute) + 'minutes after take-off. '
        boarding_script = boarding_script + 'During the flight, our cabin crew will be happy to assist you in any way we can. For departure, mobile phones should be switched to flight mode. And larger devices such as laptop computers must be stowed under your seat or in the overhead bins during take-off and landing. Please make sure electronic devices such as mobile phones and portable chargers are stowed safely as they can be damaged or become a potential fire hazard when compressed. Also, please cooperate with cabin crew who act as safety officers during the flight. And please direct your attention to the cabin crew for safety information. '
        before_gate_close_script = 'Ladies and gentlemen, this is Fly Gangwon flight ' + flight_number + ' bound for ' + destination_airport + '. We are closing the door now. Ground staff, please get off the plane. Thank you. '
        before_takeoff_script = 'Ladies and gentlemen, we will be taking off shortly. Please make sure your seatbelt is securely fastened. '
        seat_belt_and_security_script = 'Ladies and gentlemen, the captain has turned off the seatbelt sign. We recommend you keep your seatbelt fastened at all times. For your safe travel, we ask you to refrain from eating and use the hand sanitizer when you go to the lavatory. In case of changing your mask onboard, please put your used mask in the airsickness bag and throw away in the trash bin at back of the cabin. If you have a fever, cough, or any other symptoms, please inform one of our cabin crew. Thank you for your cooperation. '
        approach_script = 'Ladies and gentlemen, we will soon land at ' + destination_airport + '. Please fasten your seatbelt and return your seat back and tray table to the upright position. Also, please open your window shade stow your carry on items in the overhead bins or under the seat in front of you. Thank you. '
        before_landing_script = 'Ladies and gentlemen, we will be landing shortly. Please make sure your seatbelt is securely fastened. '
        after_landing_script = 'Ladies and gentlemen, we have landed at ' + destination_airport + '. Please remain seated until the captain turns off the seatbelt sign. Be careful when opening the overhead bins as the contents may fall out. Thank you for choosing Fly Gangwon, and we hope to see you again soon.'

    before_landing_script_2 = 'Cabin crew, please be seated. '
    en_script.append(boarding_script)
    en_script.append(before_gate_close_script)
    en_script.append(before_takeoff_script)
    en_script.append(seat_belt_and_security_script)
    en_script.append(approach_script)
    en_script.append(before_landing_script)
    en_script.append(after_landing_script)
    en_script.append(before_landing_script_2)  # End of English Script Generation

    print('English Script Generated Successfully')

    return en_script