import os
import json
import markdown2
current_dir = os.path.dirname(os.path.realpath(__file__))

def link_to_md( name ):
    path = "file:///" + current_dir + "\\" + name + ".md"
    erl = '''<a href="%s">link</a>''' % path
    return erl





json_data= open('./github_changelog.json').read()
data = json.loads(json_data)

repos = ['Markdown Repo Table']

base_table = "| Repo | Link | Last Message | Data | \n" + \
            "|:---:|:----:|:----------------------------------:|:----:| \n"
tables = {}
for repo in repos:
    tables[repo] = base_table


for key in data:
    arepo = key
    link = link_to_md(key)
    lastMsg = data[key]['0']['Message: ']

    date = data[key]['0']["Date: "]

    row = "|" + arepo +\
        "|" + link +\
        "|" + lastMsg +\
        "|" + date + '\n'

    for repo in tables.keys():
        print (tables.keys())
        tables[repo] = tables[repo] + row


output_files = []
md_file_name = "Main.md"
md_file = open(current_dir + "/../" + md_file_name, 'w')

for key, value in tables.items():
    if value != base_table:
        md_file.write("## " + key.upper() + "\n\n")
        md_file.write(value + "\n\n")
        html_file_name = key.replace(" ", "_") + ".html"
        html_file = open(current_dir + "/../" + html_file_name, "w")
        html_table = markdown2.markdown(value.encode('utf8'), extras=["tables"])
        html_file.write(html_table)
        html_file.close()
        output_files.append(html_file_name)
md_file.close()
output_files.append(md_file_name)
