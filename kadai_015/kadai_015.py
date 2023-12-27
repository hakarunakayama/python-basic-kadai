class Human:
  def __init__(self):
    self.name = ""
    self.age = ""

  def printinfo(self, name, age):
    print(f"私の名前は{name}で、今年で{age}歳です。")

# コンストラクタで引数にselfしか指定していないので、ここでは引数の値はいらない
human = Human()
# メソッド定義で引数にnameとageも指定しているので、ここで引数の値が必要
human.printinfo("中山意", "40")