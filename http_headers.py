import json
def http_headers_to_json(fin,fout):
    with open(fin) as f:
        row = f.readline()
        row = row.split()
        dic_json = {}
        dic_dubl = []
        list_return_dubl = []
        if row[0][0:6] == 'HTTP/1':
            if len(row) == 4:
                dic_json['protocol'] = row[0]
                dic_json['status_code'] = row[1]
                dic_json['status_message'] = row[2]+' '+row[3]
            else:
                dic_json['protocol'] = row[0]
                dic_json['status_code'] = row[1]
                dic_json['status_message'] = row[2]
        elif row[0][0:6] == 'HTTP/2':
            dic_json['protocol'] = row[0]
            dic_json['status_code'] = row[1]
        elif row[0] == 'GET':
            dic_json['method'] = row[0]
            dic_json['uri'] = row[1]
            dic_json['protocol'] = row[2]
        for i in f:
            if i != '\n':
                i = i.strip()
                i = i.split(': ')
                a = i[0]
                b = i[1:]
                if a in dic_json:
                    dub_key = a 
                    dic_dubl.append(b)
                else:
                    dic_json.update({i[0]:i[1]})
        if dic_dubl:
            returned = dic_json.pop(dub_key)
            list_return_dubl.append(returned)
            for i in dic_dubl:
                return_str=i[0]
                list_return_dubl.append(return_str)
            dic_json[dub_key] = list_return_dubl
            with open(fout, 'w') as f:
                json.dump(dic_json, f)
        else:
            with open(fout, 'w') as f:
                json.dump(dic_json, f)
    
    return dic_json