/** discord-js-template-100.js
 *
 * Discord.js を使った bot サーバーを作るためのテンプレート
 *
 * @author Deskuma <e-mail address> <github account> <twitter account> <discord account> など # 作者名
 * @version 1.0.0a # バージョン
 * @license MIT # ライセンス
 * @see URL # 参考URL
 * @see https://guide.discordjs-japan.org/
 * @date 2022-05-09 # 作成日
 * @update 2022-05-09 # 更新日
 *
 * @usage # 使い方
 * 準備:
 * 1. ファイル名を discord-<ボット名>-bot.js に変更する
 * 2. 作者名を変更する
 * 3. バージョンを変更する
 * 4. ライセンスを変更する
 * 5. 参考URLを変更する
 * 6. 作成日を変更する
 * 7. 更新日を変更する
 * 8. 使い方を変更する
 * 9. ファイルを保存する
 * 実行:
 * ```sh
 * DISCORD_BOT_TOKEN='bot token' node discord-<ボット名>-bot.js
 * ```
 * @note # メモ
 * ※このプログラムコードおよびコメントも含め大半は GitHub AI ペアプログラミング
 * copilot によって書かれいています。そのため、予期せぬコードが書かれている可能性も
 * あります。厳密なチェックは行っていません。コードを実行する前に、自分で確認してください。
 * （って、copilot が言っています！この上記文章の一部も AI が自動で書いてくれましたｗ）
 *
 * 変更履歴
 * version 1.0.0a コメント修正
 * version 1.0.0 初版
 */

// ------------------------------------
// const 定数定義域
/* ------------------------------------
定数は、定義された値を変更できない。
定数文字列や数値はすべて大文字で構成するのが定番。
オブジェクト類は、小文字で構成しても良い。
必要なライブラリの読み込み require() もここで定義する。

const ... ライブラリ各種の読み込み定義
*/
// -- 定数 ----------------------------
const DISCORD_BOT_TOKEN = process.env.DISCORD_BOT_TOKEN; // bot token 環境変数から読み込んでいる
const CMD_PREFIX = "!"; // コマンドのプレフィックス

// BOT 管理者情報
const BOT_ADMIN_DISCORD_ID = "<user_id>"; // user id 管理者 ID 番号 (数字18桁 開発者モードにして Copy ID で取得)
// ↑↓ どちらかを設定すれば良い（はず）数字だけど比較は文字列です
const ADMIN_USERNAME = "<username>"; // username 管理者名 (プロフィールで表示される名前)
const ADMIN_DISCRIMINATOR = "0000"; // discriminator 識別番号 (名前のあとの#数字4桁)

// -- オブジェクト ---------------------
// Discord.js オブジェクト
// const Discord = require("discord.js");
// const Intents = require("discord.js/src/extensions/Intents");
// ↓だと、思って読めばいい…。
const { Client, Intents } = require("discord.js"); // discord.js ライブラリ読み込み

// discord.js から client を作成
const client = new Client({ // TODO:2022-05-20 定数名とクラス名が大文字小文字の差しかないので混乱する可能性！
  // intents は、Discord.js が受け取るイベントを指定する
  // イベントが届かなかったら Discord 側の BOT パーミッションの設定を確認してください
  intents: [Intents.FLAGS.GUILDS, Intents.FLAGS.GUILD_MESSAGES],
});

// ------------------------------------
// var 変数定義域
/* ------------------------------------
変数は、定義された値を変更できる。

var ... 変数定義
*/
var boot_startup_time = new Date(); // ブート開始時間

// ------------------------------------
// function 関数定義域
/* ------------------------------------
関数は、共通で使う処理などを定義する。

関数定義:
function 関数名(引数) {
  処理
  return 戻り値
} 
*/

/**
 * wait 関数
 * @description 指定した時間待つ
 * @param {number} ms ミリ秒
 * @returns {Promise} Promiseオブジェクト
 * @example
 * async ... {
 *  await wait(1000); // 1秒待つ
 * }
 * @see {@link https://developer.mozilla.org/ja/docs/Web/JavaScript/Reference/Global_Objects/Promise}
 */
