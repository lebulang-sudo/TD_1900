# coding=utf-8
# 编译日期：2020-11-21 21:39:53
# 版权所有：www.i-search.com.cn
import ubpa.init_input as iinput
from ubpa.base_util import StdOutHook, ExceptionHandler
import ubpa.iautomation as iautomation
import time
import pdb
from ubpa.ilog import ILog
from ubpa.base_img import set_img_res_path
import getopt
from sys import argv
import sys
import os

class weibo:
     
    def __init__(self,**kwargs):
        self.__logger = ILog(__file__)
        self.path = set_img_res_path(__file__)
        self.robot_no = ''
        self.proc_no = ''
        self.job_no = ''
        self.input_arg = ''
        if('robot_no' in kwargs.keys()):
            self.robot_no = kwargs['robot_no']
        if('proc_no' in kwargs.keys()):
            self.proc_no = kwargs['proc_no']
        if('job_no' in kwargs.keys()):
            self.job_no = kwargs['job_no']
        ILog.JOB_NO, ILog.OLD_STDOUT = self.job_no, sys.stdout
        sys.stdout = StdOutHook(self.job_no, sys.stdout)
        ExceptionHandler.JOB_NO, ExceptionHandler.OLD_STDERR = self.job_no, sys.stderr
        sys.excepthook = ExceptionHandler.handle_exception
        if('input_arg' in kwargs.keys()):
            self.input_arg = kwargs['input_arg']
            if(len(self.input_arg) <= 0):
                self.input_arg = iinput.load_init(__file__)
            if self.input_arg is None:
                sys.exit(0)
      
    def flow1(self):
        #鼠标点击
        self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:flow1,StepNodeTag:2020112121391871676,Title:鼠标点击,Note:')
        selectorJson={"selector":[{"ControlType":"文本","ControlTypeID":"0xC364","Index":"1"},{"ControlType":"窗格","ControlTypeID":"0xC371","Index":"1"},{"ControlType":"窗格","ControlTypeID":"0xC371","Index":"1"},{"ControlType":"列表项目","ControlTypeID":"0xC357","Index":"8"},{"ControlType":"列表","ControlTypeID":"0xC358","Index":"1"},{"ControlType":"窗格","ControlTypeID":"0xC371","Index":"1"},{"ControlType":"窗格","ControlTypeID":"0xC371","Index":"2"},{"ControlType":"窗格","ControlTypeID":"0xC371","Index":"2"},{"ControlType":"窗格","ControlTypeID":"0xC371","Index":"2"},{"ControlType":"窗格","ControlTypeID":"0xC371","Index":"2"}]}
        iautomation.do_click(waitfor=10.000,run_mode='unctrl',button='left',curson='center',win_name=r'微信',win_class=r'WeChatMainWndForPC',selector=selectorJson)
      
    def Main(self):
        lv_1='body > DIV:nth-of-type(1) > DIV:nth-of-type(1) > DIV:nth-of-type(2) > DIV:nth-of-type(1) > DIV:nth-of-type(2) > DIV:nth-of-type(2) > DIV:nth-of-type(7) > DIV:nth-of-type(1) > DIV:nth-of-type(1) > DIV:nth-of-type(1) > DIV:nth-of-type(3) > UL:nth-of-type(1) > LI:nth-of-type('
        lv_2=') > DIV:nth-of-type(1) > DIV:nth-of-type(2) > DIV:nth-of-type(5) > P:nth-of-type(1) > A:nth-of-type(1) > SPAN:nth-of-type(1)'
        lv_3=None
        lv_4=None
        flag=None
 
if __name__ == '__main__':
    ILog.begin_init()
    robot_no = ''
    proc_no = ''
    job_no = ''
    input_arg = ''
    try:
        argv = sys.argv[1:]
        opts, args = getopt.getopt(argv,"hr:p:j:i:",["robot = ","proc = ","job = ","input = "])
    except getopt.GetoptError:
        print ('robot.py -r <robot> -p <proc> -j <job>')
    for opt, arg in opts:
        if opt == '-h':
            print ('robot.py -r <robot> -p <proc> -j <job>')
        elif opt in ("-r", "--robot"):
            robot_no = arg
        elif opt in ("-p", "--proc"):
            proc_no = arg
        elif opt in ("-j", "--job"):
            job_no = arg
        elif opt in ("-i", "--input"):
            input_arg = arg
    pro = weibo(robot_no=robot_no,proc_no=proc_no,job_no=job_no,input_arg=input_arg)
    pro.flow1()
