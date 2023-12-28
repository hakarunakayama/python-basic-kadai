class Human:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def printinfo(self):
    print(f"私の名前は{self.name}で、今年で{self.age}歳です。")

# コンストラクタで引数にselfしか指定していないので、ここでは引数の値はいらない
human = Human("中山意", "40")
# メソッド定義で引数にnameとageも指定しているので、ここで引数の値が必要
human.printinfo()
