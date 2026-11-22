from abc import ABC,abstractmethod


class paymentProscessor(ABC):
  @abstractmethod
  def pay(self,amount):
      pass

class Card(paymentProscessor):
  def pay(self,amount):
    self.amount=amount
    print("pay by using card  this amount :",amount)
    
class Upi(paymentProscessor):
  def pay(self,amount):
    self.amount=amount
    print("pay by using upi this amount : ",amount)
    
class paypal(paymentProscessor):
  def pay(self,amount):
    self.amount=amount
    print("pay by using paypal this amount : ",amount)
    
    
paybyCard=Card()
paybyUpi=Upi()
paybyPaypal=paypal()

paybyCard.pay(500)
paybyUpi.pay(490)
paybyPaypal.pay(590)