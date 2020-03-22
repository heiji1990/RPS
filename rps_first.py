import random
import sys

file_name = "result.txt"
hands = ["グー","チョキ","パー"]

#勝敗をファイルに書き込む
def save(userid,result):
    data = str(userid) + " " + result
    f = open(file_name,"a")
    f.write(data)
    f.write("\n")

def game_end():
    print("ゲームを終了します")
    sys.exit()

"""
第一引数：ｓ　テキストファイルの全文字数
第二引数：search_str 検索する文字
"""
def countChar(s,search_str):
    #検索する文字だけいったん消すことで、全体から検索する文字を引けば、検索する文字の数を調べられる
    return len(s) - len(s.replace(search_str,""))

def show(userid):

    print("検索するUSER_ID:",userid)

    f = open(file_name,"r")
    result = f.read()
    f.close()

    uid = str(userid)
    print("これまでじゃんけんした数",countChar(result,uid))
    print("勝った回数:")
    print(countChar(result,"勝"))
    print("負けた回数:")
    print(countChar(result,"負"))
    print("あいこの回数:")
    print(countChar(result,"あ"))

while True:
    userid = int(input("USER_IDを入力してください："))
    print("1:じゃんけんをする　2:勝敗を見る 3:ゲーム終了")
    op = int(input())

    if op == 1:
        while True:
            # 2の時
            print("じゃんけんを開始します。")
            comp_hands = random.randint(0,2)

            #オプション追加

            print("何を出しますか？０：グー　１：チョキ　２：パー　３ゲーム終了")
            my_hand = int(input())

            if my_hand == 3:
                game_end()
            elif my_hand < 0 or my_hand > 2:
                print("０～２の間で手を選んでください")
                continue

            print("自分：",hands[my_hand])
            print("コンピュータ：",hands[comp_hands])

            jadge = (my_hand - comp_hands + 3)% 3
            if jadge == 0:
                print("結果は...あいこ")
                #あいこの時は「あ」と書き込む
                save(userid,result="あ")
            elif jadge == 1:
                print("結果は...負け")
                #ユーザ名orIDと勝敗にファイルに書き込む
                save(userid,result="負")
            else:
                print("結果は...勝ち！！")
                #ユーザ名orIDと勝敗に書き込む
                save(userid,result="勝")
    elif op == 2:
        show(userid)
    elif op == 3:
        end()
    else:
        #エラーメッセージ
        print("０～３の数字を入力してください")



