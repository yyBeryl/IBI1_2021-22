class Chocolate():
    def __init__(self,total_money,single_price):
#take two needed parameters
        self.total_money=total_money
        self.single_price=single_price
    def cal(self):
        b=self.total_money//self.single_price#calculate how many chocolate bars can buy
        c=self.total_money%self.single_price#calculate how many money can be back
        print(self.total_money,"can buy",b,"bars of chocolate with",c,"back.")      
#example
money=Chocolate(100,7)
Chocolate.cal(money)
