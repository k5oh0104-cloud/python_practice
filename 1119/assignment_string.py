#1
log = "WARNing"
print("log =", log.upper(),"\n")

sensors = "temp,pressure,vibration"
print("sensors =", " / ".join(sensors.split(",")[::-1]).upper(),"\n")

data = " EQP-01 , NORMAL , 85.5 "
print("data =", data.split(",")[1].lower(),"\n")

text = " ###[ PUMP-07 ]### "
print("text =", text.strip(" #[]").replace("-", "_").lower(),"\n")

data = " TEMP / Pressure | vibration "
print("data =", data.strip().replace("|","/").replace(" / ",",").lower(),"\n")