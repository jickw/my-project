# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# PTS Script Version 1.0
# Trunner auto-generated test script at Mon Jun 06 16:59:53 CST 2016

from java.lang import String
from java.util import Random
from java.util import Date

# PTS脚本SDK：框架API、常用HTTP请求/响应处理API
from java.lang import System

System.setProperty("https.protocols", "TLSv1")
from util import PTS
from HTTPClient import NVPair
from HTTPClient import Cookie
from HTTPClient import HTTPRequest
from HTTPClient import CookieModule
from HTTPClient import ShutdownException

# PTS对参数化的相关支持
from com.aliyun.pts import DsvReader
from com.aliyun.pts import ParamManager

# 脚本初始化段，可以设置压测引擎的常用HTTP属性
PTS.HttpUtilities.setUrlEncoding('utf-8')
PTS.HttpUtilities.setFollowRedirects(True)
PTS.HttpUtilities.setTimeout(120000)
# PTS.HttpUtilities.setKeepAlive(False)
# PTS.HttpUtilities.setUseCookieModule(False)
# PTS.HttpUtilities.setProxyServer('localhost', 8888)
# PTS.Context.setParamDirectory("/Users/fei/Work/trunner/data")

# 支持socket测试, 如TCP\UDP等协议
# import socket

# 设置系统编码
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

params = ParamManager.getInstance()
params.addProvider(DsvReader(u"login_user.csv"))

expiryDate = Date()
expiryDate.year += 10


class TestRunner:

    # TestRunner对象的初始化方法，每个线程在创建TestRunner后执行一次该方法
    def __init__(self):
        self.rn = Random()
        params.nextRecord(u'login_user.csv')
        self.action_20050553()
        self.threadContext = PTS.Context.getThreadContext()
        self.init_cookies = CookieModule.listAllCookies(self.threadContext)

        # 主体压测方法，每个线程在测试生命周期内会循环调用该方法

    def __call__(self):
        for c in self.init_cookies:
            CookieModule.addCookie(c, self.threadContext)
        PTS.Data.delayReports = 1
        d = self.rn.nextDouble()

        statusCode = self.action_20050573()
        PTS.Framework.setExtraData(statusCode)

        PTS.Data.report()
        PTS.Data.delayReports = 0

    def __del__(self):
        self.action_20050554()

    def action_20050553(self):
        statusCode = [0L, 0L, 0L, 0L]

        headers = []
        result = HTTPRequest().GET(u'https://pre-sso.my089.net/sso?back_url=https%3A%2F%2Fpre-www.my089.net%2F', [],
                                   headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)
        checkPoint = u'用户名'
        if (not PTS.HttpUtilities.checkResponse(200, checkPoint)):
            PTS.Logger.error(u'检查点："' + checkPoint + u'"校验失败')
            PTS.Logger.error(result.getText())

        else:
            self.appKey = PTS.HttpUtilities.valueFromTextBetween(result.getText(),
                                                                 u'<input type="hidden" name="app_key" value="', u'"/>')
            PTS.Logger.info(u'appkey=' + self.appKey)
            self.RequestID = PTS.HttpUtilities.valueFromTextBetween(result.getText(), u'tongdunRequestID=\'', u'\';')
            PTS.Logger.info(u'RequestID=' + self.RequestID)

        headers = [NVPair(u'Content-Type', u'application/x-www-form-urlencoded'), ]
        bodyContext = u'username=' + params.getParamValue(
            u'login_user.csv:username') + u'&encryption=bf6c7e07755bfd60b359d1020fc86d58&password=&session_kept=600&back_url=https%253A%252F%252Fpre-www.my089.net%252F&app_key=' + self.appKey + u'&ltcc=&requestId=' + self.RequestID
        result = HTTPRequest().POST(u'https://pre-sso.my089.net/sso/login', String(bodyContext).getBytes('utf-8'),
                                    headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)
        checkPoint = u'红岭创投'
        if (not PTS.HttpUtilities.checkResponse(200, checkPoint)):
            PTS.Logger.error(u'检查点："' + checkPoint + u'"校验失败')
            PTS.Logger.error(u'登录用户：' + params.getParamValue(u'login_user.csv:username'))
            PTS.Logger.error(result.getText())

        return statusCode

    def action_20050573(self):
        statusCode = [0L, 0L, 0L, 0L]

        headers = []
        result = HTTPRequest().GET(u'https://pre-member.my089.net/uac', [], headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)
        if (300 <= result.getStatusCode()):
            PTS.Data.forCurrentTest.success = False

        headers = [NVPair(u'Content-Type', u'application/x-www-form-urlencoded'),
                   NVPair(u'X-Requested-With', u'XMLHttpRequest'),
                   NVPair(u'Accept', u'application/json, text/javascript, */*; q=0.01'), ]
        bodyContext = u''
        # result = HTTPRequest().POST(u'https://pre-member.my089.net/uac/newestFriendDynamic',String(bodyContext).getBytes('utf-8'), headers)
        result = HTTPRequest().POST(u'https://pre-member.my089.net/uac', String(bodyContext).getBytes('utf-8'), headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)
        checkPoint = u'账户安全'
        if (not PTS.HttpUtilities.checkResponse(200, checkPoint)):
            PTS.Logger.error(u'检查点："' + checkPoint + u'"校验失败')
            PTS.Data.forCurrentTest.success = False
        return statusCode

    def action_20050554(self):
        statusCode = [0L, 0L, 0L, 0L]
        headers = []
        result = HTTPRequest().GET(u'https://pre-sso.my089.net/sso/logout', [], headers)
        PTS.Framework.addHttpCode(result.getStatusCode(), statusCode)
        return statusCode


# 调用施压引擎施压。第一个参数是事务名，可以为中文；第二个参数是执行事务方法的方法名；第三个统一写TestRunner
PTS.Framework.instrumentMethod(u'个人账户首页', 'action_20050573', TestRunner)