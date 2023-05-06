#인트로
print()
intro = """
게임 시작 전 안내
    -선택지를 고르며 진행하는 게임으로, 예상 플레이 타임은 3~5분입니다.
    -선택지를 고를 때 선택지의 번호(숫자)를 입력하면 됩니다.
        ex) 좀비와 마주쳤습니다. 1.싸운다 2.도움을 요청한다. 3.도망친다.
            어떻게 하시겠습니까?:<선택지 번호>
    -소지품을 중복으로 선택할 수는 있지만 변화는 없습니다.
    -이름을 입력하면 시작합니다.
"""
print(intro)
print()
print("### Road to Refuge ###")
User_name = input("당신의 이름을 입력해주세요.: ")
print()
print("2098년 세계는 좀비 바이러스가 퍼져 생존자들은 모두 벙커로 피신했습니다. 당신은 위험한 집에서 나와 벙커에 도착해야합니다.")
print()
import sys

#첫번째 턴
print("시간이 없습니다. 당신은 집을 나서기 전 물건 하나를 챙겨가기로 합니다.")
print("1.샷건")
print("2.돈")
print("3.자전거")

choice_1 = input("어떤 물건을 선택하시겠습니까?: ")
if choice_1 == "1":
    has_shotgun = True
    has_money = False
    has_bike = False
    print("당신은 먼지 쌓인 창고에서 샷건을 챙겼습니다.")
    print()
elif choice_1 == "2":
    has_shotgun = False
    has_money = True
    has_bike = False
    print("그래도 쓸모가 있겠지. 당신은 서랍에서 비상금을 꺼내 가방에 넣었습니다.")
    print()
elif choice_1 == "3":
    has_shotgun = False
    has_money = False
    has_bike = True
    print("시간도 없는데 빨리빨리 가야지. 당신은 자전거를 타기로 합니다.")
    print()
else:
    print("선택지를 줬는데 굳이 다른 걸 입력하는 심리는 뭘까?")
    print(f"{User_name}은(는) 사망했다!")
    sys.exit()

#두번째 턴
print("당신은 집을 나섰습니다.")
print("1.카센터")
print("2.병원")
print("3.학교")

choice_2 = input("어느 쪽으로 가시겠습니까?: ")
if choice_2 == "1":
    location = "car center"
    has_toolset = True
    has_firstaidkit = False
    has_baseballbat = False
    print("당신은 카센터에 도착하여 공구 세트를 찾았습니다.")
elif choice_2 == "2":
    location = "hospital"
    has_toolset = False
    has_firstaidkit = True
    has_baseballbat = False
    print("당신은 병원에 도착하여 구급상자를 찾았습니다.")
elif choice_2 == "3":
    location = "school"
    has_toolset = False
    has_firstaidkit = False
    has_baseballbat = True
    print("당신은 학교에 도착하여 야구방망이를 찾았습니다.")
else:
    print("선택지를 줬는데 굳이 다른 걸 입력하는 심리는 뭘까?")
    print(f"{User_name}은(는) 사망했다!")
    sys.exit()

#세번째 턴
import random

