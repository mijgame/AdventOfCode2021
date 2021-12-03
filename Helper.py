def read_input(filename, cast=None):
    result = []
    with open(filename) as input_file:
        for line in input_file.readlines():
            if cast is not None:
                if cast == 'int':
                    result.append(int(line.strip()))
            else:
                result.append(line.strip())

    if [] == result[-1] or result[-1] is None:
        result.pop()

    return result


def read_input_split_by(filename, delimiter):
    with open(filename) as input_file:
        all_lines = input_file.read()
        result = all_lines.split(delimiter)
    return result
