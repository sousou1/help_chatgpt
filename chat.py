import openai
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-fee", help="Show the usage fee", action="store_true")
parser.add_argument("-multiline", help="Accepts multiple lines of input", action="store_true")
args = parser.parse_args()
openai.api_key = os.environ.get('OPENAI_API_KEY')

system_settings = """あなたはシステムエンジニアです。私が質問をするので、日本語で回答してください。"""

def chat(new_message_text, past_messages, fee):
    new_message = {"role": "user", "content": new_message_text}
    past_messages.append(new_message)

    result = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=past_messages
    )
    response_message = {"role": "assistant", "content": result.choices[0].message.content}
    past_messages.append(response_message)
    response_message_text = result.choices[0].message.content
    print("BOT : " + response_message_text)
    total_fee = fee + result.usage.total_tokens / 1000 * 0.002 *  136
    if args.fee:
        print(str(total_fee) + "円 ( トータル )")
    return total_fee
    
def main():
    total_fee = 0
    system = {"role": "system", "content": system_settings}
    past_messages = [system]
    if not args.multiline :
        print("入力が終わったら、enterを押してください。")
    while True:
        try:
            if args.multiline :
                print("---入力受付中 入力が終わったらendを入力してください---")
                user_input = ""
                # 標準入力から入力を受け取る
                while True:
                    line = input()
                    if line == "end":
                        break
                    else:
                        user_input += line
            else :
                print("-----入力受付中-----")
                user_input = input()
            # 入力を処理する
            print("---------通信中----------")
            total_fee = chat(user_input, past_messages, total_fee)

        except EOFError:
            break  # 入力が終了したらループを抜ける

if __name__ == "__main__":
    main()