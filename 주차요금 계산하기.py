fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN",
           "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]

import math

def get_parking_minute(in_time, out_time):
    parking_time = datetime.strptime(out_time, '%H:%M') - datetime.strptime(in_time, '%H:%M')
    hour, minute, second = str(parking_time).split(':')
    minute = (60 * int(hour)) + int(minute)
    return minute


def get_parking_fee(fees, minute):
    if minute < fees[0]: return int(fees[1])
    return int(fees[1] + math.ceil((minute - fees[0]) / fees[2]) * fees[3])


from datetime import datetime

in_car_dict = {}
parking_result = {}
for record in records:
    time, car_num, state = record.split()
    if state == "IN":
        in_car_dict[car_num] = time
    else:
        if car_num in parking_result:
            parking_result[car_num] += get_parking_minute(in_car_dict.pop(car_num), time)
        else:
            parking_result[car_num] = get_parking_minute(in_car_dict.pop(car_num), time)

for car_num, in_time in in_car_dict.items():
    if car_num in parking_result:
        parking_result[car_num] += get_parking_minute(in_time, '23:59')
    else:
        parking_result[car_num] = get_parking_minute(in_time, '23:59')

for car_num, minute in parking_result.items():
    parking_result[car_num] = get_parking_fee(fees, minute)

[i[1] for i in sorted(parking_result.items(), key=lambda x: x[0])]