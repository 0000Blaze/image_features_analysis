import requests

def download_image(url, file_name):
    response = requests.get(url)
    with open(file_name, "wb") as f:
        f.write(response.content)

URLs = [
    "https://plus.unsplash.com/premium_photo-1668902221464-402993a500ce?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MXx8bm8lMjBjb3B5cmlnaHR8ZW58MHx8MHx8&auto=format&fit=crop&w=500&q=60",
    "https://images.unsplash.com/photo-1565649373303-d478f7bfcc32?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8bm8lMjBjb3B5cmlnaHR8ZW58MHx8MHx8&auto=format&fit=crop&w=500&q=60",
    "https://images.unsplash.com/photo-1563991655280-cb95c90ca2fb?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8M3x8bm8lMjBjb3B5cmlnaHR8ZW58MHx8MHx8&auto=format&fit=crop&w=500&q=60",
    "https://images.unsplash.com/photo-1596231637233-761eb2d85503?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8NXx8bm8lMjBjb3B5cmlnaHR8ZW58MHx8MHx8&auto=format&fit=crop&w=500&q=60",
    "https://images.unsplash.com/photo-1601425276965-bdb69f1f3977?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8N3x8bm8lMjBjb3B5cmlnaHR8ZW58MHx8MHx8&auto=format&fit=crop&w=500&q=60",
    "https://images.unsplash.com/photo-1551751336-07e038f36886?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Nnx8bm8lMjBjb3B5cmlnaHR8ZW58MHx8MHx8&auto=format&fit=crop&w=700&q=60",
    "https://images.unsplash.com/photo-1601425276965-bdb69f1f3977?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8N3x8bm8lMjBjb3B5cmlnaHR8ZW58MHx8MHx8&auto=format&fit=crop&w=700&q=60",
    "https://images.unsplash.com/photo-1578951142202-e0176237a11b?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8OHx8bm8lMjBjb3B5cmlnaHR8ZW58MHx8MHx8&auto=format&fit=crop&w=700&q=60",
    "https://images.unsplash.com/photo-1573057454928-f6eda06245ed?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8OXx8bm8lMjBjb3B5cmlnaHR8ZW58MHx8MHx8&auto=format&fit=crop&w=700&q=60",
    "https://images.unsplash.com/photo-1561803102-ad65e246740c?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MTB8fG5vJTIwY29weXJpZ2h0fGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=700&q=60",
    "https://images.unsplash.com/photo-1543854474-1894d5ad1360?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MTF8fG5vJTIwY29weXJpZ2h0fGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=700&q=60",
    "https://images.unsplash.com/photo-1542387909088-0719835c242a?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MTJ8fG5vJTIwY29weXJpZ2h0fGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=700&q=60",
    "https://images.unsplash.com/photo-1602826347632-fc49a8675be6?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MTN8fG5vJTIwY29weXJpZ2h0fGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=700&q=60",
    "https://images.unsplash.com/photo-1588191508470-ad74246565c5?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MTR8fG5vJTIwY29weXJpZ2h0fGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=700&q=60",
    "https://images.unsplash.com/photo-1535963743569-591629ea26a7?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MTV8fG5vJTIwY29weXJpZ2h0fGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=700&q=60",
    "https://images.unsplash.com/photo-1602784380190-81706bc30b9b?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MTZ8fG5vJTIwY29weXJpZ2h0fGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=700&q=60",
    "https://images.unsplash.com/photo-1596850371319-cccb9fbdf4e6?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MTd8fG5vJTIwY29weXJpZ2h0fGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=700&q=60",
    "https://images.unsplash.com/photo-1594486959076-7f2fc824dd75?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MTh8fG5vJTIwY29weXJpZ2h0fGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=700&q=60",
    "https://images.unsplash.com/photo-1624450303884-d4fce1ae239f?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MTl8fG5vJTIwY29weXJpZ2h0fGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=700&q=60",
    "https://images.unsplash.com/photo-1553258318-c22356c14808?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MjB8fG5vJTIwY29weXJpZ2h0fGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=700&q=60",
]

for i, URL in enumerate(URLs):
    file_name = f"image{i}.jpg"
    download_image(URL, file_name)
