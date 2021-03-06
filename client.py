import os
from github import Github  # pip3 install PyGitHub
from datetime import datetime, timedelta
import json
import re
import requests
from os import listdir
from os.path import isfile, join

# Create a Github instance:
lastWeek = datetime.now() - timedelta(days=7)
current_dir = os.path.dirname(os.path.realpath(__file__))


def get_version(repo_name, repo_team):
    """
    :param repo_name: repository name
    :param repo_team: repository team
    :return: a dictionary with information from the last two release version: latestRelease and previousRelease
    """
    repo_path = repo_team + repo_name
    iteration = 0
    for tags in git.get_repo(repo_path).get_tags():
        if iteration == 0:
            latestRelease = {'Version': tags.name,
                    'Sha': tags.commit.sha,
                    'Date': tags.commit.commit.last_modified,
                    'Author': tags.commit.author.login
                    }
            iteration = 1
        elif iteration == 1:
            previousRelease = {'Version': tags.name,
                    'Sha': tags.commit.sha,
                    'Date': tags.commit.commit.last_modified,
                    'Author': tags.commit.author.login
                    }
            return {'LatestRelease': latestRelease, 'PreviousRelease': previousRelease}



def get_version_from_build_puppet(version_path, repo_name):
    """
    :param: version_path: Path to the requierments.txt where the version number is stored
    :param: repo_name: The repo for which we are checking the version.
    :return: Returns the version number that is stored in build-puppet for each *scriptworker
    """
    file_to_string = requests.get(version_path).text.split()
    for word in file_to_string:
        if repo_name in word:
            version_in_puppet = re.split('\\b==\\b', word)[-1]
            if version_in_puppet != repo_name:
                return version_in_puppet


def extract_email(commit_email):
    """
    Helper function!
    Takes as parameter a string that contains between "<" and ">" an email that needs to be extracted.
    The function uses find to search for the beginning of the email (that starts with "<") and adds the lengths of the
    "<" so that returned email doesn't contain the "<" symbol and rfind to find the ending character ">". Both find and
    rfind return the index where the carachters "<" and ">" are placed so when you do return commit_email with
    [start_char_index:ending_char_index] the string shrinks to what's between the characters.
    :param commit_email: String that contains an email
    :return: String that contains only the email
    """
    return commit_email[commit_email.find("<") + len("<"):commit_email.rfind(">")]


def create_md_table(repository_name, path_to_files):
    """
    Uses 'repository_name' parameter to generate markdown tables for every json file inside path_to_files parameter.
    :param repository_name: Used to display the repo name in the title row of the MD table
    :param path_to_files: Used to store path to json files (git_files, hg_files)
    :return: MD tables for every json file inside the git_files dir.
    """

    try:
        json_data = open(current_dir + "/{}/".format(path_to_files) + "{}.json".format(repository_name)).read()
        data = json.loads(json_data)
        base_table = "| Commit Number | Commiter | Commit Message | Commit Url | Date | \n" + \
                     "|:---:|:----:|:----------------------------------:|:------:|:----:| \n"
        tables = {}
        md_title = ["{} commit markdown table since {}".format(repository_name, lastWeek)]
        commit_number_list = [key for key in data]

        for repo in md_title:
            tables[repo] = base_table

        for key in data:
            commit_number = commit_number_list[-1]
            try:
                commit_author = data[key]["commiter_name"]
                commit_author = re.sub("\u0131", "i", commit_author)  #this is temporary
                date = data[key]["commit_date"]
                message = data[key]["commit_message"]
                message = re.sub("\|", "\|", message)
                url = data[key]["url"]

                row = "|" + commit_number + \
                      "|" + commit_author + \
                      "|" + message + \
                      "|" + "[URL](" + url + ")" + \
                      "|" + date + "\n"

                del commit_number_list[-1]
                for repo in tables.keys():
                    tables[repo] = tables[repo] + row
            except KeyError:
                last_checked = data[key]["lastChecked"]

        md_file_name = "{}.md".format(repository_name)
        md_file = open(current_dir + "/{}/".format(path_to_files) + md_file_name, "w")

        try:
            for key, value in tables.items():
                if value != base_table:
                    md_file.write("## " + key.upper() + "\n\n")
                    md_file.write(value + "\n\n")
        except KeyError:
            pass

        md_file.close()
    except FileNotFoundError:
        print("Json for {} is empty! Skipping!".format(repository_name))


