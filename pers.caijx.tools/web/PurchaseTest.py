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
    browser.get('http://zfcg.fuzhou.gov.cn/350100/noticelist/e8d2cd51915e4c338dc1c6ee2f02b127/?page=1&notice_type=b716da75fe8d4e4387f5a8c72ac2a937&croporgan_name=%E5%8C%BB%E9%99%A2')
    # 表头（table_top_list包含表头每一列的值）
    table_top_list = browser.find_element_by_xpath("//table/thead/tr").find_elements_by_tag_name('td')
    for c, top in enumerate(table_top_list):
        sheet.write(0, c, top.text)
        # print(top.text)

    # 循环执行 进行分页的请求
    for i in range(1):
        browser.get('http://zfcg.fuzhou.gov.cn/350100/noticelist/e8d2cd51915e4c338dc1c6ee2f02b127/?page=' + str(i + 1) +'&notice_type=b716da75fe8d4e4387f5a8c72ac2a937&croporgan_name=%E5%8C%BB%E9%99%A2')
        # 表的内容
        # 将表的每一行存在table_tr_list中
        table_tr_list = browser.find_element_by_xpath("//table/tbody").find_elements_by_tag_name('tr')
        for r, tr in enumerate(table_tr_list, 0):
            # 将表的每一行的每一列内容存在table_td_list中
            table_td_list = tr.find_elements_by_tag_name('td')
            # 写入表的内容到sheet 1中，第r行第c列
            for c, td in enumerate(table_td_list):
                sheet.write(r + i * 10, c, td.text)
                if 3 == c:
                    linkElem = browser.find_element_by_link_text(td.text)
                    # print(linkElem.get_attribute('href'))
                    # 从公告内容获取细节内容
                    detailBrowser = webdriver.Chrome()
                    detailBrowser.get(linkElem.get_attribute('href'))

                    detail_table_tr_list = detailBrowser.find_element_by_xpath("//table/tbody").find_elements_by_tag_name('tr')
                    for detail_r, detail_tr in enumerate(detail_table_tr_list, 0):
                        detail_table_td_list = detail_tr.find_elements_by_tag_name('td')
                        for k, ttd in enumerate(detail_table_td_list, 0):
                            if 1 == k:
                                print(ttd.text)
                        # print(detail_table_td_list.)
                    detailBrowser.quit()

                    # 页面跳转
                    # linkElem = browser.find_element_by_link_text(td.text)
                    # linkElem.click()
                # print(td.text)
        # elem = browser.find_element_by_class_name('wrapTable')
        # print('Found <%s> element with that class name!' % (elem.tag_name))
    wbk.save('采购信息.xls')
except:
    print('Was not able to find an element with that name.')