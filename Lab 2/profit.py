def profit(dict):
    if dict == {}:
        raise Exception("Input is empty")
    inputs = ["sell_price", "cost_price", "inventory"]
    for i in inputs:
        if i not in dict:
            raise Exception("Value {0} not provided".format(i))
        else:
            if dict[i] < 0:
                raise Exception("Value {0} must be positive".format(i))
    sum = (dict["sell_price"] - dict["cost_price"]) * dict["inventory"]
    round = 0
    residue = sum % 1
    if residue >= .5:
        round = 1
    return sum - residue + round
