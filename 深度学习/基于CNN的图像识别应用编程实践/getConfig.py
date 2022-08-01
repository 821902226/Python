import configparser


def get_config(file):
    """读取配置文件的参数"""
    parser = configparser.ConfigParser()
    parser.read(file, encoding='UTF-8')
    # 保存整型参数
    parse_ints = [(key, int(value)) for key, value in parser.items('ints')]
    # 保存浮点型参数
    parse_floats = [(key, float(value)) for key, value in parser.items('floats')]
    # 保存字符型参数
    parse_strings = [(key, str(value)) for key, value in parser.items('strings')]

    return dict(parse_ints + parse_floats + parse_strings)
