class Category:
  def __init__(self, category):
    self._ = category
    self.ledger = []
    self.balance = 0

  def check_funds(self, amount):
    if self.balance - amount < 0:
      return False
    return True

  def deposit(self, amount, description):
    if description == None:
      description = ""
    self.balance += amount
    self.ledger.append(dict([("amount",amount), ("description", description)]))

  def withdraw(self, amount, description):
    negAmount = -amount
    if self.check_funds(amount):
      self.ledger.append(negAmount)
      self.balance -= amount
      return True
    else:
      return False
      

  def get_balance(self):
    return self.balance
  
  def transfer(self, amount,  category):
    #this is for the sentences
    withdrawSentence = "Transfer to "+ str(category)
    depositSentence = "Transfer from "+ str(category)
    if self.check_funds(amount):
      self.withdraw(amount, withdrawSentence)
      self.deposit(amount, depositSentence)
      self.balance -= amount
      return True
    else:
      return False


def create_spend_chart(list):
  return "******"
