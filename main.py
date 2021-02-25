import tkinter as tk
import random

def main():
    back_ground = tk.Tk()

    back_ground.geometry('480x360')
    back_ground.title("ドラフト くじ")

    label = tk.Label(text='名前を入力してください')
    label.pack()

    txtBox = tk.Entry(width=20)
    txtBox.pack()

    names = ["主将A", "主将B", "主将C", "主将D"]
    checks = [tk.BooleanVar() for _ in range(len(names))]
    for i, n in enumerate(names):
        # checks[i] = tk.BooleanVar()
        tk.Checkbutton(back_ground,
                       variable=checks[i],
                       text=n
                       ).pack(anchor=tk.W)

    # extracted_txt = tk.Label()
    # def extract_input(text: tk.Entry()):
    #     extracted_txt['text'] = text.get()

    result_txt = tk.Label()
    def select():
        checked_names = []
        for name, check in zip(names, checks):
            if check.get():
                # print(name + "チャックされました")
                checked_names.append(name)
            if not checked_names:
                output = "主将を1人以上選択してください"
            else:
                output = txtBox.get()+"さんは"+random.choice(checked_names)+"チームに決定しました！"
            result_txt['text'] = output

    butten = tk.Button(back_ground,
                       text="START!",
                       command=select
                       )
    butten.pack(anchor=tk.W)

    result_txt.pack()





    back_ground.mainloop()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
