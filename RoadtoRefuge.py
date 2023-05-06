#인트로
print()
print = """
게임 시작 전 안내
    -선택지를 고르며 진행하는 게임으로, 예상 플레이 타임은 3~5분입니다.
    -선택지를 고를 때 선택지의 번호(숫자)를 입력하면 됩니다.
        ex) 좀비와 마주쳤습니다. 1.싸운다 2.도움을 요청한다. 3.도망친다.
            어떻게 하시겠습니까?:<선택지 번호>
    -이름을 입력하면 시작합니다.
"""
print()
User_name = input("당신의 이름을 입력해주세요.: ")
print()
print("2098년 세계는 좀비 바이러스가 퍼져 생존자들은 모두 벙커로 피신했습니다. 당신은 위험한 집에서 나와 벙커에 도착해야합니다.")
print()
import sys

#첫번째 턴
print("당신은 집을 나서기 전 물건을 챙겨가기로 합니다.")
print("1.샷건")
print("2.돈")
print("3.자전거")

choice_1 = input("어떤 물건을 선택하시겠습니까?: ")
if choice_1 == "1":
    has_shotgun = True
    has_money = False
    has_bike = False
    print()
elif choice_1 == "2":
    has_shotgun = False
    has_money = True
    has_bike = False
    print()
elif choice_1 == "3":
    has_shotgun = False
    has_money = False
    has_bike = True
    print()
else:
    print("선택지를 줬는데 굳이 다른 걸 입력하는 심리는 뭘까?")
    print("%s은(는) 사망했다!" %User_name)
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
    print("당신은 학교에 도착하여 야구배트를 찾았습니다.")
else:
    print("선택지를 줬는데 굳이 다른 걸 입력하는 심리는 뭘까?")
    print("%s은(는) 사망했다!" %User_name)
    sys.exit()

#세번째 턴
import random

events = [
    "당신은 좀비 몇 마리와 마주쳤습니다.",
    "이런! 당신이 길을 가던 중 강도와 마주쳤습니다. 강도는 당신에게 돈을 내놓으라고 협박합니다.",
    "계속해서 앞으로 나아가던 중 다른 생존자와 마주쳤습니다. 생존자는 당신과 물물교환을 하자고 합니다."
]
event = random.choice(events)
print(event)
#이벤트_좀비
if event == events[0]:
    print("1.샷건을 쏴서 물리친다.")
    print("2.돈을 준다.")
    print("3.자전거를 타고 도망간다.")
    print("4.그냥 도망간다.")

    event_zombie = input("어떻게 하시겠습니까?: ")
    if event_zombie == "1":
        if has_shotgun == True:
            print("당신의 샷건 소리를 듣고 좀비 떼가 몰려와 사망했습니다.")
            print("%s은(는) 사망했다!" %User_name)
            sys.exit()
        else:
            print("샷건이 없는데 어떻게 샷건을 쏘죠? 순간 당신은 샷건이 없다는 것을 깨달았지만 이미 늦었습니다.")
            print("%s은(는) 사망했다!" %User_name)
            sys.exit()
    elif event_zombie == "2":
        if has_money == True:
            print("진심이세요? 당신은 좀비에게 기부하려다 물려 사망했습니다.")
            print("%s은(는) 사망했다!" %User_name)
            sys.exit()
        else:
            print("당신은 가방에서 돈을 찾다가 그만 그의 친구가 되고 말았습니다.")
            print("%s은(는) 사망했다!" %User_name)
            sys.exit()
    elif event_zombie == "3":
        if has_bike == True:
            print("당신은 좀비들로부터 무사히 벗어났습니다.")
        else:
            event_zombie = "4"
            print("아 맞다 자전거 두고왔지! 당신은 죽을힘을 다해 도망쳤습니다.")
    elif event_zombie == "4":
        event_run = ["당신은 가까스로 도망쳤습니다.", "당신은 최선을 다했지만 결국 실패했습니다..."]
        run_result = random.choice(event_run)
        if run_result == event_run[0]:
            print(run_result)
        else:
            print(run_result)
            print("%s은(는) 사망했다!" %User_name)
            sys.exit()
    else:
        print("선택지를 줬는데 굳이 다른 걸 입력하는 심리는 뭘까?")
        print("%s은(는) 사망했다!" %User_name)
        sys.exit()
#이벤트_강도
elif event == events[1]:
    print("1.나도 샷건으로 협박한다.")
    print("2.순순히 돈을 준다.")
    print("3.자전거로 도망간다.")
    print("4.그냥 도망간다.")

    event_robber = input("어떻게 하시겠습니까?: ")