def filter_git_commit_data(repository_name, repository_team, repository_version):
    """
    Filters out only the data that we need from a commit
    Substitute the special characters from commit message using 'sub' function from 're' library
    :param repository_team:
    :param repository_name:
    :param repository_version
    :return: Filtered json data
    TODO: please add the exception blocks since the script fails when it can't pull a data:
    (e.g raise self.__createException(status, responseHeaders, output)
            github.GithubException.GithubException: 502 {'message': 'Server Error'}
    """
    repo_dict = {}
    number = 0
    repository_path = repository_team + repository_name
    print("Working on repo: {}, Latest release: {}".format(repository_name, repository_version))
    repo_dict.update({number: {"lastChecked": str(datetime.utcnow()),
                               "last_two_Release": repository_version}})
    number += 1
    for commit in git.get_repo(repository_path).get_commits(since=lastWeek):
        each_commit = {}
        author_info = {}
        files_changed = []
        commit_sha = commit.sha
        commiter_name = commit.author.login
        commiter_email = commit.committer.email
        commit_message = commit.commit.message
        commit_html_url = commit.html_url
        for entry in commit.files:
            files_changed.append(entry.filename)
        commit_date = str(commit.commit.author.date)
        message = re.sub("[*\n\r]", " ", commit_message)
        author_info.update({"sha": commit_sha,
                            "url": commit_html_url,
                            "commiter_name": commiter_name,
                            "commiter_email": commiter_email,
                            "commit_message": message,
                            "commit_date": commit_date,
                            "files_changed": files_changed
                            })
        each_commit.update({int(number): author_info})
        number += 1
        repo_dict.update(each_commit)

    git_json_filename = "{}.json".format(repository_name)
    json_file = open(current_dir + "/git_files/" + git_json_filename, "w")
    json.dump(repo_dict, json_file, indent=2)
    json_file.close()


def filter_hg_commit_data(repository_name, repository_url):
    """
    This function takes a repository url and push type and returns a dictionary that contains changes in that specific
    repository.
    The HG API also supports xml and rss.
    Example:
    example = get_push("https://hg.mozilla.org/build/nagios-tools/", "json-log")
    This will be later used to get the commits from https://hg.mozilla.org/
    :param repository_url: Link of the repository, eg: https://hg.mozilla.org/build/nagios-tools/
    :param push_type: Would probably be "json-log" most of the time.
    :return: Returns a dictionary that contains the commits in the provided hg_repository_name
    """
    request_url = repository_url + "json-log"
    hg_repo_data = {}
    commit_number = 0
    print("Working on repo:", repository_name)
    hg_repo_data.update({commit_number: {"lastChecked": str(datetime.utcnow())}})
    data = json.loads(requests.get(request_url).text)
    commit_number += 1

    for entry in data["changesets"]:
        node = entry["node"]
        url = repository_url + "pushloghtml?changeset=" + node[:12]
        commiter = entry["user"]
        commiter_name = commiter.split('<')[0]
        commiter_email = extract_email(commiter)
        commit_message = entry["desc"]
        message = re.sub("[*\n\r]", " ", commit_message)
        date = entry["date"]
        hg_repo_data.update({commit_number: {
            "sha": node,
            "url": url,
            "commiter_name": commiter_name,
            "commit_email": commiter_email,
            "commit_message": message,
            "commit_date": datetime.utcfromtimestamp(date[0]).strftime('%Y-%m-%d %H:%M:%S')
        }})
        commit_number += 1
    hg_json_filename = "{}.json".format(repository_name)
    json_file = open(current_dir + "/hg_files/" + hg_json_filename, "w")
    json.dump(hg_repo_data, json_file, indent=2)
    json_file.close()


def create_files_for_hg(repositories_holder):
    """
    Main HG function. Takes every Mercurial repo from a .json file which is populated with repositories and writes all
     the commit data of each repo in a.
    creates a json and MD file for each repo as well.
    :param: repositories_holder: Expects a .json file that contains a list of repositories
    :return: The end result is a .json and a .md file for every git repository. can be found inside hg_files/
    """
    for repo in repositories_holder["Mercurial"]:
        repository_name = repo
        repository_url = repositories_holder["Mercurial"][repo]["url"]
        filter_hg_commit_data(repository_name, repository_url)
        create_md_table(repository_name, "hg_files")


