#！ python3
# PurchaseTest.py - 爬虫

from selenium import webdriver
import xlwt
browser = webdriver.Chrome()
# browser.get('http://zfcg.fuzhou.gov.cn/350100/noticelist/e8d2cd51915e4c338dc1c6ee2f02b127/?page=1&notice_type=b716da75fe8d4e4387f5a8c72ac2a937&croporgan_name=%E5%8C%BB%E9%99%A2')
# browser.get('http://zfcg.fuzhou.gov.cn/350100/noticelist/e8d2cd51915e4c338dc1c6ee2f02b127/?zone_code=&zone_name=&croporgan_name=%E5%8C%BB%E9%99%A2&project_no=&fromtime=&endtime=&gpmethod=&agency_name=&title=&notice_type=b716da75fe8d4e4387f5a8c72ac2a937&purchase_item_name=')
# http://zfcg.fuzhou.gov.cn/350100/noticelist/e8d2cd51915e4c338dc1c6ee2f02b127/?page=2&notice_type=b716da75fe8d4e4387f5a8c72ac2a937&croporgan_name=%E5%8C%BB%E9%99%A2

# 创建一个excl文件
# wb = openpyxl.Workbook()
# sheet = wb.get_active_sheet()
# sheet.title = '采购信息'
# # wb.save('采购信息.xlsx')
# sheet = wb.get_sheet_by_name('采购信息')

# 创建工作簿
wbk = xlwt.Workbook(encoding='utf-8', style_compression=0)
# 创建工作表
sheet = wbk.add_sheet('采购信息', cell_overwrite_ok=True)

