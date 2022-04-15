import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# calling API and save answer
url = "https://api.github.com/search/repositories?q=language:python&sort=stars"

r = requests.get(url)

print("code: ", r.status_code)

# put response in variable (dictionary)
response_dict = r.json()

# print(response_dict.keys())
# print(response_dict["items"])

print("Number of repositories: ", response_dict["total_count"])

# work with information
repo_dicts = response_dict["items"]
# print("Number of repos: ", len(repo_dicts))

# analyze first repo
# to get information what data are available using API you can:
# - read documentation
# - analyze it with code
repo_dict = repo_dicts[0]
# print("\nKeys: ", len(repo_dict))
# for key in sorted(repo_dict.keys()):
    # print(key)

# print("\nChosen info about all repos: ")

names, plot_dicts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict["name"])

    # add labels to the bars
    plot_dict = {
        "value": repo_dict["stargazers_count"],
        "label": repo_dict["description"],
        "xlink": repo_dict["html_url"]
    }
    plot_dicts.append(plot_dict)

# creating visualization
my_style = LS("#333366", baze_style=LCS)

# set of configurations for the Bar() chart
my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 24
my_config.major_label_font_size = 24
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

# creating chart
chart = pygal.Bar(my_config, style=my_style)
chart.force_uri_protocol = "http"
chart.title = "Python repositories with the highest amount of stars on GitHub"
chart.x_labels = names
chart.add("", plot_dicts)
chart.render_to_file("python_repos.svg")
