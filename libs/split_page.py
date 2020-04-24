from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage, InvalidPage


def split_page(pre_list, each_page, now_page):
    paginator = Paginator(pre_list, each_page)
    try:
        split_list = paginator.page(now_page)

    except PageNotAnInteger:
        # 如果请求的页数不是整数, 返回第一页。
        split_list = paginator.page(1)
    except EmptyPage:
        # 如果请求的页数不在合法的页数范围内，返回结果的最后一页。
        split_list = paginator.page(paginator.num_pages)
    except InvalidPage:
        # 如果请求的页数不存在, 重定向页面
        return 1
    return split_list, paginator.count  # 数据总量


def man_split_page(this_list, each_page, start_point):
    """
    this_list 要求不重复
    :param this_list:
    :param each_page:
    :param start_point:
    :return:
    """
    print(this_list)
    if each_page <= 0:
        each_page = 1

    has_next_page = True
    total = 0

    data_len = len(this_list)  # 数据总量

    mark_point = 0  # 标记点
    if not start_point == 0:
        for tl in this_list:
            mark_point += 1
            if tl["id"] == start_point:
                break
    valid_len = data_len - mark_point  # 可使用长度
    end_point = data_len
    if valid_len >= each_page:
        end_point = mark_point + each_page
        has_next_page = False
    return_data = {
        "has_next_page": has_next_page,
        "data_total": data_len
    }
    return this_list[mark_point:end_point], return_data


