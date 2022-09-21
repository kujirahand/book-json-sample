import json, random, os
# 初期設定 --- (※1)
savefile = 'janken_history.json' # プレイ履歴を保存するファイル
history = [] # 履歴
hand_labels = ['グー', 'チョキ', 'パー']

# メイン処理 --- (※2)
def main():
    load_history() # プレイ履歴を読み込む
    # 繰り返しゲームを行う
    while True:
        show_history() # プレイ履歴の表示
        flagStop = janken_game()
        if flagStop: break

# ジャンケンゲーム --- (※3)
def janken_game():
    # コンピューターとプレイヤーの手を決める
    com = random.randint(0, 2)
    user = ask_user_hand()
    if user == 3: return True
    print('貴方:', hand_labels[user])
    print('相手:', hand_labels[com])
    # 勝負判定 --- (※4)
    result = (com - user + 3) % 3
    hantei = 'あいこ'
    if result == 1: hantei = '勝ち'
    if result == 2: hantei = '負け'
    print('判定:', hantei)
    # プレイヤーの手の情報と勝敗を履歴に追加 --- (※5)
    history.append({'com': com, 'user': user, 'result': hantei})
    save_history() # ファイルに保存
    return False

def load_history(): # プレイ履歴をファイルから読む --- (※6)
    global history
    if os.path.exists(savefile):
        with open(savefile, encoding='utf-8') as fp:
            history = json.load(fp)

def save_history(): # 履歴をファイルへ保存 --- (※7)
    with open(savefile, 'w', encoding='utf-8') as fp:
        json.dump(history, fp, ensure_ascii=False, indent=2)

def show_history():
    # あいこを除いた勝ち数を調べる --- (※8)
    cnt, win = 0, 0
    for i in history:
        if i['result'] == 'あいこ': continue
        if i['result'] == '勝ち': win += 1
        cnt += 1
    # 勝率を計算
    r = 0 if cnt == 0 else win /cnt
    print('勝率: {} ({}/{})'.format(r, win, cnt))

def ask_user_hand():
    # ユーザーからの入力を得る --- (※9)
    print('---', len(history), '回目のジャンケン ---')
    print('[0]グー [1]チョキ [2]パー [3]終了')
    user = input('どの手を出す? > ')
    try:
        no = int(user)
        if 0 <= no <= 3: return no
    except:
        pass
    return ask_user_hand() # 無効な値なら再度入力を得る

if __name__ == '__main__': main()
