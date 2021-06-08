import random

# プレイヤー
class Player:
    def count_up(self, cnt, cnt_max, finish_num):
        for _ in range(10):
            val = input('Enter number: ')
            # 整数か判定
            try:
                cnt = int(val)
            except ValueError:
                print("整数を入力してください")
                continue
            # 範囲判定
            if 1 <= cnt <= cnt_max:
                return cnt
            print("1から", cnt_max, "までの数字を選んでください")

# 敵キャラ
class EnemyCharacter:
    """
    ランダムにカウントアップする
    直前で止められるときだけ、止める
    """
    def count_up(self, cnt, cnt_max, finish_num):
        # 直前で止められるときは、止める
        if cnt <  finish_num - 1 <= cnt + cnt_max:
            return finish_num - cnt - 1
        return random.randint(1, cnt_max)

# xx言ったら負けゲーム
class CountUpGame:
    def __init__(
        self, finish_num: int, cnt_max: int, p1_first: bool
    ):
        self.finish_num = finish_num # 言ったら負け数字
        self.cnt_max = cnt_max # 一度に上げられる数
        self.cnt = 0 # カウント(ゼロスタート)
        self.players = {
            k: v for k, v in enumerate(
                [Player(), EnemyCharacter()]
                )
            }
        if p1_first: # p1が最初かどうか
            self.player_num = 0
        else:
            self.player_num = 1
    
    def play(self):
        # 1ずつ上げても、最大数字ターン目には終わる
        for i in range(self.finish_num):
            print(i+1, "ターン目")
            self.print_info()
            self.count_up()
            # 終了判定
            if self.is_finish():
                print("終了")
                print("プレイヤー", self.player_num, "の負け")
                break
            self.change_player()
    
    def print_info(self):
        print("現在")
        print("プレイヤー", self.player_num)
        print(
            "カウント", self.cnt,
            "言ったら負けの数", self.finish_num,
            "最大上げられる数字", self.cnt_max
        )
    
    def count_up(self):
        cnt_up = self.players[self.player_num].count_up(
            cnt=self.cnt,
            cnt_max=self.cnt_max,
            finish_num=self.finish_num
        )
        print(cnt_up, "上げる")
        self.cnt += cnt_up
    
    def is_finish(self):
        return self.cnt >= self.finish_num
    
    def change_player(self):
        # 最後のプレイヤーのときは、最初に戻る
        if self.player_num == max(self.players):
            self.player_num = min(self.players)
            return
        self.player_num += 1
        return

if __name__ == "__main__":
    game = CountUpGame(
        finish_num=30,
        cnt_max=3,
        p1_first=True,
    )
    game.play()
