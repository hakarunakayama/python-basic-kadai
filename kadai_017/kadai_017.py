class Human:
  # インスタンス生成するときに名前も年齢も指定するので、引数はここで設定する
  def __init__(self, name, age):
    self.name = name
    self.age = age

  # メソッドの引数としては、名前と年齢が指定済みのインスタンス自体を設定する
  def check_adult(self):
    if self.age >= 20:
      print(f"{self.name}さんはもう{self.age}歳なので大人です。")
    else:
      print(f"{self.name}さんはまだ{self.age}歳なので子供です。")

Taro = Human("Taro", 40)
Jiro = Human("Jiro", 20)
Saburo = Human("Saburo", 15)
Human_info = [Taro, Jiro, Saburo]

for i in range(0, len(Human_info)):
  Human_info[i].check_adult()