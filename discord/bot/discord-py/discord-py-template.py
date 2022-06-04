# -*- coding: utf-8 -*-
# discord-py-template-100.py
"""
#
# Discord.py を使った bot サーバーを作成するためのテンプレート
#
# 以下のコードを参考にして、Discord.py を使った bot サーバーを作成してください。
# https://discordpy.readthedocs.io/ja/latest/
#
# @author: Deskuma <e-mail address> <github account> <twitter account> <discord account>
# @version: 1.0.0a # バージョン
# @license: MIT License # ライセンス
# @see: https://discordpy.readthedocs.io/ja/latest/quickstart.html
# @see: https://discordpy.readthedocs.io/ja/latest/api.html
# @see: https://discordpy.readthedocs.io/ja/latest/ext/commands/api.html
# @date: 2022/05/17 # 作成日
# @update: 2022/05/17 # 更新日
#
# @usage: # 使い方
# 準備:
#   - Python3.6.8 以上を使用する
#   - discord.py をインストールする
#   - このファイルに対しての修正箇所を書き直す（後でも良いけど）
#       1. ファイル名を discord-<ボット名>-bot.py に変更する
#       2. 作者名を変更する
#       3. バージョンを変更する
#       4. ライセンスを変更する
#       5. 参考URLを変更する
#       6. 作成日を変更する
#       7. 更新日を変更する
#       8. 使い方を変更する
#       9. ファイルを保存する
#
# 実行:
#   ```sh
#   DISCORD_BOT_TOKEN='bot token' python3 discord-<ボット名>-bot.py
#   ```
# 参考:
#   - https://discordpy.readthedocs.io/ja/latest/quickstart.html
#   - https://discordpy.readthedocs.io/ja/latest/api.html
#   - https://discordpy.readthedocs.io/ja/latest/ext/commands/api.html
#
# @dependency: # 依存関係
#   - このテンプレートは、Python3.6.8 以上を使用する
#   - このテンプレートは、discord.py を使用する
#   - このテンプレートは、以下のライブラリを使用する
#     - asyncio
#     - aiohttp
#     - aioconsole
#     - aiohttp.client_reqrep
#     - aiohttp.client_ws
#
# @note: # 注意事項
# はじめに [PEP8](https://peps.python.org/pep-0008/) にはきっと準拠していません！
# このテンプレートを使用する際は、それらの規約に従ってください。適宜見直して修正します！
#
# ※このプログラムコードおよびコメントも含め大半は GitHub AI ペアプログラミング
#   copilot によって書かれいています。そのため、予期せぬコードが書かれている可能性も
#   あります。厳密なチェックは行っていません。コードを実行する前に、自分で確認してください。
#   （って、copilot が言っています！この上記文章の一部も AI が自動で書いてくれましたｗ）
# -----------------------------------------------------------------------------
変更履歴
version: 1.0.0a コメント修正
version: 1.0.0 初版

"""
# -------------------------------------
# const 定数定義域
# -------------------------------------
"""
定数は、定義された値を変更できない。という言語制約がある。
のだが Python では定数の概念は無くすべて変数として扱われる。
定数名は、すべて大文字と'_'で構成するのが規約になっている。
なので、この場所以外の処理コード中に「大文字変数に代入する」
コードが、あったら*おかしい*と疑うべし（このコードにも含む）
（インスタンスオブジェクト類は変数なので小文字で構成される）
必要なライブラリの読み込み import もここで定義する。

大文字_変数名 = ... 定数
import ... ライブラリの読み込み
from ... import ... as ... # 別名
"""
# -- モジュール ＆ パッケージ------------
import os
from pydoc import cli
import discord  # require: discord.py
from datetime import datetime

# -- 定数 -----------------------------
DEBUG_MODE = False
DISCORD_BOT_TOKEN = os.environ.get("DISCORD_BOT_TOKEN")  # '<discord bot token>'
CMD_PREFIX = "!"  # '<command prefix>'

# BOT 管理者情報
BOT_ADMIN_DISCORD_ID = "<user_id>"  # '<discord bot admin id number>'
BOT_ADMIN_USERNAME = "<username>"  # '<discord bot admin username>'
BOT_ADMIN_DISCRIMINATOR = "0000"  # '<discord bot admin discriminator #number>'

