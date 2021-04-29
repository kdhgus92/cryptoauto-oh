import pyupbit as pu

access = "your-access"
secret = "your-secret"
upbit = pu.Upbit(access, secret)

print(upbit.get_balance("KRW-XRP"))     # KRW-XRP 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회회

test
