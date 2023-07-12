# 인트로
print()
intro: str = """
게임 시작 전 안내
    -선택지를 고르며 진행하는 게임으로, 예상 플레이 타임은 3~5분입니다.
    -대화문이 넘어가지 않을 시 Enter를 누르세요.
    -선택지를 고를 때 선택지의 번호(숫자)를 입력하면 됩니다.
        ex) 좀비와 마주쳤습니다. 1.싸운다 2.도움을 요청한다. 3.도망친다.
            어떻게 하시겠습니까?:<선택지 번호>
    -소지품을 중복으로 선택할 수는 있지만 변화는 없습니다.
    -이름을 입력하면 시작합니다."""
print(intro)
print()
print("### Road to Refuge ###")
User_name = input("당신의 이름을 입력해주세요: ")
print()
print("""2098년 세계 여러곳에서 동시다발적으로 좀비 바이러스가 퍼져 생존자들은 모두 벙커로 피신했습니다.
      당신은 더 이상 원래 살던 곳에 머무르기엔 너무 위험합니다. 집에서 나와 벙커에 도착해야합니다.""")
print()
import sys

# 플레이어 사망
def dead():
    print(f"{User_name}은(는) 사망했다!")
    sys.exit()

# 첫번째 턴
print("(1/7)")
print()
print("시간이 없습니다. 당신은 집을 나서기 전 물건 하나를 챙겨가기로 합니다.")
print("1.샷건")
print("2.돈")
print("3.자전거")

choice_1 = int(input("어떤 물건을 선택하시겠습니까?: "))
if choice_1 == 1:
    has_shotgun = True
    has_money = False
    has_bike = False
    print("당신은 먼지 쌓인 창고에서 샷건을 챙겼습니다.")
    print()
elif choice_1 == 2:
    has_shotgun = False
    has_money = True
    has_bike = False
    print("그래도 쓸모가 있겠지. 당신은 서랍에서 비상금을 꺼내 가방에 넣었습니다.")
    print()
elif choice_1 == 3:
    has_shotgun = False
    has_money = False
    has_bike = True
    print("시간도 없는데 빨리빨리 가야지. 당신은 자전거를 타기로 합니다.")
    print()
else:
    print("선택지를 줬는데 굳이 다른 걸 입력하는 심리는 뭘까?")
    dead()

# 두번째 턴
print("(2/7)")
print()
print("당신은 집을 나섰습니다.")
print("1.카센터")
print("2.병원")
print("3.학교")

choice_2 = int(input("어느 쪽으로 가시겠습니까?: "))
if choice_2 == 1:
    location = "car center"
    has_toolset = True
    has_firstaidkit = False
    has_baseballbat = False
    print("'지금 당장 RG갱에 가입하세요!' 이상한 포스터가 붙어있네요. 당신은 카센터에 도착하여 공구세트를 찾았습니다.")
    print()
elif choice_2 == 2:
    location = "hospital"
    has_toolset = False
    has_firstaidkit = True
    has_baseballbat = False
    print("'RG갱에게 기부를 해주세요! 만약 하지 않는다면 우리가 당신을 찾아가겠습니다!' 이게 무슨 말이야? \
          당신은 기묘한 포스터가 붙어있는 병원에 도착하여 구급상자를 찾았습니다.")
    print()
elif choice_2 == 3:
    location = "school"
    has_toolset = False
    has_firstaidkit = False
    has_baseballbat = True
    print("'이 연장들은 RG갱이 후원합니다.' 갱단에서 후원도 해? 당신은 학교에 도착하여 야구방망이를 찾았습니다. \
          몇 개는 못이 박혀있지만, 무서워 보이니 두고 가기로 합니다.")
    print()
else:
    print("선택지를 줬는데 굳이 다른 걸 입력하는 심리는 뭘까?")
    dead()

# 세번째 턴
print("(3/7)")
print()
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

has_knife = False
has_keymap = False

