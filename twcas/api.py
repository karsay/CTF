import urllib.parse
import urllib.request
import json
import sys

def startAPI(accsessToken, level):
    
    headers = {
        "Authorization": "Bearer {}".format(accsessToken)
    }

    params = {
        "level": level
    }

    p = urllib.parse.urlencode(params)
    url = "https://apiv2.twitcasting.tv/internships/2019/games?" + p
    req = urllib.request.Request(url,headers=headers)

    with urllib.request.urlopen(req) as res:
        html = res.read().decode("utf-8")
        myId = json.loads(html)
        print(html)
        return myId["id"]

def answerAPI(myId, accsessToken, ope, rtnAns):

    ans = rtnAns.replace("?", ope)
    print(ans)

    url  = "https://apiv2.twitcasting.tv/internships/2019/games/" + str(myId)
    method = "POST"
    headers = {
        "Authorization":"Bearer {}".format(accsessToken)
    }

    data = {
        "answer": ans
    }

    jsonData = json.dumps(data).encode("utf-8")

    req = urllib.request.Request(url, data=jsonData, headers=headers, method=method)
    
    with urllib.request.urlopen(req) as res:
        html = res.read().decode("utf-8")
        print(html)
        rtnAns = json.loads(html)
        return rtnAns["hints"]

def deleteAPI(accsessToken):

    url = "https://apiv2.twitcasting.tv/internships/2019/games/"
    method = "DELETE"
    headers = {
        "Authorization":"Bearer {}".format(accsessToken)
    }

    req = urllib.request.Request(url,headers=headers,method=method)
    with urllib.request.urlopen(req) as res:
        html = res.read().decode("utf-8")
        print(html)


def main():

    accsessToken = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6ImUzMDQwYzk2OWI4YjNhZDE2OWFhNWY2NmNkM2NhZjkyOThiN2VkZDMyMjI3MGU2YzgxNTk1NmQwMjBjYzY4YjZjNWRkZjQ4YWRlNDQ3YmY3In0.eyJhdWQiOiIxODIyMjQ5MzguMjNhNzJmNDA2NzI4M2I0OWY5NjZmOTMyMzViMTg2NDQzN2VjNWY2YTlmY2M5NjVlOGIzOTM5MGRmNWQ2YWE5NCIsImp0aSI6ImUzMDQwYzk2OWI4YjNhZDE2OWFhNWY2NmNkM2NhZjkyOThiN2VkZDMyMjI3MGU2YzgxNTk1NmQwMjBjYzY4YjZjNWRkZjQ4YWRlNDQ3YmY3IiwiaWF0IjoxNTYxNzMxMTk4LCJuYmYiOjE1NjE3MzExOTgsImV4cCI6MTU3NzI4MzE5OCwic3ViIjoiMjI2ODU3NTAyOSIsInNjb3BlcyI6WyJyZWFkIl19.iu3O0PnL8B7pffEUspPG1JgXuRh9JKkWeOwjjFkG2Qjhk6_JNfwug7hYjWvj3Ir3FC0Eq_KuTaj24tVUZrrGJ0zHHDqJ8eQHrmdStjpZgDktucIjOeVWTzeZD0lLcD4UlC_zJK2jyl3QWYW9ptbBZ7fZ9LfzEHPgKiTT1PJNGLMG9PEavl_CAZM8koxFskD-dd0490AzAQZyvaKtTcEgRwe0m5AyChU3m0v52cix5I6NstBgjL6Cr3ZMgIEtH_gTmRnqGOd8te1ki7Aao-WOI40nqjiwPonav34umuo84p7uAiDUZFQoJjT3KfimKVy-5YmeYe710R2edQ_nHvscfA"
    level = 3
    myId = startAPI(accsessToken, level)
    rtnAns = "??????"

    for i in "+-*/":
        rtnAns = answerAPI(myId,accsessToken,i, rtnAns)
    #ゲーム終了API、使うならコメントアウト外す
    # deleteAPI(accsessToken)

if __name__ == "__main__":
    main()