function wait(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

/**
 * zeroPadding 関数
 * @description 値を指定した桁数になるように0を追加する
 * @param {string} num 数字文字列
 * @param {number} length 長さ
 * @returns {string} ゼロ埋めされた文字列
 * @example
 * zeroPadding("1", 4); // "0001"
 */
function zeroPadding(num, length) {
  return (Array(length).join("0") + num).slice(-length);
}

/**
 * getDateTimeString 関数
 * @description 現在時刻の文字列を返す
 * @returns {string} 現在時刻文字列
 */
function getDateTimeString() {
  // ----------------------------------
  // let 局所変数定義域
  /* ----------------------------------
  局所変数は、関数内でのみ有効である。
  var を使って宣言すると、関数外でも有効になってしまいます。
  そのような変数は、予め ver 定義域で定義しておくと良いでしょう。

  let ... 局所変数定義
  */
  let date = new Date();
  let hour = date.getHours();
  let min = date.getMinutes();
  let sec = date.getSeconds();
  let year = date.getFullYear();
  let mon = date.getMonth() + 1;
  let day = date.getDate();
  let week = date.getDay();
  let week_day = ["日", "月", "火", "水", "木", "金", "土"];
  return (
    zeroPadding(hour, 2) +
    ":" +
    zeroPadding(min, 2) +
    ":" +
    zeroPadding(sec, 2) +
    " " +
    zeroPadding(year, 4) +
    "-" +
    zeroPadding(mon, 2) +
    "-" +
    zeroPadding(day, 2) +
    "(" +
    week_day[week] +
    ")"
  );
}

/**
 * diffDateString 関数
 * @description 日付1と日付2の差分を表す文字列を返す
 * return = date2 - date1
 * @param {Date} date1 日付1
 * @param {Date} date2 日付2
 * @returns {string} 差分時間文字列
 * @example
 * diffDateString(new Date(), new Date()); // "0日0時0分0秒"
 * diffDateString(new Date("2020-01-01"), new Date("2020-01-02")); // "1日0時0分0秒"
 */
function diffDateString(date1, date2) {
  let now = date2;
  let diff = now.getTime() - date1.getTime();
  let diff_sec = Math.floor(diff / 1000);
  let diff_min = Math.floor(diff_sec / 60);
  let diff_hour = Math.floor(diff_min / 60);
  let diff_day = Math.floor(diff_hour / 24);
  let diff_week = Math.floor(diff_day / 7);
  let diff_month = Math.floor(diff_day / 30);
  let diff_year = Math.floor(diff_day / 365);
  let diff_str = "";
  if (diff_year > 0) {
    diff_str = `${diff_year}年`;
  } else if (diff_month > 0) {
    diff_str = `${diff_month}ヶ月`;
  } else if (diff_week > 0) {
    diff_str = `${diff_week}週間`;
  } else if (diff_day > 0) {
    diff_str = `${diff_day}日`;
  } else if (diff_hour > 0) {
    diff_str = `${diff_hour}時間`;
  } else if (diff_min > 0) {
    diff_str = `${diff_min}分`;
  } else if (diff_sec > 0) {
    diff_str = `${diff_sec}秒`;
  }
  return diff_str;
}

/**
 * サイコロプログラム
 * @description サイコロを振る
 * @param {Discord.Message} msg Discordメッセージ
 * @param {number} num 振るサイコロの数 1~5
 * @returns {number} サイコロの目の合計
 * @example
 * dice(1); // 1〜6のランダムな数字
 * dice(2); // 1〜12のランダムな数字
 * dice(3); // 1〜18のランダムな数字
 * dice(4); // 1〜24のランダムな数字
 * dice(5); // 1〜30のランダムな数字
 */
async function dice(msg, num) {
  const dice_faces = ["⚀", "⚁", "⚂", "⚃", "⚄", "⚅"];
  const dice_faces_num = 6;
  const dice_min = 1;
  const dice_max = 5;

  if (num < dice_min) {
    num = 1;
  } else if (num > dice_max) {
    num = 5;
    msg.channel.send(`[BOT] ごめんなさい。サイコロの数は ${num} 個まで。`);
  }

  let sum = 0;
  for (let i = 0; i < num; i++) {
    let dice_num = Math.floor(Math.random() * dice_faces_num) + 1;
    sum += dice_num;
    msg.channel.send(
      `[BOT] 🎲 ${i + 1} 回目 ${dice_num} ${dice_faces[dice_num - 1]} です。`
    );
    await wait(1000); // 1秒待つ
  }
  msg.channel.send(`[BOT] サイコロ🎲の目の合計は「**${sum}**」です。`);

  return sum;
}

// ------------------------------------
// client.on() ... イベント処理定義域
/* ------------------------------------
ここからは、Discord.js が受け取るイベント処理を記述する

メッセージが新規に入力された時に呼ばれる
client.on("messageCreate", (message) => { ... }

他にも Discord の変化 event に応じたいくつかのイベントで呼ばれる
これをイベント駆動型（event driven）といい、「イベントを発生させて、それに対して処理を行う」というものである
client.on("<event>", (message) => { ... }

event は、以下のようなものがある
@see {@link https://github.com/discordjs/discord.js/blob/main/packages/discord.js/src/util/Events.js}
*/

// ここは bot がログインを完了した時に呼ばれている（１回だけ）
client.once("ready", async (cl) => {
  console.log("[info] Ready, Discord BOT activated! Standby for events...");
  let date_time_str = getDateTimeString();
  console.log(`[info] boot start at: ${date_time_str}`);
  boot_startup_time = new Date();
  console.log(`[debug] ${cl}`); // Discord.Client object
});

// ここは bot が新しいメッセージが入力された時に呼ばれている
client.on("messageCreate", async (msg) => {
  // ----------------------------------
  // 初期準備
  if (msg.author.bot) return; // bot の発言は無視
  if (msg.content.startsWith(CMD_PREFIX)) {
    // コマンドが入力された場合
    const args = msg.content.slice(CMD_PREFIX.length).split(/ +/);
    const command = args.shift().toLowerCase();

    // ----------------------------------
    // コマンド実行域
    /* ----------------------------------
    ここからは、各コマンドに対応した処理を実行する
    */
    // ----------------------------------
    // bot の応答速度を調べる
    if (command === "ping") {
      const m = await msg.channel.send("[BOT] 🏓Pong!");
      await wait(1000);
      m.edit(
        `[BOT] 🏓Pong! Latency is ${
          m.createdTimestamp - msg.createdTimestamp
        }ms. API Latency is ${Math.round(client.ping)}ms`
      );
      // ----------------------------------
      // サイコロを振る
    } else if (command === "dice") {
      const num = args[0] ? parseInt(args[0]) : 1;
      dice(msg, num);
      // ----------------------------------
      // bot の稼働時間を返す
    } else if (command === "uptime") {
      let diff_str = diffDateString(boot_startup_time, new Date());
      msg.channel.send(`[BOT] 私は、起動してから ${diff_str} 経過しています。`);
      // ----------------------------------
      // bot を終了する ※ このコマンドは、管理者専用コマンドとすべきである
    } else if (command === "shutdown") {
      if (
        // 管理者のみ実行可能
        msg.author.id === BOT_ADMIN_DISCORD_ID ||
        (msg.author.username === ADMIN_USERNAME &&
          msg.author.discriminator === ADMIN_DISCRIMINATOR)
      ) {
        msg.channel.send(`[BOT] 私をシャットダウンします…`);
        await wait(1000);
        msg.channel.send(`[BOT] またお会いしましょう！`);
        await wait(5000);
        client.destroy();
      } else {
        msg.channel.send(`[BOT] ごめんなさい、管理者のみが使用できます。`);
      }
      // ----------------------------------
      // bot の機能を教えてもらう
    } else if (command === "help") {
      msg.channel.send(`[BOT] 私は、以下のコマンドを持っています。
\`\`\`
${CMD_PREFIX}ping       - bot の応答速度を調べる
${CMD_PREFIX}dice [num] - サイコロを振る
${CMD_PREFIX}uptime     - bot の稼働時間を返す
${CMD_PREFIX}shutdown   - bot を終了する
\`\`\``);
      // ----------------------------------
      // 未知のコマンドを受け取った場合
    } else {
      msg.channel.send(`[BOT] 私は、コマンドを理解できませんでした。`);
    }
  } else {
    // コマンド以外の場合
    // ----------------------------------
    // いまは何もしない
    /* ----------------------------------
     * 将来、会話を AI が聞くようになったら会話を聞かせて学習させる
     * 対応する返答がない場合は、「ごめんなさい」と返す（←と、AI が自ら定義した）
     * すべての会話に対して、AI が反応したらうるさいので気まぐれに反応するようにする
     * これを「聞き取り」という（←と、AI が教えてくれた。へぇｗ）
     * たまに、AI から発言するようにする。しかし、それはここで処理する内容ではない
     * ここは、誰かが発言した時に呼ばれる。なので、ここでは何もしない。
     * ----------------------------------
     * ここでは、その他のメッセージを受け取った場合に、そのメッセージを返す
     * ↑と AI が言っているが「そのメッセージに対応する返答があれば返す」が、正しい。
     * 何度も復唱されてもうるさいだけなので、復唱はしない。
     * ----------------------------------
     * ただし、そのメッセージを音声合成データに変換してボイスチャットで再生するという
     * 機能ならば AI 的な反応でなくとも実用的なものである。ボイスチャットに参加できない
     * 聞き専テキストチャットユーザーには役立つ機能となるだろう。
     */
    // do nothing
  }
});

// ============================================================================

// ------------------------------------
// client.login() ... bot のログイン処理
/* ------------------------------------
bot を起動する準備ができたので、bot を起動します。

  client.login(TOKEN);
  TOKEN は、bot の起動に必要なトークンです。

  ここがメイン処理の入口となるイメージです。
*/
try {
  // BOT TOKEN の確認
  if (DISCORD_BOT_TOKEN == undefined) {
    console.log("The environment variable DISCORD_BOT_TOKEN is not set.");
    process.exit(0);
  }
  // bot をログインさせる
  client.login(DISCORD_BOT_TOKEN);
  console.log("[info] BOT is running...");
  console.log("[info] Press Ctrl+C to exit.");
  console.log(`[info] or type '${CMD_PREFIX}shutdown' to exit.`);
  console.log("[info] wait...");
} catch (e) {
  // エラー処理
  console.log(e);
}
