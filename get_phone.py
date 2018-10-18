from ti_config.bootstrap import init_ti_srv_cfg
from ti_daf.sql_context import SqlContext, session_scope, iselect_rows_by_sql
import pandas as pd
from datetime import datetime
import datetime as dt

from bi_business_reports.util.query import get_mobile_phone
from bi_business_reports.util.send_email import EmailSend


def get_noWithdraw_user():
    init_ti_srv_cfg('ti-daf')
    db = SqlContext('/python/db/ac_cif_db')

    today = datetime.date(datetime.today())

    time = today - dt.timedelta(days=1)
    time_s = "'" + str(time) + "'"

    sql = '''
          select a.personname,a.partyid,a.applydate,a.auditline,
           case when c.partyid is null then '新用户' else '老用户' end as cate
          from ac_lms_db.LoanApplyInfo a
          left join ac_cif_db.LoanAgreement b
          on a.applyno=b.applyid
          left join 
          (
            select distinct partyid from ac_cif_db.LoanAgreement 
            where loantime <'''+time_s+''' and loanstatus in ('D','O','R','E') and idproduct<>21
          ) c
          on a.partyid=c.partyid
          where b.id is  null and date_format(a.applydate, '%Y-%m-%d')=''' + time_s + ''' and a.status  like '%A%'
          and a.applytype<>'repayCredit'
            '''

    user_list = []
    with session_scope(db) as session:
        for row in iselect_rows_by_sql(session, sql, []):
            phone_name = get_mobile_phone(row['partyid'])

            row_list = list(row)
            row_list[1] =  phone_name
            user_list.append(row_list)

    user_df = pd.DataFrame(user_list, columns=['username', 'phone', 'applytime', 'auditline','usercate'])
    user_df = user_df.rename(columns={'username': '用户姓名', 'phone': '用户电话', 'applytime': '申请时间',
                                      'auditline': '审批额度','usercate':'用户类型'})

    return user_df


def get_noRenew_user():
    db = SqlContext('/python/db/dev_dw_db')

    today = datetime.date(datetime.today())

    time = today - dt.timedelta(days=2)
    time_s = "'" + str(time) + "'"


    sql='''
    select  c.corporaterepresentname name,a.partyid,a.repaytime ,d.loannum
    from
    (
        select   distinct a.partyid,b.repaytime  from dev_dw.f_loanagreement  a
        left join dev_dw.f_loanrepayschedule b
        on a.id=b.idloanagreement
        where loanstatus in ('D','O','R','E') and a.idproduct<>21
        and to_char(b.repaytime,'yyyy-mm-dd')='''+time_s+'''
        and b.repaytime-b.duedate<15
        and a.repaytime  is not null
    ) a
    left join dev_dw.f_loanapplyinfo b
    on a.partyid=b.partyid and b.applytype not in ('repayCredit') 
    and b.applydate>=to_date('''+time_s+'''，'yyyy-mm-dd')
    left join dev_dw.dim_txnparty c
    on a.partyid=c.partyid
    left join 
    (
        select  partyid,count(distinct id) loannum from dev_dw.f_loanagreement
        where loanstatus in ('D','O','R','E') and idproduct<>21
        group by partyid
    ) d
    on a.partyid=d.partyid
    where  b.partyid is null
    '''

    user_list = []
    with session_scope(db) as session:
        for row in iselect_rows_by_sql(session, sql, []):
            phone_name = get_mobile_phone(row['partyid'])

            row_list = list(row)
            row_list[1] =  phone_name
            user_list.append(row_list)

    user_df = pd.DataFrame(user_list, columns=['username', 'phone', 'repaytime','loannum'])
    user_df = user_df.rename(columns={'username': '用户姓名', 'phone': '用户电话', 'repaytime': '还款时间','loannum':'历史借款次数'})

    return user_df



def send_email_phone():

    today = datetime.date(datetime.today())
    time = today - dt.timedelta(days=1)

    noWithdrawUser_df = get_noWithdraw_user()
    noRenewUser_df=get_noRenew_user()

    excel_writer = pd.ExcelWriter('/data/excel/user_list.xlsx', engine='xlsxwriter')
    work_book = excel_writer.book
    format_1 = work_book.add_format({'align': 'center', 'font_name': '微软雅黑'})

    noWithdrawUser_df.to_excel(excel_writer, '未提现用户', index=False)
    noWithdrawUser_sheet = excel_writer.sheets['未提现用户']
    noWithdrawUser_sheet.set_column('A:H', 20, format_1)

    noRenewUser_df.to_excel(excel_writer, '未续借用户', index=False)
    noRenewUser_sheet = excel_writer.sheets['未续借用户']
    noRenewUser_sheet.set_column('A:H', 20, format_1)

    excel_writer.save()

    subject = str(time) + '未提现+未续借用户列表'
    to_addrs = ['diao.xie@andpay.me','qian.yuan@andpay.me','liping.peng@andpay.me','lulu.zhang@andpay.me','sha.wu@andpay.me','jing.che@andpay.me','kesheng.wang@andpay.me',
                'hao.sun@andpay.me']

    body_text = str(time) + '未提现+未续借用户列表'
    attachment_file = "/data/excel/user_list.xlsx"

    EmailSend.send_email(subject, to_addrs, body_text, attachment_files=[attachment_file])