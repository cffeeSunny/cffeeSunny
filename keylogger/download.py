import requests
def list_it():
    name="list"
    url = f"http://127.0.0.1:5000/download/{name}"
    response = requests.get(url, auth=("admin", "KoiZnaiBe"))
    print(response.text)
def download (filename:str):
    name=filename
    down = requests.get(f"http://127.0.0.1:5000/download/{name}", auth=("admin", "KoiZnaiBe") )
    print(down.status_code)
    print(down.text)
def run():
    choice = input("List(1) or Download some file(2)? (1/2) ")
    if choice == "1":
        list_it()
    if choice == "2":
        name = input("Enter file name: ")
        download(name)
while True:
    run()