# 이벤트 좀비
if event == zom:
    print(event)
    for value in events_turn3[zom].values():
        print(value)

    choice_zom = int(input("어떻게 하시겠습니까?: "))
    if choice_zom == 1:
        if has_shotgun:
            print("당신의 샷건 소리를 듣고 좀비 떼가 몰려와 사망했습니다.")
            dead()
        else:
            print("샷건이 없는데 어떻게 샷건을 쏘죠? 순간 당신은 샷건이 없다는 것을 깨달았지만 이미 늦었습니다.")
            dead()
    elif choice_zom == 2:
        if has_money:
            print("진심이세요? 당신은 좀비에게 자선가 행세를 하다 물려 사망했습니다.")
            dead()
        elif has_baseballbat:
            print("당신은 돈을 찾으려고 가방을 뒤졌고 야구방망이가 눈에 들어왔습니다. 당신은 야구방망이를 휘둘러 좀비를 쓰러뜨렸습니다.")
            print("좀비를 상대하다 야구방망이를 부러뜨렸습니다. 아까워라...")
            has_baseballbat = False
        else:
            print("당신은 가방에서 돈을 찾다가 그만 그 녀석의 친구가 되고 말았습니다.")
            dead()
    elif choice_zom == 3:
        if has_bike:
            print("당신은 자전거로 좀비들을 따돌렸습니다. 훗, 느려.")
        else:
            print("아 맞다 자전거 두고왔지! 당신은 죽을 힘을 다해 도망쳤습니다.")
            choice_zom = 4
    elif choice_zom == 4:
        event_run = ["당신은 가까스로 도망쳤습니다.", "당신은 최선을 다했지만 결국 실패했습니다..."]
        run_result = random.choice(event_run)
        if run_result == event_run[0]:
            print(run_result)
        else:
            print(run_result)
            dead()
    else:
        print("선택지를 줬는데 굳이 다른 걸 입력하는 심리는 뭘까?")
        dead()
# 이벤트 강도
elif event == rob:
    print(event)
    for value in events_turn3[rob].values():
        print(value)

    choice_rob = int(input("어떻게 하시겠습니까?: "))
    if choice_rob == 1:
        if has_shotgun:
            event_rob = [
                "당신은 용감하게 맞서 싸웠지만 장렬히 전사하였습니다...", 
                 "칫, 재수없긴. 강도들은 불필요한 리스크보다는 떠나는게 좋다고 판단했습니다."
            ]
            rob_result = random.choice(event_rob)
            if rob_result == event_rob[0]:
                print(rob_result)
                dead()
            else:
                print(rob_result)
        elif has_money:
            print("뭐야, 이 녀석 사실 총 없는 거 같은데? 당신은 가진 돈을 모두 빼앗겼습니다.")
            has_money = False
        else:
            print("당신이 샷건을 가지고 있지 않고 있다는 것을 들켜 몸에 바랑구멍이 생겼습니다.")
            dead()
    elif choice_rob == 2:
        if has_money:
            print("당신은 돈을 주고 풀려났습니다. 목숨보다 중요한건 없죠!")
            has_money = False
        else:
            print("당신은 그들에게 ATM기만 있으면 돈을 줄 수 있다고 설득했으나 통하지 않았습니다.")
            dead()
    elif choice_rob == 3:
        event_run = [
            "당신은 용감하게 맞서 싸웠지만 장렬히 전사하였습니다...",
            "칫, 재수없긴. 강도들은 불필요한 리스크보다는 떠나는게 좋다고 판단했습니다."
        ]
        run_result = random.choice(event_run)
        if run_result == event_run[0]:
            print(run_result)
        else:
            print(run_result)
            dead()
    else:
        print("선택지를 줬는데 굳이 다른 걸 입력하는 심리는 뭘까?")
        dead()
