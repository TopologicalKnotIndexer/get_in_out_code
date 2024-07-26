# 给定两个扭结的 PD_CODE
# 计算他们连通和的 PD_CODE

def __status_reverse(status: str):
    assert status in ["IN", "OUT"] and status is not None
    if status == "IN":
        return "OUT" # 获得出入状态的相反相态
    else:
        return "IN"

def __get_next(total_n:int, val_now:int) -> int:
    if val_now == total_n:
        return 1
    else:
        return val_now + 1

def get_in_out_code(pd_code:list) -> list:
    total_n = len(pd_code) * 2
    in_out_code = []
    for idx in range(len(pd_code)): # 第一个弧线一定是 IN,第三个弧线一定是 OUT
        in_out_code.append(["IN", None, "OUT", None])
        if pd_code[idx][1] == __get_next(total_n, pd_code[idx][3]):
            in_out_code[-1][1] = "OUT"
            in_out_code[-1][3] = "IN"
        else:
            in_out_code[-1][1] = "IN"
            in_out_code[-1][3] = "OUT"
    return in_out_code

if __name__ == "__main__":
    print(get_in_out_code([[4,1,5,2],[15,1,16,22],[10,4,11,3],[2,12,3,11],[9,16,10,17],[7,18,8,19],[17,8,18,9],[19,12,20,13],[5,15,6,14],[13,20,14,21],[21,6,22,7]]))