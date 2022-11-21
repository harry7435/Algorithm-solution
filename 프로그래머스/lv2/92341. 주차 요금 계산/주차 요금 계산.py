# 입차, 출차 시간으로 주차 시간 계산 함수
def cal_time(in_hours, in_minutes, out_hours, out_minutes):
    total = 60 * (out_hours - in_hours) + (out_minutes - in_minutes)
    return total
# 주차 시간으로 주차 요금 계산 함수
def cal_fee(times, basic_time, basic_fee, over_time, over_fee):
    if times < basic_time:
        return basic_fee
    else:
        if (times - basic_time) % over_time == 0:
            return basic_fee + ((times - basic_time) // over_time) * over_fee
        else: return basic_fee + ((times - basic_time) // over_time + 1) * over_fee
    
def solution(fees, records):
    answer = []
    total_fee = []
    basic_time, basic_fee, over_time, over_fee = fees
    time_check = {}
    in_car = {}
    # 입차와 출차 시간 체크해 주차 시간 계산
    for record in records:
        record = record.split(" ")
        times = record[0]
        car_num = record[1]
        if record[2] == 'IN':
            in_car[car_num] = times
        else:
            total = cal_time(int(in_car[car_num][:2]),
                             int(in_car[car_num][3:]),
                             int(times[:2]),
                             int(times[3:]))
            if car_num in time_check:
                time_check[car_num] += total
            else:
                time_check[car_num] = total
            del in_car[car_num]
    
    for car_num in in_car:
        total = cal_time(int(in_car[car_num][:2]),
                        int(in_car[car_num][3:]), 23, 59)
        if car_num in time_check:
            time_check[car_num] += total
        else:
            time_check[car_num] = total
    # 주차 시간으로 주차 요금 계산 후 차량 번호 기준 오름차순으로 정렬
    for car_num in time_check:
        total_fee.append([car_num, cal_fee(time_check[car_num], basic_time, basic_fee, over_time, over_fee)])
    total_fee.sort()
    
    for fee in total_fee:
        answer.append(fee[1])
    return answer