# 이벤트 생존자
elif event == suv:
    print(event)
    for value in events_turn3[suv].values():
        print(value)

    choice_suv = int(input("어떻게 하시겠습니까?: "))
    if choice_suv == 1:
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
                dead()
        else:
            print("아뿔싸! 그는 칼을 가지고 있었습니다. 당신에게는 아무것도 남아있지 않습니다.")
            has_money = False
            has_bike = False
            has_toolset = False
            has_firstaidkit = False
    elif choice_suv == 2:
        print("1.주방용 식칼")
        print("2.구급상자")
        print("3.벙커쪽으로 향하는 지름길 약도")
        print("4.별로 맘에 드는 것이 없다.")

        choice_moneybuy = int(input("어느 것을 사시겠습니까?: "))
        if has_money == False:
            if choice_moneybuy == 1 or 2 or 3:
                print("사고싶은데 돈이 없네... 눈앞에 물건이 아른거립니다.")
                print()
                choice_moneybuy = 4
            else:
                print("당신은 아무것도 사지 않고 가기로 했습니다.")
                print()
        elif choice_moneybuy == 1:
            print("당신은 주방용 식칼을 구입했다.")
            print()
            has_money = False
            has_knife = True
        elif choice_moneybuy == 2:
            print("당신은 구급상자를 구입했다.")
            print()
            has_money = False
            has_firstaidkit = True
        elif choice_moneybuy == 3:
            print("당신은 벙커쪽으로 향하는 지름길 약도를 구입했다.")
            print()
            has_money = False
            has_keymap = True
        elif choice_moneybuy == 4:
            print("당신은 아무것도 사지 않고 가기로 했습니다.")
            print()
        else:
            print("선택지를 줬는데 굳이 다른 걸 입력하는 심리는 뭘까?")
            dead()
    elif choice_suv == 3:
        print("1.샷건")
        print("2.돈")
        print("3.공구세트")
        print("4.별로 맘에 드는 것이 없다.")

        choice_bbuy = int(input("어느 것과 바꾸시겠습니까?"))
        if has_bike == False:
            if choice_bbuy == 1 or 2 or 3:
                print("그냥 자전거 타고 올걸... 눈앞에 물건이 아른거립니다.")
                print()
                choice_bbuy = 4
            else:
                print("당신은 아무것도 사지 않고 가기로 했습니다.")
                print()
        elif choice_bbuy == 1:
            print("당신은 샷건과 교환했다.")
            print()
            has_bike = False
            has_shotgun = True
        elif choice_bbuy == 2:
            print("당신은 돈과 교환했다.")
            print()
            has_bike = False
            has_money = True
        elif choice_bbuy == 3:
            print("당신은 공구세트와 교환했다.")
            print()
            has_bike = False
            has_toolset = True
        elif choice_bbuy == 4:
            print("당신은 아무것도 사지 않고 가기로 했습니다.")
            print()
        else:
            print("선택지를 줬는데 굳이 다른 걸 입력하는 심리는 뭘까?")
            dead()
    elif choice_suv == 4:
        print("당신은 아무것도 사지 않고 가기로 했다.")
        print()
    else:
        print("선택지를 줬는데 굳이 다른 걸 입력하는 심리는 뭘까?")
        dead()

# 네번째 턴
print("(4/7)")

