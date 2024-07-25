# 给定两个扭结的 PD_CODE
# 计算他们连通和的 PD_CODE

def __status_reverse(status: str):
    assert status in ["IN", "OUT"] and status is not None
    if status == "IN":
        return "OUT" # 获得出入状态的相反相态
    else:
        return "IN"

def get_in_out_code(pd_code:list) -> list:
    in_out_code = []
    for _ in pd_code: # 第一个弧线一定是 IN,第三个弧线一定是 OUT
        in_out_code.append(["IN", None, "OUT", None])
    in_out_status = {}
    for i in range(len(pd_code)):
        for j in range(4): # 考虑每一个弧线，是否做过入弧线，是否做过出弧线
            if in_out_code[i][j] is not None:
                in_out_status[pd_code[i][j]] = in_out_code[i][j]
    need_next_turn = True
    while need_next_turn:
        need_next_turn = False # 正常来说，一轮计算就能结束
        for i in range(len(pd_code)):
            for j in range(4):
                if in_out_code[i][j] is None:
                    if in_out_status.get(pd_code[i][j]) is not None:
                        in_out_code[i][j] = __status_reverse(in_out_status[pd_code[i][j]])
                    elif in_out_status.get(pd_code[i][(j+2) % 4]) is not None:
                        in_out_code[i][j] = __status_reverse(in_out_status[pd_code[i][(j + 2) % 4]])
                    else:
                        need_next_turn = True # 说明需要进行下一轮计算
    return in_out_code

if __name__ == "__main__":
    print(get_in_out_code([[1, 4, 2, 5], [3, 6, 4, 1], [5, 2, 6, 3]]))