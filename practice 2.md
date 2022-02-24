## practice 2 - 은행업무

```bash
홍길동 통장
-------------
1. 잔액확인
2. 입금
3. 출금
4. 종료
-------------
메뉴를 선택해 주세요 :
계좌 비밀번호를 입력해 주세요 :

1번선택 : 잔액은 ???원입니다.
2번선택 : 입금할 금액을 알려주세요 (ex 1000원)
		1000원 입금되었습니다. 잔액은 ???원입니다.
3번선택 : 출금할 금액을 알려주세요 (ex 500원)
		500원 출금되었습니다. 잔액은 ???원입니다.
4번선택 : 거래가 종료되었습니다.
```

```bash
[class명] - CAccount

[기능] 
1. 입금 : deposit()
2. 출금 : withdraw()
	
[변수]
owner
amount : 초기값 0

[유의사항]
만약 입출금액이 마이너스 값이면 - 정확한 금액을 입력하세요.
출금시 입력한 값이 잔액보다 많으면 - 잔액부족, 거래가 거절되었습니다 (종료)
```

```python
class CAccount:
    # 기본 설정 함수
    def __init__(self, owner, amount=0, password='1234'):
        self.owner = owner
        self.balance = amount
        self.password = password
        self.message = """
        ----------------------
        1. 잔액확인
        2. 입금
        3. 출금
        4. 종료
        ----------------------
        """
        self.dispTitleMsg()
```

```python
	# 메뉴 선택을 위한 함수
	def bankTransaction(self):
        inNum = int(input("메뉴를 선택해 주세요."))
        if inNum == 4:
            self.dispEndBanking()
            return

        inpass = input("계좌 비밀번호를 입력해 주세요.")
        if inpass != self.password:
            self.dispPassErr()
            return

        if inNum == 1:
            self.dispBalance()
        elif inNum == 2:
            self.deposit()
        elif inNum == 3:
            self.withdraw()
```

```python
	# 입금 함수	
    def deposit(self):
        inAmount = int(input("입금할 금액을 알려주세요."))
        if inAmount < 0:
            self.dispAmountErr()
        else:
            self.balance += inAmount
            self.dispDepositSucc(inAmount)
            self.dispBalance()
```

```python
	#출금 함수	
    def withdraw(self):
        inAmount = int(input("출금할 금액을 알려주세요."))
        if inAmount < 0:
            self.dispAmountErr()
        elif self.balance < inAmount:
            self.dispLackbalance()
        else:
            self.balance -= inAmount
            self.dispwithdrawSucc(inAmount)
            self.dispBalance()
```

```python
	# 디스플레이 메시지
	def dispTitleMsg(self):
        print("%s 통장" % self.owner)
        print(self.message)

    def dispBalance(self):
        print("잔액은 %d원 입니다." % self.balance)

    def dispAmountErr(self):
        print("정확한 금액을 입력해주세요.")

    def dispLackbalance(self):
        print("잔액부족, 거래가 거절되었습니다.")

    def dispDepositSucc(self, amount):
        print(amount, "원이 성공적으로 입금되었습니다.")

    def dispwithdrawSucc(self, amount):
        print(amount, "원이 성공적으로 인출되었습니다.")

    def dispPassErr(self):
        print("%s님은 거래할 수 없습니다." % self.owner)

    def dispEndBanking(self):
        print("은행 업무를 종료합니다.")
```

```python
# class가 실행되는지 확인
amounHong = CAccount("홍길동", 50000)
amounHong.bankTransaction()
```

+ 출력 결과

```bash
# 1을 선택한 후 비밀번호를 맞게 입력한 경우
홍길동 통장

        ---------------------
        1. 잔액확인
        2. 입금
        3. 출금
        4. 종료
        ---------------------
        
메뉴를 선택해 주세요.1
계좌 비밀번호를 입력해 주세요.1234
잔액은 50000원 입니다.

# 1을 선택한 후 비밀번호를 틀리게 입력한 경우
홍길동 통장

        ---------------------
        1. 잔액확인
        2. 입금
        3. 출금
        4. 종료
        ---------------------
        
메뉴를 선택해 주세요.1
계좌 비밀번호를 입력해 주세요.1111
홍길동님은 거래할 수 없습니다.
```

```bash
# 2를 선택한 후 입금 금액이 0원보다 많을 경우
홍길동 통장

        ---------------------
        1. 잔액확인
        2. 입금
        3. 출금
        4. 종료
        ---------------------
        
메뉴를 선택해 주세요.2
계좌 비밀번호를 입력해 주세요.1234
입금할 금액을 알려주세요.65000
65000 원이 성공적으로 입금되었습니다.
잔액은 115000원 입니다.

# 2를 선택한 후 입금 금액이 0원보다 적을 경우
홍길동 통장

        ---------------------
        1. 잔액확인
        2. 입금
        3. 출금
        4. 종료
        ---------------------
        
메뉴를 선택해 주세요.2
계좌 비밀번호를 입력해 주세요.1234
입금할 금액을 알려주세요.-1000
정확한 금액을 입력해주세요.
```

```bash
# 3을 선택한 후 출금 금액이 통장잔액보다 적을 경우
홍길동 통장

        ---------------------
        1. 잔액확인
        2. 입금
        3. 출금
        4. 종료
        ---------------------
        
메뉴를 선택해 주세요.3
계좌 비밀번호를 입력해 주세요.1234
출금할 금액을 알려주세요.20000
20000 원이 성공적으로 인출되었습니다.
잔액은 30000원 입니다.

# 3을 선택한 후 출금 금액이 통장잔액보다 많을 경우
홍길동 통장

        ---------------------
        1. 잔액확인
        2. 입금
        3. 출금
        4. 종료
        ---------------------
        
메뉴를 선택해 주세요.3
계좌 비밀번호를 입력해 주세요.1234
출금할 금액을 알려주세요.60000
잔액부족, 거래가 거절되었습니다.
```

```bash
# 4를 선택한 경우
홍길동 통장

        ---------------------
        1. 잔액확인
        2. 입금
        3. 출금
        4. 종료
        ---------------------
        
메뉴를 선택해 주세요.4
은행 업무를 종료합니다.
```