# 약도가 있으면 턴을 스킵해야 하기 때문에 네번째 턴은 함수화
def turn_four(keymap: bool, skip_true: str):
    # 각종 엔딩 불리언 값 선언
    soldier_ending = False
    keyman_ending = False
    murderer = False

    lst_skip = ["당신이 어디로 가야할지 고민했지만 곧 약도의 도움으로 빠르게 나아갔습니다.", "Noskip"]
    skip_true = random.choice(lst_skip)
    if (keymap == True) and (skip_true == lst_skip[0]):
        print("당신은 약도의 도움으로 빠르게 앞으로 나아갔습니다.")
    else:
        # 세 갈래 길 선택
        print("약도가 딱히 쓸모있는 것 같진 않습니다. 아... 당했다...")
        print("당신은 길을 가던 중 세 갈래 길을 발견했습니다.")
        print("1.왼쪽")
        print("2.가운데")
        print("3.오른쪽")
        choice_way = int(input("어느쪽으로 가시겠습니까?"))
        
        # 왼쪽-군인을 만났을 경우
        if choice_way == 1:
            print("당신은 잠시 모여서 쉬고있는 군인들을 마주쳤습니다.")
            print("1.달려든다.")
            print("2.도움을 요청한다.")
            print("3.슬쩍 지나간다.")
            choice_soldier = int(input("어떻게 하시겠습니까?"))
            
            if choice_soldier == 1:
                print("갑자기 무슨 짓이야? 당신은 당신의 행동에 책임을 졌습니다.")
                dead()
            elif choice_soldier == 2:
                print("""군인들은 다짜고짜 도와달라고 하는 당신에게 당황스러워했지만
                      곧 몇 가지 검사를 거친 후 당신이 안전하다는 것을 확인했습니다.""")
                if has_firstaidkit:
                    print("군인들은 상비약이 필요하다고 말했고 당신은 운좋게도 그 요구를 들어줄 수 있었습니다.")
                    print("고맙군, 기회가 된다면 도움을 주도록 하지. 군인과 좋은 대화를 끝마친 당신은 발걸음을 재촉합니다.")
                    soldier_ending = True
                    has_firstaidkit = False
                else:
                    print("""군인들은 상비약이 필요하다고 했지만 구급상자가 없어 도울 수 없었습니다.
                          당신은 군인들에게 간단한 치료를 받고 다시 길을 떠났습니다.""")
            elif choice_soldier == 3:
                print("당신은 군인들에게 가로막혔지만 몇 가지 검사를 받고 별 문제 없이 지나갔습니다.")
            else:
                print("선택지를 줬는데 굳이 다른 걸 입력하는 심리는 뭘까?")
                dead()
        
        # 가운데-죽어가는 사람을 본 경우
        elif choice_way == 2:
            print("길을 따라 걷는 도중 피를 흘리며 쓰러져있는 사람을 보았습니다.")
            print("1.도와준다.")
            print("2.가진 거 다 내놔!")
            print("3.그냥 지나친다.")
            choice_keyman = int(input("어떻게 하시겠습니까?"))
            print(choice_keyman)

            if (choice_keyman == 1) and (has_firstaidkit == True):
                print("당신은 구급상자를 이용해 남자를 치료했습니다.")
                print("정말 고맙습니다. 남자는 다음에 만나면 꼭 보답하겠다고 하고선 떠났습니다.")
                print("벙커 위치라도 물어볼걸 그랬나요? 당신은 다시 걷기 시작했습니다.")
                keyman_ending = True
            elif (choice_keyman == 1) and (has_firstaidkit == False):
                print("그를 치료하려고 했지만 아무 도구도 없는 당신은 별로 할 수 있는게 없었고 남자는 서서히 빛을 잃었습니다.")
                print("안타깝지만 당신은 다시 걷기 시작했습니다.")
            elif choice_keyman == 2:
                print("당신은 말도 하기 힘든 그를 협박했고 그는 곧 식어갔습니다.")
                print("그를 뒤져보았지만 딱히 유용해보이는 물건은 없었습니다.")
                print("당신은 사람을 죽였다는 찝찝함과 함께 다시 걷기 시작했습니다.")
                murderer = True
            elif choice_keyman == 3:
                print("자신이 별로 도울 수 없을 것 같다고 판단한 당신은 재빨리 그 자리를 벗어났습니다.")
            else:
                print("선택지를 줬는데 굳이 다른 걸 입력하는 심리는 뭘까?")
                dead()
        
        # 오른쪽-아무일도 없음
        elif choice_way == 3:
            print("당신은 오른쪽 길로 걸어갔습니다. 곳곳에 피가 묻어있고 사람이 급하게 떠난 흔적이 보입니다.")
            print("내가 과연 살아남을 수 있을까? 도중에 좀비 떼가 나타나면 어쩌지?")
            print("흉흉한 생각을 하며 걷다보니 어느새 길을 빠져나왔습니다.")
        #함수 끝
        else:
            print("선택지를 줬는데 굳이 다른 걸 입력하는 심리는 뭘까?")
            dead()

    return soldier_ending, keyman_ending, murderer

turn_four(has_keymap)

# 다섯번째 턴
"""
다섯번째 턴에서 자고 여섯번째 턴에서는 자다가 쫓기고 일곱번째 턴에서 엔딩
"""
print("(5/7)")
print("꽤 많이 걸어왔다고 생각한 당신은 휴식을 취하기로 합니다.")
print("다행히 좀비는 적어 보이네요. 쉴곳도 어느정도 있는 것 같습니다.")
print("""1.낡은 빌라
      2.가로등 옆 벤치
      3.버려진 차""")
sleep_place = int(input("어디서 휴식을 취할까요?: "))

