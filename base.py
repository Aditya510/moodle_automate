from selenium import webdriver
driver = webdriver.Chrome()

def download_url(downloadurl):
    download_dir = "User/Documents/GitHub/moodle_automate/test1"  # for linux/*nix, download_dir="/usr/Public"
    options = webdriver.ChromeOptions()

    profile = {"plugins.plugins_list": [{"enabled": False, "name": "Chrome PDF Viewer"}],  # Disable Chrome's PDF Viewer
               "download.default_directory": download_dir, "download.extensions_to_open": "applications/pdf"}
    options.add_experimental_option("prefs", profile)
    driver = webdriver.Chrome(
        options=options)  # Optional argument, if not specified will search path.

    driver.get(downloadurl)
    print("here")


def download_resources(sub_url):
    driver.get(sub_url)
    links = driver.find_elements_by_tag_name("a")
    links_url = []

    for item in links:

        if "https://moodle.iitd.ac.in/mod/resource" in item.get_attribute("href"):
            links_url.append(item.get_attribute("href"))
        if "https://moodle.iitd.ac.in/mod/folder" in item.get_attribute("href"):
            download_resources(item.get_attribute("href"))

    driver.get("https://moodle.iitd.ac.in/my/")
    for item in links_url:
        download_url(item)
    print(links_url)


driver.get("https://moodle.iitd.ac.in")
driver.find_element_by_id("username").send_keys("")
driver.find_element_by_id("password").send_keys("")
login = driver.find_element_by_id("login")
query = (login.text.split('\n')[3])
answer = ""
if "second" in query:
    answer = query.split()[-2]
if "first" in query:
    answer = query.split()[-4]
if "+" in query:
    answer = (int(query.split()[-4]) + int(query.split()[-2]))
if "-" in query:
    answer = (int(query.split()[-4]) - int(query.split()[-2]))

driver.find_element_by_id("valuepkg3").send_keys(answer)
driver.find_element_by_id("loginbtn").click()
links = driver.find_elements_by_tag_name("a")
links_url = []
for item in links:
    if item.get_attribute("href") == "https://moodle.iitd.ac.in/my/#myoverview_courses_view_in_progress":
        break
    elif "https://moodle.iitd.ac.in/course" in item.get_attribute("href") :
        links_url.append(item.get_attribute("href"))
download_resources(links_url[0])
print(links_url)



