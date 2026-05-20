count_employee = int(input("Nhập số lượng nhân viên: "))

isContinue = True
while count_employee > 0 and isContinue:

    while True:
        input_name = input("Nhập vào tên: ").strip()
        if input_name != "":
            break
        print("yêu cầu nhập lại")
    while True:
        input_workday = input("Nhập vào số ngày đi làm: ").strip()
        if input_workday != "":
            workday = int(input_workday)
            if workday > 0:
                break
            else:
                print("Ngày đi làm phải lớn hơn 0")
        else:
            print("Không được để trống ngày làm việc")
        print(f"Yêu cầu nhập lại {input_workday}")

    print("Thông tin nhân viên")
    print(f"Tên: {input_name}")
    print(f"Số ngày đi làm: {workday}")

    if workday < 20:
        print("Cần cải thiện chuyên cần")
    else:
        print("Nhân viên chuyên cần tốt")

    confirm = input("Tiếp tục chương trình?(y/n): ").strip()
    isContinue = True if confirm == "y" else False
