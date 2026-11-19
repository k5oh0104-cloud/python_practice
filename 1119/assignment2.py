#1
log = "2026/11/19 23:58:45 | DELAY=135s | EQP-09"
info = log.strip().split(" | ")
start = info[0]
delay = int(info[1].replace("DELAY=", "").replace("s", ""))
eqp = info[2]
start_date = start.split(" ")[0]
start_time = start.split(" ")[1]

year = start_date.split("/")[0]
month = start_date.split("/")[1]
day = int(start_date.split("/")[2])

hour = start_time.split(":")[0]
min = start_time.split(":")[1]
sec = start_time.split(":")[2]

d_min = delay//60
d_sec = delay%60

end_hr = int(hour)
end_min = int(min) + d_min
end_sec = int(sec) + d_sec

if end_sec >= 60:
    end_sec -= 60
    end_min += 1 

if end_min >= 60:
    end_min -= 60
    end_hr += 1

if end_hr >= 24:
    end_hr -= 24
    day += 1 

end_year = year
end_month = month
end_day = day

list = (":").join([str(end_hr), str(end_min), str(end_sec)])
list1 = ("/").join([str(end_year), str(end_month), str(end_day)])
print("==== 설비 작업 정보 ====")
print(f'설비 코드:{eqp}')
print(f'작업 날짜: {start_date}')
print(f'작업 시작 시간: {hour}시 {min}분 {sec}초')
print(f'소요 시간: {delay}초',"\n")

print("완료 시간", list1, list)
print(f'날짜 변경 여부: {list1 != start_date}')
