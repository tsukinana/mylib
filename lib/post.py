import requests

url=""

headers={
    "": "",
    "":""    
}

post_data={
    "":"",
    "":""
}

print(post_data)

r_post=requests.post(url,headers=headers,data=post_data)
print(r_post.text)