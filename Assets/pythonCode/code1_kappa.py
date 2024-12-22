##code1[float,float]
##可以讓學生試試看kappa
from sklearn.metrics import cohen_kappa_score
import numpy as np

# 定義函數 f(x) = x - c
def calculate_kappa(data, c):
    # 計算 x - c
    transformed_data = [x - c for x in data]

    # 將原始數據與變換後的數據作為兩個評分者的結果
    kappa = cohen_kappa_score(data, transformed_data)
    return kappa

# # 主程式
# if __name__ == "__main__":
#     # 使用者輸入數據與 c
#     try:
#         # data = float(input("please input value of x :").strip())

#         # c = float(input("please input constant c :").strip())
#         data, c = map(float, input("Please input value of x and constant c separated by a space: ").strip().split(','))
#         # 計算 Kappa
#         a = data-c
#         print(a)
#         kappa = data/a
#         print(f"Kappa for f(x) = x - {c}: {kappa}")
        
#     except ValueError:
#         print("error! make sure c and x are number。")

def kappa_main(inputString):
    try:
        data, c = map(float, inputString.strip().split(','))
        # 計算 Kappa
        a = data-c
        print(a)
        kappa = data/a
        print(f"Kappa for f(x) = x - {c}: {kappa}")
        output = f"{a}\nKappa for f(x) = x - {c}: {kappa}"
        return output
    except ValueError:
        print("error! make sure c and x are number。")
        return "error! make sure c and x are number。"