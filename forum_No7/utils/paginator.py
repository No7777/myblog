from django.core.paginator import Paginator


def paginator_query(objs, page_no, displays=15, half_show_length=4):
    pages = Paginator(objs, displays)
    page_nums = pages.num_pages

    if page_no < 1 :
        page_no = 1
    if page_no > page_nums:
        page_no = page_nums

    page_links = [i for i in range(page_no - half_show_length, page_no + half_show_length + 1) if 0 < i <= page_nums]
    page = pages.page(page_no)
    page_previous = page_links[0] - 1
    page_last = page_links[-1] + 1

    pagination_data = {"page_links": page_links,
               "has_previous": page_previous > 0,
               "page_previous": page_previous,
               "has_next": page_last <= page_nums,
               "page_next": page_last,
               "page_current": page_no,
               "page_nums": page_nums}

    return page.object_list, pagination_data

