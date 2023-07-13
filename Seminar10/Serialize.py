import json


class DumpJson():
    def __init__(self, file, new_file_name):
        self.file = file
        self.new_file_name = new_file_name
        
    def dump_j(self):
        with (
            open(self.file, 'r', encoding='utf-8') as read,
            open(self.new_file_name, 'w', encoding='utf-8') as write
        ):
            my_dict = {}
            for row in read:
                key, value = row.replace('\n', '').split(',')
                my_dict[key.capitalize()] = value
            json.dump(my_dict, write, ensure_ascii=False, indent=1)
            

if __name__ == '__main__':
    dump_j = DumpJson('res.txt', 'file.json')
    dump_j.dump_j()