# 좀비액괴
if sleep_place == 1:
    input("안은 생각보다 깨끗한데? 당신은 적당한 침대를 발견하고 누웠습니다.")
    input("제대로 된 휴식 없이 며칠을 걸어왔던 당신은 금새 잠듭니다. Zzz...")
    input("부스럭 부스럭")
    input("당신은 다른 방에서 나는 수상한 소리에 잠에서 깼습니다. 좀비라기엔 꽤 느린 것 같은데...")
    input("다친 생존자일 수도 있겠다고 판단한 당신은 방문을 조심스레 열어봅니다.")
    input("""오, 이런. 최악의 선택이었습니다. 마치 좀비 여러마리를 합쳐놓은 것처럼 생긴 거대한 괴물이 당신을 인지한 듯 싶습니다.
          잠깐, 저 녀석 이쪽으로 오는데? 당신은 짐을 챙겨 빠르게 도망치기 시작합니다.""")
# 늑대
elif sleep_place == 2:
    input("실내는 위험하지. 당신은 가로등 옆 벤치에서 휴식을 취하기로 했습니다.")
    input("밖에서 잠들면 위험하다는 것을 알고 있었지만 당신은 너무 지친 나머지 잠들고 말았습니다.")
    input("아우우우우우! 당신은 하울링 소리를 듣고 잠에서 깨어났습니다. 이건 명백히 사람 소리가 아닙니다.")
    input("""위험을 직감한 당신은 서둘러 짐을 챙겨 일어났습니다.
          굶주린 늑대들이 무리를 짓고 먹이를 찾는 듯 합니다.""")
    input("이런! 늑대 무리가 당신의 냄새를 맡은 것 같습니다. 하필 가로등이 켜져 있어 쉽게 발각되었습니다. 도망쳐!")
    input("당신은 미친듯이 달리기 시작합니다.")
# 무법자
elif sleep_place == 3:
    input("배기관이 보통 크기가 아닌 것 같은데... 튜닝인가? 당신은 버려진 마개조 빨간 티코를 발견하고 그 안으로 숨어들었습니다.")
    input("자리를 잡고 누워서 잠을 청합니다. 이 정도면 좀비도 못보겠지.")
    input("Zzz...")
    input("간만에 제대로 숙면을 취하던 당신은 시끄러운 엔진 소리에 잠에서 깼습니다. 부아아앙~")
    input("도대체 누가 차를 끄는거지? 당신은 숨죽이며 백미러로 시선을 돌렸습니다.")
    input('''"돈 될만한 거 다 챙겨!", 골목에 아슬아슬하게 들어올만큼 큰 지프차량을 앞세워 뒤로 수많은 차들이 일제히 움직이고 있습니다.
          아무래도 이 근방에서 가장 큰 갱단 같습니다.''')
    input("직감적으로 위험을 감지한 당신은 차에서 내려 도망갈 준비를 했습니다.")
    input("이건...? 당신은 카시트에 있던 차키를 발견했습니다. \n아차! 크기만큼 엄청난 불길을 내뿜으며 시동이 걸리는 바람에 들키고 말았습니다!")
    input("당신은 바로 악셀을 밟고 달리기 시작했습니다.")
else:
    print("선택지를 줬는데 굳이 다른 걸 입력하는 심리는 뭘까?")
    dead()

