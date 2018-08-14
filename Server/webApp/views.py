# coding:utf-8
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
import webApp.models as models
import pymysql
db = pymysql.connect("localhost","root","root","test" )
model=db.cursor(pymysql.cursors.DictCursor)

def login(request):

    html="login.html"
    dataname='rlt'
    data=''
    if request.method=='POST':
        username=request.POST.get('username',None)
        userpass = request.POST.get('userpass',None)
        if username!="" and userpass !="":
            try:
                print(username)
                print(userpass)
                flag=models.UserInfo.objects.get(user=username,pwd=userpass)
                print(flag)
                if flag:
                    return HttpResponseRedirect('/user_List/1')
            except:
                html = 'login.html'
                data = '账户密码错误'
                dataname='rlt'
        else:
            html = 'login.html'
            data = '账户密码不能为空'
            dataname = 'rlt'


    # models.UserInfo.objects.filter(user='').delete()
    return render(request, html, {dataname:data})

def user_List(request, page=1):
    if request.method=="POST":
        u_id=request.POST.get('u_id',None)
        print(type(u_id))
        if u_id!=None:
            if u_id=='':
                sql = "select * from user "
            else:
                sql = "select * from user as u where u.u_id=" + u_id
        else:
            sql="select * from user "
    else:
        sql = "select * from user "
    print(sql)
    model.execute(sql)
    books_obj = model.fetchall()
    from static.utils.paging import Paging
    paging = Paging(page, books_obj)
    return render(request, 'user_List.html', {'books': books_obj, 'paging': paging})

def to_user_home(request,u_id=None):
    sql='select m_id from user_movies where u_id='+str(u_id)
    model.execute(sql)
    u_look=model.fetchmany(6)
    user_look=[]
    for i in u_look:
        m_movies = 'select * from movies where m_id=' +str(i['m_id'])
        model.execute(m_movies)
        u_look = model.fetchone()
        user_look.append(u_look)

    import static.model.recommendation as rec

    # 根据用户id推荐前五个电影
    movielist_uid = rec.recommend_your_favorite_movie(u_id, 5)
    # 根据用户id最喜欢的电影推荐前五个类似的电影
    mid = movielist_uid[0]['m_id']
    movielist_mid = rec.recommend_same_type_movie(mid, 5)
    # 根据用户id最喜欢的电影推荐同样喜欢这部电影的人喜欢的电影
    movielist_mid_uid = rec.recommend_other_favorite_movie(mid, 6)

    return render(request, 'user_home.html',{'u_id':u_id,'user_look':user_look,'movie_uid':movielist_uid,'movie_mid':movielist_mid,"movie_mid_uid":movielist_mid_uid,'user':id})
def go_movie(request,page=1):
    sql='select * from movies'
    model.execute(sql)
    books_obj = model.fetchall()
    from static.utils.paging import Paging
    paging = Paging(page, books_obj,page_index=20)
    return render(request, 'movies.html', {'books': books_obj, 'paging': paging})



def aaa():
    pass