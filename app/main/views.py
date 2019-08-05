from flask import render_template,request,redirect,url_for,abort
from . import main
# from ..request import get_movies,get_movie,search_movie
from .forms import ReviewForm,UpdateProfile
from ..models import Pitch,User
from flask_login import login_required, current_user
from .forms import ReviewForm,UpdateProfile
from .. import db,photos
import markdown2 
# post = post.post
@main.route('/movie/post/new/<int:id>', methods = ['GET','POST'])
@login_required
def new_r(id):
    form = ReviewForm()
    movie = get_movie(id)
    if form.validate_on_submit():
        title = form.title.data
        post = form.post.data

        # Updated post instance
        new_post = post(movie_id=movie.id,movie_title=title,image_path=movie.poster,movie_review=post,user=current_user)

        # save post method
        new_post.save_post()
        return redirect(url_for('.movie',id = movie.id ))

    title = f'{movie.title} post'
    return render_template('new_post.html',title = title, post_form=form, movie=movie)


# @main.route('/movie/<int:id>')
# def movie(id):

#     '''
#     View movie page function that returns the movie details page and its data
#     '''
#     movie = get_movie(id)
#     title = f'{movie.title}'
#     posts = post.get_posts(movie.id)
#     return render_template('movie.html',title = title,movie = movie,reviews = reviews)

# @main.route('/')
# def index():
#     '''
#     View root page function that returns the index page and its data
#     '''
#     # Getting popular movie
#     popular_movies = get_movies('popular')
#     upcoming_movie = get_movies('upcoming')
#     now_showing_movie = get_movies('now_playing')
#     title = 'Home - Welcome to The best Movie post Website Online'
#     search_movie = request.args.get('movie_query')

#     if search_movie:
#         return redirect(url_for('main.search',movie_name=search_movie))
#     else:
#         return render_template('index.html', title = title, popular = popular_movies, upcoming = upcoming_movie, now_showing = now_showing_movie )




@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.post = form.post.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)
@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))
@main.route('/post/<int:id>')
def single_post(id):
    post=post.query.get(id)
    if post is None:
        abort(404)
    format_post = markdown2.markdown(post.movie_review,extras=["code-friendly", "fenced-code-blocks"])
    return render_template('post.html',post = post,format_post=format_post)
@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)