# 여섯번째 턴 네스팅을 줄이기 위해 턴을 두개로 나눔
if sleep_place == 1:
    input("급하게 거리로 나와 최대한 빠르게 달립니다. 저 녀석 점점 빨리 쫓아오는것 같은데요?")
    print("1.맞서 싸운다. \n2.왔던 길로 되돌아가 안전한 장소를 찾는다. \n3.가던 길로 쭉 달린다.")
    place1_end = int(input("어떻게 하시겠습니까?: "))
    if (place1_end == 1) and (has_shotgun == True) and (has_baseballbat == True) and (has_knife == True):
        input("이대로 도망치면 어차피 죽을거라고 판단한 당신은 지금껏 모아왔던 무기들을 들고 맞서 싸우기 시작했습니다.")
        input("꾸역꾸역 달려오는 좀비덩어리는 속도는 빠르지만 방향 전환이 힘들어보였습니다. 당신은 그 헛점을 노리기로 합니다.")
        input("좀비덩어리가 당신 코앞까지 온 순간, 당신은 몸을 날려 옆으로 구릅니다.")
        input("차를 들이받고 넘어져 둔해진 틈을 타 당신은 샷건을 꺼내 녀석에게 한 방 먹입니다.")
        input("끼에에엑! 귀가 찢어질 것 같은 괴성을 지르며 다시 공격해옵니다.")
        input("장전을 하려면 시간이 많이 소모되어 야구방망이로 무기를 바꿔듭니다.")
        print("1.계속해서 싸운다. \n2.역시 도망간다.")
        # 싸워서 기회 엿보기
        place1_end2 = input("어떻게 하시겠습니까?")
        if place1_end2 == 1:
            input("조금만 더 하면 끝낼 수 있을 것 같습니다. 당신은 녀석이 달려드는 것을 잽싸게 피한 뒤 다시 야구방망이로 마구 후려칩니다.")
            input("좀비덩어리가 화가 난 듯이 일어섭니다. 이건 별로 효과적이진 않은 것 같군요. 녀석이 다시 달려듭니다.")
            input("허억! 가까스로 피했습니다. 야구방망이는 부러져버렸네요. 당신은 나이프를 집어듭니다.")
            has_baseballbat = False
            input("돌진이 잘 먹히지 않자 마구잡이로 팔을 휘두릅니다. 이 정도야 피하기 쉽죠. \
                  당신은 팔을 힘껏 휘두르다가 중심을 못잡고 휘청거리는 녀석에게 나이프로 긁어 큰 상처를 만들어냈습니다.")
            input("갸아아아악! 피인지 뭔지 모를 기분 나쁜 액체가 흘러나오는 녀석이 온힘을 다해 돌진하기 시작합니다. \
                  이것만 피하면 어떻게 할 수 있을것 같습니다!")
            print("1.옆으로 굴러 피한다. \n2.뒤로 물러나 거리를 확보한다.")
            place1_end3 = input("어떻게 하시겠습니까?")
            # 옆으로 굴러 살기
            if place1_end3 == 1:
                input("당신은 고된 몸을 이끌고 옆으로 힘껏 구릅니다. 녀석은 당신 뒤에 있던 트럭과 강하게 부딪혀 정신을 못차립니다.")
                input("지금이다. 당신은 재빨리 샷건을 장전해 마지막 총알을 녀석의 무지막지 큰 머리에 대고 쏩니다.")
                input("꾸륵꾸륵... 괴물은 이상한 소리를 내며 주저앉고 맙니다. 더 이상 움직이는 것 같진 않네요.")
                input("해치웠나? 당신은 오염된 나이프와 끝부분이 터진 샷건을 버리고 시야에 들어오는 벙커 안내문을 읽고 벙커를 향해 갑니다.")
                input("당신의 승리입니다.")
            elif place1_end3 == 2:
                input("이건 옆으로 피하기엔 위험하겠는데? 당신은 빠르게 뒷걸음질 치며 기회를 보기로 합니다.")
                input("'턱'")
                input("아뿔싸! 등 뒤에 있던 트럭을 못보고 걸음이 막혔습니다! 당신은 어쩔수 없이 샷건을 장전합니다.")
                input("장전을 하기엔 시간이 너무 모자랐습니다. 당신은 트럭과 함께 납작쥐포가 되었습니다.")
                dead()
            else:
                print("선택지를 줬는데 굳이 다른 걸 입력하는 심리는 뭘까?")
                dead()
        elif place1_end2 == 2:
            input("야구방망이로는 택도 없겠는데? 이 괴물을 상대하기엔 벅찰것 같아 도망치기 시작합니다.")
            input("쿵쿵쿵쿵쿵쿵쿵. 한번 달리기 시작한 괴물의 직선 속도가 당신보다 월등히 빨라 금방 따라잡히고 말았습니다.")
            print("당신은 괴물에게 깔려 바닥과 물아일체를 이뤘습니다.")
            dead()
        else:
            print("선택지를 줬는데 굳이 다른 걸 입력하는 심리는 뭘까?")