### 環境
Ubuntuのpython3環境想定です。

### 準備
1. openaiのサイトに登録し、クレジットカードも登録。ただし、最初の18＄は無料。https://platform.openai.com/
1. https://platform.openai.com/account/api-keys から、api-keysを取得する。
1. API keyを設定。環境変数に追加する場合は扱いに注意。
```
$ export OPENAI_API_KEY="hogehoge"
```

### 使い方

```
$ python3 chat.py
```
実行すると入力待ち状態になります。enterで返信が返ってきます。Ctrl + Dで終了します。

#### オプション
```
$ python3 -multiline
```
複数行入力可能です。入力が終わったら新たな行で"end"と入力してください。

引数に-fee を付けると利用料金(yen)を表示します。
```
$ python3 chat.py -fee

入力が終わったら、enterを押してください。
-----入力受付中-----
こんにちは
---------通信中----------
BOT : こんにちは、何か質問がありますか？
0.017136円
```

#### おまけ：alias登録
~/.bashrc などに登録しておくとすぐに呼び出せます。
```
export OPENAI_API_KEY=hogehoge
alias help_gpt="python3 ~/help_chatgpt/chat.py"
```

#### おまけ：利用料金について
以下の文章で0.25円程度です。
```
入力が終わったら、enterを押してください。
-----入力受付中-----
何か面白い漫才を1000文字程度で考えてください
---------通信中----------
BOT : 

漫才タイトル「キュウリと茄子」

ある日の夕飯で、夫婦がキュウリと茄子を食べていた。

夫「最近、キュウリと茄子ばっかり食べてる気がするんだよね」

妻「別に、ずっと同じものばっかり食べてるわけじゃないじゃない」

夫「でも、最近は特にそんな気がするんだ」

妻「何か問題でもあるの？」

夫「いや、あんまりバランスが悪い気がしてさ」

妻「そんなことないじゃん。茄子は野菜だし、キュウリは水分が多くて体にいいじゃん」

夫「でも、同じ味付けじゃないと飽きてくる気がするんだよね」

妻「なら、次はキュウリの味噌汁を作ってみようか」

夫「キュウリの味噌汁って……」

妻「美味しいよ。私が子供の頃からよく食べてるし」

夫「じゃあ、次は茄子の茄子を作ってみようか」

妻「茄子の茄子って？」

夫「そう、茄子を茄子に詰めたやつ」

妻「ああ、それね。でも、それって茄子食べ過ぎじゃない？」

夫「そうかもしれないけど、せっかくの食材だから有効活用したいじゃないか」

妻「……そうだね」

夫「そういや、最近キュウリと茄子の夢ばっかり見てるんだよね」

妻「夢？何か心配なことでもあるの？」

夫「いや、なんか不思議な夢なんだよ。キュウリと茄子があちこち飛び回ってる夢」

妻「それ、やっぱり毎日食べ過ぎてるからじゃない？」

夫「かもしれないね。でも、あの夢って面白いんだよね」

妻「そう？どんな感じ？」

夫「なんか、キュウリが突然現れて、茄子に振り回されたりするんだよ」

妻「それって……」

夫「はい、そうです。『キュウリと茄子』でした！」

妻「あの夢、もしかして漫才のネタになるかも」

夫「そうだね！やってみようか！」

二人は「キュウリと茄子」をネタにして、コントを始めました。それは非常に面白く、満員の観客が大笑いしていました。こんな出来事があり、以降、二人は「キュウリと茄子」を家族として大切にしていくのでした。
0.25187200000000004円
```