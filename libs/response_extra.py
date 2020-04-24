from django.http import JsonResponse


def response_template(msg, result, code, data):
    return JsonResponse({
        'result': result, 'code': code,
        'msg': msg, 'data': data
    })


def response_success(msg="", result=1, code=0, data=None):
    return response_template(msg, result, code, data)


def response_failure(msg="", result=0, code=0, data=None):
    return response_template(msg, result, code, data)


def al_does_not_exists(code=0):
    return response_failure(msg="没有对应课程，没有binding？", code=code)


def student_does_not_exists(code=0):
    return response_failure(msg="没有对应学生", code=code)


def face_does_not_exists(code=0):
    return response_failure(msg="没有发现人像", code=code)


def view_exception(code=0):
    return response_failure(msg="网络不好", code=code)


def msg_template(task, msg, result, code, data):
    return {
        "task": task, 'result': result, 'code': code,
        'msg': msg, 'data': data
    }


def msg_success(task="", msg="", result=1, code=0, data=None):
    return msg_template(task, msg, result, code, data)


def msg_failure(task="", msg="", result=0, code=0, data=None):
    return msg_template(task, msg, result, code, data)