zom = "당신은 좀비 몇 마리와 마주쳤습니다."
rob = "이런! 당신이 길을 가던 중 강도와 마주쳤습니다. 강도는 당신에게 돈을 내놓으라고 협박합니다."
suv = "당신은 또 다른 생존자와 마주쳤습니다. 생존자는 당신에게 물물교환을 하자고 합니다."
events_turn3 = {
    zom: {
        "1": "1.샷건을 쏴서 물리친다.",
        "2": "2.돈을 준다.",
        "3": "3.자전거를 타고 도망간다.",
        "4": "4.그냥 도망간다."
    },
    rob: {
        "1": "1.질 수 없지, 나도 샷건으로 협박한다.",
        "2": "2.순순히 돈을 준다.",
        "3": "3.도망간다."
    },
    suv: {
        "1": "1.가진 걸 모두 내놓으라고 위협한다.",
        "2": "2.돈으로 물물교환을 한다.",
        "3": "3.자전거로 물물교환을 한다.",
        "4": "4.별로 교환하고 싶지 않은데... 가던 길을 계속 간다."
    }
}
event = random.choice(list(events_turn3.keys()))
print(event)
#이벤트 좀비
if event == events_turn3[zom]:
    for key, value in events_turn3[zom].items():    #events_turn3[key].items()는 events_turn3 안에 있는 key에 해당하는 value 값을 튜플로 돌려준다.
        print(value)                                #여기선 event_turnt3의 key의  value가 다시한번 딕셔너리 형태이다. 고로 인자 두 개를 할당하는것.

    choice_zom = input("어떻게 하시겠습니까?: ")
    if choice_zom == "1":
        if has_shotgun:
            print("당신의 샷건 소리를 듣고 좀비 떼가 몰려와 사망했습니다.")
            print(f"{User_name}은(는) 사망했다!")
            sys.exit()
        else:
            print("샷건이 없는데 어떻게 샷건을 쏘죠? 순간 당신은 샷건이 없다는 것을 깨달았지만 이미 늦었습니다.")
            print(f"{User_name}은(는) 사망했다!")
            sys.exit()
    elif choice_zom == "2":
        if has_money:
            print("진심이세요? 당신은 좀비에게 자선가 행세를 하다 물려 사망했습니다.")
            print(f"{User_name}은(는) 사망했다!")
            sys.exit()
        elif has_baseballbat:
            print("당신은 돈을 찾으려고 가방을 뒤졌고 야구방망이가 눈에 들어왔습니다. 당신은 야구방망이를 휘둘러 좀비를 쓰러뜨렸습니다.")
            print("좀비를 상대하다 야구방망이를 부러뜨렸습니다. 아까워라...")
            has_baseballbat = False
        else:
            print("당신은 가방에서 돈을 찾다가 그만 그의 친구가 되고 말았습니다.")
            print(f"{User_name}은(는) 사망했다!")
            sys.exit()
    elif choice_zom == "3":
        if has_bike:
            print("당신은 자전거로 좀비들을 따돌렸습니다. 훗, 느려.")
        else:
            print("아 맞다 자전거 두고왔지! 당신은 죽을 힘을 다해 도망쳤습니다.")
            choice_zom = "4"
    elif choice_zom == "4":
        event_run = ["당신은 가까스로 도망쳤습니다.", "당신은 최선을 다했지만 결국 실패했습니다..."]
        run_result = random.choice(event_run)
        if run_result == event_run[0]:
            print(run_result)
        else:
            print(run_result)
            print(f"{User_name}은(는) 사망했다!")
            sys.exit()
    else:
        print("선택지를 줬는데 굳이 다른 걸 입력하는 심리는 뭘까?")
        print(f"{User_name}은(는) 사망했다!")
        sys.exit()

#이벤트 강도
if event == events_turn3[rob]:
    for key, value in events_turn3[rob].items():
        print(value)
    
    choice_rob = input("어떻게 하시겠습니까?: ")
    if choice_rob == "1":
        if has_shotgun:
            event_rob = ["당신은 용감하게 맞서 싸웠지만 장렬히 전사하였습니다...", 
                         "칫, 재수없긴. 강도들은 불필요한 리스크보다는 떠나는게 좋다고 판단했습니다."]
            rob_result = random.choice(event_rob)
            if rob_result == event_rob[0]:
                print(rob_result)
            else:
                print(rob_result)
                print(f"{User_name}은(는) 사망했다!")
                sys.exit()
        elif has_money:
            print("뭐야, 이 녀석 샷건 없는 거 같은데? 당신은 가진 돈을 모두 빼앗겼습니다.")
            has_money = False
        else:
            print("당신이 샷건을 가지고 있지 않고 있다는 것을 들켜 몸에 바랑구멍이 생겼습니다.")
            print(f"{User_name}은(는) 사망했다!")
            sys.exit()
    elif choice_rob == "2":
        if has_money:
            print("당신은 돈을 주고 풀려났습니다. 목숨보다 중요한건 없죠!")
            has_money = False
        else:
            print("당신은 그들에게 ATM기만 있으면 돈을 줄 수 있다고 설득했으나 통하지 않았습니다.")
            print(f"{User_name}은(는) 사망했다!")
            sys.exit()
    elif choice_rob == "3":
        run_result = random.choie(event_run)
        if run_result == event_run[0]:
            print(run_result)
        else:
            print(run_result)
            print(f"{User_name}은(는) 사망했다!")
            sys.exit()
    else:
        print("선택지를 줬는데 굳이 다른 걸 입력하는 심리는 뭘까?")
        print(f"{User_name}은(는) 사망했다!")
        sys.exit()