# -------------------------------------
# def 関数定義域
# -------------------------------------
"""
関数は、共通で使う処理などを定義する。
def 関数名(引数1, 引数2=デフォルト値, ...):
    処理
    return 戻り値
"""


def wait(seconds):
    """
    処理を待つ関数
    """
    import time

    time.sleep(seconds)


def zero_pad(num, length):
    """
    数値をゼロで埋める関数
    """
    return str(num).zfill(length)


def get_current_time():
    """
    現在時刻を取得する関数
    """
    return datetime.now().strftime("%Y/%m/%d %H:%M:%S")


def str_date_to_epoch(str_date):
    """
    文字列日付を epoch 日時に変換する関数
    """
    return datetime.strptime(str_date, "%Y/%m/%d %H:%M:%S").timestamp()


def diff_date_time(date_time_1, date_time_2):
    """
    日時差を取得する関数
    """
    epoch_1 = str_date_to_epoch(date_time_1)
    epoch_2 = str_date_to_epoch(date_time_2)
    return epoch_1 - epoch_2


def rand(min, max):
    """
    乱数を取得する関数
    """
    import random

    return random.randint(min, max)


def roll_dice(ndn):
    """
    ダイスロールを行う関数
    """
    nd = ndn.split("d")
    n = int(nd[0])
    d = int(nd[1])
    if n < 1 or d < 1 or n > 9 or d > 100:
        raise ValueError("invalid dice roll")

    result = []
    for _ in range(n):
        result.append(rand(1, d))
    return result


def log(*message):
    """
    ログを出力する関数
    """
    out_flag = True
    # ログ出力フラグを確認して表示するか否かを判断する
    if len(message) != 0 and not DEBUG_MODE:
        if message[0].startswith("[debug]"):
            out_flag = False

    if out_flag:
        print(get_current_time(), *message)


def print_test():
    """
    テスト用関数

    定数や変数の状態確認用です。
    初心のうちは print() 命令たくさん使って中身を常に確認しましょう。
    慣れたら変数の中身を見なくても想像つくようになります。
    """
    log("[test] === test === begin")
    # log("[test] DISCORD_BOT_TOKEN:", DISCORD_BOT_TOKEN)
    log("[test] CMD_PREFIX:", CMD_PREFIX)
    log("[test] BOT_ADMIN_DISCORD_ID:", BOT_ADMIN_DISCORD_ID)
    log("[test] BOT_ADMIN_USERNAME:", BOT_ADMIN_USERNAME)
    log("[test] BOT_ADMIN_DISCRIMINATOR:", BOT_ADMIN_DISCRIMINATOR)
    log("[test] waiting... 2 seconds")
    wait(2)  # 2 秒待つ（これは diff_date_time() のテスト用）
    log("[test] boot_startup_time:", boot_startup_time)
    log("[test] get_current_time:", get_current_time())
    log("[test] diff_date_time:", diff_date_time(get_current_time(), boot_startup_time))
    log("[test] === test === end")
    log()


# -------------------------------------
# class 定義域
# -------------------------------------
"""
クラスは、特定のまとまった処理を定義する。
class クラス名:
    def __init__(self, 引数):
        初期化処理
    def 関数名(self, 引数):
        処理
"""
from abc import ABCMeta, abstractmethod


# -- クラス定義 ------------------------
class Bot:
    def __init__(self, client, token=DISCORD_BOT_TOKEN):
        self.client = client
        self.token = token

    def run(self):
        """bot を起動する"""
        log("[info] === start bot ===")
        log("Bot is running...")
        log("Ready, Discord Bot is activated!")
        log("Standby for events...")
        self.client.run(self.token)
        log()
        log("[info] === Bot is stopped ===")

    def stop(self):
        """bot を停止する"""
        # 停止する前に処理する内容を書く
        log("[info] boot_startup_time:", boot_startup_time)
        log("[info] get_current_time:", get_current_time())
        log(
            "[info] diff_date_time:",
            diff_date_time(get_current_time(), boot_startup_time),
        )


