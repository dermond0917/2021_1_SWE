import json, io

f=io.open('QA2_210310.txt', mode='wt', encoding='utf8')
with open('210310.json')as json_file:
    data=json.load(json_file)

    for item in data:
        if("user_profile" in item):
            txt = item["text"]
            prof = item["user_profile"]
            if("display_name" in prof):
                name = prof["display_name"]
            if(len(name)==0):
                name = prof["real_name"]
            f.write(name)
            f.write(': '.decode('utf8'))
            f.write(txt)
            f.write('\n\n'.decode('utf8'))
