# _*_ coding: utf-8 _*_
__author__ = 'Ruis'
__date__ = '2018/10/16 下午2:31'

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from urllib.parse import quote

browser = we