class Command(metaclass=ABCMeta):
    """コマンド：基底クラス"""

    def __init__(self, name, description, func):
        # 基底クラスの初期化
        self.name = name
        self.description = description
        self.func = func
        # 初期化完了ログを出力する
        # （コマンドサブクラスがインスタンス化されるたびに出力される）
        log("[info] command:", self.name, "-", self.description)

    @abstractmethod
    def run(self):
        """コマンドの実行内容を実装する"""
        msg = "Not implemented: run()\n"
        msg += "command: " + self.name + "-" + self.description
        return msg


class DiceCommand(Command):
    """ダイスコマンド：サブクラス"""

    def __init__(self, message):
        # ここで基底クラスを初期化する
        super().__init__("Dice", "Dice rolling", self.run)
        # 受け取ったメッセージを保存する
        self.message = message
        # これでクラスの初期化、終わり（インスタンス化された）

    def run(self):
        # def run(self):
        """実行メソット"""
        try:
            mc = self.message.content
            an = self.message.author.name
            ndn = mc.split(" ")[1]
            result = roll_dice(ndn)
            msg = f"```\n{an} rolled {ndn} = {result} = {sum(result)}\n```"
            return msg
        except Exception as e:
            log("[error]", e)
            return f"{an} ... invalid dice roll: {ndn}"


# -------------------------------------
# グローバル変数定義域
# -------------------------------------
"""
グローバル変数は、関数内部でも参照できる。定義された値も変更できる。
Python は予約語以外、すべて変数として扱われる。
変数名はすべて小文字と '_' で構成するのが理想。
オブジェクト類は、大文字を含めて構成しても良い。

変数名 = ... 変数
"""

boot_startup_time = get_current_time()  # ブート時間

intents = discord.Intents.default()  # Discord.py のインテントを設定
intents.messages = True  # メッセージ情報を取得する
# その他のインテントを設定する場合は、以下のように設定する
# intents.members = True  # メンバー情報を取得する
# intents.guilds = True  # グループ情報を取得する
# intents.channels = True  # チャンネル情報を取得する
client = discord.Client(intents=intents)  # Discord.py のインスタンスを生成

# -------------------------------------
# イベント駆動処理定義域
# -------------------------------------
"""
イベント駆動処理は、イベントが発火したときに行う。
※この定義は client.run() を実行する前に行ってください！
  さらに discord.Client() インスタンスの生成後に行ってください。
（client.run() 以降の処理は bot が停止してから実行されるため）
要するに…
client = discord.Client()  # Discord.py のインスタンスを生成
...
@client.event
async def on_ready():
    log('ログインしました。')
    log('名前:', client.user.name)
    log('ID:', client.user.id)
    log('Discord.pyバージョン:', discord.__version__)
    log('現在時刻:', get_current_time())
...
client.run(DISCORD_BOT_TOKEN)  # Discord bot token を渡して実行
"""


@client.event
async def on_ready():
    """
    ボットが起動した時に呼び出される
    """
    log("[info] Catch 'on_ready' event")
    log("[info] Bot is ready! Discord BOT activated! Standby for next events...")
    log()
    log("[debug] ====== Bot Information ====== begin")
    log("[debug] bot_name:", bot.client.user.name)
    log("[debug] bot_id:", bot.client.user.id)
    log("[debug] bot_discriminator:", bot.client.user.discriminator)
    log("[debug] bot_avatar:", bot.client.user.avatar_url)
    log("[debug] bot_avatar_id:", bot.client.user.avatar)
    log("[debug] bot_avatar_url:", bot.client.user.avatar_url)
    log("[debug] bot_guilds:", bot.client.guilds)
    log("[debug] bot_private_channels:", bot.client.private_channels)
    log("[debug] bot_emojis:", bot.client.emojis)
    log("[debug] bot_activity:", bot.client.activity)
    log("[debug] bot_user:", bot.client.user)
    log("[debug] ====== Bot Information ====== end")
    log()
    log("[info] Bot startup time:", boot_startup_time)
    log("[info] Bot stop command is [Ctrl + C]")
    log()


