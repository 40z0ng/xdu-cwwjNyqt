import requests
import json

#个人信息
def info(userinfo):
    '''
    登录获取cookie
    :param userinfo: 用户信息（学号，密码）
    '''
    url = "https://xxcapp.xidian.edu.cn/uc/wap/login/check"

    payload = f"username={userinfo[0]}&password={userinfo[1]}"
    headers = {
    'Host': 'xxcapp.xidian.edu.cn',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0',
    'Accept':'application/json, text/javascript, */*; q=0.01',
    'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Accept-Encoding':'gzip, deflate, br',
    'Referer':'https://xxcapp.xidian.edu.cn/uc/wap/login?redirect=https%3A%2F%2Fxxcapp.xidian.edu.cn%2Fsite%2Fncov%2Fxidiandailyup',
    'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Requested-With':'XMLHttpRequest',
    'Content-Length':'41',
    'Origin':'https://xxcapp.xidian.edu.cn',
    'Connection':'keep-alive',
    # 'Cookie':'UqZBpD3n3iPIDwJU=v1sqtbQwSDjDM; eai-sess=43uv316ord83hf66nlu2i4brr2; UUkey=2b1fa50dc7616df1ae8498aa38b51580',
    'Pragma':'no-cache',
    'Cache-Control':'no-cache'
    }

    response = requests.post(url, headers=headers, data = payload)

    if response.status_code == 200 and response.json()["e"] == 0:
        print(f"{userinfo[0]}登录成功")
        UUkey = response.cookies["UUkey"]
        eai_sess = response.cookies["eai-sess"]
        UqZBpD3n3iPIDwJU = response.cookies["UqZBpD3n3iPIDwJU9BKntX+NXbQN-YJCcdeKvoWd5Q+X"]
        cookie = {'Cookie':f'UqZBpD3n3iPIDwJU={UqZBpD3n3iPIDwJU}; eai-sess={eai_sess}; UUkey={UUkey}'}
    else:
        print(f"{userinfo[0]}登陆失败,{response.json()['m']}")
        raise RuntimeError(f"登陆失败,{response.json()['m']}")
        
    return cookie

