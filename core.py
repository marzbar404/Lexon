execute(line):
    # ts the most basic it can get pmo 
    match = re.match(r'say "(.*)"', line)
    if match:
         print(match[1])
         return
