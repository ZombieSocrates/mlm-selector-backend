import requests

from bs4 import BeautifulSoup
from pprint import pprint


CHIDEO_ROSTER_PAGE = "https://inside.ideo.com/users/search?user_location_ids%5B%5D=3"
# payroll@ideo.com gets this hilarious
IDS_TO_SKIP = [31374]


def get_chideoers_from_soup(souped_html):
    chideoers = souped_html.find_all("figure")
    return [k for k in chideoers]


def get_chideoer_name(chideoer_div):
    div_match_dict = {"class":"sentinel18 book"}
    name_div = chideoer_div.find("a", div_match_dict)
    return name_div["title"]


def get_chideoer_email(chideoer_div):
    div_match_dict = {"class":"mugshot-picture-hovered-wrapper"}
    email_div = chideoer_div.find("div", div_match_dict)
    return email_div["data-email"]


def get_employee_id(chideoer_div):
    div_match_dict = {"class":"pull-left js-main-asset-placeholder"}
    id_div = chideoer_div.find("div", div_match_dict)
    return int(id_div["data-resource-id"])


def chideo_employees_inside_ideo():
    '''TODO: Ask Andrea Rabinelli to add you to the inside_pydeo repo, then
    see if you can clone it properly
    '''
    chideo_page = requests.get(CHIDEO_ROSTER_PAGE)
    print(chideo_page.status_code)
    pprint(chideo_page.text)
    chideo_soup = BeautifulSoup(chideo_page.text)
    chideo_emps = get_chideoers_from_soup(chideo_soup)
    print(f"{len(chideo_emps)} chideoers found")
    pprint(chideo_emps)


def chideo_employees_from_html(skip_ids = IDS_TO_SKIP, verbose = False):
    chideo_employees = []
    with open("chideo_roster.html", "r") as f:
        contents = f.read()
        chideo_soup = BeautifulSoup(contents, "html.parser")
        soup_emps = get_chideoers_from_soup(chideo_soup)
        for emp in soup_emps:
            if get_employee_id(emp) in skip_ids:
                continue
            chideo_employees.append({
                "id": get_employee_id(emp), 
                "name": get_chideoer_name(emp),
                "email": get_chideoer_email(emp)
                })
    if verbose: 
        print(f"{len(chideo_employees)} records preserved out of {len(soup_emps)} found")
    return chideo_employees


if __name__ == "__main__":
    pass