def submit(users, loc):
    '''
    提交健康卡
    :param users: 用户信息
    :param loc: 用户所在位置
    '''
    #上报地址
    url = "https://xxcapp.xidian.edu.cn/ncov/wap/default/save"

    #位置信息
    locations = {
    #西电北校区（陕西省西安市雁塔区电子城街道西安电子科技大学北校区）
    "xian_bei" : "szgjcs=""&\
                szcs=""&\
                szgj=""&\
                zgfxdq=0&\
                mjry=0&\
                csmjry=0&\
                tw=2&\
                sfcxtz=0&\
                sfjcbh=0&\
                sfcxzysx=0&\
                qksm=""&\
                sfyyjc=0&\
                jcjgqr=0&\
                remark=""&\
                address=%E9%99%95%E8%A5%BF%E7%9C%81%E8%A5%BF%E5%AE%89%E5%B8%82%E9%9B%81%E5%A1%94%E5%8C%BA%E7%94%B5%E5%AD%90%E5%9F%8E%E8%A1%97%E9%81%93%E8%A5%BF%E5%AE%89%E7%94%B5%E5%AD%90%E7%A7%91%E6%8A%80%E5%A4%A7%E5%AD%A6%E5%8C%97%E6%A0%A1%E5%8C%BA&\
                geo_api_info=%7B%22type%22%3A%22complete%22%2C%22info%22%3A%22SUCCESS%22%2C%22status%22%3A1%2C%22VDa%22%3A%22jsonp_324977_%22%2C%22position%22%3A%7B%22Q%22%3A34.23254%2C%22R%22%3A108.91516000000001%2C%22lng%22%3A108.91802%2C%22lat%22%3A34.23231%7D%2C%22message%22%3A%22Get%20ipLocation%20success.Get%20address%20success.%22%2C%22location_type%22%3A%22ip%22%2C%22accuracy%22%3Anull%2C%22isConverted%22%3Atrue%2C%22addressComponent%22%3A%7B%22citycode%22%3A%22029%22%2C%22adcode%22%3A%22610113%22%2C%22businessAreas%22%3A%5B%5D%2C%22neighborhoodType%22%3A%22%22%2C%22neighborhood%22%3A%22%22%22building%22%3A%22%22%2C%22buildingType%22%3A%22%22%2C%22street%22%3A%22%E7%99%BD%E6%B2%99%E8%B7%AF%22%2C%22streetNumber%22%3A%22238%E5%8F%B7%22%2C%22country%22%3A%22%E4%B8%AD%E5%9B%BD%22%2C%22province%22%3A%22%E9%99%95%E8%A5%BF%E7%9C%81%22%2C%22city%22%3A%22%E8%A5%BF%E5%AE%89%E5%B8%82%22%2C%22district%22%3A%22%E9%9B%81%E5%A1%94%E5%8C%BA%22%2C%22township%22%3A%22%E7%94%B5%E5%AD%90%E5%9F%8E%E8%A1%97%E9%81%93%22%7D%2C%22formattedAddress%22%3A%22%E9%99%95%E8%A5%BF%E7%9C%81%E8%A5%BF%E5%AE%89%E5%B8%82%E9%9B%81%E5%A1%94%E5%8C%BA%E7%94%B5%E5%AD%90%E5%9F%8E%E8%A1%97%E9%81%93%E8%A5%BF%E5%AE%89%E7%94%B5%E5%AD%90%E7%A7%91%E6%8A%80%E5%A4%A7%E5%AD%A6%E5%8C%97%E6%A0%A1%E5%8C%BA%22%2C%22roads%22%3A%5B%5D%2C%22crosses%22%3A%5B%5D%2C%22pois%22%3A%5B%5D%7D&\
                area=%E9%99%95%E8%A5%BF%E7%9C%81%20%E8%A5%BF%E5%AE%89%E5%B8%82%20%E9%9B%81%E5%A1%94%E5%8C%BA&\
                province=%E9%99%95%E8%A5%BF%E7%9C%81&\
                city=%E8%A5%BF%E5%AE%89%E5%B8%82&\
                sfzx=1&\
                sfjcwhry=0&\
                sfjchbry=0&\
                sfcyglq=0&\
                gllx=""&\
                glksrq=""&\
                jcbhlx=""&\
                jcbhrq=""&\
                ismoved=0&\
                bztcyy=""&\
                sftjhb=0&\
                sftjwh=0&\
                sfjcjwry=0&\
                jcjg=""",      

    #西电南校区（陕西省西安市长安区兴隆街道西安电子科技大学长安校区办公辅楼）
    "xian_nan" : "szgjcs=""&\
                szcs=""&\
                szgj=""&\
                zgfxdq=0&\
                mjry=0&\
                csmjry=0&\
                tw=2&\
                sfcxtz=0&\
                sfjcbh=0&\
                sfcxzysx=0&\
                qksm=""&\
                sfyyjc=0&\
                jcjgqr=0&\
                remark=""&\
                address=%E9%99%95%E8%A5%BF%E7%9C%81%E8%A5%BF%E5%AE%89%E5%B8%82%E9%95%BF%E5%AE%89%E5%8C%BA%E5%85%B4%E9%9A%86%E8%A1%97%E9%81%93%E8%A5%BF%E5%AE%89%E7%94%B5%E5%AD%90%E7%A7%91%E6%8A%80%E5%A4%A7%E5%AD%A6%E9%95%BF%E5%AE%89%E6%A0%A1%E5%8C%BA%E8%A1%8C%E6%94%BF%E8%BE%85%E6%A5%BC&\
                geo_api_info=%7B%22type%22%3A%22complete%22%2C%22position%22%3A%7B%22Q%22%3A34.121994628907%2C%22R%22%3A108.83715983073%2C%22%22lng%22%3A108.83716%2C%22lat%22%3A34.121995%7D%2C%22location_type%22%3A%22html5%22%2C%22message%22%3A%22Get%20ipLocation%20%22failed.Get%20geolocation%20success.Convert%20Success.Get%20address%20success.%22%2C%22accuracy%22%3A65%2C%22%22isConverted%22%3Atrue%2C%22status%22%3A1%2C%22addressComponent%22%3A%7B%22citycode%22%3A%22029%22%2C%22%22adcode%22%3A%22610116%22%2C%22businessAreas%22%3A%5B%5D%2C%22neighborhoodType%22%3A%22%22%2C%22neighborhood%22%3A%22%22%2C%22%22building%22%3A%22%22%2C%22buildingType%22%3A%22%22%2C%22street%22%3A%22%E9%9B%B7%E7%94%98%E8%B7%AF%22%2C%22streetNumber%22%3A%22264%E5%8F%B7%22%2C%22%22country%22%3A%22%E4%B8%AD%E5%9B%BD%22%2C%22province%22%3A%22%E9%99%95%E8%A5%BF%E7%9C%81%22%2C%22city%22%3A%22%E8%A5%BF%E5%AE%89%E5%B8%82%22%2C%22district%22%3A%22%E9%95%BF%E5%AE%89%E5%8C%BA%22%2C%22%22township%22%3A%22%E5%85%B4%E9%9A%86%E8%A1%97%E9%81%93%22%7D%2C%22formattedAddress%22%3A%22%E9%99%95%E8%A5%BF%E7%9C%81%E8%A5%BF%E5%AE%89%E5%B8%82%E9%95%BF%E5%AE%89%E5%8C%BA%E5%85%B4%E9%9A%86%E8%A1%97%E9%81%93%E8%A5%BF%E5%AE%89%E7%94%B5%E5%AD%90%E7%A7%91%E6%8A%80%E5%A4%A7%E5%AD%A6%E9%95%BF%E5%AE%89%E6%A0%A1%E5%8C%BA%E5%8A%9E%E5%85%AC%E8%BE%85%E6%A5%BC%22%2C%22roads%22%3A%5B%5D%2C%22%22crosses%22%3A%5B%5D%2C%22pois%22%3A%5B%5D%2C%22info%22%3A%22SUCCESS%22%7D&\
                area=%E9%99%95%E8%A5%BF%E7%9C%81%20%E8%A5%BF%E5%AE%89%E5%B8%82%20%E9%95%BF%E5%AE%89%E5%8C%BA&\
                province=%E9%99%95%E8%A5%BF%E7%9C%81&\
                city=%E8%A5%BF%E5%AE%89%E5%B8%82&\
                sfzx=1&\
                sfjcwhry=0&\
                sfjchbry=0&\
                sfcyglq=0&\
                gllx=""&\
                glksrq=""&\
                jcbhlx=""&\
                jcbhrq=""&\
                ismoved=0&\
                bztcyy=""&\
                sftjhb=0&\
                sftjwh=0&\
                sfjcjwry=0&\
                jcjg=""",  
    
    #广研院（广东省广州市黄埔区九龙镇御禾田公寓广州绿地城）
    "guangzhou" : "szgjcs=""&\
                szcs=""&\
                szgj=""&\
                zgfxdq=0&\
                mjry=0&\
                csmjry=0&\
                tw=2&\
                sfcxtz=0&\
                sfjcbh=0&\
                sfcxzysx=0&\
                qksm=""&\
                sfyyjc=0&\
                jcjgqr=0&\
                remark=""&\
                address=%E5%B9%BF%E4%B8%9C%E7%9C%81%E5%B9%BF%E5%B7%9E%E5%B8%82%E9%BB%84%E5%9F%94%E5%8C%BA%E4%B9%9D%E9%BE%99%E9%95%87%E5%BE%A1%E7%A6%BE%E7%94%B0%E5%85%AC%E5%AF%93%E5%B9%BF%E5%B7%9E%E7%BB%BF%E5%9C%B0%E5%9F%8E&\
                geo_api_info=%7B%22type%22%3A%22complete%22%2C%22info%22%3A%22SUCCESS%22%2C%22status%22%3A1%2C%22%24Da%22%3A%22jsonp_121788_%22%2C%22position%22%3A%7B%22Q%22%3A23.32582%2C%22R%22%3A113.55039999999997%2C%22lng%22%3A113.5504%2C%22lat%22%3A23.32582%7D%2C%22message%22%3A%22Get%20ipLocation%20success.Get%20address%20success.%22%2C%22location_type%22%3A%22ip%22%2C%22accuracy%22%3Anull%2C%22isConverted%22%3Atrue%2C%22addressComponent%22%3A%7B%22citycode%22%3A%22020%22%2C%22adcode%22%3A%22440112%22%2C%22businessAreas%22%3A%5B%5D%2C%22neighborhoodType%22%3A%22%22%2C%22neighborhood%22%3A%22%22%2C%22building%22%3A%22%22%2C%22buildingType%22%3A%22%22%2C%22street%22%3A%22%E4%B9%9D%E9%BE%99%E5%A4%A7%E9%81%93%22%2C%22streetNumber%22%3A%22108%E5%8F%B7%22%2C%22country%22%3A%22%E4%B8%AD%E5%9B%BD%22%2C%22province%22%3A%22%E5%B9%BF%E4%B8%9C%E7%9C%81%22%2C%22city%22%3A%22%E5%B9%BF%E5%B7%9E%E5%B8%82%22%2C%22district%22%3A%22%E9%BB%84%E5%9F%94%E5%8C%BA%22%2C%22township%22%3A%22%E4%B9%9D%E9%BE%99%E9%95%87%22%7D%2C%22formattedAddress%22%3A%22%E5%B9%BF%E4%B8%9C%E7%9C%81%E5%B9%BF%E5%B7%9E%E5%B8%82%E9%BB%84%E5%9F%94%E5%8C%BA%E4%B9%9D%E9%BE%99%E9%95%87%E5%BE%A1%E7%A6%BE%E7%94%B0%E5%85%AC%E5%AF%93%E5%B9%BF%E5%B7%9E%E7%BB%BF%E5%9C%B0%E5%9F%8E%22%2C%22roads%22%3A%5B%5D%2C%22crosses%22%3A%5B%5D%2C%22pois%22%3A%5B%5D%7D&\
                area=%E5%B9%BF%E4%B8%9C%E7%9C%81%20%E5%B9%BF%E5%B7%9E%E5%B8%82%20%E9%BB%84%E5%9F%94%E5%8C%BA&\
                province=%E5%B9%BF%E4%B8%9C%E7%9C%81&\
                city=%E5%B9%BF%E5%B7%9E%E5%B8%82&\
                sfzx=0&\
                sfjcwhry=0&\
                sfjchbry=0&\
                sfcyglq=0&\
                gllx=""&\
                glksrq=""&\
                jcbhlx=""&\
                jcbhrq=""&\
                ismoved=0&\
                bztcyy=""&\
                sftjhb=0&\
                sftjwh=0&\
                sfjcjwry=0&\
                jcjg=""",            
                }

    headers = {
    'Host': 'xxcapp.xidian.edu.cn',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Accept-Encoding': 'gzip, deflate, br',
    'Content-Type': 'application/x-www-form-urlencoded',
    'X-Requested-With': 'XMLHttpRequest',
    'Content-Length': '1721',
    'Origin': 'https://xxcapp.xidian.edu.cn',
    'Connection': 'keep-alive',
    'Referer': 'https://xxcapp.xidian.edu.cn/site/ncov/xidiandailyup'
    }
    for user in users:
        cookie = info((user, users[user]))
        headers_with_cookie = {**headers, **cookie}   #请求头中添加cookie
        for t in range(3):
            try:
                response = requests.post(url=url, headers=headers_with_cookie, data = locations[loc])
                if response.status_code == 200 and response.json()["e"] == 0:
                    print(f"{user}填报成功\n")
                    break
                elif response.status_code == 200 and response.json()["e"] == 1:
                    print(f"{user}已填报了\n")
                    break
                else:
                    print(f"{user.userinfo[0]}填报失败")
                    raise RuntimeError(f"填报失败,{response.json()['m']}\n")
            except:
                continue

if __name__ == "__main__":
    xian_bei = {
    }
    
    xian_nan = {
    }

    guangzhou = {
    }
    
    submit(xian_bei, "xian_bei")
    submit(xian_nan, "xian_nan")
    submit(jiaxing, "guangzhou") 


