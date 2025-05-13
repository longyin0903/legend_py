from google.protobuf import text_format

def load_from_string(data, target):
  text_format.Parse(data, target)

def load_from_file(path, target):
  f = open(path, 'r', encoding='utf-8')
  text_format.Parse(f.read(), target)
  f.close()
  
def save_to_file(path, data):
  f = open(path, 'w', encoding='utf-8')
  f.write(text_format.MessageToString(data))
  f.close()