@client.event
async def on_message(message):
    """
    メッセージが送信された時に呼び出される
    """
    log("[info] Catch 'on_message' event")
    log("[debug] ====== Message Information ====== begin")
    log("[debug] message:", message)
    log("[debug] message.author:", message.author)
    log("[debug] message.author.name:", message.author.name)
    log("[debug] message.author.id:", message.author.id)
    log("[debug] message.author.discriminator:", message.author.discriminator)
    log("[debug] message.author.avatar_url:", message.author.avatar_url)
    log("[debug] message.author.avatar_id:", message.author.avatar)
    log("[debug] message.author.avatar_url:", message.author.avatar_url)
    log("[debug] message.channel:", message.channel)
    log("[debug] ====== Message Information ====== end")

    if message.author.bot:
        # ボットのメッセージは無視する
        return

    mc = message.content
    log("[debug] message.content:", mc)

    if mc.startswith(CMD_PREFIX):  # コマンドが送信された場合
        if mc.startswith("!hello"):
            await message.channel.send("Hello!")
            log("[info] Send 'Hello!' message")
        elif mc.startswith("!ping"):
            late = client.latency
            ping = round(late * 1000)
            await message.channel.send("🏓Pong! Latency: {} ms".format(ping))
            log("[info] Send 'Pong!' message")
        elif mc.startswith("!time"):
            await message.channel.send(get_current_time())
            log("[info] Send current time")
        elif mc.startswith("!dice2"):
            msg = DiceCommand(message).run()
            await message.channel.send(msg)
            log("[info] Send dice2 message")
        elif mc.startswith("!dice"):
            params = mc.split(" ")
            try:
                if len(params) == 2:
                    ndn = params[1]
                    result = roll_dice(ndn)
                    if result == []:
                        raise ValueError("Invalid dice number")
                    await message.channel.send("Dice result: " + str(result))
                    log("[info] Send dice result")
                else:
                    raise ValueError("Invalid dice number")
            except ValueError:
                await message.channel.send("Usage: !dice <num>d<face>")
                log("[info] Send 'Usage: !dice <min>d<max>' message")

        elif mc.startswith("!help"):
            help_msg = """
            Command list:
            > !help  : Show this help message
            > !hello : Say hello
            > !ping  : Ping pong
            > !time  : Show current time
            > !dice <num>d<face> (ex. !dice 2d6) (num = 1-9, face = 2-100)
            > !dice2 Implemented in CommandClass. (Params are the same as for !dice)
            >        : Roll dice command
            > !debug : Toggle debug mode (see console log)
            > !!stop : Stop bot
            """
            await message.channel.send(help_msg)
            log("[info] Send help message")
        elif mc.startswith("!debug"):
            global DEBUG_MODE
            DEBUG_MODE = not DEBUG_MODE
            if DEBUG_MODE:
                await message.channel.send("Debug mode is enabled.")
            else:
                await message.channel.send("Debug mode is disabled.")
        elif mc.startswith("!!"):
            if mc.startswith("!!stop"):
                await message.channel.send("Bot Stopping...")
                log("[info] Stopping...")
                wait(5)
                await client.close()  # Discordサーバーとの接続を切断する
                bot.stop()  # Botを停止させる
                log("[info] Stopped.")
            else:
                await message.channel.send("Unknown command.")
                log("[info] Unknown command.")
        else:
            await message.channel.send("Unknown command!: " + mc)
            log("[info] Send unknown command message")


# -------------------------------------
# メイン処理
# -------------------------------------
"""
メイン処理は、ここから始まる。
Python では `if __name__ == '__main__':` という書き方をしている。
これは、このファイルが直接実行された場合にのみ、以下の処理を実行する。
このファイルが import された場合には、以下の処理は実行されない。
"""

if __name__ == "__main__":
    # ---------------------------------
    # main 処理域
    # ---------------------------------
    """
    main 関数（じゃないけど）は、
    プログラムのエントリーポイントとなる。
    """

    # -- 初期化 ------------------------
    """
    初期化処理は、プログラムの最初に行う。
    """
    bot = Bot(client)  # Bot クラスのインスタンスを生成

    # -- メイン処理 --------------------
    """
    メイン処理は、プログラムの中で最も多くのコードを書く。
    """
    log("startup_time:", boot_startup_time)
    # Bot クラスの run() メソッドを実行する
    # 中で client.run() が実行されている
    print_test()
    bot.run()
    # ↓これ以下は bot が停止(Ctrl+C)するまで実行されない！
    # test
    print_test()

    # -- プログラム終了処理 -------------
    """
    プログラム終了処理は、プログラムの最後に行う。
    """
    log("[info] Program end time:", get_current_time())
