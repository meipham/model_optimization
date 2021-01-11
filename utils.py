import sqldf

def course_code2id(code):
    """
    Chuyển Mã môn thành Id môn
    """

    q = 'select STT from df_Course where MaMon="%s"'%code
    return sqldf.run(q)


def get_courses(cl):
    """
    Lấy danh sách môn học của 1 lớp từ tkb
    """

    q = """
    select distinct MaMon
    from df_Schedule
    where ID_Lop = %s
    """%cl

    course_code = sqldf.run(q).MaMon
    return course_code

def get_tutors_by_course(c):
    """
    Lấy danh sách các giáo viên có thể dạy môn c
    """
    pass

def get_sessions_by_total(t):
    """
    Lấy danh sách tất cả các buổi dạy của giáo viên t
    """
    pass

import itertools


def get_session_from_week_range(start, end):
    """
    Danh sách tất cả các buổi học (session) từ tuần thứ start đến tuần thứ end
    """
    sess = list(itertools.product(weeks.index[start:end], days, shifts))
    return sess

def get_week_index(start, end, day):
    pass

def get_sessions_by_daterange(begin, end, timetable, day=None, shift=None):
    temp = timetable[(timetable.mon>=begin) & (timetable.sun<=end)]
    if day: temp = temp[(timetable.Day == day)]
    if shift: temp = temp[(timetable.Shift==shift)]
    return temp.index