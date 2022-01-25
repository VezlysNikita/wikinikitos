from django.shortcuts import render, redirect

from . import util

from markdown2 import Markdown



def index(request):

    if request.method == "POST":

        search=request.POST["q"]
        print(util.list_entries())

        if search in util.list_entries():

            return redirect("/wiki/" + search, {"entries": util.list_entries()})

        display = []
                
        for word in util.list_entries():
                    
            if search in word:
                        
                display.append(word)
                print(display)
                print(len(display))

        return render(request, "encyclopedia/index.html", {
                "entries": display
            })

                
    else:
        print("hello")
        return render(request, "encyclopedia/index.html", {
            "entries": util.list_entries()
        })


def title(request, title):
    nd = Markdown()
    page = util.get_entry(title)
    finalPage = nd.convert(page)
    print(page)
    return render(request, "encyclopedia/title.html", {
            "title": title,
            "entries":finalPage
        })

def create(request):
    if request.method == "POST":
        print("hello")
        nd = Markdown()
        

        searchnew = request.POST["createform"]
        content = request.POST["content"]

        if searchnew in util.list_entries():

            return redirect("/wiki/" + searchnew)

        else:  
            nd._encode_code(content)
            
            util.save_entry(searchnew, content)

            return redirect("/wiki/" + searchnew)



    
    return render(
        request,
        "encyclopedia/create.html"
    )