try:
    # 福建省采购网 http://120.35.30.176/index.html
    # 福州市采购信息
    # browser.get('http://zfcg.fuzhou.gov.cn/350100/noticelist/e8d2cd51915e4c338dc1c6ee2f02b127/?page=1&notice_type=b716da75fe8d4e4387f5a8c72ac2a937&croporgan_name=%E5%8C%BB%E9%99%A2')
    # 厦门市采购信息
    # browser.get('http://202.109.244.105/350200/noticelist/e8d2cd51915e4c338dc1c6ee2f02b127/?page=1&notice_type=b716da75fe8d4e4387f5a8c72ac2a937&croporgan_name=%E5%8C%BB%E9%99%A2')
    # 莆田市采购网
    browser.get('http://www.ptzfcg.gov.cn/350300/noticelist/e8d2cd51915e4c338dc1c6ee2f02b127/?page=1&notice_type=b716da75fe8d4e4387f5a8c72ac2a937&croporgan_name=%E5%8C%BB%E9%99%A2')
    # 表头（table_top_list包含表头每一列的值）
    table_top_list = browser.find_element_by_xpath("//table/thead/tr").find_elements_by_tag_name('td')
    for c, top in enumerate(table_top_list):
        sheet.write(0, c, top.text)
    sheet.write(0, 5, '项目名称')
    sheet.write(0, 6, '项目编号')
    sheet.write(0, 7, '采购人名称')
    sheet.write(0, 8, '地址')
    sheet.write(0, 9, '项目负责人')
    sheet.write(0, 10, '联系电话')
    sheet.write(0, 11, '代理机构名称')
    sheet.write(0, 12, '地址')
    sheet.write(0, 13, '评审部经办人')
    sheet.write(0, 14, '联系电话')
    sheet.write(0, 15, '招标公告日期')
    sheet.write(0, 16, '招标结果确定日期')
    sheet.write(0, 17, '资格性及符合性审查情况')
    sheet.write(0, 18, '商品名称')
    sheet.write(0, 19, '品牌')
    sheet.write(0, 20, '规格型号')
    sheet.write(0, 21, '数量')
    sheet.write(0, 22, '单价')
    sheet.write(0, 23, '总价')
    sheet.write(0, 24, '中标供应商')
    lineNumber = 0
    flag = 0
    dateLine = 0
    # 循环执行 进行分页的请求
    for i in range(1):
        # 福州市采购信息
        # browser.get('http://zfcg.fuzhou.gov.cn/350100/noticelist/e8d2cd51915e4c338dc1c6ee2f02b127/?page=' + str(i + 1) +'&notice_type=b716da75fe8d4e4387f5a8c72ac2a937&croporgan_name=%E5%8C%BB%E9%99%A2')
        # 厦门市采购信息
        # browser.get('http://202.109.244.105/350200/noticelist/e8d2cd51915e4c338dc1c6ee2f02b127/?page=' + str(i + 1) +'&notice_type=b716da75fe8d4e4387f5a8c72ac2a937&croporgan_name=医院')
        # 莆田市采购信息
        browser.get('http://www.ptzfcg.gov.cn/350300/noticelist/e8d2cd51915e4c338dc1c6ee2f02b127/?page=' + str(i + 1) + '&notice_type=b716da75fe8d4e4387f5a8c72ac2a937&croporgan_name=%E5%8C%BB%E9%99%A2')
        # 表的内容
        # 将表的每一行存在table_tr_list中
        table_tr_list = browser.find_element_by_xpath("//table/tbody").find_elements_by_tag_name('tr')
        for r, tr in enumerate(table_tr_list, 0):
            # 将表的每一行的每一列内容存在table_td_list中
            table_td_list = tr.find_elements_by_tag_name('td')
            length = len(table_td_list)
            lineNumber = lineNumber + 1
            print(lineNumber)
            # 写入表的内容到sheet 1中，第r行第c列
            for c, td in enumerate(table_td_list):
                # sheet.write(r + i * 10 + 1, c, td.text)
                # print(td.text)
                if c != 4:
                    sheet.write(lineNumber, c, td.text)
                else:
                    if dateLine != 0:
                        sheet.write(dateLine, c, td.text)
                    else:
                        sheet.write(lineNumber, c, td.text)
                    dateLine = 0
                if 3 == c:
                    linkElem = browser.find_element_by_link_text(td.text)
                    # print(linkElem.get_attribute('href'))
                    # 从公告内容获取细节内容
                    detailBrowser = webdriver.Chrome()
                    detailBrowser.get(linkElem.get_attribute('href'))

                    detail_table_tr_list = detailBrowser.find_element_by_xpath("//table/tbody").find_elements_by_tag_name('tr')
                    for detail_r, detail_tr in enumerate(detail_table_tr_list, 0):
                        # print(detail_r)
                        detail_table_td_list = detail_tr.find_elements_by_tag_name('td')
                        if (detail_r == 16) and (len(detail_table_td_list) > 3):
                            flag = detail_r
                        if (detail_r > 16) and (len(detail_table_td_list) > 3):
                            lineNumber = lineNumber + 1 # 有多个品目名称，则换行
                            flag = detail_r
                        for k, ttd in enumerate(detail_table_td_list, 0):
                            if (1 == k) and (detail_r < 13):
                                # print('位置：' + str(r + i * 10 + 1) + ':' + str(detail_r + length) + '内容：' + ttd.text)
                                sheet.write(lineNumber, (length + detail_r), ttd.text)
                            elif (detail_r == 16) and (len(detail_table_td_list) == 2):
                                # print("内容2：" + ttd.text)
                                continue
                            elif detail_r >= 16 and k > 3:
                                # print("内容3：" + str(14 + k) + '    ' + ttd.text)
                                # if detail_r != 16:
                                #     lineNumber = lineNumber + 1
                                # lineNumber = lineNumber + (detail_r - 16)
                                sheet.write(lineNumber, 14 + k, ttd.text)
                            elif (detail_r == (flag + 2)) and (k == 1):
                                sheet.write(lineNumber - (detail_r - 18), 24, ttd.text)
                                dateLine = lineNumber - (detail_r - 18)
                                continue
                        # print("flag" + str(flag))
                    # 关闭新开浏览器
                    detailBrowser.quit()

                    # 页面跳转
                    # linkElem = browser.find_element_by_link_text(td.text)
                    # linkElem.click()
    # 保存文件
    wbk.save('莆田市采购信息.xls')
    browser.quit()
except:
    print('Was not able to find an element with that name.')