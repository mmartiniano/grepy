import csv


def writer(filename, input, delimiter='|'):
    '''
    Writes input to a CSV file

    :param filename: file path to write
    :type filename: str
    :param input: generator containing data to write
    :type input: generator
    :param delimiter: character chosen to separate ouput CSV data. defaults to '|'
    :type delimiter: str, optional
    '''

    header = False

    print(f'writing "{filename}"...')
    lines = 0

    header = next(input, {}).keys()

    if not header:
        print('empty input')
        return

    with open(filename, 'w') as f:
        dict_writer = csv.DictWriter(
            f,
            fieldnames=header,
            delimiter=delimiter
        )

        for row in input:
            dict_writer.writerow(row)
            lines += 1

        print(f'wrote "{filename}" with {lines} lines')
