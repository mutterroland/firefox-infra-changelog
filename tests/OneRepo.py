import os
import json
import markdown2

### Tried to create a python script that generates a .md file for every repo so we can have another .md file for each repo.
### That could be used if we want to link main page to each .md file for every repo.

current_dir = os.path.dirname(os.path.realpath(__file__))

json_data= open('./github_changelog.json').read()
data = json.loads(json_data)

repos = ['beetmoverscript']

base_table = "| Commit Number | Message | Data | \n" + \
            "|:---:|:----------------------------------:|:----:| \n"
tables = {}
for repo in repos:
    tables[repo] = base_table

for key in data:
    ncommit = key
    print(data[key])
    lastMsg = data[key]['Message']
    date = data[key]["Date"]

    row = "|" + ncommit +\
        "|" + lastMsg +\
        "|" + date + '\n'
    #print(row)
    for repo in tables.keys():
        #print (tables[repo])
        tables[repo] = tables[repo] + row

#print (tables.items())
output_files = []
md_file_name = "{}.md".format(categories)
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
