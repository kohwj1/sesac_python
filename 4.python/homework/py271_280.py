import random

class Account:
    #272
    account_quantity = 0
    
    #271
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.bank = 'SC제일은행'
        self.account_no = f'{str(random.randint(1,999)).zfill(3)}-{str(random.randint(1,99)).zfill(2)}-{str(random.randint(1,999999)).zfill(6)}'
        self.deposit_count = 1
        Account.account_quantity += 1
        #279
        self.account_log = [{'transaction_type':'deposit','amount':balance}]

    #273
    @classmethod
    def get_account_num(cls):
        # print(cls.account_quantity)
        return cls.account_quantity
    
    #274
    def deposit(self, amount):
        if amount >= 1:
            self.balance += amount
            self.deposit_count += 1
            #279
            self.account_log.append({'transaction_type':'deposit','amount':amount})

            #277
            if self.deposit_count % 5 == 0:
                self.balance *= 1.01

    #275
    def withdraw(self, amount):
        if self.balance - amount >= 0:
            self.balance -= amount
            #279
            self.account_log.append({'transaction_type':'withdraw','amount':amount})
    
    #276
    def display_info(self):
        print(f'은행이름: {self.bank}')
        print(f'예금주: {self.name}')
        print(f'계좌번호: {self.account_no}')

        str_balance = str(self.balance)
        formatted_balance = ''
        front_remain = len(str_balance) % 3
        
        for i in range(front_remain, len(str_balance), 3):
            formatted_balance += f'{str_balance[i:i+3]},'

        if front_remain > 0:
            formatted_balance = f'{str_balance[0:front_remain]},' + formatted_balance

        print(f'잔고: {formatted_balance[:-1]}원')

    #280
    def deposit_history(self):
        deposit_list = [history for history in self.account_log if history['transaction_type'] == 'deposit']
        for log in deposit_list:
            print(log)
    
    #280
    def withdraw_history(self):
        withdraw_list = [history for history in self.account_log if history['transaction_type'] == 'withdraw']
        for log in withdraw_list:
            print(log)

#278
김민수 = Account('김민수',1374500)
이용주 = Account('이용주', 987650)
정재형 = Account('정재형', 123456780)

customer_list = []

customer_list.append(김민수)
customer_list.append(이용주)
customer_list.append(정재형)

#279
for customer in customer_list:
    if customer.balance >= 1000000:
        print(customer.display_info())

#280
이용주.deposit(27500)
이용주.deposit(129000)
이용주.withdraw(3000)
이용주.deposit(500000)
이용주.deposit(70000)

이용주.deposit_history()
이용주.withdraw_history()