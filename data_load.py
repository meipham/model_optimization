# Read data files

from os import path
import pandas as pd
from datetime import datetime
import itertools

def load_data(path):

    # Đọc dữ liệu thời khóa bieeur hiện hành
    df_Schedule = pd.read_excel(sheet_name="TKB", index_col=0, usecols=["ID_", "ID_Lop", "MaMon", "start", "end", "day", "beginning", "time", "MAGV"], io=path)

    # Đọc dữ liệu danh sách giảng viên và bộ môn tương ứng
    df_Tutor = pd.read_excel(sheet_name="GV", index_col=0, usecols=[u"STT", u"Mã giáo viên", u"Bộ môn", "Khoa", u"Họ Và Tên"], io=path)

    # Đọc dữ liệu danh sách các lớp
    df_Class = pd.read_excel(sheet_name="Lop", index_col=0, usecols=[u"STT", u"Mã lớp", u"Tên lớp"], io=path)

    # Đọc dữ liệu danh sách các môn học và bộ môn tương ứng
    df_Course = pd.read_excel(sheet_name="Mon", index_col=0, usecols=[u"STT", u"Mã môn", u"Tên môn", u"Bộ môn"], io=path)

    # Drop duplicates
    for df in [df_Schedule, df_Tutor, df_Class, df_Course]:
        df.drop_duplicates(inplace=True)
        df.reset_index(inplace=True)

    # Đổi tên cột
    df_Tutor.columns = ["STT", "TenGV", "MaGV", "BoMon", "Khoa"]
    df_Course.columns = ["STT", "TenMon", "MaMon", "BoMon"]
    df_Class.columns = ["STT", "MaLop", "TenLop"]

    # Dùng cột STT làm index cho cho các bảng
    df_Tutor.set_index("STT", inplace=True)
    df_Course.set_index("STT", inplace=True)
    df_Class.set_index("STT", inplace=True)


    # period_begin: Thời điểm bắt đầu năm học 
    # period_end: Thời điểm kết thúc học kỳ

    sem_begin, sem_end = datetime(2020, 8, 3), datetime(2021, 2, 14)

    suns = pd.date_range(start=sem_begin, end=sem_end, freq="W-SUN")
    mons = pd.date_range(start=sem_begin, end=sem_end, freq="W-MON")
    assert len(suns)==len(mons)
    weeks = pd.DataFrame({'mon':mons, 'sun': suns})
    days = [2, 3, 4, 5, 6]
    shifts = [1, 6] #1: buoi sang, 6: buoi chieu

    # Danh sách các buổi học trong toàn bộ học kỳ
    sem_sessions = list(itertools.product(weeks.index[0:28], days, shifts))
    df_TimeTable = pd.DataFrame(sem_sessions, columns=["WeekId", "Day", "Shift"]).merge(weeks, left_on="WeekId", right_on=weeks.index)




    return df_Schedule, df_Tutor, df_Class, df_Course, df_TimeTable