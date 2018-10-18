#!/usr/bin/python
# encoding=utf-8

from datetime import datetime
import calendar
import datetime as dt


#获取月份的最后一天
def getFirstDay_LastDay(year=None, month=None):
    """
    :param year: 年份，默认是本年，可传int或str类型
    :param month: 月份，默认是本月，可传int或str类型
    :return: firstDay: 当月的第一天，datetime.date类型
              lastDay: 当月的最后一天，datetime.date类型
    """
    if year:
        year = int(year)
    else:
        year = datetime.date(datetime.today()).year

    if month:
        month = int(month)
    else:
        month = datetime.date(datetime.today()).month

    # 获取当月第一天的星期和当月的总天数
    firstDayWeekDay, monthRange = calendar.monthrange(year, month)


    # 获取当月的第一天
    firstDay = dt.date(year=year, month=month, day=1)
    lastDay = dt.date(year=year, month=month, day=monthRange)

    return lastDay


#判断是否是闰年
def isYear(year):
	if (year%4 == 0) & (year%100 != 0):
	    return 'yes'
	elif year%400 == 0:
		return 'yes'
	else:
		return 'no'
