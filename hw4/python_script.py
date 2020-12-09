import os
import re
import sys
import json


def get_logs_arr():
    path = os.path.realpath(os.path.join(os.path.dirname(__file__), 'access.log'))
    arr = []
    try:
        with open(path) as fp:
            line = fp.readline()
            while line:
                arr.append(line)
                line = fp.readline()
        return arr
    except FileNotFoundError:
        print('no such file')
        return None


def get_parse_log_and_safe():

    arr = []
    url_dict = {}
    request_dict = {}
    client_errors = []
    server_errors = []
    the_longest_requests = []
    is_json = False

    if len(sys.argv) > 1 and sys.argv[1] == 'json':
        is_json = True

    arr = get_logs_arr()

    if arr is None:
        print('No such file')
        return

    number_of_requests = len(arr)

    for item in arr:
        splitted_line = item.split('"')

        request = splitted_line[1].split()[0]
        validation = re.match(r'^[A-Z]+$', request)

        if validation is not None:
            if request in request_dict:
                request_dict[request] += 1
            else:
                request_dict[request] = 1

        if splitted_line[3] in url_dict:
            url_dict[splitted_line[3]] += 1
        else:
            url_dict[splitted_line[3]] = 1

    for item in arr:
        splitted_line = item.split('"')

        if splitted_line[3] in url_dict:

            code_and_length = splitted_line[2].split()
            if not code_and_length[1].isdigit() or splitted_line[3] == '-':
                continue

            length = int(code_and_length[1])

            the_longest_requests.append([splitted_line[3], url_dict[splitted_line[3]], code_and_length[0], length])

            if re.match(r'^5[0-9][0-9]$', code_and_length[0]) is not None:
                server_errors.append([splitted_line[3], url_dict[splitted_line[3]], code_and_length[0], length, splitted_line[0]])

            if re.match(r'^4[0-9][0-9]$', code_and_length[0]) is not None:
                client_errors.append([splitted_line[3], url_dict[splitted_line[3]], code_and_length[0], length, splitted_line[0]])

    server_errors = sorted(server_errors, key=lambda item: item[1], reverse=True)
    client_errors = sorted(client_errors, key=lambda item: item[1], reverse=True)
    the_longest_requests = sorted(the_longest_requests, key=lambda item: item[3], reverse=True)

    the_longest_requests_format = []
    client_errors_format = []
    server_errors_format = []
    for i in range(min(len(the_longest_requests), 10)):
        request = the_longest_requests[i]
        the_longest_requests_format.append(f'{request[0]} {request[2]} {request[1]}')

    for i in range(min(len(client_errors), 10)):
        request = client_errors[i]
        client_errors_format.append(f'{request[0]} {request[2]} {request[-1].split()[0]}')

    for i in range(min(len(server_errors), 10)):
        request = server_errors[i]
        server_errors_format.append(f'{request[0]} {request[2]} {request[-1].split()[0]}')

    if not is_json:
        with open('python.log', 'w') as f:
            f.write('Number of requests\n')
            f.write(f'{str(number_of_requests)}\n')
            f.write('Number of requests type\n')
            for request_type in request_dict.keys():
                f.write(f'{(request_type)} {str(request_dict[request_type])}\n')
            f.write('Top 10 requests with the longest content length\n')
            for i in the_longest_requests_format:
                f.write(f'{i}n')
            f.write('Top 10 requests with client error\n')
            for i in client_errors_format:
                f.write(f'{i}\n')
            f.write('Top 10 requests with server error\n')
            for i in server_errors_format:
                f.write(f'{i}\n')
            return

    data_dict = {
        'Number of requests': number_of_requests,
        'Number of requests type': request_dict,
        'Top 10 requests with the longest content length': the_longest_requests_format,
        'Top 10 requests with client error': client_errors_format,
        'Top 10 requests with server error': server_errors_format,
    }

    json_dict = json.dumps(data_dict)
    with open('python.json', 'w') as f:
        f.write(json_dict)


get_parse_log_and_safe()
