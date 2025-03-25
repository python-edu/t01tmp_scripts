import sys


def read_data(path):
    with open(path) as f:
        data = f.read()
    data = data.split('\n')
    return data


def data2float(data):
    res = []
    for it in data:
        res.append(float(it))
    return res


def mean(data):
    res = sum(data) / len(data)
    return round(res, 2)


def stdd(data: list):
    res_mean = mean(data)
    sq = []
    for it in data:
        sq.append((it - res_mean)**2)
    std = sum(sq) / (len(data) - 1)
    return round(std, 2)
        
    
if __name__ == '__main__':
    path = sys.argv[1]

    data = read_data(path)
    data = data2float(data)

    res_mean = mean(data)
    res_std = stdd(data)

    print(f'mean: {res_mean}, standard dev: {res_std}')



