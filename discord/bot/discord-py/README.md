# Python 用 Discord Bot テンプレート

discord.py を使ったワンファイル Bot プログラムです。

## Header Comment

```python
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
```