#이벤트 생존자
if event == events_turn3[suv]:
    for key, value in events_turn3[suv].items():
        print(value)
    
    choice_suv = input("어떻게 하시겠습니까?: ")
    if choice_suv == "1":
        if has_shotgun:
            print("어이쿠 당연히 드려야지요^^ 당신은 그에게서 가진 돈을 모두 빼앗았다.")
            has_money = True
        elif has_baseballbat:
            event_suv = ["살려만 주십쇼! 당신은 그를 빈털털이로 만들었다.",
                         "죽어도 안 돼! 당신은 그와 몸싸움을 하던 중 넘어져 돌부리에 머리를 부딪히고 말았습니다."]
            suv_result = random.choice(event_suv)
            if suv_result == event_suv[0]:
                print(suv_result)
                has_money = True
            else:
                print(suv_result)
                print(f"{User_name}은(는) 사망했다!")
                sys.exit()
        else:
            print("아뿔싸! 그는 칼을 가지고 있었습니다. 당신에게는 아무것도 남아있지 않습니다.")
            has_money = False
            has_bike = False
            has_toolset = False
            has_firstaidkit = False
    elif choice_suv == "2":
        print("1.주방용 식칼")
        print("2.구급상자")
        print("3.벙커쪽으로 향하는 지름길 약도")
        print("4.별로 맘에 드는 것이 없다.")

        choice_mbuy = input("어느 것을 사시겠습니까?")
        if has_money == False:
            if choice_mbuy == "1" or "2" or "3":
                print("사고싶은데 돈이 없네... 눈앞에 물건이 아른거립니다.")
                choice_mbuy = "4"
            else:
                print("당신은 아무것도 사지 않고 가기로 했습니다.")
        elif choice_mbuy == "1":
            print("당신은 주방용 식칼을 구입했다.")
            has_money = False
            has_knife = True
        elif choice_mbuy == "2":
            print("당신은 구급상자를 구입했다.")
            has_money = False
            has_firstaidkit = True
        elif choice_mbuy == "3":
            print("당신은 벙커쪽으로 향하는 지름길 약도를 구입했다.")
            has_money = False
            has_keymap = True
        elif choice_mbuy == "4":
            print("당신은 아무것도 사지 않고 가기로 했습니다.")
        else:
            print("선택지를 줬는데 굳이 다른 걸 입력하는 심리는 뭘까?")
            print(f"{User_name}은(는) 사망했다!")
            sys.exit()
    elif choice_suv == "3":
        print("1.샷건")
        print("2.돈")
        print("3.공구세트")
        print("4.별로 맘에 드는 것이 없다.")

        choice_bbuy = input("어느 것과 바꾸시겠습니까?")
        if has_bike == False:
            if choice_bbuy == "1" or "2" or "3":
                print("그냥 자전거 타고 올걸... 눈앞에 물건이 아른거립니다.")
                choice_bbuy = "4"
            else:
                print("당신은 아무것도 사지 않고 가기로 했습니다.")
        elif choice_bbuy == "1":
            print("당신은 샷건과 교환했다.")
            has_bike = False
            has_shotgun = True
        elif choice_bbuy == "2":
            print("당신은 돈과 교환했다.")
            has_bike = False
            has_money = True
        elif choice_bbuy == "3":
            print("당신은 공구세트와 교환했다.")
            has_bike = False
            has_toolset = True
        elif choice_bbuy == "4":
            print("당신은 아무것도 사지 않고 가기로 했습니다.")
        else:
            print("선택지를 줬는데 굳이 다른 걸 입력하는 심리는 뭘까?")
            print(f"{User_name}은(는) 사망했다!")
            sys.exit()
    elif choice_suv == "4":
        print("당신은 아무것도 사지 않고 가기로 했다.")
    else:
        print("선택지를 줬는데 굳이 다른 걸 입력하는 심리는 뭘까?")
        print(f"{User_name}은(는) 사망했다!")
        sys.exit()