from flask import render_template,request,redirect,url_for,abort,flash
from . import main
from .forms import PostForm
# from ..request import get_movies,get_movie,search_movie

from ..models import Pitch,User
from flask_login import login_required, current_user
from .forms import UpdateProfile
from .. import db,photos
import markdown2 
# post = post.post


@main.route("/post/new", methods= ['GET', 'POST'])
@login_required
def new_post():

    form = PostForm()
    if form.validate_on_submit():
        pitch = Pitch(title=form.title.data, content = form.content.data, category = form.category.data)
        db.session.add(pitch)
        db.session.commit()
        
        return redirect(url_for('main.home'))
    return render_template('post.html',title = 'New Post', form = form, legend = 'New Post')

@main.route("/")
@main.route("/home")
def home():

   '''
   View root page function that returns the index page and its data
   '''
   title = 'Welcome to Pitch app'

   # Getting reviews by category
   page = request.args.get('page', 1, type=int)
   inspiration = Pitch.get_pitches('inspiration')
   biograghy = Pitch.get_pitches('biograghy')
   business = Pitch.get_pitches('business')

   return render_template('home.html', title=title, inspiration=inspiration, biograghy=biograghy, business=business)

@main.route('/pitches/inspiration')
def inspiration():
   pitches = Pitch.get_pitches('inspiration')

   return render_template('inspirational.html', pitches=pitches)


@main.route('/pitches/biography')
def biograpghy():

   pitches = Pitch.get_pitches('biography')

   return render_template("biograghy.html", pitches=pitches)
main.route('/user/<uname>/pitches')
def user_pitches(uname):
   user = User.query.filter_by(username=uname).first()
   pitches = Pitch.query.filter_by(user_id=user.id).all()
   pitches_count = Pitch.count_pitches(uname)
   user_joined = user.date_joined.strftime('%b %d, %Y')

   return render_template("profile/pitches.html", user=user, pitches=pitches, pitches_count=pitches_count, date=user_joined)

@main.route('/pitches/idea')
def idea():

   pitches = Pitch.get_pitches('idea')

   return render_template("ideas.html", pitches=pitches)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('main.profile',uname=user.username))

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

# @main.route('/interview/pitchs')
# def interview_pitch():
#     pitchs = Pitch.get_all_pitches()
#     title = 'Interview Pitches'
#     return render_template('interview.html',title = title,pitchs = pitchs)

# @main.route('/promotion/pitchs')
# def promotion_pitch():
#     pitchs = Pitch.get_all_pitches()
#     title = 'Promotion Pitches'
#     return render_template('promotion.html',title = title,pitchs = pitchs)

# @main.route('/product/pitchs')
# def inspiration():
#     pitchs = Pitch.get_all_pitches()
#     title = 'inspiration'
#     return render_template('inspiration.html',title = title,pitchs = pitchs)