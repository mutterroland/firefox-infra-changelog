import os
import json
import markdown2

current_dir = os.path.dirname(os.path.realpath(__file__))
json_data= open('./github_changelog.json').read()  # opens github_changelog.json
data = json.loads(json_data) # converts the load and assigns a variable so we can work with it

def link_to_md(name): #function for generating hyperlink that leads into md table of a specific repo ### See OneRepo.py for further reference
    path = "file:///" + current_dir + "\\" + name + ".md"
    erl = '''<a href="%s">link</a>''' % path
    return erl

def link_in_repo(name): #function to generate hyperlink that leads to github repo
    link = data[key]['0']['Url Repo']
    repo = '''<a href={}>{}</a>'''.format(link, key)
    return repo


repos = ['Markdown Repo Table']

base_table = "| Repo | Link | Last Message | Data | \n" + \
            "|:---:|:----:|:----------------------------------:|:----:| \n"
tables = {}
for repo in repos:
    tables[repo] = base_table


for key in data: #for that "selects" needed informations from github_changelog json and stores data that ends in the actual .md file
    arepo = link_in_repo(key) #variable that use link_in_repo(name) function
    link = link_to_md(key) #variable that use link_to(name) function
    lastMsg = data[key]['0']['Message'] #variable that takes data from github_changelog.json
    date = data[key]['0']['Date'] #variable that takes data from github_changelog.json

    row = "|" + arepo +\
        "|" + link +\
        "|" + lastMsg +\
        "|" + date + '\n'

    for repo in tables.keys():
        tables[repo] = tables[repo] + row


output_files = []
md_file_name = "Main.md"
md_file = open(current_dir + "/../" + md_file_name, 'w') #creates the actual md file

for key, value in tables.items(): #for that converts .md file into .html file
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
