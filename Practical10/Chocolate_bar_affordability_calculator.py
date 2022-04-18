class Chocolate():
    def __init__(self,total_money,single_price):
        self.total_money=total_money
        self.single_price=single_price
    def cal(self):
        b=self.total_money//self.single_price
        c=self.total_money%self.single_price
        print(self.total_money,"can buy",b,"bars of chocolate with",c,"back.")      
money=Chocolate(100,7)
Chocolate.cal(money)
