import sys
from jinja2 import Environment, FileSystemLoader
import os.path
from konachan import *

#path = os.path.dirname(__file__) + '/templates/'
#print(path)
loader = FileSystemLoader('./templates')
env = Environment(loader = loader)
template_pc = env.get_template('postlist.html')
template_mobile = env.get_template('postlist_mobile.html')

def gen_post_list_page(post_list, template, output):
    if post_list is None:
        return
    print("Rendering to "+output)
    page = template.render(posts = post_list)
    with open(output, 'w') as fn:
        fn.write(page)
    print("Page refreshed")

def gen_post_matrix_page(post_list, template, output):
    if post_list is None:
        return
    row = []
    col = []
    for p in post_list:
        col.append(p)
        if len(col)>=4:
            row.append(col)
            col = []
    if len(col)>0:
        row.append(col)
    print("Rendering to "+output)
    page = template.render(postrow = row)
    with open(output, 'w') as fn:
        fn.write(page)
    print("Page refreshed")

def gen_all_post_list_page(pl_s, pl_q, pl_e):
    print("Generating static pages")
    gen_post_matrix_page(pl_s, template_pc, "index.html")
    gen_post_matrix_page(pl_q, template_pc, "q/index.html")
    gen_post_matrix_page(pl_e, template_pc, "e/index.html")
    gen_post_list_page(pl_s, template_mobile, "m/index.html")
    gen_post_list_page(pl_q, template_mobile, "mq/index.html")
    gen_post_list_page(pl_e, template_mobile, "me/index.html")

def gen():
    pl_s = DataSourceS().Get()
    pl_q = DataSourceQ().Get()
    pl_e = DataSourceE().Get()
    gen_all_post_list_page(pl_s, pl_q, pl_e)

def gentest():
    pl = DataSourceTest().Get()
    gen_all_post_list_page(pl, pl, pl)

if __name__ == "__main__":
    isTest = False
    for arg in sys.argv:
        if arg.strip() == '-t':
            isTest = True
            break
    if isTest:
        gentest()
    else:
        gen()

