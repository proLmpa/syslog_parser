import re

def syslog_parser() :
    with open(route, 'r') as file :
        data = file.read()
        pattern = r'ver:(\d+),stime:(.+),etime:(.+),device:(\w+),src:(\S+),dst:(\S+),sport:(\d+),dport:(\d+),action:(\w+),proto:(\d+),vd_id:(\d+),rule_id:(\d+),security_lvl:(\d+),message:(.+)'
        logs_data = re.findall(pattern, data)

        return logs_data

route = 'wwww'