def create_files_for_git(repositories_holder):
    """
    Main GIT function. Takes every Git repo from a .json file which is populated with repositories and writes all
    the commit data of each repo in a.
    creates a json and MD file for each repo as well.
    :param: repositories_holder: Expects a .json file that contains a list of repositories
    :return: The end result is a .json and a .md file for every git repository. can be found inside git_files/
    """
    for repo in repositories_holder["Github"]:
        repository_name = repo
        repository_team = repositories_holder["Github"][repo]["team"]
        repository_version = get_version(repository_name, repository_team)
        try:
            repository_version_path = repositories["Github"][repo]["configuration"]["version-path"]
            version_in_puppet = get_version_from_build_puppet(repository_version_path, repository_name)
        except KeyError:
            pass
        filter_git_commit_data(repository_name, repository_team, repository_version)
        create_md_table(repository_name, "git_files")


def clear_file(file_name):
    """
    This function takes a file that clears the content and output's a base table header for a markdown file.
    :param file_name: Name of the file to be written. (should also contain the path)
    :return: A file should be created and should contain base table.
    """
    file = open(file_name, "w")
    heading = "###  Last commits from every repository"
    base_table = "|      Repository      |                   Last commit               |    Deploy time       | \n" + \
                 "|:--------------------:|:-------------------------------------------:|:--------------------:| \n"
    file.write(heading + "\n" + base_table)
    file.close()


def write_main_md_table(file_name, repository, last_commit, deploy_time):
    """
    This function opens a file (that file should be already created and should contain a markdown table header) and
    appends to it a row that will contain the repository, the last commit and the deploy time.
    :param file_name: Name of the file in which the content is appended. (should also contain the path)
    :param repository: Repository name for the first element of the table.
    :param last_commit: Description of the last commit used as the 2nd element of the table
    :param deploy_time: Time and Time designator used as the 3rd element of the table
    :return:
    """
    row = "|" + repository + \
          "|" + last_commit + \
          "|" + deploy_time + \
          "|" + "\n"
    write_file = open(file_name, "a")
    write_file.write(row)


def extract_json(json_files, path_to_files):
    """
    Extracts the json data from json files and writes the data to the main markdown table file. The function looks
    into json files after the last commit, extracts it and calls the write_main_md_table function.
    :param json_files: List of files to extract commits from.
    :param path_to_files: Folder to json files
    :return: none
    """
    for file in json_files:
        file_path = "{}/".format(path_to_files) + file

        with open(file_path) as json_files:
            data = json.load(json_files)
            base_link = "https://github.com/Akhliskun/firefox-infra-changelog/blob/master/{}/".format(path_to_files)
            repository_name = "[" + file.rstrip().replace(".json", "") + "]" + "(" + base_link + \
                              file.rstrip().replace(" ", "%20").rstrip().replace(".json", ".md") + ")"

            try:
                commit_number = "1"
                commit_description = data[commit_number]["commit_message"]
                commit_date = data[commit_number]["commit_date"]
                write_main_md_table("main_md_table.md", repository_name, commit_description, commit_date)
            except KeyError:
                print("File " + file + " is empty. \n Please check:" + repository_name + " for more details.\n")
                pass


def generate_main_md_table(path_to_files):
    """
    Looks into repositories folders (hg_files & git files), filters the files to load the json's using a passfilter and
    calls after extraction functions.
    :param path_to_files: Folder to json files
    """
    # Get current folder path.
    dir_path = os.path.dirname(os.path.realpath(__file__))

    # Look into repositories folder and list all of the files
    only_files = [f for f in listdir(dir_path + "/{}".format(path_to_files)) if isfile(join(dir_path + "/{}".format(path_to_files), f))]

    # Pass filter only the ".json" objects
    json_files = [jf for jf in only_files if ".json" in jf]

    # Extract data from json_files and writes to main markdown table.
    extract_json(json_files, path_to_files)

    print("Table successfully generated.")


if __name__ == "__main__":
    TOKEN = os.environ.get("GIT_TOKEN")
    git = Github(TOKEN)
    repositories_data = open("./repositories.json").read()
    repositories = json.loads(repositories_data)
    create_files_for_git(repositories)
    create_files_for_hg(repositories)
    clear_file("main_md_table.md")
    generate_main_md_table("hg_files")
    generate_main_md_table("git_files")
