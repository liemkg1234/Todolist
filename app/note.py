from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from app.models import User, Note
from app.forms import NoteForm
from app import db

'''
Search: tim kiem notes cua user khac
Home: hien thi Note cua ban? than va cua nguoi khac
'''


note = Blueprint("note", __name__)

@note.route('/home')
@login_required # When Logged in -> Can use
def home():
    user = User.query.filter_by(username=current_user.username).first_or_404()
    return render_template('home.html', user=user)


@note.route('/notes/<username>', methods=['GET', 'POST'])
@login_required
def notes(username):
    user = User.query.filter_by(username=username).first_or_404()

    # if user.id != current_user.id: # Check note of anyone Note (/notes/a -> /notes/b)
    #     render_template('note.html', user=current_user, s1_user=user)

    form = NoteForm()
    if form.validate_on_submit():
        new_note = Note(form.data.data, current_user.id)
        db.session.add(new_note)
        db.session.commit()
        flash('New Note has been added!', category='success')
        return redirect(url_for('note.notes', username=current_user.username))

    return render_template('note.html', user=current_user, form=form, s1_user=user)

@note.route('/deleteNote/<int:note_id>', methods= ['GET', 'POST'])
@login_required
def deleteNote(note_id):
    find_id = Note.query.get(note_id)
    if find_id:
        data_find_id = find_id.data # Get data form db
        if find_id.user_id == current_user.id:
            db.session.delete(find_id)
            db.session.commit()
    flash(f'''You has been delete "{data_find_id}" ''', category='success')
    return redirect(url_for('note.notes', username=current_user.username))