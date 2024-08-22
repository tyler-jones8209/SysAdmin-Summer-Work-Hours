def total_hours():
    with open("hours.txt", "r") as file:
        list_hours = [float(line.split(":")[1].strip()) for line in file]

    count = len(list_hours)
    worked_hours = round(sum(list_hours), 2)
    allowed_hours = 20 * count
    hours_remaining = round(allowed_hours - worked_hours, 2)

    print(f"Sys Admin Stats Over {count} Weeks:\n")
    print(f"Total Hours Worked: {worked_hours}")
    print(f"Extra Hours Remaining: {hours_remaining}")

total_hours()
