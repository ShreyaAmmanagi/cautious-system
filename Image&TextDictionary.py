import webbrowser
word = input("what's your word_ ")
def search():
    url = "https://dictionary.cambridge.org/dictionary/english/"+word
    url2 = "https://www.gettyimages.in/photos/"+word
    browser = "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
    webbrowser.open(url)
    webbrowser.open(url2)
search()