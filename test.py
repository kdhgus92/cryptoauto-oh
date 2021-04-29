import pyupbit as pu

access = "x2NIfC2tR4UMsCHVDfoTWXqmrFdZsvuB3qf7BDph"          # 본인 값으로 변경
secret = "MUxHvWzJDqhCFX9zyo0L4urgaT2BV53YcuDNUnNr"          # 본인 값으로 변경
upbit = pu.Upbit(access, secret)

print(upbit.get_balance("KRW-XRP"))     # KRW-XRP 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회회

