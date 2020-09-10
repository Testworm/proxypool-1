spider_rule_list =[
    {
        'urls': ['http://www.ip3366.net/free/?stype={}'.format(i) for i in range(1, 9)],
        'type': 'xpath',
        'node': '//tbody/tr',
        'target': {'ip': './td[1]/text()', 'port': './td[2]/text()'},
    },
    {
        'urls': ['https://www.kuaidaili.com/free/inha/{}/'.format(j) for j in range(1, 7)],
        'type': 're',
        'delay': 1,
        'pattern': r'<tr>(.*?)</tr>',
        'target': {'ip': r'="IP">(.*?)</td>', 'port': r'="PORT">(.*?)</td>'}
    },

]